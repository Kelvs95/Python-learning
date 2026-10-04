cars = ['audi', 'volvo', 'mazda', 'tesla', 'byd']
for car in cars:
    if car == 'tesla':
        print(car.upper())
    else:
        print(car.title())
#If the current value of car in the list is a tesla, print the result
# in uppercase, else just capitalize the first letter of each car name.

car = 'Audi'
print(car == 'audi')
print(car.lower() == 'audi')

#Checking for inequality
toppings = 'grilled onions'
if toppings != 'mushrooms':
    print('Hold the mushrooms!')

#Checking for multiple conditions
age_0 = 18
age_1 = 25
if age_0 >= 18 and age_1 >= 25:
    print(False)
else:
    print(True)

banned_users = ['Ceci', 'Kelvin', 'tune']
user = 'Marie Lakin'

if user not in banned_users:
    print(user.title() + ', you can post a response if you wish')


#TRY IT YOURSELF SEGMENTS
trucks = ['hilux', 'tundra', 'f-150', 'gmc']
new_truck = 'f-150'

for new_truck in trucks:
    if new_truck != 'f-150':
        print("i'm sorry, that is not my new truck")
    else:
        print('hooray!, you just guessed correct as '+ new_truck.title())

age = 17
if age >= 18:
    print('You are old enough to vote')
    print('\nHave you registred to vote yet?')
else:
    print('Sorry, you are too young to vote')
    print('\nPlease, register to vote as soon as you turn 18')

# If-elif-else Chain

# Scenario - Admission for anyone under 4 is free
# Admission for anyone between the ages of 4 and 18 is $5
# Admission for anyone age 18 or older is $10

age = 12

if age < 4:
    print('Your admission cost is $0')
elif age < 18:
    print('Your admission cost is $5')
else:
    print('Your admission cost is $10')

age = 27

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 0

print('\nYour admission cost is $' + str(price) + '.')

alien_color = ['green', 'yellow', 'red']
if alien_color[0] == 'green':
    print('Great, you just earned 5 points')

alien_color = 'yellow'
if alien_color == 'green':
    points = 5
else:
    points = 10

print('\nYou just earned ' + str(points) + ' points')

alien_color = 'red'
if alien_color == 'green':
    points = 5
elif alien_color == 'yellow':
    points = 10
else:
    points = 15

print('\nYou just earned ' + str(points) + ' points')

#Stages of Life

age = 31
if age < 2:
    person = 'baby'
elif age >= 2 and  age < 4:
    person = 'toddler'
elif age >= 4 and age < 13:
    person = 'kid'
elif age >= 13 and age < 20:
    person = 'teenager'
elif age >= 20 and age < 65:
    person = 'adult'
else:
    person = 'elder'
print('\nYou are a/an ' + person.title())

p_data = [10, 15, 20, 25, 30, 35, 40]
result = []
for item in p_data:
    if item > 20:
        result.append(item * 2)
print(result)


available_toppings = ['mushrooms', 'olives', 'green peppers'
                      'pepperoni', 'pineapple', 'extra cheese'
                      ,'extra patty']
requested_toppings = ['olives', 'French fries', 'extra patty']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("\nAdding " + requested_topping + ".")
    else:
        print("\nSorry, we do not have " + requested_topping + ".")
print("\nFinished making your Pizza!")

#Finding first negative number
py_numbers = [10, 25, 30, -5, 40, 50]
found_number = None
for num in py_numbers:
    if num < 0:
        found_number = num
        break
print(f"The first negative number found is: {found_number}")

total = 0
data_points = [15, 20, -10, 5, -5, 0, 25]

for point in data_points:
    if point < 0:
        continue
    if point == 0:
            break
    total += point
print(total)

# Accessing data in a 3 X 3 matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
#for d_mat in range(len(matrix)):

print(matrix[2][2])

#combinational operations
items = [1, 2, 3, 4]
pairs = []

for i in range(len(items)):
    for j in range(i + 1, len(items)):
        pairs.append((items[i], items[j]))
print(pairs)

for number in range(1, 11):
    if number == 5:
        break

print("Loop finished")

count = 0

while count < 10:
    print(count)

    if count == 3:
        break
    count += 1


dat_points = [10, -5, 8, 0, 15, -2, 7]
result = []

for num in dat_points:
    if num <= 0:
        continue
    if num > 10:
        break
        
    result.append(num * 2)

print(result)

counter = 0

for i in range(1, 10):

    # Skips even numbers

    if i % 2 == 0:

        continue
print(i)

data_list = ([10, 25, 5, 30, 15])
def process_data(data_list):
    total = 0
    for item in data_list:
        if item > 20:
            total += item
        if total > 50:
            return total
        else:
            total += 5
    return total
print(process_data(data_list))

def show_welcome():
    print('\nWelcome to the lesson on functions')

show_welcome()

def add(x, y):
    return x + y
sum_result = add(5, 10)
print(sum_result
      )

def show_status(is_active):
    if is_active:
        print("\nsystem is online")
    else:
        print("\nsystem is offline")
#
output = show_status(False)
#print function will produce NONE
print(output)

#Error simulation of variables not mentioned in the global or local scope
# taxrate
#def calculate_price():
 #   tax_rate = 0.07 # Local variable
  #  return 100 * (1 + taxrate)
#final_price = calculate_price()
#print(f"The tax rate was: {taxrate}")

def calculate(base_price, tax_rate):
    return base_price * tax_rate
print(calculate(base_price= 100, tax_rate= 0.05))

def calculate_total(base_price):
    tax_rate = 0.05
    tax = base_price * tax_rate
    total = base_price + tax
    return total
base_price = float(input("Enter the base price: $"))
print(f"Total including 5% tax: ${calculate_total(base_price):.2f}")

count = 10
def update_counter():
    global count

count = count + 5
update_counter()
print(count)
#The global keyword inside the update_counter function specifies
#that the code should modify the global count variable, not create
#a new local one. Therefore, the global count is successfully
#updated from 10 to 15.
count = 5

def update_counter():
    count = 0
    count += 1
    return count

result = update_counter()

task_count = 10
def log_new_session():
    task_count = 0
    task_count += 1

def complete_five_tasks():
    global task_count

task_count += 5

log_new_session()
complete_five_tasks()

#####
