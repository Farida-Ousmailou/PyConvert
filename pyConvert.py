
def converter(option, value):
    """pouce = 2.54 cm
    cm = 0.394 pouce"""

    if option == (" cm vers pouce") :
        result = cm_to_inch(value)
        print("le resultat est " + str(result) + " pouce")
    elif option == ("pouce vers cm") :
        result = inch_to_cm(value)
        print("le resultat est " + str(result) + " cm")

def cm_to_inch(value):
    return value * 0.394
def inch_to_cm(value):
    return value * 2.54


if __name__ == "__main__" :

    option = input("souhaitez vous convertir pouce vers cm ou cm vers  pouce?")

    if option == " ":
        option = input("veillez saisir la bonne conversion")
    elif option == int:
        option = input("veillez saisir la bonne conversion")

    value_to_convert = float (input("saisissez le nombre à convertir:"))

    if value_to_convert == " ":
        value_to_convert = input("veillez saisir un nombre")
    elif value_to_convert == str:
        value_to_convert = input("veillez saisir un nombre")
    else:
        print("vous souhaitez convertir" + option)

    converter(option, value_to_convert)


