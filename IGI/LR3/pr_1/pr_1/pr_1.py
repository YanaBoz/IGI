# Program: Power Series Expansion of asin(x)
# Lab: Lab 1
# Version: 1.0
# Bozhko Yana
# 02.05.2024
import math

def factorial(n):
    """Calculate the factorial of a number."""
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def power(x, n):
    """Calculate the power of a number."""
    if n == 0:
        return 1
    else:
        return x * power(x, n-1)
    
def taylor_series(x, eps):
    """Calculate the value of arcsin(x) using power series expansion."""
    max_iterations=500
    n = 0
    sum = 0
    term = x
    sum += term
    n += 1
    while abs(term) > eps and n < max_iterations:
        term = factorial(2*n)/(power(4,n)*power(factorial(n),2)*(2*n+1))*power(x,(2*n+1))
        sum = sum + term
        n += 1
    if n>=1:
      return sum, n
    else:
       sum = x
       n = n  
       return sum, n

def task1():
    while True:
       x = input("Enter x:")
       try:
        x = float(x)
        break
       except ValueError:
         print (f"ERROR")
    while x>1 or x<-1:
        print (f"ERROR")
        while True:
         x = input("x:")
         try:
          x = float(x)
          break
         except ValueError:
           print (f"ERROR")
           
    while True:
       eps = input("Enter eps:")
       try:
        eps = float(eps)
        break
       except ValueError:
         print (f"ERROR")
    while eps<0:
        print (f"ERROR")
        while True:
         eps = input("eps:")
         try:
          eps = float(eps)
          break
         except ValueError:
           print (f"ERROR")
           
    value, iterations = taylor_series(x, eps)
    z = math.asin(x)
    print(f"x = {x}")
    print(f"eps = {eps}")
    print(f"Math F(x) = {z}")
    print(f"F(x) = {value}")
    print(f"eps = {iterations}")

if __name__ == "__main__":
    task1()

