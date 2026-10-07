total = 0
for i in range(2):
    for j in range(4):
        total = total + 1

print(total)

#For nested loops: Total iterations = outer loop iterations *
# inner loop iterations
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in data:
    for element in row:
        print(element)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
for i in range(4):
    for j in range(1, i + 1):
        print("*", end="")
    print()

for i in range(5):
    print('*', end="")
print()

for i in range(1, 4):
    for j in range(1, 4):
        print("*", end="")
    print()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
output = ['orange', 'green', 'red']
print(output.pop(1))