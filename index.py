try:
 name = input("Enter your name: ")
 age = float(input("Enter your age: "))
 if age.is_integer():
    print("vrai")
 else:
    print("faux")
except ValueError:
    print("Invalid input. Please enter a valid age.")

print(f"Hello, {name}! You are {age} years old.")
