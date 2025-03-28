def count_vowels(text):
    return sum(1 for char in text.lower() if char in "aeiou")

sentence = input("Enter a sentence: ")
print("Number of vowels:", count_vowels(sentence))
