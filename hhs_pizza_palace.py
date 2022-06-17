import time
import sys
from collections import namedtuple
from tokenize import Name

pizzas = {
    "classic cheese": 8.50,
    "americano": 8.50,
    "ham and cheese": 8.50,
    "classic veggie": 8.50,
    "garlic and aioli": 8.50,
    "pepperoni": 8.50,
    "hawaiian": 8.50,
    "beef and onion": 13.50,
    "cheesy garlic": 13.50,
    "chicken deluxe": 13.50,
    "peri peri chicken": 13.50,
    "buffalo chicken": 13.50,
}
pizza_toppings = {
    "cheese": 0.50,
    "ham": 0.50,
    "olives": 0.50,
    "pepperoni": 0.50,
    "onions": 0.50,
    "mushrooms": 0.50,
}
user_details = {"Name": "", "Address": "", "Mobile": ""}
final_order = {}
user_total = 0


# Displays possible user actions
def actions():
    """Displays the actions the user can do"""
    print("\nTo execute action, type:")
    time.sleep(0.1)
    print("'1' to view actions")
    time.sleep(0.1)
    print("'2' to view the menu")
    time.sleep(0.1)
    print("'3' to place an order (maximum 5 pizzas)")
    time.sleep(0.1)
    print("'4' to exit\n")
    time.sleep(0.1)


# Displays the pizza menu
list_pizzas = namedtuple("list_pizzas", ["pizza", "price"])
pizza_choices = []
pizza_choices.append(list_pizzas("- Classic Cheese", "$8.50"))
pizza_choices.append(list_pizzas("- Americano", "$8.50"))
pizza_choices.append(list_pizzas("- Ham And Cheese", "$8.50"))
pizza_choices.append(list_pizzas("- Classic Veggie", "$8.50"))
pizza_choices.append(list_pizzas("- Garlic And Aioli", "$8.50"))
pizza_choices.append(list_pizzas("- Pepperoni", "$8.50"))
pizza_choices.append(list_pizzas("- Hawaiian", "$8.50"))
pizza_choices.append(list_pizzas("- Beef And Onion", "$13.50"))
pizza_choices.append(list_pizzas("- Cheesy Garlic", "$13.50"))
pizza_choices.append(list_pizzas("- Chicken Deluxe", "$13.50"))
pizza_choices.append(list_pizzas("- Peri Peri Chicken", "$13.50"))
pizza_choices.append(list_pizzas("- Buffalo Chicken", "$13.50\n"))


# Prints out a list of all pizzas
def view_pizzas():
    """Displays the pizzas within the pizza_choices list"""
    print("The pizzas we offer are:")
    time.sleep(0.3)
    for entry in pizza_choices:
        pizza = getattr(entry, "pizza").ljust(25)
        price = getattr(entry, "price").ljust(7)
        print("{}{}".format(pizza, price))
        time.sleep(0.1)


# Prints out a list of all toppings
def view_toppings():
    """Displays the toppings within the topping_choices list"""
    print("The toppings we offer are:")
    time.sleep(0.5)
    for entry in topping_choices:
        topping = getattr(entry, "topping").ljust(25)
        price = getattr(entry, "price").ljust(7)
        print("{}{}".format(topping, price))
        time.sleep(0.1)


# Display toppings Menu
list_toppings = namedtuple("list_toppings", ["topping", "price"])
topping_choices = []
topping_choices.append(list_toppings("- Cheese", "$0.50"))
topping_choices.append(list_toppings("- Ham", "$0.50"))
topping_choices.append(list_toppings("- Olives", "$0.50"))
topping_choices.append(list_toppings("- Pepperoni", "$0.50"))
topping_choices.append(list_toppings("- Onions", "$0.50"))
topping_choices.append(list_toppings("- Mushrooms", "$0.50"))


