# Deploy a Virtual Machine in Azure

For deploying a VM in Microsoft Azure, also have a look [here](https://learn.microsoft.com/en-us/azure/developer/terraform/).

1. Install `azure-cli` and `terraform` on your local machine
2. Run `az login` and enter your Azure credentials
3. On success, initialize terraform: `terraform init`
4. Create a plan of "what would happen": `terraform plan -out main.tfplan`
5. If it looks good, perform the plan: `terraform apply main.tfplan`
6. In case we changed something in the config, just re-run `terraform apply` to roll it out
7. When we are done with our resources: `terraform destroy`

8. Get the private ssh key from the VM: `terraform output -raw tls_private_key > id_rsa_azure_lab2_vm (chmod 600 id_rsa_azure_lab2_vm) `
9. Get the public IP: `terraform output public_ip_address`
10. Connect via ssh: `ssh -i id_rsa_azure_lab2_vm ubuntu@hsh-lab2-vm.westeurope.cloudapp.azure.com`