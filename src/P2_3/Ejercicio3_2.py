def cadena_impar(num: int = 1) -> str:
    """Counts each odd number from 1 to the parameter separated by ","

    Args:
        num (int): The final number

    Returns:
        cadena (str): every odd number from 1 to num separated by ","
    """
    cadena = ""
    for i in range(1, num + 1, 2):
        if i == num or i == num - 1:
            cadena += str(i)
        else:
            cadena += str(i) + ", "
    return cadena


def pedir_num() -> int:
    """Asks for a positive int until the user gets a valid one

    Returns:
        num (int): inserted number
    """
    while True:
        try:
            num = int(input("Introduce un numero entero positivo: "))
            if num < 1:
                raise ValueError("El numero no puede ser menor a 1")
            else:
                return num
        except ValueError:
            print("Eso no es un numero valido")


def main():
    numero = pedir_num()
    print(cadena_impar(numero))


if __name__ == "__main__":
    main()
