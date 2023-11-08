def pedir_num_entero(entrada: str):
    """Asks for an input and returns it or returns None and raises and error if input is not an integer

    Returns:
        num: an inserted integer or None value
    """
    if not str(abs(int(entrada))).isnumeric():
        raise ValueError

    return int(entrada)


def main():
    entrada = input("Introduce un numero entero: ")
    try:
        print(pedir_num_entero(entrada))
    except ValueError:
        print("La entrada no es correcta")


if __name__ == "__main__":
    main()
