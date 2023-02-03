"""CREATE LISTS FOR SAVE ODD AND EVEN NUMBERSZZZZ """
even_numbers = []
odd_numbers = []

while True:
    n = int(input("Type the size of the list (maximum 20):"))
    if 1 <= n <= 20:
        while len(even_numbers) + len(odd_numbers) < 2 * n:
            num = int(input("Enter a whole number: "))
            if num % 2 == 0:
                if len(even_numbers) < n:
                    even_numbers.append(num)
                else:
                    print("The even_numbers is full, please enter odd numbers.")
            else:
                if len(odd_numbers) < n:
                    odd_numbers.append(num)
                else:
                    print("The odd_numbers is full, please enter even numbers.")
        break
    print("The number should be in the range from 1 to 20")
    
print("Even numbers: ", even_numbers)
print("Odd numbers: ", odd_numbers)
