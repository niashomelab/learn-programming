"""
Create a Class Square
Calculate its perimeter
Change its size
"""
class Square():
    def __init__(self, side):
        self.side = side

    def calculate_perimeter(self):
        return self.side * 4
    
    def change_size(self, add_size):
        self.side = self.side + add_size

new_square = Square(100)
print(new_square.calculate_perimeter()) # not "calculate_perimeter(new_square)"

new_square.change_size(200) # not "new_square = new_square.change_size(200)"
print(new_square.calculate_perimeter())
