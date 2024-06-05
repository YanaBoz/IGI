import os
from pr_1 import task1
from pr_2 import task2
from pr_3 import task3
from pr_4 import task4
from pr_5 import task5
from colorama import Fore, Back, Style

while True:
    print(Fore.RED + "hi")
    while True:
       choice = input("Select one of the five task numbers:")
       try:
        choice = int(choice)
        break
       except ValueError:
         print (f"ERROR")
    while choice>5 or choice<=0:
        print (f"ERROR")
        while True:
         choice = input("Select one of the five task numbers:")
         try:
          choice = int(choice)
          break
         except ValueError:
           print (f"ERROR")
    choice = str(choice)    
    match choice:
        case "1":
            task1()
        case "2":
            task2()
        case "3":
            task3()
        case "4":
            task4()
        case "5":
            task5()
        case _:
            print("Program was finished ")
            break
    choice = input("Would you like to perform another task? (y/n): ").lower()
    if choice == "n":
        print("Program was finished ")
        break
    elif choice != "y":
        print("Invalid choice. Program was finished ")
        break
    else:
        os.system('cls')
        continue