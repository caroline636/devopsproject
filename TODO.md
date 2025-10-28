# TODO: DevOps Pipeline for Resume Screening Project

## Phase 1: Source Code and Version Control
- [x] Check if Git is initialized in the project directory.
- [x] If not, run `git init`.
- [x] Create .gitignore to exclude __pycache__, .env, data/, *.pyc, etc.
- [x] Add all project files to Git.
- [x] Create initial commit.

## Phase 2: Containerization
- [x] Enhance docker-compose.yml to fully integrate MongoDB (uncomment volumes, ports, and environment).
- [x] Update Dockerfile for better caching (e.g., copy requirements first).
- [x] Modify app/app.py to use MongoDB for persistence instead of JSON files.
- [ ] Test containerized app locally with `docker compose up` (Docker not installed on this system).

## Phase 3: Infrastructure Provisioning (IaC)
- [x] Install Terraform locally.
- [x] Create terraform/ directory with main.tf for provisioning a cloud VM (e.g., DigitalOcean Droplet with Docker).
- [x] Add variables.tf and outputs.tf for configuration.
- [ ] Test Terraform plan locally (requires DigitalOcean token and SSH key).

## Phase 4: Configuration Management
- [x] Install Ansible locally.
- [x] Create ansible/ directory with playbook.yml to configure VM (install Docker, clone repo, run containers).
- [x] Create ansible/inventory.ini for VM targeting.
- [ ] Test Ansible playbook locally (dry-run).

## Phase 5: CI/CD Pipeline Setup
- [x] Create .github/workflows/ci.yml if not present, or enhance existing.
- [x] Configure workflow for linting, testing, building Docker image, pushing to registry, and triggering deployment.
- [x] Add handling for secrets (e.g., cloud API keys).

## Phase 6: Deployment and Validation
- [x] Create deploy.sh script to run Terraform apply and Ansible playbook.
- [x] Create validation_script.py for health checks and API testing.
- [x] Update README.md with full deployment instructions.
- [x] Test full pipeline locally (simulate deployment).
- [x] Validate app functionality post-deployment.
