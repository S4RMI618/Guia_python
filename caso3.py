def sum_of_divisors(n):
    # Returns the sum of all divisors of n
    result = 0
    for i in range(1, n):
        if n % i == 0:
            result += i
    return result

def is_perfect_number(n):
    # Returns True if n is a perfect number
    return sum_of_divisors(n) == n

def get_perfect_number(position):
    # Returns the perfect number at the given position
    current_position = 0
    current_number = 1
    while True:
        if is_perfect_number(current_number):
            current_position += 1
        if current_position == position:
            return current_number
        current_number += 1

# Get the user's input
position = int(input("Enter a position: "))

# Calculate and print the result
result = get_perfect_number(position)
print("The perfect number at position", position, "is", result)