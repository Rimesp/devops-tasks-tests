import pytest
from unittest.mock import patch
import devops_tasks  

#  BASIC TESTS
def test_deploy_application():
    with patch("random.choice", return_value=True): 
        result = devops_tasks.deploy_application("1.0")
        assert result is True, "deploy_application should return True when successful"

def test_check_service_status():
    with patch("random.choice", return_value="running"):  
        status = devops_tasks.check_service_status("web")
        assert status == "running", "check_service_status should return 'running' for a valid service"

def test_validate_configuration():
    with patch("os.path.exists", return_value=True):  
        with patch("builtins.open", create=True) as mock_open:  
            mock_open.return_value.__enter__.return_value.read.return_value = "valid configuration"
            with patch("random.choice", return_value=True):  
                is_valid = devops_tasks.validate_configuration("config.yml")
                assert is_valid is True, "validate_configuration should return True for valid configurations."

#  EDGE CASES
def test_deploy_application_invalid_input():
    with patch("random.choice", return_value=False):  
        result = devops_tasks.deploy_application(123)  
        assert result is False, "deploy_application should handle invalid input gracefully"

def test_check_service_status_invalid_service():
    with patch("random.choice", return_value="failed"):  
        status = devops_tasks.check_service_status("")  
        assert status == "failed", "check_service_status should handle empty service names gracefully"

#  MOCKED CALLS
def test_mocked_call_behavior():
    with patch("random.choice", return_value=True):  
        devops_tasks.deploy_application("1.0")
       
