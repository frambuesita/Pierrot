import pytest
from src.functions import prueba

@pytest.fixture
def test_1():
    assert prueba(2, 3) == 5