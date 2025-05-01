# Function that returns multiple values using a tuple
def calculate_stats(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    return total, average, maximum, minimum  # Returning as a tuple

# Sample data
data = (10, 20, 30, 40, 50)

# Call the function and unpack the result
total, avg, max_val, min_val = calculate_stats(data)

# Display the results
print("Data:", data)
print("Total:", total)
print("Average:", avg)
print("Maximum:", max_val)
print("Minimum:", min_val)
