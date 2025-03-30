num = int(input("Enter a number: "))
sum_of_digits = sum(int(digit) ** len(str(num)) for digit in str(num))

if num == sum_of_digits:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
