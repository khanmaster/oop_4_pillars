# super class

class Animal:

    def __init__(self):

        self.alive = True
        self.eyes = True

    def breathe(self):
        return "NOTHING MORE IMPORTANT TO LIVE THAN KEEP BREATHING! "

reptiles = Animal()

# print(reptiles.eyes)
# print(reptiles.breathe())