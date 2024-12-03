
fruits = ["apple", "banana", 10, "date", "elderberry"]

for fruit in fruits:
    print(fruit)

try:
    for i in range(0, fruits.__len__(), 2):
        print(fruits[i])
except IndexError:
    print("Error: Index out of range")