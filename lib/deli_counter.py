katz_deli = []

def line(katz_deli):
    if len(katz_deli) == 0:
        print('The line is currently empty.')
        return 'The line is currently empty.'
    else:
        line_string = ''
        for i in range(len(katz_deli)):
            line_string += f"{katz_deli.index(katz_deli[i]) + 1}. {katz_deli[i]} "
        print(f"The line is currently: {line_string}")
        


def take_a_number(line, name):
    line.append(name)
    line_place = line.index(name) + 1
    print(f"Welcome, {name}. You are number {line_place} in line.")

def now_serving(katz_deli):
    if len(katz_deli) == 0:
        print('There is nobody waiting to be served!')
    else:
        print(f"Currently serving {katz_deli[0]}.")
        katz_deli.pop(0)


take_a_number(katz_deli, "Ada") #=> Welcome, Ada. You are number 1 in line.
take_a_number(katz_deli, "Grace") #=> Welcome, Grace. You are number 2 in line.
take_a_number(katz_deli, "Kent")

line(katz_deli) #=> "The line is currently: 1. Ada 2. Grace 3. Kent"

now_serving(katz_deli) #=> "Currently serving Ada."

line(katz_deli) #=> "The line is currently: 1. Grace 2. Kent"

take_a_number(katz_deli, "Matz") #=> Welcome, Matz. You are number 3 in line.

line(katz_deli) #=> "The line is currently: 1. Grace 2. Kent 3. Matz"

now_serving(katz_deli) #=> "Currently serving Grace."

line(katz_deli) #=> "The 
