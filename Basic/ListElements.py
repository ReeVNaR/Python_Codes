fruits = ["apple", "banana", "cherry"]

# Access by index (0-based indexing)
print(fruits[0])  # apple
print(fruits[1])  # banana

# Negative Indexing (Last element is -1)
print(fruits[-1])  # cherry
print(fruits[-2])  # banana


# Change an element
fruits[1] = "blueberry"
print(fruits)  # ['apple', 'blueberry', 'cherry']

# Append (adds at end)
fruits.append("mango")  

# Insert at a specific index
fruits.insert(1, "grape")

print(fruits)  # ['apple', 'grape', 'blueberry', 'cherry', 'mango']
