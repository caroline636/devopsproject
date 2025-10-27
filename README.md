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

## CI/CD

This project includes a GitHub Actions workflow for continuous integration and deployment:

- **Test**: Runs on every push and PR to main/master branches
- **Build & Deploy**: Builds and pushes Docker image to Docker Hub on pushes to main/master

### Setting up CI/CD
1. Push this code to a GitHub repository
2. Add the following secrets to your GitHub repository:
   - `DOCKER_USERNAME`: Your Docker Hub username
   - `DOCKER_PASSWORD`: Your Docker Hub password or access token
3. The workflow will automatically trigger on pushes

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