# Displays the ordering options so caller can pick an option
def service_type(user_total):
    """Displays the options of service for the user, or to go back to menu"""
    repeat = True
    while repeat:
        print(
            "\nFor delivery($3.00 surcharge), enter '1'."
            "\nFor pick-up, enter '2'."
            "\nTo go back to menu, enter '3'"
        )
        time.sleep(1)
        service = input("\nWhat would you like to do?\n")
        if service == "1":
            user_total += 3
            print(
                "\nYou chose delivery. There is a $3 surcharge "
                "that has been added to your total."
            )
            time.sleep(1.5)
            repeat = True
            while repeat:
                name = input("\nWhat is your name?\n").strip().lower()
                while repeat:
                    if name.isalpha() is True and len(name) > 0:
                        pass
                    else:
                        print("\nWarning: Please enter only letters")
                        break
                    confirm = (
                        input(
                            "\nYour name is '{}'. Is this correct? "
                            "Enter 'yes' or 'no'\n".format(name.title())
                        )
                        .strip()
                        .lower()
                    )
                    time.sleep(0.5)
                    if confirm == "yes" or confirm == "y":
                        user_details["Name"] = name.title()
                        repeat = False
                    elif confirm == "no" or confirm == "n":
                        break
                    else:
                        print("\nWarning: Please enter 'yes' or 'no'")
                        time.sleep(0.5)
                        continue

            repeat = True
            while repeat:
                address = input("\nWhat is the address?\n").strip().lower()
                while repeat:
                    if len(address) > 0:
                        pass
                    else:
                        print("\nWarning: Please enter an address.")
                        break
                    confirm = (
                        input(
                            "\nThe address is '{}'. Is this correct? "
                            "Enter 'yes' or 'no'\n".format(address.title())
                        )
                        .strip()
                        .lower()
                    )
                    time.sleep(0.5)
                    if confirm == "yes" or confirm == "y":
                        user_details["Address"] = address
                        repeat = False
                    elif confirm == "no" or confirm == "n":
                        break
                    else:
                        print("\nWarning: Please enter 'yes' or 'no'")
                        time.sleep(0.5)
                        continue

            repeat = True
            while repeat:
                try:
                    mobile = int(
                        input(
                            "\nWhat mobile number should "
                            "we contact you with?\n"
                        ).strip()
                    )
                except ValueError:
                    print("\nWarning: Please enter only integers.")
                    time.sleep(0.5)
                    continue
                while repeat:
                    confirm = (
                        input(
                            "\nThe mobile number you entered is '{}'. "
                            "Is this correct? Enter 'yes' or 'no'\n"
                            .format(mobile)
                        )
                        .strip()
                        .lower()
                    )
                    time.sleep(0.5)
                    if confirm == "yes" or confirm == "y":
                        user_details["Mobile"] = mobile
                        repeat = False
                    elif confirm == "no" or confirm == "n":
                        break
                    else:
                        print("\nWarning: Please enter 'yes' or 'no'")
                        time.sleep(0.5)
                        continue

            time.sleep(1)
            order(final_order, user_total)

        elif service == "2":
            print("\nYou chose pick-up.")
            time.sleep(1)
            print(
                "You can order up to 5 pizzas "
                "from our available pizza range")
            time.sleep(1)
            repeat = True
            while repeat:
                name = input("\nWhat is your name?\n").strip().lower()
                while repeat:
                    if name.isalpha() is True and len(name) > 0:
                        pass
                    else:
                        print("\nWarning: Please enter only letters")
                        break
                    confirm = (
                        input(
                            "\nYour name is '{}'. Is this correct? "
                            "Enter 'yes' or 'no'\n".format(name.title())
                        )
                        .strip()
                        .lower()
                    )
                    time.sleep(0.5)
                    if confirm == "yes" or confirm == "y":
                        user_details["Name"] = name.title()
                        repeat = False
                    elif confirm == "no" or confirm == "n":
                        break
                    else:
                        print("\nWarning: Please enter 'yes' or 'no'")
                        time.sleep(0.5)
                        continue
            order(final_order, user_total)

        elif service == "3":
            repeat = False
            break

        else:
            print("\nWarning: Please enter '1', '2', or '3'\n")
            time.sleep(0.5)
            continue


