# TODO: DevOps Pipeline for Resume Screening Project

## Phase 1: Source Code and Version Control
- [ ] Check if Git is initialized in the project directory.
- [ ] If not, run `git init`.
- [ ] Create .gitignore to exclude __pycache__, .env, data/, *.pyc, etc.
- [ ] Add all project files to Git.
- [ ] Create initial commit.

## Phase 2: Containerization
- [ ] Enhance docker-compose.yml to fully integrate MongoDB (uncomment volumes, ports, and environment).
- [ ] Update Dockerfile for better caching (e.g., copy requirements first).
- [ ] Modify app/app.py to use MongoDB for persistence instead of JSON files.
- [ ] Test containerized app locally with `docker compose up`.

## Phase 3: Infrastructure Provisioning (IaC)
- [ ] Install Terraform locally.
- [ ] Create terraform/ directory with main.tf for provisioning a cloud VM (e.g., DigitalOcean Droplet with Docker).
- [ ] Add variables.tf and outputs.tf for configuration.
- [ ] Test Terraform plan locally.

## Phase 4: Configuration Management
- [ ] Install Ansible locally.
- [ ] Create ansible/ directory with playbook.yml to configure VM (install Docker, clone repo, run containers).
- [ ] Create ansible/inventory.ini for VM targeting.
- [ ] Test Ansible playbook locally (dry-run).

## Phase 5: CI/CD Pipeline Setup
- [ ] Create .github/workflows/ci.yml if not present, or enhance existing.
- [ ] Configure workflow for linting, testing, building Docker image, pushing to registry, and triggering deployment.
- [ ] Add handling for secrets (e.g., cloud API keys).

## Phase 6: Deployment and Validation
- [ ] Create deploy.sh script to run Terraform apply and Ansible playbook.
- [ ] Create validation_script.py for health checks and API testing.
- [ ] Update README.md with full deployment instructions.
- [ ] Test full pipeline locally (simulate deployment).
- [ ] Validate app functionality post-deployment.
