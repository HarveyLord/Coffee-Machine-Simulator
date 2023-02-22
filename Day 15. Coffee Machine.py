MENU = {
    "espresso": {
    "ingredients": {
            "water": 50,
            "coffee": 18,},
    "cost": 1.50,},

    "latte": {
    "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,},
    "cost": 2.50,},

    "cappuccino": {
    "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,},
    "cost": 3.00,}
}

resources = {
    "water": 1000,
    "milk": 400,
    "coffee": 150,
    "money": 0.00,
}


### variables

machine_on = True

#### auxiliary functions



def report():
    print(f'Water:  {resources["water"]}')
    print(f'Milk:   {resources["milk"]}')
    print(f'Coffee: {resources["coffee"]}')
    print(f'Money: ${resources["money"]}\n')


def enough_for_drink(esp = 0, lat = 0, cap = 0):

    if esp == 1:
        if resources["water"] < MENU["espresso"]["ingredients"]["water"]:
            print("Sorry not enough water\n")
            return False
        if resources["coffee"] < MENU["espresso"]["ingredients"]["coffee"]:
            print("Sorry not enough coffee\n")
            return False
        else:
            return True

    if lat == 1:

        if resources["water"] < MENU["latte"]["ingredients"]["water"]:
            print("Sorry not enough water\n")
            return False
        if resources["milk"] < MENU["latte"]["ingredients"]["milk"]:
            print("Sorry not enough milk\n")
            return False
        if resources["coffee"] < MENU["latte"]["ingredients"]["coffee"]:
            print("Sorry not enough coffee\n")
            return False
        else:
            return True

    if cap == 1:

        if resources["water"] < MENU["cappuccino"]["ingredients"]["water"]:
            print("Sorry not enough water\n")
            return False
        if resources["milk"] < MENU["cappuccino"]["ingredients"]["milk"]:
            print("Sorry not enough milk\n")
            return False
        if resources["coffee"] < MENU["cappuccino"]["ingredients"]["coffee"]:
            print("Sorry not enough coffee\n")
            return False
        else:
            return True

def transaction(esp = 0, lat = 0, cap = 0):

    if esp == 1:
        print(f'The price for an espresso is ${MENU["espresso"]["cost"]}')
        qua = int(input("How many quarters: "))
        nic = int(input("How many nickles: "))
        dim = int(input("How many dimes: "))
        pen = int(input("How many pennies: "))

        payed = (qua * 0.25) + (nic * 0.1) + (dim * 0.05) + (pen * 0.01)

        if payed >= MENU["espresso"]["cost"]:

            change =  payed - MENU["espresso"]["cost"]
            print(f"Thank you, here is the change of ${round(change,2)}")
            resources["money"] = resources["money"] + payed
            resources["money"] = resources["money"] - change
            return True

        if payed < MENU["espresso"]["cost"]:

            owed = MENU["espresso"]["cost"] - payed
            print(f"Please insert ${round(owed,2)}")
            return False

    if lat == 1:
        print(f'The price for an latte is ${MENU["latte"]["cost"]}')
        qua = int(input("How many quarters: "))
        nic = int(input("How many nickles: "))
        dim = int(input("How many dimes: "))
        pen = int(input("How many pennies: "))

        payed = (qua * 0.25) + (nic * 0.1) + (dim * 0.05) + (pen * 0.01)


        if payed >= MENU["latte"]["cost"]:

            change =  payed - MENU["latte"]["cost"]
            print(f"Thank you, here is the change of ${round(change,2)}")
            resources["money"] = resources["money"] + payed
            resources["money"] = resources["money"] - change
            return True

        if payed < MENU["latte"]["cost"]:

            owed = MENU["latte"]["cost"] - payed
            print(f"Please insert ${round(owed,2)}")
            return False

    if cap == 1:
        print(f'The price for an cappuccino is ${MENU["cappuccino"]["cost"]}')
        qua = int(input("How many quarters: "))
        nic = int(input("How many nickles: "))
        dim = int(input("How many dimes: "))
        pen = int(input("How many pennies: "))

        payed = (qua * 0.25) + (nic * 0.1) + (dim * 0.05) + (pen * 0.01)


        if payed >= MENU["cappuccino"]["cost"]:
            change = payed - MENU["cappuccino"]["cost"]
            print(f"Thank you, here is the change of ${round(change,2)}")
            resources["money"] = resources["money"] + payed
            resources["money"] = resources["money"] - change
            return True

        if payed < MENU["cappuccino"]["cost"]:
            owed = MENU["cappuccino"]["cost"] - payed
            print(f"Please insert ${round(owed,2)}")
            return False


def make_drink(esp = 0, lat = 0, cap = 0):

    if esp == 1:

        resources["water"] = resources["water"] - MENU["espresso"]["ingredients"]["water"]
        resources["coffee"] = resources["coffee"] - MENU["espresso"]["ingredients"]["coffee"]
        print("Here is your espresso, have a great day!\n")

    if lat == 1:

        resources["water"] = resources["water"] - MENU["latte"]["ingredients"]["water"]
        resources["milk"] = resources["milk"] - MENU["latte"]["ingredients"]["milk"]
        resources["coffee"] = resources["coffee"] - MENU["latte"]["ingredients"]["coffee"]
        print("Here is your latte, have a great day!\n")

    if cap == 1:

        resources["water"] = resources["water"] - MENU["cappuccino"]["ingredients"]["water"]
        resources["milk"] = resources["milk"] - MENU["cappuccino"]["ingredients"]["milk"]
        resources["coffee"] = resources["coffee"] - MENU["cappuccino"]["ingredients"]["coffee"]
        print("Here is your cappuccino, have a great day!\n")



#### main user interface logic tree

while machine_on:

    command = input("Choose drink ( espresso = 1 / latte = 2 / cappuccino = 3 ): ")

    if command != "1" and command != "2" and command != "3" and command != "report" and command != "switch off":
        print("Please ensure your input is correct, try again\n")

    if command == "off":
        machine_on = False
        print("beep boop beep, shutting off processor")
        break

    if command == "report":
        report()

    if command == "1":

         if enough_for_drink(1, 0, 0):

             if transaction(1, 0, 0):

                 make_drink(1, 0, 0)

    if command == "2":

         if enough_for_drink(0, 1, 0):

             if transaction(0, 1, 0):

                 make_drink(0, 1, 0)

    if command == "3":

         if enough_for_drink(0, 0, 1):

             if transaction(0, 0, 1):

                 make_drink(0, 0, 1)

