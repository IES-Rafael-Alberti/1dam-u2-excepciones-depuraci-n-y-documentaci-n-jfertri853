def contar_edad(edad: int = 1) -> str:
    """Count each year from 1 to your current age

    Args:
        edad (int): Your current age which is 1 if no value given

    Returns:
        cadena (str): every year from 1 to current age separated by ","
    """
    cadena = "Has cumplido: "
    for i in range(1, edad + 1):
        if i == edad:
            cadena += str(i)
        elif i == edad - 1:
            cadena += str(i) + " y "
        else:
            cadena += str(i) + ", "
    cadena += " años"
    return cadena


def pedir_edad() -> int:
    """Asks for your current age and returns it or if the value is wrong the age stays = 1

    Returns:
        edad (int): an int number which is supposed to be your current age

    """
    try:
        edad = int(input("Introduce tu edad: "))
        if edad <= 0:
            raise ValueError("La edad no puede ser negativa o 0")
    except ValueError:
        print("Eso no es un numero valido")
        edad = 1
    return edad


def main():
    mi_edad = pedir_edad()
    print(contar_edad(mi_edad))


if __name__ == "__main__":
    main()
