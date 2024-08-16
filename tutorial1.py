from pizzapy import Customer, StoreLocator, Order

# def searchMenu(menu):
#     print("You are now searching the menu...")
#     while True:
#         item = input("Type an item to look for : ").strip().lower()
#         if item !="" and len(item)>1:
#             item = item[0].upper() + item[1:]
#         else:
#             print("Please enter a valid item name")
#             break
    
#         print(f"Results for: {item}")
#         menu.search(Name=item)
        
def searchMenu(menu):
    print("You are now searching the menu...")
    
    item = input("Type an item to look for : ").strip().lower()
    if item !="" and len(item)>1:
        item = item[0].upper() + item[1:]
        print(f"Results for: {item}")
        menu.search(Name=item)
        print()
    else:
        print("No results")

    
    print(f"Results for: {item}")
    menu.search(Name=item)
        
def addToOrder(order):
    print("Please type the codes of the items you'd like to order...")
    print("Please ENTER to stop ordering.")
    while True:
        item = input("Code: ").upper()
        try:
            order.add_item(item)
        except:
            if item == "":
                break
            print("Invalid Code...")        
        
customer= Customer("Akshaya", "Murali", "akshayam1712@gmail.com", "9057678989", "40 Bay St, Toronto,  ON, M5J2X2")
# customer = Customer('Barack', 'Obama', 'barack@whitehouse.gov', '2024561111', '700 Pennsylvania Avenue NW, Washington, DC, 20408')
my_local_dominos = StoreLocator.find_closest_store_to_customer(customer)

print(customer)
print(my_local_dominos)
print("\nMENU\n")

menu = my_local_dominos.get_menu()
# menu.search(Name="Coke")

order = Order.begin_customer_order(customer, my_local_dominos, "ca")

while True:
    searchMenu(menu)
    addToOrder(order)
    answer=input("WOuld you like to add more items(y/n)? ")
    if answer.lower() not in ["yes", "y"]:
        break
    
print("Your order is as follows: ")
print(order)
for item in order.data["Products"]:
    print(item["Code"])
    