# Allows the user to select their pizza of choice and extra toppings
def order(pizza, user_total):
    """"User selects a pizza and toppings(optional) then displays order"""
    order_loop = 0
    loop = True
    while loop:
        order_loop += 1
        if order_loop > 1:
            order_another = (
                input("\nDo you want to order another pizza?\n")
                .strip().lower()
            )
            time.sleep(0.5)
            if order_another == "yes" or order_another == "y":
                pass
            elif order_another == "no" or order_another == "n":
                loop = False
                break
            else:
                print("\nPlease enter 'yes' or 'no'.")
                time.sleep(0.5)

        if order_loop > 5:
            print(
                "\nYou have ordered the maximum amount of 5 pizzas. "
                "\nWe will display your order and "
                "then continue to your order total."
            )
            time.sleep(2.5)
            loop = False
            break
        elif order_loop == 1:
            print("\nYou are ordering your 1st pizza.\n")
            time.sleep(1)
        else:
            if order_loop == 2:
                print("\nThis is your {}nd pizza.\n".format(order_loop))
                time.sleep(1)
            elif order_loop == 3:
                print("\nThis is your {}rd pizza.\n".format(order_loop))
                time.sleep(1)
            else:
                print("\nThis is your {}th pizza.\n".format(order_loop))
                time.sleep(1)

        view_pizzas()
        time.sleep(1.5)
        ordering_pizza = True
        while ordering_pizza:
            pizza = input(
                "Which pizza would you like to select?\n"
            ).strip().lower()
            time.sleep(0.5)
            if pizza in pizzas:
                print("\nYou have selected the {} pizza".format(pizza))
                user_total += pizzas.get(pizza)
                time.sleep(0.5)
                ordering_pizza = False
            else:
                print("\nSorry, we do not have {} pizza\n".format(pizza))
                time.sleep(0.5)

        ordering_topping = True
        while ordering_topping:
            add_topping = (
                input(
                    "\nWould you like to add an extra topping? "
                    "Enter 'yes' or 'no'\n"
                )
                .strip()
                .lower()
            )
            time.sleep(0.5)
            if add_topping == "yes" or add_topping == "y":
                repeat = True
                while repeat:
                    list_toppings = (
                        input(
                            "\nDo you want to view the available toppings? "
                            "Please enter 'yes' or 'no'\n"
                        )
                        .strip()
                        .lower()
                    )
                    time.sleep(0.5)
                    if list_toppings == "yes" or list_toppings == "y":
                        print("")
                        view_toppings()
                        time.sleep(2)
                        repeat = False
                    elif list_toppings == "no" or list_toppings == "n":
                        repeat = False
                    else:
                        print("\nWarning: Please enter 'yes' or 'no'\n")
                        time.sleep(0.5)
                        continue
            elif add_topping == "no" or add_topping == "n":
                break
            else:
                print("\nPlease enter 'yes' or 'no'\n")
                time.sleep(0.5)
                continue

            topping = (
                input("\nWhat topping would you like to add?\n")
                .strip().lower()
            )
            time.sleep(1)
            if topping in pizza_toppings:
                final_order.setdefault(pizza, [])
                final_order[pizza].append(topping)
                user_total += pizza_toppings.get(topping)
                if len(final_order[pizza]) > 1:
                    for pizza in final_order:
                        # maybe use final_order.keys and
                        # then use final_order[topping]
                        print(
                            "\nYou have ordered "
                            "a {} with {}.".format(pizza, final_order[pizza])
                        )
                        time.sleep(1)
                        print("\nYour total is: ${:.2f}".format(user_total))
                    # print out the multiple toppings in one print statement
                    # print {pizza} with {""}

                else:
                    print(
                        "\nI have added {} to your {} pizza"
                        .format(topping, pizza)
                    )
                    time.sleep(1)
                    for key in final_order:
                        print(
                            "\nYou have ordered a {} with {}"
                            .format(pizza, topping)
                        )
                        time.sleep(1)
                    print("\nYour total is: ${:.2f}".format(user_total))

            else:
                print("\nSorry, we do not have {}".format(topping))
                time.sleep(0.5)

    print("\nYou have ordered:")
    for key in final_order:
        print("- {} pizza with {}".format(key, topping).capitalize())
        time.sleep(1)

    print(
        "\nYour total cost for your order comes to ${:.2f}"
        .format(user_total)
    )
    time.sleep(1.5)
    if order_loop >= 1:
        print(
            "\nYour order will be ready soon. "
            "Thank you for calling Henderon High School Pizza Palace!"
        )
    else:
        print("\nThank you for calling Henderon High School Pizza Palace!")
    sys.exit()

# The if/else code that runs through the entire pizza ordering process
print("Hi, thank you for calling Henderson High School Pizza Palace.")
repeat = True
while repeat:
    actions()
    user_action = input(
        "Which action would you "
        "like to execute?\n").strip().lower()
    if user_action == "1":
        continue
    elif user_action == "2":
        print("")
        view_pizzas()
        time.sleep(0.5)
        view_toppings()
        time.sleep(1.5)
    elif user_action == "3":
        service_type(user_total)
        # break
    elif user_action == "4":
        print("\nThank you for calling Henderon High School Pizza Palace.")
        time.sleep(1)
        if len(user_details["Name"]) > 1:
            print("\nHave a good day, {}.".format(user_details["Name"]))
        else:
            print("Have a good day, goodbye.")
        break
    else:
        print("\nWarning: Please enter one of the available actions.")
        time.sleep(0.5)
        continue
