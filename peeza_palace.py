import time
from collections import namedtuple

pizzas = {"classic cheese": 8.50, "americano": 8.50, "ham and cheese": 8.50, "classic veggie": 8.50, "garlic and aioli": 8.50, "pepperoni": 8.50, "hawaiian": 8.50, "beef and onion": 13.50, "cheesy garlic": 13.50, "chicken deluxe": 13.50, "peri peri chicken": 13.50, "buffalo chicken": 13.50}
pizza_toppings = {"extra cheese": 0.5, "ham": 0.5, "olives": 0.5, "pepperoni": 0.5, "onions": 0.5, "mushrooms": 0.5}
user_details = {"Name": "" , "Address": "", "Mobile": ""}
final_order = {}
user_total = 0

#Displays possible user actions
def actions():
    """Displays the actions the user can do"""
    print("""\nTo execute action, type:
    '1' to view actions
    '2' to view the menu
    '3' to place an order (maximum 5 pizzas)
    '4' to exit\n""")

#Displays the menu
#def list_pizzas():
    #"""Displays the available pizzas and toppings for order"""
    #print("\nThe available pizzas that we offer are: \n{}".format("\n".join(pizzas).title()))
    #print("\nThe available toppings are: \n{}".format("\n".join(pizza_toppings).title()))

#Displays the pizza menu
list_pizzas = namedtuple('list_pizzas', ['pizza','price'])
pizza_choices = []
pizza_choices.append(list_pizzas('- Classic Cheese', '$8.50'))
pizza_choices.append(list_pizzas('- Americano', '$8.50'))
pizza_choices.append(list_pizzas('- Ham And Cheese', '$8.50'))
pizza_choices.append(list_pizzas('- Classic Veggie', '$8.50'))
pizza_choices.append(list_pizzas('- Garlic And Aioli', '$8.50'))
pizza_choices.append(list_pizzas('- Pepperoni', '$8.50'))
pizza_choices.append(list_pizzas('- Hawaiian', '$8.50'))
pizza_choices.append(list_pizzas('- Beef And Onion', '$13.50'))
pizza_choices.append(list_pizzas('- Cheesy Garlic', '$13.50'))
pizza_choices.append(list_pizzas('- Chicken Deluxe', '$13.50'))
pizza_choices.append(list_pizzas('- Peri Peri Chicken', '$13.50'))
pizza_choices.append(list_pizzas('- Buffalo Chicken', '$13.50\n'))

def view_pizzas():
    for entry in pizza_choices:
        pizza = getattr(entry,'pizza').ljust(25)
        price = getattr(entry,'price').ljust(7)
        print('{}{}'.format(pizza,price))

#Display toppings Menu
list_toppings = namedtuple('list_toppings', ['topping','price'])
topping_choices = []
topping_choices.append(list_toppings('Extra Cheese', '$0.50'))
topping_choices.append(list_toppings('Extra Ham', '$0.50'))
topping_choices.append(list_toppings('Extra Olives', '$0.50'))
topping_choices.append(list_toppings('Extra Pepperoni', '$0.50'))
topping_choices.append(list_toppings('Extra Onions', '$0.50'))
topping_choices.append(list_toppings('Extra Mushrooms', '$0.50'))

def view_toppings():
    for entry in topping_choices:
        topping = getattr(entry,'topping').ljust(25)
        price = getattr(entry,'price').ljust(7)
        print('{}{}'.format(topping,price))

#Create function for ordering pizza
def service_type():
    """Displays the options of service for the user, or to go back to menu"""
    repeat = True
    while repeat:
        print("\nFor delivery($3.00 surcharge), enter '1'. For pick-up, enter '2'. To go back to menu, enter '3'")
        service = input("What would you like to do?\n")
        if service == "1":
            print("\nYou chose delivery.")
            repeat = True
            while repeat:
                address = input("What is the address?\n").strip().lower()
                while repeat:    
                    confirm = input("\nThe address is {}. Is this correct? Enter 'yes' or 'no'\n".format(address.title())).strip().lower()
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
                mobile = input("\nWhat mobile number should we contact you with?\n").strip()
                while repeat:    
                    confirm = input("\nThe mobile number you entered is {}. Is this correct? Enter 'yes' or 'no'\n".format(mobile)).strip()
                    if confirm == "yes":
                        user_details["Mobile"] = mobile
                        repeat = False
                    elif confirm == "no":
                        break
                    else:
                        print("\nWarning: Please enter 'yes' or 'no'\n")
                        continue
            order(final_order, user_total)
            break
        elif service == "2":
            print("\nYou chose pick-up.")
            print("You can order up to 5 pizzas from our available pizza range")
            order(final_order, user_total)
            break
        elif service == "3":
            break
        else:
            print("\nWarning: Please enter '1', '2', or '3'\n")
            continue

#Orders the user's pizza/s
def order(pizza, user_total):
    """"User selects a pizza and toppings(optional) then displays order"""
    view_pizzas()
    ordering_pizza = True
    while ordering_pizza:
        pizza = input("What pizza would you like to select?\n").strip().lower()
        if pizza in pizzas:
            print("\nYou have selected the {} pizza".format(pizza))
            user_total += pizzas.get(pizza)
            print(pizzas.get(pizza))
            ordering_pizza = False
        else:
            print("Sorry, we do not have {} pizza".format(pizza))
    ordering_topping = True
    while ordering_topping:
        add_topping = input("Would you like to add more toppings? Enter 'yes' or 'no'\n").strip().lower()
        if add_topping == "yes":
            repeat = True
            while repeat:
                list_toppings = input("Do you want to view the available toppings? Please enter 'yes' or 'no'\n").strip().lower()
                if list_toppings == "yes":
                    print("")
                    view_toppings()
                    repeat = False
                elif list_toppings == "no":
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
            user_total += pizza_toppings.get(topping)
            if len(final_order[pizza]) > 1:
                print(final_order)
                print(user_total)
                print(len(final_order[pizza]))
                #print out the multiple toppings in one print statement
                #print {pizza} with {""}

            else:
                print("I have added {} to your {} pizza".format(topping, pizza))
                print(user_total)
                for key, value in final_order.items():
                    print("You have ordered a {} with {}".format(pizza, topping))
        else:
            print("Sorry, we do not have {}\n".format(topping))
            
    
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
        print("")
        view_pizzas()
        view_toppings()
    elif user_action == "3":
        service_type()
        print("Your order will be ready soon. Thank you for calling Henderon High School Pizza Palace!")
        print(user_total)
        break
    elif user_action == "4":
        print("\nThank you for calling Henderon High School Pizza Palace.")
        print("\nFarewell {}!".format(user_details["Name"]))
        break
    else:
        print("\nWarning: Please enter one of the available actions.")
        continue


#to-do list:
#add $3 charge for delivery
#add costs to global user_total
#fix spacings
#create if else for dictionary in list using index greater than 0, display pizza with more than 1 topping 
