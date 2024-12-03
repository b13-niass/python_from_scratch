# 1. Nested list comprehension
matrix = [[j for j in range(3)] for _ in range(3)] # Result: [[0, 1, 2], [0, 1, 2], [0, 1, 2]]

# 2. Transforming strings
names = ['alice', 'bob', 'charlie']
capitalized_names = [name.capitalize() for name in names] # Result: ['Alice', 'Bob', 'Charlie']