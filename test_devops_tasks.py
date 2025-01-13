import pytest
from unittest.mock import patch, MagicMock
import devops_tasks  # Import the module, not the functions directly.

# SECTION 1: BASIC TESTS
def test_deploy_application():
    with patch("devops_tasks.deploy_application", return_value=True) as mock_deploy:
        result = devops_tasks.deploy_application("1.0")
        mock_deploy.assert_called_once_with("1.0")
        assert result is True, "deploy_application should return True when successful"

def test_check_service_status():
    with patch("devops_tasks.check_service_status", return_value="running") as mock_status:
        status = devops_tasks.check_service_status("web")
        mock_status.assert_called_once_with("web")
        assert status == "running", "check_service_status should return 'running' for a valid service"

def test_validate_configuration():
    with patch("os.path.exists", return_value=True):
        with patch("builtins.open", create=True) as mock_open:
            mock_open.return_value.__enter__.return_value.read.return_value = "valid configuration"
            is_valid = devops_tasks.validate_configuration("config.yml")
            assert is_valid is True, "validate_configuration should return True for valid configurations."

# SECTION 2: EDGE CASES
def test_deploy_application_invalid_input():
    with patch("devops_tasks.deploy_application", return_value=False) as mock_deploy:
        result = devops_tasks.deploy_application(123)  # Invalid input
        mock_deploy.assert_called_once_with(123)
        assert result is False, "deploy_application should handle invalid input gracefully"

def test_check_service_status_invalid_service():
    with patch("devops_tasks.check_service_status", return_value="failed") as mock_status:
        status = devops_tasks.check_service_status("")  # Empty service name
        mock_status.assert_called_once_with("")
        assert status == "failed", "check_service_status should handle empty service names gracefully"

# SECTION 3: MOCKED CALLS
def test_mocked_call_behavior():
    with patch("devops_tasks.deploy_application", return_value=True) as mock_deploy:
        devops_tasks.deploy_application("1.0")
        mock_deploy.assert_called_once_with("1.0")
