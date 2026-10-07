current_age = 31
years_to_add = int(input("Enter years to add: "))
future_age = int(current_age + years_to_add)

#print(future_age)
print(f"In {years_to_add} years, you will be {future_age}"
      f" years old.")
#__________________________________________________________
item_price = 150
taxrate = 0.08
itemtax = item_price * taxrate
total_cost = item_price + itemtax

print(f"\nTotal cost: ${total_cost}")
#____________________________________________________-----\
## A SIMPLE CALCULATOR
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# prompt the user for which operation
op = input("Enter operation (+, -, /, *): ")

if op == "+":
    value = num1 + num2
    print(f"{value}")
elif op == "-":
    value = num1 - num2
    print(f"{value}")
elif op == "/" and num2 != 0:
    value = num1 / num2
    print(f"{value}")
elif op == "*":
    value = num1 * num2
    print(f"{value}")
else:
    print("Invalid operation")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#CONVERT Celcius to Farenheit F = (c * 9/5) + 32
celsius_str = (
    float(input("\nEnter your temperature in Celsius: ")))

fahrenheit = (celsius_str * 9/5) + 32

print(f"\nThe temperature in Fahrenheit is {fahrenheit}")

#7% sales tax
item_name = "Gadget"
quantity = 5
price_per_item = 12.50
print(f"\nOrder Summary: {quantity} "
      f"units of {item_name} at "
      f"${price_per_item * quantity * 1.07:.2f} total.")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
questions = [
    ("What is 2 + 2?", "4"),
    ("What is the capital of France?", "paris"),
    ("What keyword is used to define a function in Python?", "def")
]

score = 0

for question, correct_answer in questions:
    answer = input(question + " ")

    if answer.lower() == correct_answer:
        score += 1

print(f"You scored {score} out of {len(questions)}")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`
