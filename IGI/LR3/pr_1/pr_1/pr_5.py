# Program: Program for processing real lists
# Lab: Lab 1
# Version: 1.0
# Bozhko Yana
# 02.05.2024
def get_float_list_from_user(n):
    numbers = []
    m=1
    while m<=n:
        try:
            number = float(input("number: "))
            numbers.append(number)
        except ValueError:
            print("Uncorrect")
        m+=1    
    return numbers


def get_product_of_even_elements(numbers):
    product = 1
    for i, number in enumerate(numbers):
        if (i+1) % 2 == 0 and i!= 0:
            product *= number

    return product


def get_sum_of_elements_between_zeros(numbers):
    first_zero_index = None
    last_zero_index = None
    sum = 0

    for i, number in enumerate(numbers):
        if number == 0:
            if first_zero_index is None:
                first_zero_index = i
            else:
                last_zero_index = i

    if first_zero_index is None or last_zero_index is None:
        return 0

    for i in range(first_zero_index + 1, last_zero_index):
        sum += numbers[i]

    return sum


def print_list(numbers):
    print("List:")
    for number in numbers:
        print(number)


def task5():
    while True:
       n = input("n:")
       try:
        n = int(n)
        break
       except ValueError:
         print (f"ERROR")
    numbers = get_float_list_from_user(n)
    print_list(numbers)

    product_of_even_elements = get_product_of_even_elements(numbers)
    print(f"Product of elements: {product_of_even_elements}")

    sum_of_elements_between_zeros = get_sum_of_elements_between_zeros(numbers)
    print(f"sum of elements between zeros {sum_of_elements_between_zeros}")


if __name__ == "__main__":
    task5()
