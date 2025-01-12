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

# SECTION 2: PARAMETERIZED TESTS
@pytest.mark.parametrize("version", ["1.0", "2.0", "3.0"])
def test_deploy_application_parametrize(version):
    result = deploy_application(version)
    assert result in [True, False], f"Deployment of version {version} failed unexpectedly"

@pytest.mark.parametrize("service", ["web", "db", "cache", "unknown_service"])
def test_check_service_status_parametrize(service):
    status = check_service_status(service)
    assert status in ["running", "stopped", "failed"], f"Service status of {service} is not valid"

@pytest.mark.parametrize("config_file", ["valid_config.yml", "invalid_config.yml", "non_existent_file.yml"])
def test_validate_configuration_parametrize(config_file):
    is_valid = validate_configuration(config_file)
    assert is_valid in [True, False], f"Validation of {config_file} returned an invalid result"

# SECTION 3: EDGE CASES
def test_deploy_application_invalid_input():
    with pytest.raises(Exception):  # Expect exception for invalid input
        deploy_application(123)

def test_check_service_status_invalid_service():
    status = check_service_status("")  # Empty service name
    assert status in ["running", "stopped", "failed"], "Empty service name should return a valid status"

def test_validate_configuration_missing_file():
    with pytest.raises(Exception):  # Expect an exception for a missing file
        validate_configuration("non_existent_file.yml")

# SECTION 4: PERFORMANCE TESTS
def test_deploy_application_performance():
    start_time = time.time()
    deploy_application("1.0")
    assert time.time() - start_time < 3.1, "deploy_application should execute within 3.1 seconds"

# SECTION 5: MOCKING WITH FIXTURES
@pytest.fixture
def mock_service_status(monkeypatch):
    """
    Fixture to mock the random behavior of service status.
    Always returns 'running' for consistent testing.
    """
    def mock_choice(options):
        return "running"
    monkeypatch.setattr("random.choice", mock_choice)

@pytest.fixture
def mock_deployment_success(monkeypatch):
    """
    Fixture to mock the random behavior of deployment.
    Always returns True for consistent testing.
    """
    def mock_choice(options):
        return True
    monkeypatch.setattr("random.choice", mock_choice)

@pytest.fixture
def mock_deployment_failure(monkeypatch):
    """
    Fixture to mock the random behavior of deployment.
    Always returns False for consistent testing.
    """
    def mock_choice(options):
        return False
    monkeypatch.setattr("random.choice", mock_choice)

# Using fixtures to mock deployments
def test_deploy_application_success(mock_deployment_success):
    assert deploy_application("1.0") is True, "Deployment should succeed when mocked"

def test_deploy_application_failure(mock_deployment_failure):
    assert deploy_application("1.0") is False, "Deployment should fail when mocked"

def test_check_service_status_with_fixture(mock_service_status):
    assert check_service_status("web") == "running", "Fixture should always return 'running'"
