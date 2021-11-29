class bill:
    unit = int(input("Enter the unit consumed: "))


def Bill_Calc(unit):
    if unit <= 50:
        # below 50 units
        print(unit * 1.50)

    elif unit <= 150:
        # below 150 units
        print((50 * 1.5) + (unit - 50) * 2.00)

    elif unit <= 250:
        print((50 * 1.5) + ((150 - 50) * 2.00) + (unit - 150) * 3.00)

    else:
        print((50 * 1.5) + ((150 - 50) * 2.00) + ((250 - 150) * 3.00) + (unit - 250) * 4)

Bill_Calc(unit)

