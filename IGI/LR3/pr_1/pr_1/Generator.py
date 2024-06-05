def my_generator(first, last, step):
    """Creating my own generator."""
    number = first
    while number < last:
        yield number
        number += step

def initialize_with_user_input():
    """Initialize sequence using user input."""
    sequence = []
    while True:
        try:
            number = int(input("Enter an integer number (Enter > 100 to end): "))
            if number > 100:
                break
            sequence.append(number)
        except ValueError:
            print("Wrong input. Please enter an integer number.")
    return sequence