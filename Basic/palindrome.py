text = input("Enter a word or number: ")
if text == text[::-1]:
    print(text, "is a palindrome")
else:
    print(text, "is not a palindrome")
