#! /bin/bash

cd $REPO_HOME/scripts
oc create secret generic htpass-secret --from-file=htpasswd=users.htpasswd -n openshift-config

oc apply -f htpasswd.cr

for i in {1..30}
do
    oc adm policy add-role-to-user admin user$i -n ml-workshop
done
oc adm policy add-cluster-role-to-user cluster-admin user29

