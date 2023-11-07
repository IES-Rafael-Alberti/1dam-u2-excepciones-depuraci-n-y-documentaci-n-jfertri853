from src.P2_3.Ejercicio3_2 import pedir_num


def cuenta_atras(num: int = 1) -> str:
    """Counts backwards from the parameter num to 0

    Args:
        num (int): First number of the countdown

    Returns:
        cadena (str): countdown from num to 0 separated by ","
    """
    cadena = ""
    for i in range(num, -1, -1):
        if i == 0:
            cadena += str(i)
        else:
            cadena += str(i) + ", "
    return cadena


def main():
    numero = pedir_num()
    print(cuenta_atras(numero))


if __name__ == "__main__":
    main()
