class BankAccount:
    def __init__(self, name, balance = 0):
        self.name = name
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
        else:
            print("Insufficent funds")
    def get_balance(self):
        return self._balance
#In Python, self is a convention for the first parameter of an instance method.
# It is a reference to the object instance itself.

my_account = BankAccount('John Doe', 100)
my_account.withdraw(500)

print(my_account)

my_account.deposit(300)
get_balance = my_account.get_balance()
print(get_balance)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Dog:
    def __init__(self, name):
        self.name = name
# Sets the name for this specific dog

    def speak(self):
        print(f"{self.name} says woof!")
# Accesses the name of this specific dog print(f"{self.name} says woof!")

dog1 = Dog("Fido")
dog2 = Dog("Buddy")

dog1.speak() # Output: Fido says woof! dog2.speak() #
dog2.speak()


for x in range(5, 10):
    print(x)



