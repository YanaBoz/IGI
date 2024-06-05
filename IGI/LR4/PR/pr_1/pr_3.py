# Program: Power Series Expansion of asin(x)
# Lab: Lab 1
# Version: 1.0
# Bozhko Yana
# 02.05.2024
import numpy as np
import matplotlib.pyplot as plt
import django as dj
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
    Solve = []
    while abs(term) > eps and n < max_iterations:
        Solve.append(term)
        term = factorial(2*n)/(power(4,n)*power(factorial(n),2)*(2*n+1))*power(x,(2*n+1))
        sum = sum + term
        n += 1
    if n>=1:
      Solve.append(term)
      return sum, n, Solve
    else:
       Solve.append(term)
       sum = x
       n = n  
       return sum, n, Solve

def calculate_sum(x, eps):
    max_iterations=500
    n = 0
    sum = 0
    term = x
    sum += term
    n += 1
    Solve = []
    while abs(term) > eps and n < max_iterations:
        Solve.append(term)
        term = factorial(2*n)/(power(4,n)*power(factorial(n),2)*(2*n+1))*power(x,(2*n+1))
        sum = sum + term
        n += 1
    if n>=1:
      Solve.append(term)
      return sum
    else:
       Solve.append(term)
       sum = x
       n = n  
       return sum

class ploter():
    """
    Draws graph
    :param x_min:
    :param x_max:
    :param step:
    :param path_to_file:
    :return: plot
    """
    def plot (self, x_min, x_max, step, path_to_file=None):
      x = np.arange(x_min, x_max, step)#Возвращает равномерно распределенные значения в пределах заданного интервала
      y_series = [calculate_sum(xi, 0.001) for xi in x]
      y_function = [math.asin(xi) for xi in x]

      fig, ax = plt.subplots() #Создание объекта рисунка и объекта осей
      ax.grid(True) #Включение сетки

      plt.plot(x, y_series, color="green")
      plt.plot(x, y_function, color="red")
      plt.xlabel('x')
      plt.ylabel('asin(x)')
      plt.legend(['math.asin', 'taylor series for asin'])
      plt.annotate("Asin", xy=(1, -0.3), xytext=(1, -0.3))
      plt.title("Function:")
      plt.text(-2, 0.3,"Func:\nAsin")
 
      if path_to_file:
          try:
              plt.savefig(path_to_file)#Сохраните текущую фигуру в виде изображения или векторной графики в файл
          except ValueError as e:
              print(f"ERROR {e}.")

      plt.show()

def task3():
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

    Series = []       
    value, iterations, Series = taylor_series(x, eps)
    z = math.asin(x)
    print(f"x = {x}")
    print(f"eps = {eps}")
    print(f"Math F(x) = {z}")
    print(f"F(x) = {value}")
    print(f"eps = {iterations}")
    Copy = []
    Copy = Series
    print(f"Data: {Copy}")
    print(f"Average: {np.average(Copy)}")
    print(f"Median: {np.median(Copy)}")
    vals, counts = np.unique(Copy, return_counts=True)
    mode_value = np.argwhere(counts == np.max(counts))#Найдите индексы элементов массива, которые не равны нулю, сгруппированные по элементам.
    print(f"Mode: {(vals[mode_value])}")
    print(f"Dispersion {np.var(Copy)}")
    print(f"Average square deviation: {np.std(Copy)}")
    Ploter = ploter
    Ploter.plot(Series,-1,1,eps,'plot.png')

if __name__ == "__main__":
    task3()

