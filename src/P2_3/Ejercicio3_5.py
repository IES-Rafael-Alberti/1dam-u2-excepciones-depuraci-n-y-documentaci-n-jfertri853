def solicitar_password():
    """Asks for an input and returns it

    Returns:
        password (str): the input with no changes, it's supposed to be a password try
    """
    password = input("Introduce tu contraseña: ")
    return password


def comprobar_password(clave_real: str, clave_intento: str) -> bool:
    """Compares 2 strings and returns True if they are equal or raises an error if not

    Args:
        clave_real (str): Stored password (real one)
        clave_intento (str): The password that the user has inserted to verify with the real one

    Returns:
        (bool): will always be True
    """
    if clave_real == clave_intento:
        return True
    else:
        raise NameError("Incorrect Password!!")


def main():
    clave = "abc123"
    intentoClave = solicitar_password()
    try:
        ingresar = comprobar_password(clave, intentoClave)
        if ingresar:
            print(ingresar)
    except NameError as e:
        print("***ERROR*** - ", e)
    except Exception:
        print("***ERROR*** - Desconocido")


if __name__ == "__main__":
    main()
