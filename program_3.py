#Total Purchase
#Samuel Renneke, 1/30/2026
def calculate_total_purchase():
    #inputs
    item_1 = input("Enter price of item 1: ")
    item_1 = float(item_1)
    item_2 = input("Enter price of item 2: ")
    item_2 = float(item_2)
    item_3 = input("Enter price of item 3: ")
    item_3 = float(item_3)
    item_4 = input("Enter price of item 4: ")
    item_4 = float(item_4)
    item_5 = input("Enter price of item 5: ")
    item_5 = float(item_5)
    #Calculations
    subtotal = round(item_1 + item_2 + item_3 + item_4 + item_5, 2)
    sales_tax = round(subtotal - (subtotal * 0.07), 2)
    total = subtotal + sales_tax
    #Prints
    print('Subtotal = ', subtotal)
    print('Sales tax = ', sales_tax)
    print('Total = ', total)
    
#Calls function
calculate_total_purchase()
