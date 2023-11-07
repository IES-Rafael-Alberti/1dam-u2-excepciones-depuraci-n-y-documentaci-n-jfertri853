def solicitar_password():
    """Asks for an input and returns it

    Returns:
        password (str): the input with no changes, it's supposed to be a password try
    """
    password = input("Introduce tu contraseña: ")
    return password


def comprobar_password(clave_real: str, clave_intento: str) -> bool:
    """Compares 2 strings and returns if they are equal or not

    Args:
        clave_real (str): Stored password (real one)
        clave_intento (str): The password that the user has inserted to verify with the real one

    Returns:
        (bool): True or False depending on whether the strings match
    """
    try:
        if clave_real == clave_intento:
            return True
        else:
            raise NameError("Incorrect Password!!")
    except NameError:
        print("Incorrect Password!!")
        return False


def main():
    clave = "abc123"
    print(comprobar_password(clave, solicitar_password()))


if __name__ == "__main__":
    main()
