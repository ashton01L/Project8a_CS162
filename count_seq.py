# Author: Ashton Lee
# Github User: ashton01L
# Date: 11/20/2024
# Description: Write a generator function named count_seq that doesn't require any arguments and generates a sequence
# that starts like this: 2, 12, 1112, 3112, 132112, 1113122112, 311311222112, 13211321322112, ...
def count_seq():
    """
    Generator function to produce a special-case, spoken, sequentialized count sequence

    :yields:
        str: the next term in the sequence as a string
    """
    current = "2"  # Start with the first term of the sequence
    while True:
        yield current
        next_term = []
        count = 1
        # Loop through the current sequence to calculate the next term
        for i in range(1, len(current)):
            if current[i] == current[i - 1]:
                count += 1
            else:
                next_term.append(str(count))
                next_term.append(current[i - 1])
                count = 1
        # Append the last group
        next_term.append(str(count))
        next_term.append(current[-1])
        current = ''.join(next_term)  # Update to the next term as a string


# Example usage
def test_row_puzzle():
    """
    Demonstrates count_seq() generator by printing first 20 terms of it
    """
    my_gen = count_seq()
    for i in range(20):
        print(next(my_gen))
