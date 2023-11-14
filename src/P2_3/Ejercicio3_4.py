def pedir_num_entero(entrada: str):
    """Verifies if the parameter is numeric and returns it as an integer

    Returns:
        num: an inserted integer or None value
    """
    if not entrada.isnumeric():
        raise ValueError("La entrada no es correcta")

    return int(entrada)


def main():
    entrada = input("Introduce un numero entero: ")
    try:
        print(pedir_num_entero(entrada))
    except ValueError as e:
        print("***ERROR*** -", e)


if __name__ == "__main__":
    main()
