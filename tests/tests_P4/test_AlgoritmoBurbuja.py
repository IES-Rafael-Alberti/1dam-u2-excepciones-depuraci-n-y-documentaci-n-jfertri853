import pytest
from src.P2_4.AlgoritmoBurbuja import (
    ordenar_lista,
    mostrar_lista,
    continuar,
    pedir_num,
)

@pytest.mark.parametrize(
    "lista, expected",
    [
        ([8, 5, 13, 2, 2, 2], [2, 2, 2, 5, 8, 13]),
        ([-4, 12, 33], [-4, 12, 33]),
        ([15, 9, 8, 4, 1, 0], [0, 1, 4, 8, 9, 15]),
        ([-7, -1, 0, 29, 3, -12], [-12, -7, -1, 0, 3, 29]),
        ([5, 8, 5], [5, 5, 8]),
        (["Azul", "amarillo", "Blanco", "beige"], ["Azul", "Blanco", "amarillo", "beige"])
    ]
)
def test_params_ordenar_lista(lista, expected):
    assert ordenar_lista(lista) == expected


@pytest.mark.parametrize(
    "lista, expected",
    [
        ([8, 5, 13, 2, 2, 2], "8, 5, 13, 2, 2, 2"),
        ([0, 3, 3, 8], "0, 3, 3, 8"),
        ([False, "Hola", 5.3, 2, 1.0, None], "False, Hola, 5.3, 2, 1.0, None")
    ]
)
def test_params_mostrar_lista(lista, expected):
    assert mostrar_lista(lista) == expected
