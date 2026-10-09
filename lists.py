# In Python, square brackets ([]) indicate a list, and individual elements
# in the list are separated by commas.
#from script import quantity

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0].title())
print(bicycles[1].title())
print(bicycles[2].title())
print(bicycles[3].title())


#If we want to extract starting from the right side of the list or end of list
print(bicycles[-1].title())
print(bicycles[-2].title())

output = "My first bicycle was a " + (bicycles[1].title()) + "."
print(output)

#Changing, Adding, and Removing Elements
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

#Adding using .append()
motorcycles.append('ducati')
print(motorcycles)

#Creating an empty list
cities = []
cities.append('Toronto')
cities.append('Paris')
cities.append('London')
cities.append('Lagos')
cities.append('Swansea')

print(cities)

#adding a new city to the list and deciding exactly
#where it should be(position) on the list, use .insert(position, str)

cities.insert(3, 'Accra')
print(cities)

#Removing element from the list use del

del cities[2]
print(cities)

del cities[-3]
print(cities)

#We can also remove an item from a list using pop()
#Pop() removes the last item on the list but still allows you to work with it
popped_cities = cities.pop(-3)
#without specifying the index to pop, the function pops the last item
#it can be useful to get the most recent item purchased
print(cities)
print(popped_cities)

last_visit = "The recent city i visited was " + popped_cities + "."
print(last_visit)

#Removing an item by value
bicycles.remove("trek")
print(bicycles)


#Organizing a list using Sort(), in this case, we are sorting the list
# permanently
phones = ['Iphone', 'Samsung', 'Huawei', 'OnePlus', 'Redmi']
phones.sort()
print(phones)

#To sort a list temporarily
phones1 = ['Iphone', 'Samsung', 'Huawei', 'OnePlus', 'Redmi']

print(sorted(phones1))
print(phones1)
print(phones1[-3])

#finding the length of a list
print(len(phones))


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Using enumerate ()
courses = ["physics", "biology", "chemistry", "agric"]
for index, course in enumerate(courses):
    print(f" Course #{index}: {course.title()}")

subjects = ['History', 'Music', 'Physics']
for i, subject in enumerate(subjects, start=1):
    if i == 2: print(f"The second subject is {subject}")


#~~~~~~~~~~~~~~~~ LIST COMPREHENSIONS ~~~~~~~~~~~~~~~~~~~~~~~~~
#Traditional code
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
evens = []
for x in numbers:
    if x % 2 == 0:
        evens.append(x)

print(evens)

#List Comprehensions
evens = [x for x in numbers if x % 2 == 0]
print(evens)

temperatures = [68, 75, 52, 81, 49, 90]
temps = [x for x in temperatures if x >= 70]
print(temps)

new_list = [i*i for i in range(10) if i % 2 == 0]
print(new_list)

#List slicing
s = 'programming'
print(s[::3])
print(s[1:9:2])
print(s[::-1])
print(s[7::-2])
print(s[4:9:1])

data = "0123456789"
print(data[8:1:-2])

# F- String
username = "Alex"
user_role = "Admin"
message = f"User '{username}' has the role {user_role}"
print(message)

order_id = 101
quantity = 3
price = 25
message1= (f"Order #{order_id}: {quantity} "
           f"items for a total of ${price * quantity:.2f}")
print(message1)

# .format() method
greeting = "Hello, {}!, Welcome to {}"
print(greeting.format("Learner", "Python"))

# .find()
text = "hello world"
position = text.find("o")
print(position)

report = "Customer ID: [CUSTID], Order ID: [ORDERID]"
final_report = report.replace("[CUSTID]",
                              "C4815").replace("[ORDERID]",
                                               "O9263")
print(final_report)

# Split() method is a good method of preparing texts for analysis
sentence = "This is a sample sentence."
print(sentence.split())

fruit = "Apple, 0.50, fruit"
print(fruit.split(","))

record = "2023-11-15,LOGIN,user_jane,SUCCESS"
record_user = record.split(",")[2]
print(record_user)

my_string = 'hello, world'
print(my_string[7:12])

s = "user:john doe"
print(s.upper().replace(":", ":-").replace(" ", "-"))

data = '1,2,3,4,5'
print(data.split(","))

