#! /bin/bash

cd $REPO_HOME/src/deploy/scripts
oc delete secret htpasswd-secret -n openshift-config
oc create secret generic htpasswd-secret --from-file=htpasswd=pre-bakedusers.httpasswd -n openshift-config

oc create secret generic htpass-secret --from-file=htpasswd=users.htpasswd -n openshift-config

oc apply -f htpasswd-oauth.yaml

# the application of the oauth object will trigger the bounce of the auth pods in openshift-auth ns
#oc scale deployment/oauth-deployment --replicas=0 -n openshift-authentication
#oc scale deployment/oauth-deployment --replicas=3 -n openshift-authentication
oc rollout status deployment/oauth-openshift --watch=true -n openshift-authentication


for i in {1..30}
do
    oc adm policy add-role-to-user admin user$i -n ml-workshop
done
oc adm policy add-cluster-role-to-user cluster-admin user29


