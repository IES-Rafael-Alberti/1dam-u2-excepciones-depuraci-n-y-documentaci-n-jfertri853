import pytest
from src.P2_3.Ejercicio3_4 import pedir_num_entero


@pytest.mark.parametrize(
    "entrada, expected",
    [
        ("8", 8),
        ("15", 15),
        ("-5", -5),
        ("-34", -34),
        ("0", 0)
    ]
)
def test_params_pedir_num_entero(entrada, expected):
    assert pedir_num_entero(entrada) == expected


def test_errors_pedir_num_entero():
    with pytest.raises(ValueError) as excinfo:
        pedir_num_entero("Hola mundo")
    assert str(excinfo.value) == "La entrada no es correcta"
