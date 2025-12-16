from shape import Shape

class Circle(Shape):
    def draw(self):
        print("Circle with color:", end=" ")
        self.color.apply_color()
