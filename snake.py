from reptile import Reptile

class Snake(Reptile):


    def __init__(self):
        super().__init__()
        self.venom = True
        self.fly = False
        self.run = False


python = Reptile()
print(Reptile)
print(python)

# print(python.breathe())
# print(python.eyes)
# print(python.alive)