# Reescribe el programa conversor de temperaturas para que lea repetidamente la temperatura hasta que sea correcta,
# debe detectar los fallos usando try y except

def conversionCelsiusFahrenheit(gradosCelsius: float):
    gradosFahrenheit = (gradosCelsius * 1.8) + 32
    return gradosFahrenheit


def pedirTemperatura():
    celsius = input("Introduce la temperatura en Celsius: ")
    return float(celsius)


def main():
    temperaturaFah = None
    while type(temperaturaFah) != float:
        try:
            temperatura = pedirTemperatura()
            temperaturaFah = conversionCelsiusFahrenheit(temperatura)
            print(temperaturaFah)
        except ValueError as e:
            print("***ERROR*** -", e)


if __name__ == "__main__":
    main()
