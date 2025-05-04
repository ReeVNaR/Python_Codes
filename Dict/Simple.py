def get_meaning(word, dictionary):
    word = word.lower()
    if word in dictionary:
        return dictionary[word]
    else:
        # Suggest similar words
        suggestions = [w for w in dictionary if word in w or w in word]
        if suggestions:
            return f"Word not found. Did you mean: {', '.join(suggestions)}?"
        return "Word not found in dictionary."

def main():
    # Sample dictionary
    my_dict = {
        "python": "A programming language.",
        "dictionary": "A collection of key-value pairs.",
        "algorithm": "A step-by-step procedure to solve a problem.",
        "data": "Facts and statistics collected for reference or analysis.",
        "variable": "A storage location identified by a name."
    }

    print("📘 Welcome to the Mini Dictionary!")
    while True:
        word = input("\nEnter a word (or type 'exit' to quit): ")
        if word.lower() == 'exit':
            break
        print("🔍 Meaning:", get_meaning(word, my_dict))

if __name__ == "__main__":
    main()
