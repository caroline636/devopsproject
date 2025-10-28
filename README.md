# Resume Screening (Dockerized)

A Flask-based AI resume screening application that uses TF-IDF and cosine similarity to score resumes against job descriptions.

## Features
- Upload PDF or text resumes
- Paste job descriptions
- AI-powered scoring using machine learning
- Docker containerized for easy deployment
- CI/CD pipeline with GitHub Actions

## Local Development

### Prerequisites
- Python 3.10+
- Docker and Docker Compose (optional, for containerized run)

### Running Locally with Python
1. Install dependencies:
   ```bash
   pip install -r app/requirements.txt
   ```

2. Run the application:
   ```bash
   python -m flask --app app/app.py run --host=0.0.0.0 --port=5000
   ```

3. Open http://localhost:5000 in your browser

### Running with Docker Compose
1. Build the containers:
   ```bash
   docker compose build
   ```

2. Run the application:
   ```bash
   docker compose up -d
   ```

3. Open http://localhost:5000 in your browser

Results are saved to `./data` directory.

## DevOps Pipeline

This project implements a full DevOps pipeline including containerization, infrastructure as code, configuration management, and CI/CD.

### Components
- **Containerization**: Docker and Docker Compose with MongoDB integration
- **Infrastructure as Code**: Terraform for provisioning cloud infrastructure (DigitalOcean Droplet)
- **Configuration Management**: Ansible for server configuration and app deployment
- **CI/CD**: GitHub Actions for automated testing, linting, building, and deployment

### Prerequisites
- Python 3.10+
- Docker and Docker Compose
- Terraform
- Ansible
- GitHub repository with secrets configured

### Local Development
1. Install dependencies: `pip install -r app/requirements.txt`
2. Run locally: `python -m flask --app app/app.py run --host=0.0.0.0 --port=5000`
3. Test: `python test_script.py`

### Deployment
1. **Provision Infrastructure**: Run `terraform apply` in the `terraform/` directory
2. **Configure Server**: Update `ansible/inventory.ini` with the provisioned VM IP, then run `ansible-playbook -i inventory.ini playbook.yml`
3. **Or use the deploy script**: `./deploy.sh` (automates Terraform and Ansible steps)

### CI/CD Setup
1. Push code to GitHub repository
2. Add these secrets to your GitHub repo:
   - `DOCKER_USERNAME`: Docker Hub username
   - `DOCKER_PASSWORD`: Docker Hub password/access token
   - `DO_TOKEN`: DigitalOcean API token (for automated deployment)
   - `DEPLOY_TOKEN`: Token for triggering deployment (optional)
3. The pipeline runs on pushes to main/master:
   - Linting and testing
   - Docker image build and push
   - Automated deployment trigger

### Validation
Run the validation script: `python validation_script.py http://<app-url>:5000`

## API Usage

- **GET /**: Main upload form
- **POST /upload**: Upload resume and job description for screening
  - Form data: `job_description` (text), `resume` (file)

## Testing

Run the test script:
```bash
python test_script.py
```
# devopsproject
