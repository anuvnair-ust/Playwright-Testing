import os
import pytest

@pytest.fixture
def user_data():
    return{
        "username" : "testuser",
        "password" : "test@123"
    }

@pytest.fixture(scope="session", autouse=True)
def create_results_folder():
    os.makedirs("test-results", exist_ok=True)