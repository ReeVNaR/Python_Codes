
my_tuple = ("apple", "banana", "cherry", 42, 3.14)


print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])


print("Sliced tuple (index 1 to 3):", my_tuple[1:4])


print("Length of tuple:", len(my_tuple))


print("Items in tuple:")
for item in my_tuple:
    print(item)

new_tuple = my_tuple + ("orange", "grape")
print("Concatenated tuple:", new_tuple)


if "banana" in my_tuple:
    print("Yes, 'banana' is in the tuple!")

nested_tuple = (my_tuple, ("x", "y", "z"))
print("Nested tuple:", nested_tuple)


