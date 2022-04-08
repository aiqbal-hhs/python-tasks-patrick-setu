pizzas = {"classic cheese": 8.50, "americano": 8.50, "ham and cheese": 8.50, "classic veggie": 8.50, "garlic and aioli": 8.50, "pepperoni": 8.50, "hawaiian": 8.50, "beef and onion": 13.50, "cheesy garlic": 13.50, "chicken deluxe": 13.50, "peri peri chicken": 13.50, "buffalo chicken": 13.50}
pizza_toppings = {"extra cheese": 0.5, "ham": 0.5, "olives": 0.5, "pepperoni": 0.5, "onions": 0.5}
user_details = {"Name": "" , "Address": "", "Mobile": ""}
user_pizzas = {}
user_toppings = {}
#user_total =

name = input("What is your name? ")
user_details["Name"] = name.title()
for details, value in user_details.items():
    print(details, value)

def actions():
    """Displays the actions the user can do"""
    print("""To execute action, type: \n
    '1' to view actions
    '2' to view the menu
    '3' to place an order (maximum 5 pizzas)
    '4' to exit""")
actions()


#Create function for viewing menu
def view_menu():
    """Displays the available pizzas and toppings for order"""
    print("\nThe available pizzas that we offer are: \n{}".format("\n".join(pizzas).title()))
    print("The available toppings are: \n{}".format("\n".join(pizza_toppings).title()))
view_menu()    

#Create function for ordering pizza
def service_type():
    """Displays the options of service for the user, or to go back to menu"""
    print("\nFor delivery, enter '1'. For pick-up, enter '2'. To go back to menu, enter '3'")
    service = input("What would you like to do? ")
    if service == "1":
        print("You chose delivery.")
        repeat = True
        while repeat:
            address = input("What is the address? ")
            while repeat:    
                confirm = input("The address is {}. Is this correct? Enter 'yes' or 'no' ".format(address))
                if confirm == "yes":
                    user_details["Address"] = address
                    repeat = False
                elif confirm == "no":
                    break
                else:
                    print("Please enter 'yes' or 'no' ")
                    continue
        repeat = True
        while repeat:
            mobile = input("What mobile number should we contact you with?")
            while repeat:    
                confirm = input("The mobile number you entered is {}. Is this correct? Enter 'yes' or 'no'".format(mobile))
                if confirm == "yes":
                    user_details["Mobile"] = mobile
                    repeat = False
                elif confirm == "no":
                    break
                else:
                    print("Please enter 'yes' or 'no' ")
                    continue
            print(user_details["Mobile"])


service_type()
                
           
           
#Create function for getting details

#Create module for each action

#user_action = input("What would you like to do?")
#if user_action == "1":
    #actions()
#elif user_action == "2":

#Create function for adding total