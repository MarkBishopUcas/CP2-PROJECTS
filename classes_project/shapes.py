

# --- Import necessary modules and prepare paths ---
import sys
import os
from collections import defaultdict
from helper_funcs.main import inq_select

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# --- Helper function for validated numeric input ---
def get_positive_float(prompt):
    while True:
        try:
            val = float(input(prompt))
            if val <= 0:
                raise ValueError("Value must be positive.")
            return val
        except ValueError as e:
            print(f"Invalid input: {e}")


# --- Base class to enable comparison features shared by all shapes ---
class ShapeBase:
    def has_larger_area(self, other):
        return self.area() > other.area()

    def has_longer_perimeter(self, other):
        return self.perimeter() > other.perimeter()

    def compare_area(self, name, other, other_name):
        a1, a2 = self.area(), other.area()
        if a1 > a2:
            diff = a1 - a2
            print(f"{name}'s area is larger than {other_name}'s by {diff:.2f}.")
        elif a2 > a1:
            diff = a2 - a1
            print(f"{other_name}'s area is larger than {name}'s by {diff:.2f}.")
        else:
            print(f"{name} and {other_name} have the same area.")

    def compare_perimeter(self, name, other, other_name):
        p1, p2 = self.perimeter(), other.perimeter()
        if p1 > p2:
            diff = p1 - p2
            print(f"{name}'s perimeter is longer than {other_name}'s by {diff:.2f}.")
        elif p2 > p1:
            diff = p2 - p1
            print(f"{other_name}'s perimeter is longer than {name}'s by {diff:.2f}.")
        else:
            print(f"{name} and {other_name} have the same perimeter.")


# --- Shape classes (Triangle, Rectangle, Circle, etc.) ---
class Shapes:

    class Triangle(ShapeBase):
        def __init__(self, base=1, height=1, side_a=1, side_b=1, side_c=1):
            self.base = base
            self.height = height
            self.side_a = side_a
            self.side_b = side_b
            self.side_c = side_c

        def area(self):
            return 0.5 * self.base * self.height

        def perimeter(self):
            return self.side_a + self.side_b + self.side_c

        def display_info(self):
            print(f"Triangle:\n  Base: {self.base}\n  Height: {self.height}\n"
                  f"  Sides: {self.side_a}, {self.side_b}, {self.side_c}\n"
                  f"  Area: {self.area()}\n  Perimeter: {self.perimeter()}")
            self.formulas()

        def formulas(self):
            print("Formulas:\n  Area = 0.5 * base * height\n  Perimeter = sum of all sides")

    class Rectangle(ShapeBase):
        def __init__(self, length=1, width=1):
            self.length = length
            self.width = width

        def area(self):
            return self.length * self.width

        def perimeter(self):
            return 2 * (self.length + self.width)

        def display_info(self):
            print(f"Rectangle:\n  Length: {self.length}\n  Width: {self.width}\n"
                  f"  Area: {self.area()}\n  Perimeter: {self.perimeter()}")
            self.formulas()

        def formulas(self):
            print("Formulas:\n  Area = length * width\n  Perimeter = 2 * (length + width)")

        class Square(ShapeBase):
            def __init__(self, side=1):
                self.side = side

            def area(self):
                return self.side ** 2

            def perimeter(self):
                return 4 * self.side

            def display_info(self):
                print(f"Square:\n  Side: {self.side}\n"
                      f"  Area: {self.area()}\n  Perimeter: {self.perimeter()}")
                self.formulas()

            def formulas(self):
                print("Formulas:\n  Area = side^2\n  Perimeter = 4 * side")

    class Circle(ShapeBase):
        def __init__(self, radius=1):
            self.radius = radius

        def area(self):
            return 3.14159 * self.radius ** 2

        def perimeter(self):
            return 2 * 3.14159 * self.radius

        def display_info(self):
            print(f"Circle:\n  Radius: {self.radius}\n"
                  f"  Area: {self.area()}\n  Circumference: {self.perimeter()}")
            self.formulas()

        def formulas(self):
            print("Formulas:\n  Area = π * radius^2\n  Circumference = 2 * π * radius")


# --- Shape collection and counter tracking ---
shapes = {}
shape_counts = defaultdict(int)

