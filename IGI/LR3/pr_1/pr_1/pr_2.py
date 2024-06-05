# Program: Finding the sum of a sequence of numbers
# Lab: Lab 1
# Version: 1.0
# Bozhko Yana
# 02.05.2024
import Generator

def count_odd_numbers(sequence):
    count = 0
    for num in sequence:
        if num < 0:
            count += num
    return count

def task2():
    while True:
      choice = input("('g' generation, 'u' by yourself): ").lower()
      if choice == 'g':
        sequence = list(Generator.my_generator(-10, 0, 1))
        break
      elif choice == 'u':
        sequence = Generator.initialize_with_user_input()
        break
      else:
        print("Unright.")
        continue
      
    print (f"{sequence}{count_odd_numbers(sequence)}")

if __name__ == "__main__":
    task2()
