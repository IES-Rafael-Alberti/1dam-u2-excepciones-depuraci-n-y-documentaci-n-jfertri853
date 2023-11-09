import pytest
from src.P2_3.Ejercicio3_3 import cuenta_atras


@pytest.mark.parametrize(
    "num, expected",
    [
        (4, "4, 3, 2, 1, 0"),
        (0, "0"),
        (19, "19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0"),
        (-1, ""),
        (1, "1, 0"),
        (6, "6, 5, 4, 3, 2, 1, 0")
    ]
)
def test_params_cuenta_atras(num, expected):
    assert cuenta_atras(num) == expected
