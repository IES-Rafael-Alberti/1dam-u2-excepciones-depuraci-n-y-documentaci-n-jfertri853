import pytest
from src.P2_3.Ejercicio3_2 import cadena_impar


@pytest.mark.parametrize(
    "num, expected",
    [
        (7, "1, 3, 5, 7"),
        (-7, ""),
        (8, "1, 3, 5, 7"),
        (6, "1, 3, 5"),
        (11, "1, 3, 5, 7, 9, 11"),
        (0, ""),
        (1, "1"),
        (2, "1")
    ]
)
def test_params_cadena_impar(num, expected):
    assert cadena_impar(num) == expected
