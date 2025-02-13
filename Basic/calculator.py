num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

sum = num1 + num2
diffrence = num1 - num2
product = num1 * num2

if num2 == 0:
    print("Cannot divide by zero")
else:
    quotient = num1 / num2

print("Sum: ", sum)
print("Difference: ", diffrence)
print("Multiplication: ", product)
print("Divison: ", quotient)
