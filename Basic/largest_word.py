sentence = input("Enter a sentence: ").split()
largest = max(sentence, key=len)
print("Largest word:", largest)
