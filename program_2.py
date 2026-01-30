#Average Age
#Samuel Renneke, 1/30/2026
def average_age():
    age_1 = input("Enter age 1: ")
    age_1 = int(age_1)
    age_2 = input("Enter age 2: ")
    age_2 = int(age_2)
    age_3 = input("Enter age 3: ")
    age_3 = int(age_3)
    age_4 = input("Enter age 4: ")
    age_4 = int(age_4)
    age_5 = input("Enter age 5: ")
    age_5 = int(age_5)

    average = round((age_1 + age_2 + age_3 + age_4 + age_5)/5, 3)

    print(average)
# Line which calls the above function.
average_age()
