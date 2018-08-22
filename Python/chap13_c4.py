class Horse():
    def __init__(self, name):
        self.name = name

class Rider():
    def __init__(self, name, horse):
        self.name = name
        self.horse = horse

the_horse = Horse("Bucephalus")
the_rider = Rider("Alexander", the_horse)

print(the_rider.name)
print(the_rider.horse.name)
