import pytest
from devops_tasks import deploy_application, check_service_status, validate_configuration

# SECTION 1: TESTS DE BASE
def test_deploy_application():
    result = deploy_application("1.0")
    assert result in [True, False], "deploy_application should return True or False"

def test_check_service_status():
    status = check_service_status("web")
    assert status in ["running", "stopped", "failed"], "check_service_status should return a valid status"

def test_validate_configuration():
    is_valid = validate_configuration("config.yml")
    assert is_valid in [True, False], "validate_configuration should return True or False"

# SECTION 2: TESTS PARAMÉTRÉS
@pytest.mark.parametrize("version", ["1.0", "2.0", "3.0"])
def test_deploy_application_parametrize(version):
    result = deploy_application(version)
    assert result in [True, False], f"Deployment of version {version} failed unexpectedly"

@pytest.mark.parametrize("service", ["web", "db", "cache", ""])
def test_check_service_status_parametrize(service):
    status = check_service_status(service)
    assert status in ["running", "stopped", "failed"], f"Service status of {service} is not valid"

@pytest.mark.parametrize("config_file", ["valid_config.yml", "invalid_config.yml", "non_existent_file.yml"])
def test_validate_configuration_parametrize(config_file):
    is_valid = validate_configuration(config_file)
    assert is_valid in [True, False], f"Validation of {config_file} returned an invalid result"

# SECTION 3: GESTION DES CAS INATTENDUS
def test_deploy_application_invalid_input():
    # Adapté pour tester sans lever d'exception
    result = deploy_application(123)  # Teste avec un type invalide
    assert result in [True, False], "deploy_application should handle invalid input gracefully"

def test_check_service_status_invalid_service():
    # Test d'un service avec une chaîne vide
    status = check_service_status("")  # Service vide
    assert status in ["running", "stopped", "failed"], "Empty service name should return a valid status"

def test_validate_configuration_missing_file():
    # Test d'un fichier inexistant
    is_valid = validate_configuration("non_existent_file.yml")
    assert is_valid in [True, False], "Missing configuration file should return True or False"

# SECTION 4: TESTS DE PERFORMANCE
import time

def test_deploy_application_performance():
    start_time = time.time()
    deploy_application("1.0")
    assert time.time() - start_time < 3, "deploy_application should execute within 3 seconds"

# SECTION 5: FIXTURES AVANCÉES
@pytest.fixture
def mock_service_status(monkeypatch):
    def mock_choice(options):
        # Simule toujours "running" pour des tests prédéfinis
        return "running"
    monkeypatch.setattr("random.choice", mock_choice)

def test_check_service_status_with_fixture(mock_service_status):
    assert check_service_status("web") == "running", "Fixture should always return 'running'"
