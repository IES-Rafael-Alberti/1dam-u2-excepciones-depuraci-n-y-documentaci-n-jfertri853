import pytest
from src.P2_3.Ejercicio3_4 import pedir_num_entero


@pytest.mark.parametrize(
    "entrada, expected",
    [
        ("8", 8),
        ("15", 15),
        ("0", 0),
        ("19", 19),
        ("8174913", 8174913)
    ]
)
def test_params_pedir_num_entero(entrada, expected):
    assert pedir_num_entero(entrada) == expected


def test_value_error_pedir_num_entero_negativos():
    with pytest.raises(ValueError) as excinfo:
        pedir_num_entero("-8")
    assert str(excinfo.value) == "La entrada no es correcta"


def test_value_error_pedir_num_entero_flotantes():
    with pytest.raises(ValueError) as excinfo:
        pedir_num_entero("7.4")
    assert str(excinfo.value) == "La entrada no es correcta"


def test_value_error_pedir_num_entero_noNumericos():
    with pytest.raises(ValueError) as excinfo:
        pedir_num_entero("Hola mundo")
    assert str(excinfo.value) == "La entrada no es correcta"


def test_noExceptions_pedir_num_entero():
    try:
        pedir_num_entero("8")
        pedir_num_entero("12")
        pedir_num_entero("0")
    except Exception as excinfo:
        pytest.fail(f"Unexpected exception raised: {excinfo}")
