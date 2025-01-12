import pytest
from devops_tasks import deploy_application, check_service_status, validate_configuration
import time

# SECTION 1: BASIC TESTS
def test_deploy_application():
    result = deploy_application("1.0")
    assert result in [True, False], "deploy_application should return True or False"

def test_check_service_status():
    status = check_service_status("web")
    assert status in ["running", "stopped", "failed"], "check_service_status should return a valid status"

def test_validate_configuration():
    is_valid = validate_configuration("config.yml")
    assert is_valid in [True, False], "validate_configuration should return True or False"

# SECTION 2: EDGE CASES
def test_deploy_application_invalid_input():
    result = deploy_application(123)  # Invalid input
    assert result in [True, False], "deploy_application should handle invalid input gracefully"

def test_check_service_status_invalid_service():
    status = check_service_status("")  # Empty service name
    assert status in ["running", "stopped", "failed"], "check_service_status should handle empty service names"

def test_validate_configuration_missing_file():
    result = validate_configuration("non_existent_file.yml")  # Missing file
    assert result in [True, False], "validate_configuration should return True or False for missing files"

# SECTION 3: MOCKING WITH FIXTURES
@pytest.fixture
def mock_service_status(monkeypatch):
    def mock_choice(options):
        return "running"
    monkeypatch.setattr("random.choice", mock_choice)

@pytest.fixture
def mock_deployment_success(monkeypatch):
    def mock_choice(options):
        return True
    monkeypatch.setattr("random.choice", mock_choice)

@pytest.fixture
def mock_deployment_failure(monkeypatch):
    def mock_choice(options):
        return False
    monkeypatch.setattr("random.choice", mock_choice)

def test_deploy_application_success(mock_deployment_success):
    assert deploy_application("1.0") is True, "Deployment should succeed when mocked"

def test_deploy_application_failure(mock_deployment_failure):
    assert deploy_application("1.0") is False, "Deployment should fail when mocked"

def test_check_service_status_with_fixture(mock_service_status):
    assert check_service_status("web") == "running", "Fixture should always return 'running'"
