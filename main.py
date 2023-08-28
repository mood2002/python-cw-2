my_name= input("what is your name?")
my_age= input("how old are you")

print(f"my name is {my_name} and i am {my_age} years old")

frist_number=int(input("enter frist_number") )
secound_number=int(input("enter secound_number"))
operation=(input("enter operation: "))
if operation == '+':
    print(frist_numder+second_number)
elif operation == '-': 
    print(frist_number-secound_number)
elif operation == '*':    
    print(frist_number*secound_number)
elif operation == '/':
    print(frist_number/secound_number)
else:
    print("not valid")
    
bus_capacity=(30)
people_inbus=input("enter the number of people who ride the bus")
people_waiting=int(input(how many prople are waiting))
empty_seats = bus_capacity - people_inbus
if empty_seats>outside_the_bus:
    print("there are seats on the bus")
else:
    print("the bus is full")