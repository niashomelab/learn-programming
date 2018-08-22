class Shape():
    def what_i_am(self):
        print("I am a shape")

class Rectangle(Shape):
    def __init__(self, length, height):
        self.length = length
        self.height = height

new_rec = Rectangle(20,30)
new_rec.what_i_am()
