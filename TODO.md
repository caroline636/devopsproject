# TODO: Run Project and Simulate CI/CD Pipeline

## Step 1: Run the Project
- [x] Run the application: `python app/app.py`
- [x] Verify app is running at http://localhost:5000

## Step 2: Simulate CI/CD Pipeline Locally
- [x] Install dependencies: `pip install -r app/requirements.txt flake8 black`
- [x] Lint with flake8: `flake8 app/ --count --select=E9,F63,F7,F82 --show-source --statistics` and `flake8 app/ --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics`
- [x] Format check with black: `black --check --diff app/`
- [x] Run tests: `python test_script.py`

## Step 3: CI/CD with Git Alone
- [x] Remove Docker-related deployment from CI/CD pipeline
- [x] Update CI/CD to deploy directly via Git (e.g., using GitHub Actions for deployment without Docker)
