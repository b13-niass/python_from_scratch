# 1. Transforming existing dictionary
original_dict = {'a': 1, 'b': 2, 'c': 3}
doubled_dict = {k: v * 2 for k, v in original_dict.items()}
# Result: {'a': 2, 'b': 4, 'c': 6}

# 2. Swapping keys and values
original_dict = {'a': 1, 'b': 2, 'c': 3}
swapped_dict = {v: k for k, v in original_dict.items()}
# Result: {1: 'a', 2: 'b', 3: 'c'}

# 3. Conditional dictionary creation
words = ['hello', 'world', 'python', 'programming']
word_lengths = {word: len(word) for word in words if len(word) > 5}
# Result: {'hello': 5, 'world': 5, 'python': 6, 'programming': 11}
