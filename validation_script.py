#!/usr/bin/env python3
"""
Validation script for Resume Screening App
Performs health checks and API testing
"""

import requests
import time
import sys

def check_app_health(base_url, timeout=30):
    """Check if the app is responding"""
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            response = requests.get(f"{base_url}/", timeout=5)
            if response.status_code == 200:
                print(f"✓ App is healthy at {base_url}")
                return True
        except requests.RequestException as e:
            print(f"Waiting for app to be ready... {e}")
        time.sleep(5)
    print(f"✗ App failed to respond within {timeout} seconds")
    return False

def test_resume_upload(base_url, resume_file="test_resume.txt", job_desc="Python developer with Flask experience"):
    """Test resume upload functionality"""
    try:
        with open(resume_file, 'rb') as f:
            files = {'resume': f}
            data = {'job_description': job_desc}
            response = requests.post(f"{base_url}/upload", files=files, data=data, timeout=10)

        if response.status_code == 200:
            print("✓ Resume upload test passed")
            return True
        else:
            print(f"✗ Resume upload test failed with status {response.status_code}")
            return False
    except Exception as e:
        print(f"✗ Resume upload test failed: {e}")
        return False

def main():
    if len(sys.argv) != 2:
        print("Usage: python validation_script.py <base_url>")
        print("Example: python validation_script.py http://localhost:5000")
        sys.exit(1)

    base_url = sys.argv[1].rstrip('/')

    print("Starting validation tests...")

    # Health check
    if not check_app_health(base_url):
        sys.exit(1)

    # API test
    if test_resume_upload(base_url):
        print("✓ All tests passed!")
        sys.exit(0)
    else:
        print("✗ Some tests failed!")
        sys.exit(1)

if __name__ == "__main__":
    main()
