import math
import matplotlib.pyplot as plt
import numpy as np
from abc import ABC, abstractmethod
from colorama import init, Fore, Style, Back

class GeometricalFigure(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def draw(self):
        pass
    
    @abstractmethod
    def save_to_file(self, filename):
        pass

class Color:
    def __init__(self, color):
        self.color = color

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

class Rectangle(GeometricalFigure):
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = Color(color)

    def calculate_area(self):
        return self.width * self.height

    def draw(self):
        plt.gca().add_patch(plt.Rectangle((0, 0), self.width, self.height, edgecolor=self.color.color, facecolor=self.color.color, fill=True))
        plt.axis('equal')
        plt.show()

    def save_to_file(self, filename):
        plt.gca().add_patch(plt.Rectangle((0, 0), self.width, self.height, edgecolor=self.color.color, facecolor=self.color.color, fill=True))
        plt.axis('equal')
        plt.savefig(filename)
        plt.close()

    def __str__(self):
        return "Rectangle"

class Circle(GeometricalFigure):
    def __init__(self, radius, color):
        self.radius = radius
        self.color = Color(color)

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def draw(self):
        circle = plt.Circle((0, 0), self.radius, color=self.color.color, fill=True)
        plt.gca().add_patch(circle)
        plt.axis('equal')
        plt.show()

    def save_to_file(self, filename):
        circle = plt.Circle((0, 0), self.radius, color=self.color.color, fill=True)
        plt.gca().add_patch(circle)
        plt.axis('equal')
        plt.savefig(filename)
        plt.close()
        
    def __str__(self):
        return "Circle"

class Rhombus(GeometricalFigure):
    def __init__(self, side_length_1, side_length_2, color):
        self.side_length_1 = side_length_1
        self.side_length_2 = side_length_2
        self.color = Color(color)

    def calculate_area(self):
        return ((self.side_length_1 * self.side_length_2 )/2)

    def draw(self):
        x = [0,self.side_length_1 / 2, self.side_length_1, self.side_length_1 / 2, 0] 
        y = [0, self.side_length_2 / 2, 0, -self.side_length_2 / 2, 0]
        plt.plot(x,y, color=self.color.color)
        plt.fill_between(x,y, color=self.color.color)
        plt.xlim(-self.side_length_1 / 2 - 1, self.side_length_1 / 2 + 1)
        plt.ylim(-self.side_length_2 / 2 - 1, self.side_length_2 / 2 + 1)
        plt.axis('equal')
        plt.show()

    def save_to_file(self, filename):
        x = [0,self.side_length_1 / 2, self.side_length_1, self.side_length_1 / 2, 0] 
        y = [0, self.side_length_2 / 2, 0, -self.side_length_2 / 2, 0]
        plt.plot(x,y, color=self.color.color)
        plt.fill_between(x,y, color=self.color.color)
        plt.xlim(-self.side_length_1 / 2 - 1, self.side_length_1 / 2 + 1)
        plt.ylim(-self.side_length_2 / 2 - 1, self.side_length_2 / 2 + 1)
        plt.axis('equal')
        plt.savefig(filename)
        plt.close()
        
    def __str__(self):
        return "Rhombus"

def task4():
    while True:
        print("===============================")
        
        print("Select a figure or exit:")
        print("0. Exit")
        print("1. Rectangle")
        print("2. Circle")
        print("3. Rhombus")
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == "0":
            print("Exiting program.")
            break
        elif choice == "1":
            width = float(input("Enter the width of the rectangle: "))
            height = float(input("Enter the height of the rectangle: "))
            color = input("Enter the color of the rectangle: ")
            rectangle = Rectangle(width, height, color)
            print("Area of the rectangle is:", rectangle.calculate_area())
            rectangle.draw()
            filename = "Rectangle"
            rectangle.save_to_file(filename)
        elif choice == "2":
            radius = float(input("Enter the radius of the circle: "))
            color = input("Enter the color of the circle: ")
            circle = Circle(radius, color)
            print("Area of the circle is:", circle.calculate_area())
            circle.draw()
            filename = "Circle"
            circle.save_to_file(filename)
        elif choice == "3":
            side_length_1 = int(input("Enter the side length of the rhombus_1: "))
            side_length_2 = float(input("Enter the side length of the rhombus_2: "))
            color = input("Enter the color of the rhombus: ")
            rhombus = Rhombus(side_length_1, side_length_2, color)
            print("Area of the rhombus is:", rhombus.calculate_area())
            rhombus.draw()
            filename = "Rhombus"
            rhombus.save_to_file(filename)
        else:
            print(Fore.RED + "Invalid choice!")

if __name__ == "__main__":
    task4()