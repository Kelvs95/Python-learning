#Basic function

def create_ui_element(text, element_type):
    return f"<{element_type}>{text}</{element_type}>"

print(create_ui_element("Click Me", 'button'))

#Adding default parameters

def create_ui_element(text,
                      element_type="button",
                      color="blue",
                      size="medium"):
    style = (f"color: {color}; "
             f"font-size: {size};")
    return (f'<{element_type} '
            f'style="{style}">'
            f'{text}'
            f'</{element_type}>')

print(create_ui_element("Submit"))

def create_ui_element(text,
                      elementtype="button",
                      color="red",
                      size="medium",
                      **kwargs):
    attributes = '' # Process additional attributes
    # from kwargs for key, value in kwargs.items():
    # attributes += f' {key}="{value}"'

#LAMBDA
#BASIC fucntion (def)

def add_value(x):
    return x + 5
print(add_value(12))

#Lambda
add_five_lambda = lambda x: x + 5
print(add_five_lambda(22))

numbers = [10, 21, 34, 45, 56]
divide_lambda = lambda x: x % 2 == 0
# filter for numbers divisible by 2 in numbers
even_numbers = list(filter(divide_lambda, numbers))
print(even_numbers)

#map
numbers = [1, 2, 3, 4]
squared_numbers = list(map(lambda x: x ** x, numbers))
print(squared_numbers)

#filter
numbers1 = [1, 2, 3, 4, 5, 6]
even_numbers1 = list(filter(lambda x: x % 2 == 0, numbers1))
print(even_numbers1)

# Initializing a class aeroplane
class aeroplane:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        print(f"This is a {self.make} {self.model}")


plane = aeroplane("Antonov", "8745")
plane.display_info()

#Without a class
def display_specs(make, model):
    print(f"This is a {make} {model}.")

display_specs("Tesla", "Model Y")

#Basically, we can initiate a function without defining a class
#However, when you want to define a class you use "self"
#because the method works with the object's attributes

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} : ${self.price}"

item1 = Product("Laptop", 1200)
item2 = Product("Mouse", 25)
print(item1)
print(item2)


#DEPOSITING MONEY INTO A BANK ACCOUNT
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount


accounts = {
    "1001": BankAccount("1001", 500),
    "1002": BankAccount("1002", 1000)
}

account_number = input("Enter your bank account number: ")

if account_number in accounts:
    account = accounts[account_number]

    print(f"Current balance: ${account.balance:.2f}")

    deposit_amount = float(input("Enter the deposit amount: "))
    account.deposit(deposit_amount)

    print(f"New balance: ${account.balance:.2f}")
else:
    print("Account not found.")

#-------------------------------------------------------------------------
def login():
    user_list = ["admin", "Kay", "Ceci", "Tune"]
    username = input("Enter your username: ")

    for users in user_list:
        if users == 'admin' and username == 'admin':
            print(f"Hello {username}, would you like "
              f"to see a status report")
            return
        else:
            print(f"Hello {username}, thank "
              f"you for logging in again")
            return
login()

#Another approach
user_list = ["admin", "Kay", "Ceci", "Tune"]
username = input("Enter your username: ")
if username == "admin":
    print(f"Hello {username}, would you like to see a status report")

else:
    print(f"Hello {username}, thank you for logging in again")
#---------------------------------------------------------------------
hello_admin = []
if not hello_admin:
    print("We need to find more users!")
else:
    print(f"Hello, {hello_admin}")
print(hello_admin)
#------------------------------------------------
current_users = ['mair', 'arpu', 'fatou', 'shak', 'vero']
new_users = ['VERO', 'fatou', 'nneji', 'uwalaka', 'ibe']

#we use .lower to make the list case insensitive
for names in new_users:
    if names in [user.lower() for user in current_users]:
        print(f'Username {names} already exits')
    else:
        print(f"Username {names} is available")

#--------------------------------------------------------------
ordi_numbers = list(range(1,10))
for numbers in ordi_numbers:
    if numbers == 1:
        print("1st")
    elif numbers == 2:
        print("2nd")
    elif numbers == 3:
        print("3rd")
    else:
        print(f"{numbers}th")
#-----------------------------------------------------------



