from math import pi


class SimpleCircle:
    def __init__(self, radius=-1, diameter=-1):
        if radius == -1:
            self.diameter = diameter
            self.radius = self.diameter / (2 * pi)
        elif diameter == -1:
            self.radius = radius
            self.diameter = self.radius * 2 * pi
        elif radius != -1 and diameter != -1:
            raise Exception('Can\'t take more than 1 argument!')

    def __repr__(self):
        return f'Radius = {self.radius}'

    def __add__(self, other):
        if isinstance(other, SimpleCircle):
            return other.diameter + self.diameter

    def __gt__(self, other):
        if isinstance(other, SimpleCircle):
            return other.diameter < self.diameter

    def __eq__(self, other):
        if isinstance(other, SimpleCircle):
            return other.diameter == self.diameter

    @staticmethod
    def list_it(*args):
        # instead of using an if statement to figure out if it is a SimpleCircle,
        # We use the filter function to leave just the instances of SimpleCircle.
        just_circles = list(filter(lambda circle: isinstance(circle, SimpleCircle), args))
        # Then we are being left with only the SimpleCircle class.
        # The next stage is to take a list of just the radius from the just_circles list.
        circles = list(map(lambda circle: circle.radius, just_circles))
        return f' this is sorting just by the radius: {sorted(circles)},\n this is sorting by the repr of each circle: {sorted(just_circles)}'


circle1 = SimpleCircle(2)
circle2 = SimpleCircle(radius=900)
circle3 = SimpleCircle(diameter=40)

print(SimpleCircle.list_it(circle1, 'Hello', circle2, 123, circle3))
