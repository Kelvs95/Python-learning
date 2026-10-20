def sandwich():
    sandwich_type = input("Enter a sandwich type: ")
    toppings = []
    print("\nEnter 'q' to quit.")

    while True:
        tops = input("Enter a topping: ")

        if tops == "q":
            break
        toppings.append(tops)

    return sandwich_type, toppings

#my_order = sandwich()
#print(f"{my_order[0]} sandwich")
#print(f"toppings include: {my_order[1]}")