import pytest

from logic import analyzer


def prueba(x, y):
    return x - y



def test_2():
    assert prueba(3, 2) == 1
    assert prueba(4, 2) == 2

def test_analyzer():
    assert analyzer.prueba(3, 2) == 5