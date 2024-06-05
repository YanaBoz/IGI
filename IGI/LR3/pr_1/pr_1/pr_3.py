# Program: Text analysis(3 task)
# Lab: Lab 1
# Version: 1.0
# Bozhko Yana
# 02.05.2024

def is_binary(string):
    for char in string:
        if char not in ['0', '1']:
            return False

    return True


def task3():
    string = input("x: ")

    if is_binary(string):
        print("TRUE")
    else:
        print("FALSE")


if __name__ == "__main__":
    task3()
