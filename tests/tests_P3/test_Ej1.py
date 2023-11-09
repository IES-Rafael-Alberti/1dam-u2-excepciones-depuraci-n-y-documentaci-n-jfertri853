import pytest
from src.P2_3.Ejercicio3_1 import contar_edad


@pytest.mark.parametrize(
    "edad, expected",
    [
        (5, "Has cumplido: 1, 2, 3, 4 y 5 años"),
        (0, "Has cumplido:  años"),
        (-21, "Has cumplido:  años"),
        (1, "Has cumplido: 1 años"),
        (13, "Has cumplido: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 y 13 años"),
        (2, "Has cumplido: 1 y 2 años")
    ]
)
def test_params_contar_edad(edad, expected):
    assert contar_edad(edad) == expected
