print("Enter details.")
print("Enter 'X' to quit")

first_name = str(input("Enter first name: "))
while first_name != "X":                                       # If first_name isn't 'X', aka if the user doesn't want to quit
    if not first_name:                                      # If first_name is blank
        print("Blank first name input.")
        first_name = input("Enter first name: ")
    elif not first_name.isalpha():                          # If first_name has characters that aren't in names like numbers
        print("Invalid first name input.")
        first_name = input("Enter first name: ")
    else:
        break
if first_name == "X":                                                       # If 'X' is entered
    print("Quitting...")
    quit()
    
surname = str(input("Enter surname: "))
while surname != "X":                                       # If first_name isn't 'X', aka if the user doesn't want to quit
    if not surname:                                      # If first_name is blank
        print("Blank surname input.")
        surname = input("Enter surname: ")
    elif not surname.isalpha():                          # If first_name has characters that aren't in names like numbers
        print("Invalid surname input.")
        surname = input("Enter surname: ")
    else:
        break
if surname == "X":                                                       # If 'X' is entered
    print("Quitting...")
    quit()

age = input("Enter age: ")
while age != "X":                                              # If age isn't X, aka if the user doesn't want to quit
    if not age:                                             # If age is blank or has characters that aren't in ages like letters
        print("Blank age input.")
        age = input("Enter age: ")
    elif not age.isnumeric():
        print("Invalid age input.")
        age = input("Enter age: ")
    elif int(age) < 18 or int(age) > 70:
        print("not within range")
        age = input("Enter age: ")
    else:
        break
if age == "X":                                                      # If 'X' is entered
    print("Quitting...")
    quit()

former_company = input("Enter former company: ")
while former_company != "X":
    if not former_company:
        print("Blank former company input.")
        former_company = input("Enter former company: ")
    elif not former_company.isalpha():
        print("Invalid former company input.")
        former_company = input("Enter former company: ")
    else:
        break
if former_company == "X":
    print("Quitting...")
    quit()

skill_type = input("Enter skill type: ")
while skill_type != "X":
    if not skill_type:
        print("Blank skill type input.")
        skill_type = input("Enter skill type: ")
    elif not skill_type.isalpha():
        print("Invalid skill type input.")
        skill_type = input("Enter skill type: ")
    elif not(skill_type == "Programming" or skill_type == "Cybersecurity" or skill_type == "Engineering" or skill_type == "Data Analysis" or skill_type == "Administration"):
        print("nonononononono")
        skill_type = input("Enter skill type: ")
    else:
        break
