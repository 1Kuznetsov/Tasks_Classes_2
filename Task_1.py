class Circle:
    """
    Class representing circle
    """

    all_circles = []
    pi = 3.1415

    def __init__(self, radius=1):
        """
        Sets all the necessary attributes for the class Circle
        :param radius: radius of circle
        """

        self.radius = radius
        self.all_circles.append(self)

    def area(self):
        """
        Method calculating the circle area
        :return: float number of area
        """

        return self.radius ** 2 * self.pi

    @staticmethod
    def total_area():
        """
        Method calculating area of all circles
        :return: summarized area
        """

        total_area = 0

        for circle in Circle.all_circles:
            total_area += circle.area()

        return total_area

    def __repr__(self):
        return str(self.radius)


if __name__ == '__main__':
    circle1 = Circle(2)
    circle2 = Circle()

    print(circle1.area())
    print(circle2.area())

    print(Circle.total_area())
