# test2.py
# testing and revising for the upcoming SAC
# Julian Jurista
# 21 April 2026

fruit_array = []

my_file = open("input.csv", "r")
fruit_string = my_file.read()
my_file.close()

for line in fruit_string.strip().split("\n"):
    fruit_array.append(line.split(","))
print(fruit_array)

output_file = open("output.csv", "w")
for row in fruit_array:
    upper_row = [item.upper() for item in row]
    output_file.write(",".join(upper_row) + "\n")
output_file.close()