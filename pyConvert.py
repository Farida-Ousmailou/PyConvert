
def converter (option, value_to_convert):
    """pouce = 2.54 cm
    cm = 0.394 pouce"""

    if option == (" cm vers pouce") :
        result = value_to_convert * 0.394
        print("le resultat est " + str(result) + " pouce")
    elif option == ("pouce vers cm") :
        result = value_to_convert * 2.54
        print("le resultat est " + str(result) + " cm")
    return result


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


result = converter(option, value_to_convert)


