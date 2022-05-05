pizzas = {"classic cheese": 8.50, "americano": 8.50, "ham and cheese": 8.50, "classic veggie": 8.50, "garlic and aioli": 8.50, "pepperoni": 8.50, "hawaiian": 8.50, "beef and onion": 13.50, "cheesy garlic": 13.50, "chicken deluxe": 13.50, "peri peri chicken": 13.50, "buffalo chicken": 13.50}
pizza_toppings = {"extra cheese": 0.5, "ham": 0.5, "olives": 0.5, "pepperoni": 0.5, "onions": 0.5}
user_details = {"Name": "" , "Address": "", "Mobile": ""}
final_order = {}
user_toppings = {}
#user_total =

#Displays possible user actions
def actions():
    """Displays the actions the user can do"""
    print("""\nTo execute action, type:
    '1' to view actions
    '2' to view the menu
    '3' to place an order (maximum 5 pizzas)
    '4' to exit\n""")

#Displays the menu
def view_menu():
    """Displays the available pizzas and toppings for order"""
    print("\nThe available pizzas that we offer are: \n{}".format("\n".join(pizzas).title()))
    print("\nThe available toppings are: \n{}".format("\n".join(pizza_toppings).title()))

#Displays the pizzas
def all_pizzas():
    print("\nThe available pizzas that we offer are: \n{}".format("\n".join(pizzas).title()))

#Displays the toppings
def all_toppings():
    print("\nThe available toppings are: \n{}".format("\n".join(pizza_toppings).title()))

#Create function for ordering pizza
def service_type():
    """Displays the options of service for the user, or to go back to menu"""
    repeat = True
    while repeat:
        print("\nFor delivery, enter '1'. For pick-up, enter '2'. To go back to menu, enter '3'")
        service = input("What would you like to do?\n")
        if service == "1":
            print("You chose delivery.")
            repeat = True
            while repeat:
                address = input("What is the address?\n").strip().lower()
                while repeat:    
                    confirm = input("The address is {}. Is this correct? Enter 'yes' or 'no'\n".format(address.title())).strip().lower()
                    if confirm == "yes":
                        user_details["Address"] = address
                        repeat = False
                    elif confirm == "no":
                        break
                    else:
                        print("\nWarning: Please enter 'yes' or 'no'\n")
                        continue
            repeat = True
            while repeat:
                mobile = input("What mobile number should we contact you with?\n").strip()
                while repeat:    
                    confirm = input("The mobile number you entered is {}. Is this correct? Enter 'yes' or 'no'\n".format(mobile)).strip()
                    if confirm == "yes":
                        user_details["Mobile"] = mobile
                        repeat = False
                    elif confirm == "no":
                        break
                    else:
                        print("\nWarning: Please enter 'yes' or 'no'\n")
                        continue
            order(final_order, user_toppings)

        elif service == "2":
            print("\nYou chose pick-up.")
            print("You can order up to 5 pizzas from our available pizza range")
            #order function
        elif service == "3":
            actions()
        else:
            print("\nWarning: Please enter '1', '2', or '3'\n")
            continue

#Orders the user's pizza/s
def order(pizza, topping):
    """"User selects pizzas and toppings then displays order"""
    all_pizzas()
    ordering_pizza = True
    while ordering_pizza:
        pizza = input("What pizza would you like to select?\n").strip().lower()
        if pizza in pizzas:
            print("You have selected the {} pizza".format(pizza))
            ordering_pizza = False
        else:
            print("Sorry, we do not have {} pizza".format(pizza))
    ordering_topping = True
    while ordering_topping:
        add_topping = input("Would you like to add a topping? Enter 'yes' or 'no'\n").strip().lower()
        #fix add topping loop
        if add_topping == "yes":
            repeat = True
            while repeat:
                view_toppings = input("Do you want to view the available toppings? Please enter 'yes' or 'no'\n").strip().lower()
                if view_toppings == "yes":
                    all_toppings()
                    repeat = False
                elif view_toppings == "no":
                    repeat = False
                else:
                    print("\nWarning: Please enter 'yes' or 'no'\n")
                    continue
        elif add_topping == "no":
            break
        else:
            print("Please enter 'yes' or 'no'\n")
            continue
        topping = input("What topping would you like?\n").strip().lower()
        if topping in pizza_toppings:
            final_order.setdefault(pizza, [])
            final_order[pizza].append(topping)
            print("I have added {} to your {}".format(topping, pizza))
            print(final_order)
            #for key, value in final_order.items():
                #print("You have ordered a {} with {}".format(pizza, topping))
        else:
            print("Sorry, we do not have {}\n".format(topping))
        
#fix toppings and pizza order func

#---------------------------------------------------------------------------------------------

#Collects user's name and greets them
name = input("What is your name?\n")
user_details["Name"] = name.title()
print("\nHello {}, welcome to Henderson High School Pizza Palace!".format(user_details["Name"]))  

#if/else that runs through the entire pizza ordering process
repeat = True
while repeat:
    actions()
    user_action = input("Which action would you like to execute?\n").strip().lower()
    if user_action == "1":
        continue
    elif user_action == "2":
        view_menu()
    elif user_action == "3":
        service_type()
    elif user_action == "4":
        print("\nThank you for calling Henderon High School Pizza Palace.")
        print("\nFarewell {}!".format(user_details["Name"]))
        break
    else:
        print("\nWarning: Please enter one of the available actions.")
        continue
#Fix else repeat loop


#Create function for adding total
