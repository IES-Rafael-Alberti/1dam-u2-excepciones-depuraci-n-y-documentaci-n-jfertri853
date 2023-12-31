import pytest
from src.P2_3.Ejercicio3_5 import comprobar_password


@pytest.mark.parametrize(
    "clave, user_input, expected",
    [
        ("123abc", "123abc", True),
        ("ABC", "ABC", True),
        ("123", "123", True),
        ("guindilla", "guindilla", True),
        ("c0c0", "c0c0", True),
        (4, 4, True),
        (12.0, 12, True),
        (True, True, True),
        (False, False, True)
    ]
)
def test_params_comprobar_password(clave, user_input, expected):
    assert comprobar_password(clave, user_input) == expected


def test_NameError_comprobar_password():
    with pytest.raises(NameError) as excinfo:
        comprobar_password("123abc", "gorilas")
    assert str(excinfo.value) == "Incorrect Password!!"


def test_another_Exception_comprobar_password():
    try:
        comprobar_password("hola", "hola")
    except Exception as excinfo:
        pytest.fail(f"Unexpected exception raised: {excinfo}")
