num = int(input("Enter a number: "))
sum_digits = sum(int(digit) for digit in str(num))
print("Sum of digits:", sum_digits)
