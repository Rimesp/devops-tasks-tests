import pytest
from unittest.mock import patch, MagicMock
from devops_tasks import deploy_application, check_service_status, validate_configuration

# SECTION 1: BASIC TESTS
def test_deploy_application():
    with patch("devops_tasks.external_service_call") as mock_service_call:
        mock_service_call.return_value = True
        result = deploy_application("1.0")
        assert result is True, "deploy_application should return True when successful"

def test_check_service_status():
    with patch("devops_tasks.service_status_checker") as mock_service_status:
        mock_service_status.return_value = "running"
        status = check_service_status("web")
        assert status == "running", "check_service_status should return 'running' for a valid service"

def test_validate_configuration():
    with patch("builtins.open", create=True) as mock_open:
        mock_open.return_value.__enter__.return_value.read.return_value = "valid configuration"
        is_valid = validate_configuration("config.yml")
        assert is_valid is True, "validate_configuration should return True for valid configuration"

# SECTION 2: EDGE CASES
def test_deploy_application_invalid_input():
    with patch("devops_tasks.external_service_call") as mock_service_call:
        mock_service_call.return_value = False
        result = deploy_application(123)  # Invalid input
        assert result is False, "deploy_application should handle invalid input gracefully"

def test_check_service_status_invalid_service():
    with patch("devops_tasks.service_status_checker") as mock_service_status:
        mock_service_status.return_value = "failed"
        status = check_service_status("")  # Empty service name
        assert status == "failed", "check_service_status should handle empty service names gracefully"

def test_validate_configuration_missing_file():
    with patch("os.path.exists") as mock_exists:
        mock_exists.return_value = False
        result = validate_configuration("non_existent_file.yml")  # Missing file
        assert result is False, "validate_configuration should return False for missing files"

# SECTION 3: MOCKING WITH FIXTURES
@pytest.fixture
def mock_service_status(monkeypatch):
    def mock_status_checker(service_name):
        return "running"
    monkeypatch.setattr("devops_tasks.service_status_checker", mock_status_checker)

@pytest.fixture
def mock_deployment_success(monkeypatch):
    def mock_service_call(version):
        return True
    monkeypatch.setattr("devops_tasks.external_service_call", mock_service_call)

@pytest.fixture
def mock_deployment_failure(monkeypatch):
    def mock_service_call(version):
        return False
    monkeypatch.setattr("devops_tasks.external_service_call", mock_service_call)

def test_deploy_application_success(mock_deployment_success):
    assert deploy_application("1.0") is True, "Deployment should succeed when mocked"

def test_deploy_application_failure(mock_deployment_failure):
    assert deploy_application("1.0") is False, "Deployment should fail when mocked"

def test_check_service_status_with_fixture(mock_service_status):
    assert check_service_status("web") == "running", "Fixture should always return 'running'"

# SECTION 4: ASSERTIONS ON MOCKED CALLS
def test_mocked_call_behavior():
    with patch("devops_tasks.external_service_call") as mock_service_call:
        mock_service_call.return_value = True
        deploy_application("1.0")
        mock_service_call.assert_called_once_with("1.0")

    with patch("devops_tasks.service_status_checker") as mock_service_status:
        mock_service_status.return_value = "running"
        check_service_status("web")
        mock_service_status.assert_called_once_with("web")

# SECTION 5: EDGE CASE MOCKING
def test_validate_configuration_empty_file():
    with patch("builtins.open", create=True) as mock_open:
        mock_open.return_value.__enter__.return_value.read.return_value = ""
        is_valid = validate_configuration("config.yml")
        assert is_valid is False, "validate_configuration should return False for empty configuration files"
