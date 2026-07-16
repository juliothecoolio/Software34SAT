enter_name = input("Enter your name: ")

while not enter_name.isalpha() or enter_name == "X":
    if enter_name == "X":
        exit()
    print("Invalid input.")
    enter_name = input("Enter your name: ")
    
enter_age = input("Enter your age: ")

while not enter_age.isnumeric():
    if enter_age == "X":
        exit()
    print("Invalid input.")
    enter_age = input("Enter your age: ")

print("Hi " + enter_name + ", wow " + enter_age + " is really old!")