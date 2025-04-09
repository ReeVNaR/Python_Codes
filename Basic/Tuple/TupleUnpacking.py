# Tuple unpacking
person = ("Pratiksha", 22, "Pune")
name, age, city = person

print("Name:", name)
print("Age:", age)
print("City:", city)

# Swapping values using tuple
a = 10
b = 20
print("\nBefore swapping: a =", a, "b =", b)

a, b = b, a

print("After swapping: a =", a, "b =", b)
