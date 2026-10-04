# Author Chijioke Okeke

def print_even_odds(n: int):
    if  n % 2 == 0:
        print("Even number")
    else:
        print("Odd number")


if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print_even_odds(n)


