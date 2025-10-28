#!/bin/bash

# Deploy script for Resume Screening App
# This script provisions infrastructure with Terraform and configures it with Ansible

set -e

echo "Starting deployment..."

# Step 1: Provision infrastructure with Terraform
echo "Provisioning infrastructure with Terraform..."
cd terraform
terraform init
terraform plan -out=tfplan
terraform apply tfplan

# Get the droplet IP
DROPLET_IP=$(terraform output -raw droplet_ip)
echo "Droplet IP: $DROPLET_IP"

# Step 2: Update Ansible inventory
echo "Updating Ansible inventory..."
cd ../ansible
sed -i "s/# droplet ansible_host=<DROPLET_IP>/droplet ansible_host=$DROPLET_IP/" inventory.ini

# Step 3: Run Ansible playbook
echo "Running Ansible playbook..."
ansible-playbook -i inventory.ini playbook.yml

echo "Deployment completed successfully!"
echo "App should be accessible at http://$DROPLET_IP:5000"
