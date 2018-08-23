class Rectangle():
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calculate_perimeter(self): # tinh chu vi
        return self.width * 2 + self.length * 2 # P = 2(a+b)


class Square():
    def __init__(self, side):
        self.side = side

    def calculate_perimeter(self):
        return self.side * 4 # P = 4a

new_rectangle = Rectangle(25, 50) # Create a new rectangle
new_square = Square(20) # Create a new square

print(new_rectangle.calculate_perimeter()) # Calculate and print out the perimeter of the rectangle
print(new_square.calculate_perimeter()) # Calculate and print out the perimeter of the square
