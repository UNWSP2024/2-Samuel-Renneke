#Total Purchase
#Samuel Renneke, 1/30/2026
def calculate_total_purchase():

    #Inputs
    item_1 = float(input("Enter price of item 1: "))
    item_2 = float(input("Enter price of item 2: "))
    item_3 = float(input("Enter price of item 3: "))
    item_4 = float(input("Enter price of item 4: "))
    item_5 = float(input("Enter price of item 5: "))

    #Calculations
    subtotal = round(item_1 + item_2 + item_3 + item_4 + item_5, 2)
    sales_tax = round(subtotal - (subtotal * 0.07), 2)
    total = subtotal + sales_tax

    #Prints
    print('Subtotal = ', subtotal)
