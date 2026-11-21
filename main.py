def sum_numbers(n):
    if n == 0:
        return 0
    else:
        return n + sum_numbers(n - 1)
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent - 1)
choice = ""
while choice != "q":
    print("===== recursive number explorer =====")
    print("1. sum of natural numbers")
    print("2. factorial calculator")
    print("3. power calculator")
    print("q. quit")
    choice = input("enter your choice: ")
    if choice == "1":
        n = int(input("enter a nonnegative integer: "))
        print("sum of natural numbers:", sum_numbers(n))
    elif choice == "2":
        n = int(input("enter a nonnegative integer: "))
        print("factorial:", factorial(n))
    elif choice == "3":
        base = int(input("enter a base: "))
        exponent = int(input("enter a nonnegative integer exponent: "))
        print("power:", power(base, exponent))
    elif choice == "q":
        print("thank you for using recursive number explorer.")
    else:
        print("invalid choice. please try again.")