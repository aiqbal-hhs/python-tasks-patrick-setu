pizzas = {"classic cheese": 8.50, "americano": 8.50, "ham and cheese": 8.50, "classic veggie": 8.50, "garlic and aioli": 8.50, "pepperoni": 8.50, "hawaiian": 8.50, "beef and onion": 13.50, "cheesy garlic": 13.50, "chicken deluxe": 13.50, "peri peri chicken": 13.50, "buffalo chicken": 13.50}
pizza_toppings = {"extra cheese": 0.5, "ham": 0.5, "olives": 0.5, "pepperoni": 0.5, "onions": 0.5}
user_details = {"Name": "" , "Address": "", "mobile": ""}
user_pizzas = {}
user_toppings = {}
#user_total = 

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
    print("The available pizzas that we offer are: {}".format(", ".join(pizzas)))
    print("The available toppings are: {}".format(", ".join(pizza_toppings)))
view_menu()    

#Create function for ordering pizza 
def order_pizza():
    order_type = input("Would you like for it to be delivered or pick-up?").strip().lower()
    if order_type == "pick up":
        print("To keep selecting your pizzas")
        repeat = True
        while repeat:
            

#Create function for getting details

#Create module for each action

#user_action = input("What would you like to do?")
#if user_action == "1":
    #actions()
#elif user_action == "2":

#Create function for adding total
