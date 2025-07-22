def find_duplicates(lst):
    seen = set()
    duplicates = set()
    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return list(duplicates)

# Example
print(find_duplicates([1, 2, 3, 2, 4, 1]))  # Output: [1, 2]