# --- Function to add a new shape via user input ---
def add_shape(shapes):
    select = inq_select("Which shape would you like to add:",
                        "Circle",
                        "Square/Rectangle",
                        "Triangle")

    # Create Circle
    if select == 1:
        rads = get_positive_float("Please enter the radius of your circle: ")
        new_shape = Shapes.Circle(radius=rads)
        shape_type = "circle"

    # Create Square or Rectangle
    elif select == 2:
        squarectangle = inq_select("Is this a square or rectangle?",
                                   "Square",
                                   "Rectangle")
        if squarectangle == 1:
            side = get_positive_float("Please enter the side length of your square: ")
            new_shape = Shapes.Rectangle.Square(side=side)
            shape_type = "square"
        else:
            length = get_positive_float("Please enter the length of your rectangle: ")
            width = get_positive_float("Please enter the width of your rectangle: ")
            new_shape = Shapes.Rectangle(length=length, width=width)
            shape_type = "rectangle"

    # Create Triangle (with subtype selection)
    elif select == 3:
        triangle_type = inq_select("What type of triangle are you adding?",
                                   "Right-angled triangle",
                                   "Equilateral triangle",
                                   "Isosceles triangle",
                                   "Scalene triangle")
        shape_type = "triangle"

        if triangle_type == 1:
            base = get_positive_float("Enter the base (one leg): ")
            height = get_positive_float("Enter the height (other leg): ")
            hypotenuse = (base**2 + height**2) ** 0.5
            new_shape = Shapes.Triangle(base=base, height=height,
                                        side_a=base, side_b=height, side_c=hypotenuse)

        elif triangle_type == 2:
            side = get_positive_float("Enter the length of each side: ")
            height = (3**0.5 / 2) * side
            new_shape = Shapes.Triangle(base=side, height=height,
                                        side_a=side, side_b=side, side_c=side)

        elif triangle_type == 3:
            base = get_positive_float("Enter the base: ")
            equal_side = get_positive_float("Enter the length of the two equal sides: ")
            height = ((equal_side**2) - (base/2)**2) ** 0.5
            new_shape = Shapes.Triangle(base=base, height=height,
                                        side_a=equal_side, side_b=base, side_c=equal_side)

        elif triangle_type == 4:
            side_a = get_positive_float("Enter side A: ")
            side_b = get_positive_float("Enter side B: ")
            side_c = get_positive_float("Enter side C: ")
            s = (side_a + side_b + side_c) / 2
            area = (s * (s - side_a) * (s - side_b) * (s - side_c)) ** 0.5
            height = (2 * area) / side_b
            new_shape = Shapes.Triangle(base=side_b, height=height,
                                        side_a=side_a, side_b=side_b, side_c=side_c)

        else:
            print("Invalid triangle type.")
            return

    else:
        print("Invalid shape selection.")
        return

    # Assign unique name and store shape
    shape_counts[shape_type] += 1
    shape_name = f"{shape_type} {shape_counts[shape_type]}"
    shapes[shape_name] = new_shape

    print(f"{shape_name} added.")
    new_shape.display_info()


# --- Function to compare two shapes ---
def compare_shapes(shapes):
    if len(shapes) < 2:
        print("You need at least two shapes to compare.")
        return

    shape_names = list(shapes.keys())
    index1 = inq_select("Select the first shape to compare:", *shape_names) - 1
    index2 = inq_select("Select the second shape to compare:", *shape_names) - 1

    name1 = shape_names[index1]
    name2 = shape_names[index2]

    shape1 = shapes[name1]
    shape2 = shapes[name2]

    print("\n--- Area Comparison ---")
    shape1.compare_area(name1, shape2, name2)

    print("\n--- Perimeter Comparison ---")
    shape1.compare_perimeter(name1, shape2, name2)


# --- Function to sort all shapes ---
def sort_shapes(shapes):
    if not shapes:
        print("No shapes to sort.")
        return

    sort_by = inq_select("Sort shapes by:", "Area", "Perimeter")
    key_func = lambda shape: shape.area() if sort_by == 1 else shape.perimeter()
    sorted_shapes = sorted(shapes.items(), key=lambda item: key_func(item[1]), reverse=True)

    print("\nShapes sorted by " + ("area" if sort_by == 1 else "perimeter") + ":")
    for name, shape in sorted_shapes:
        print(f"\n{name}:")
        shape.display_info()
