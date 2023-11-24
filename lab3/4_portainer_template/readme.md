# Putting everthing together

Now we are able to put all our services together. We can distribute the containers among several servers or run them locally. For a first test, let us try a local run with portainer and create a new stack therein.

1. Install portainer on your host and import the `stack-template.yml` (change the volume paths to your file system)
2. Deploy the stack/all containers
3. Login to grafana and create a dashboard
4. Create some load with, e.g., [ddosify](https://github.com/ddosify/ddosify) (`ddosify -t target.site -n 20000 -d 20 -p HTTP -m GET`)
5. Also test the alarmmanager

TODO: secure all connections with https.

Reference:
- https://www.portainer.io/