import pytest
from src.actividad02 import conversionCelsiusFahrenheit


@pytest.mark.parametrize(
    "grados, expected",
    [
        (0.0, 32.0),
        (3.9, 39.019999999999996),
        (-5.62, 21.884)
    ]
)
def test_params_conversionCelsiusFahrenheit(grados, expected):
    assert conversionCelsiusFahrenheit(grados) == expected
