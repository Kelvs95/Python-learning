# function functionName(parameter1, parameter2):{
#       Code to be executed
#}

#functionName(argument1, argument2)

def calculate_price(base_cost, tax_rate):
    total = base_cost + (base_cost * tax_rate)
    return total #return total basically tells the code to run
                # total and return it in the function that called it

final_price = calculate_price(100, 0.08)
print(final_price)

def calculate_area(width, height):
    area = width * height
    return area
print(calculate_area(4.65, 15))

#Calculating final cost after discount and tax

def calculate_finalprice(item_price, discount):
    initial_discount = item_price * discount
    return item_price - initial_discount

def applytax(price):
    tax_rate = 0.10
    return price * (1 + tax_rate)

discounted = calculate_finalprice(200, 0.25)
print(discounted)
final_price = applytax(discounted)
print(final_price)

value = 100
def scope_test():
    value = 50
    print("inside function:", value)
scope_test()
print("outside function:", value)
print(f"Outside function: {value}")

