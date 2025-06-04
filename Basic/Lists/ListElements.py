fruits = ["apple", "banana", "cherry"]


print(fruits[0])  
print(fruits[1])  


print(fruits[-1])  
print(fruits[-2])  



fruits[1] = "blueberry"
print(fruits)  # ['apple', 'blueberry', 'cherry']

# Append (adds at end)
fruits.append("mango")  

# Insert at a specific index
fruits.insert(1, "grape")

print(fruits)  # ['apple', 'grape', 'blueberry', 'cherry', 'mango']


# Remove by value
fruits.remove("cherry")  

# Remove last element
fruits.pop()  

# Remove by index
del fruits[0]  

print(fruits)  # ['grape', 'blueberry']
