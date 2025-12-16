from shape import Shape

class Square(Shape):
    def draw(self):
        print("Square with color:", end=" ")
        self.color.apply_color()
