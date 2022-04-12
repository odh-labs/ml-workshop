import openshift as oc
from jinja2 import Template

print('OpenShift client version: {}'.format(oc.get_client_version()))
print('OpenShift server version: {}'.format(oc.get_server_version()))

build_name = "fm-python-client"

with oc.project('ml-workshop'), oc.timeout(10*60):
    build_config = oc.selector(f"bc/{build_name}").count_existing() #.object

    print(build_config)
    if build_config == 0:
        oc.new_build(["--strategy", "docker", "--binary", "--docker-image", "registry.access.redhat.com/ubi8/python-38:1-71", "--name", build_name ])
    else:
        build_details = oc.selector(f"bc/{build_name}").object()
        print(build_details.as_json())

    print("Starting Build and Wiating.....")
    build_exec = oc.start_build([build_name, "--from-dir", ".", "--follow", "--build-loglevel", "10"])
    print("Build Finished")
    status = build_exec.status()
    print(status)
    for k, v in oc.selector(["bc/fm-python-client"]).logs(tail=500).items():
        print('Build Log: {}\n{}\n\n'.format(k, v))

    seldon_deploy = oc.selector(f"SeldonDeployment/{build_name}").count_existing()
    if seldon_deploy == 0:
        template_data = {"experiment_id": "e001", "model_name": "fm-python-client"}
        applied_template = Template(open("SeldonDeploy.yaml").read())
        print(applied_template.render(template_data))


