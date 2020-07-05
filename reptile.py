from animal import Animal


# inheriting animal class in Reptile class

class Reptile(Animal):
    # creating Reptile class and passing Animal class as an arg

    def __init__(self):
        super().__init__()
        self.venom = True
        self.fly = False

        def _hidden_method(self):
            return " I am hidden"


snake = Reptile()

# print(Reptile)
