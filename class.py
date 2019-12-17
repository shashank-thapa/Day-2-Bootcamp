class Car():
    def __init__(self, name):
        self.name = name
    def honk(self):
        print('I am a car')

class Tata(Car):
    def __init__(self, name):
        self.name = name

t = Tata('Swift')
t.honk()