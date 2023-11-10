# Configure a VM to Run a Docker Container

In this exercise, we will configure our previous created VM with ansible and start our previously created docker container on it. 

We will use the ansible docker environment from [here](https://github.com/cytopia/docker-ansible) but you can also install it on your local machine.

1. Change the `ansible-hosts` file to match your hostname in the cloud
2. Change the image in the playbook to your docker image
3. If not already done: get the private ssh key `id_rsa_azure_lab2_vm` from the VM and save it to your ~/.ssh folder
4. Try to ssh to the host- this should work without password
5. Run this docker command: `docker run --rm -v $PWD:/data -v ~/.ssh:/root/.ssh cytopia/ansible ansible-playbook playbook.yml -i ansible-hosts --private-key /root/.ssh/id_rsa_azure_lab2_vm`. We mount the current directory with our playbook and the .ssh directory with the private ssh key to the container and run ansible. The playbook is performed on every host in the ansible-hosts file.
The playbook updates the packages, installs docker, and starts the container.
