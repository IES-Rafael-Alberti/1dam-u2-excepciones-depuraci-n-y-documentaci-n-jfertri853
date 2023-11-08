# Too easy
def ordenar_lista(lista: list) -> list:
    total = len(lista) - 1
    intercambios = None
    contador = 0

    while contador != len(lista) and intercambios != 0:
        intercambios = 0
        for i in range(0, total):
            if lista[i] > lista[i + 1]:
                mayor = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = mayor
                intercambios += 1
        total -= 1
        contador += 1
    return lista


def mostrar_lista(lista: list) -> str:
    cadena = ""
    for i in range(0, len(lista)):
        if i == len(lista) - 1:
            cadena += str(lista[i])
        else:
            cadena += str(lista[i]) + ", "
    return cadena


def main():
    lista1 = [13, 8, 9, -3, 3, 2, 2]
    listaOrdenada = ordenar_lista(lista1)
    print(mostrar_lista(listaOrdenada))


if __name__ == "__main__":
    main()
