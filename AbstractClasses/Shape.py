from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):

    def __init__(self, radius_in):
        self.radius = radius_in

    def area(self):
        area = 3.14 * (self.radius ** 2)
        return area

    def perimeter(self):
        perimeter = 2 * (3.14 * self.radius)
        return perimeter

    def print(self):
        print('Area is:', self.area())
        print('Perimiter is:', self.perimeter())


class Rectangle(Shape):

    def __init__(self, length_in, width_in):
        self.length = length_in
        self.width = width_in

    def area(self):
        area = self.length * self.width
        return area

    def perimeter(self):
        perimeter = (2 * self.width) + (2 * self.length)
        return perimeter

    def print(self):
        print('Area is:', self.area())
        print('Perimiter is:', self.perimeter())


circle1 = Circle(12)

circle1.print()

rect = Rectangle(2, 4)

rect.print()