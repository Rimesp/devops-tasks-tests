# DevOps Tasks: Automation and CI/CD Pipeline

## Overview
This project demonstrates the implementation of key DevOps tasks and their automation using Python scripts, pytest for testing, and a CI/CD pipeline using GitHub Actions. The goal is to simulate deployment steps, monitor services, validate configurations, and integrate them into an automated pipeline.

## Repository Structure
- **`devops_tasks.py`**: Contains Python functions to simulate deployment tasks, service monitoring, and configuration validation.
- **`test_devops_tasks.py`**: Contains pytest test cases to validate the functionality of the `devops_tasks.py` functions.
- **`.github/workflows/pytest.yml`**: Defines the CI/CD pipeline to automate testing, quality analysis, and Docker image deployment.

## Features
1. **Simulated DevOps Tasks**
   - `deploy_application`: Simulates application deployment with success/failure outcomes.
   - `check_service_status`: Simulates status checks for services like `web`, `db`, and `cache`.
   - `validate_configuration`: Simulates configuration file validation with random outcomes (valid/invalid).

2. **Automated Testing**
   - Tests are written using `pytest` to validate different scenarios for each function.
   - Includes edge cases such as deployment failures, stopped services, and invalid configurations.

3. **CI/CD Pipeline**
   - Executes automated tests and generates coverage reports on each commit or pull request.
   - Integrates with SonarCloud for code quality analysis.
   - Builds and pushes a Docker image to Docker Hub.
   - Simulates and validates deployment tasks.

## Screenshots

### 1. Local Testing Results
Below is an example of the test results after running `pytest` locally, showing 6 successful test cases:

![image](https://github.com/user-attachments/assets/60340454-53d6-4e3b-8356-6d669c49412e)


### 2. Repository Structure
The repository structure includes all essential files and workflows for the project:

![image](https://github.com/user-attachments/assets/e609bdc4-51c5-4f5f-b81a-3859772a1477)

### 3. CI/CD Pipeline Success
The pipeline successfully executes all steps, including testing and quality checks:

![image](https://github.com/user-attachments/assets/41fa9050-3e11-4744-ba71-da4eab9a86e9)


### 4. Workflow Steps
A detailed view of the steps executed in the CI/CD pipeline:

![image](https://github.com/user-attachments/assets/e993aba8-e984-415f-9316-d62019644847)


### 5. SonarCloud Code Analysis
SonarCloud analysis results highlighting code quality, coverage, and maintainability:

![image](https://github.com/user-attachments/assets/953042e7-82b4-4f7b-a20d-3797a0e01213)

## Prerequisites
1. **Secrets Configuration**
   Ensure the following secrets are added to the GitHub repository:
   - `SONAR_TOKEN`: Token for SonarCloud integration.
   - `DOCKER_USERNAME`: Docker Hub username.
   - `DOCKER_PASSWORD`: Docker Hub password.

2. **Tools Required**
   - Python 3.8 or higher.
   - Docker installed locally for testing Docker-related tasks.

## Running the Project Locally

1. **Clone the Repository**
  
   git clone https://github.com/Rimesp/devops-tasks-tests.git
   cd devops-tasks-tests
   

2. **Set Up Virtual Environment**
   
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. **Install Dependencies**
   
   pip install -r requirements.txt
  

4. **Run Tests Locally**
   
   pytest --cov=.
  

## CI/CD Pipeline

The CI/CD pipeline is defined in `.github/workflows/pytest.yml` and performs the following steps:

1. **Checkout Repository**
   - Fetches the latest code from the `main` branch.

2. **Set Up Python Environment**
   - Configures a Python 3.8 environment.

3. **Install Dependencies**
   - Installs `pytest` and `pytest-cov` for testing.

4. **Run Tests and Generate Coverage Report**
   - Executes tests and creates a coverage report.

5. **Run SonarCloud Analysis**
   - Sends code analysis data to SonarCloud for quality checks.

6. **Build and Push Docker Image**
   - Builds a Docker image and pushes it to Docker Hub.

7. **Simulate and Validate Deployment**
   - Tests deployment logic and service validation using mocked results.

## Expected Outputs

- **Local Tests:**
  ```
  ======================== test session starts ===========================
  collected 6 items
  test_devops_tasks.py ......
  ==================== 6 passed in X.XX seconds ==========================
  ```

- **GitHub Actions:**
  - Displays success or failure for each pipeline step.
  - Includes detailed logs for troubleshooting.

- **SonarCloud:**
  - Updates project quality metrics and coverage.

- **Docker Hub:**
  - Publishes a Docker image tagged as `latest` on successful builds.



