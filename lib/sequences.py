#!/usr/bin/env python3  # Specifies that the script should be run using Python 3

# Define a function to generate and print a Fibonacci sequence of a specified length
def print_fibonacci(length):
    # Initialize the Fibonacci sequence with the first two numbers: 0 and 1
    fibonacci = [0, 1]
    
    # Get the current length of the Fibonacci list (starts with 2 because of [0, 1])
    current_length = len(fibonacci)
    
    # Set the last and second-to-last numbers in the sequence
    last_number = fibonacci[-1]        # Last number in the list (1 initially)
    second_last_number = fibonacci[-2]  # Second-to-last number in the list (0 initially)

    # Handle the edge case where the desired length is 0
    if length == 0:
        print([])  # Print an empty list since no numbers are needed
        return     # Exit the function

    # Handle the edge case where the desired length is 1
    if length == 1:
        print([0])  # Print a list with only the first Fibonacci number
        return      # Exit the function

    # Use a while loop to generate the sequence until it reaches the desired length
    while current_length < length:
        # Calculate the next number in the sequence as the sum of the last two numbers
        next_number = last_number + second_last_number
        
        # Add the next number to the Fibonacci list
        fibonacci.append(next_number)
        
        # Update the last and second-to-last numbers for the next iteration
        last_number = fibonacci[-1]        # Update to the new last number
        second_last_number = fibonacci[-2]  # Update to the new second-to-last number
        
        # Update the current length of the list after adding the new number
        current_length = len(fibonacci)

    # Print the final Fibonacci sequence after generating all required numbers
    print(fibonacci)

# Call the function to test it with a length of 9
# Expected output: [0, 1, 1, 2, 3, 5, 8, 13, 21]
print_fibonacci(9)
