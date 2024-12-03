
try:
    a, b = input("Enter two values separated by a space: ").split(sep=",")
    print(f"the sum of {a} and {b} is: {int(a) + int(b)}")
except ValueError:
    print("Invalid input. Please enter two integers separated by a space.")
