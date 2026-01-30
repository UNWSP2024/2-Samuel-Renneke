#Average Age
#Samuel Renneke, 1/30/2026
def average_age():
    #Inputs
    age_1 = int(input("Enter age 1: "))
    age_2 = int(input("Enter age 2: "))
    age_3 = int(input("Enter age 3: "))
    age_4 = int(input("Enter age 4: "))
    age_5 = int(input("Enter age 5: "))

    #Calculation
    average = round((age_1 + age_2 + age_3 + age_4 + age_5)/5, 3)

    #Print
    print(average)
# Line which calls the above function.
average_age()
