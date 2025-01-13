import pytest
from unittest.mock import patch
import devops_tasks  # Import the module, not the functions directly.

# SECTION 1: BASIC TESTS
def test_deploy_application():
    with patch("random.choice", return_value=True):  # Mock randomness
        result = devops_tasks.deploy_application("1.0")
        assert result is True, "deploy_application should return True when successful"

def test_check_service_status():
    with patch("random.choice", return_value="running"):  # Mock randomness
        status = devops_tasks.check_service_status("web")
        assert status == "running", "check_service_status should return 'running' for a valid service"

def test_validate_configuration():
    with patch("os.path.exists", return_value=True):  # Mock file existence
        with patch("builtins.open", create=True) as mock_open:  # Mock file reading
            mock_open.return_value.__enter__.return_value.read.return_value = "valid configuration"
            with patch("random.choice", return_value=True):  # Mock randomness
                is_valid = devops_tasks.validate_configuration("config.yml")
                assert is_valid is True, "validate_configuration should return True for valid configurations."

# SECTION 2: EDGE CASES
def test_deploy_application_invalid_input():
    with patch("random.choice", return_value=False):  # Mock randomness
        result = devops_tasks.deploy_application(123)  # Invalid input
        assert result is False, "deploy_application should handle invalid input gracefully"

def test_check_service_status_invalid_service():
    with patch("random.choice", return_value="failed"):  # Mock randomness
        status = devops_tasks.check_service_status("")  # Empty service name
        assert status == "failed", "check_service_status should handle empty service names gracefully"

# SECTION 3: MOCKED CALLS
def test_mocked_call_behavior():
    with patch("random.choice", return_value=True):  # Mock randomness
        devops_tasks.deploy_application("1.0")
       
