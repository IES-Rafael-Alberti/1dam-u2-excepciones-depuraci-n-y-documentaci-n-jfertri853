def pedir_num_entero():
    """Asks for an input and returns it or returns None and raises and error if input is not an integer

    Returns:
        num: an inserted integer or None value
    """
    num = input("Introduce un numero entero: ")
    if not str(abs(int(num))).isnumeric():
        raise ValueError
    else:
        return num


def main():
    try:
        print(pedir_num_entero())
    except ValueError:
        print("La entrada no es correcta")


if __name__ == "__main__":
    main()
