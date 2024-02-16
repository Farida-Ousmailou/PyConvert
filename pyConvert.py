
def converter(option, value):
    """
        Convert between centimeters and inches based on the specified option.
        Parameters:
        - option (str): The conversion option. Should be either "cm vers pouce" or "pouce vers cm".
        - value (float): The value to be converted.
         Prints the converted value with appropriate unit.
        """
    validate_value(value)
    if option not in [1,2]:
        raise ValueError("Option invalide...")

    if option == 1:
        result = cm_to_inch(value)
        print("Le resultat est " + str(result) + " pouce")
    elif option == 2:
        result = inch_to_cm(value)
        print("Le resultat est " + str(result) + " cm")


def cm_to_inch(value):
    """
    Convert centimeters to inches.
    Parameters:
    - value (float): The value in centimeters to be converted to inches.
    Returns:
    float: The converted value in inches.
    """
    validate_value(value)
    return value * 0.394

def inch_to_cm(value):
    """
    Convert inches to centimeters.
    Parameters:
    - value (float): The value in inches to be converted to centimeters.
    Returns:
    float: The converted value in centimeters.
    """
    validate_value(value)
    return value * 2.54

def validate_value(value):
    """
    Validate the input value for conversion.

    Parameters:
    - value (float): The value to be validated.

    Returns:
    None: Raises TypeError if value is not numeric or ValueError if value is negative.
    """
    if not isinstance(value, (int, float)):
        raise TypeError("La valeur doit être de type numérique (int ou float)")
    if value < 0:
        raise ValueError("La valeur ne peut pas être négative")


def get_option_label(option):
    if option == 1:
        return "cm vers pouce"
    elif option == 2:
        return "pouce vers cm"

if __name__ == "__main__":
    value_to_convert = None
    option = None

    print("Bienvenu dans votre programme convertisseur pouce")
    print("Programme: \n Option 1 ===> pouce vers cm \n Option 2 ===> cm vers pouce ")

    while option not in [1, 2]:
        try:
            option = int(input("Saisissez votre choix [1/2]"))
            if option not in [1, 2]:
                print("L'option choisie n'est pas valide.\n Veuillez saisir  entre 1 et 2 .")
        except ValueError:
            print("L'option choisie n'est pas valide.\n Veuillez saisir  entre 1 et 2 .")

    while not isinstance(value_to_convert, (int, float)):
        try:
            value_to_convert = float(input("Saisissez le nombre à convertir: "))
        except ValueError:
            print("La valeur saisie n'est pas valide. Veuillez saisir un nombre.")

    print("Vous souhaitez convertir de " + get_option_label(option))

    try:
        converter(option, value_to_convert)
    except Exception as e:
        print(e)


