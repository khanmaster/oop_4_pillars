from snake import Snake

class Python(Snake):

    def __init__(self):
        super().__init__()
        self.large = True
        self.lungs = True

    def _change_skin(self): # hidden methods are created by using _
        return " python sheds skin while growing up"

cobra = Python()
print(Python._change_skin(self=""))
#print(cobra)
#print(cobra.run)#
#print(cobra.breathe())
# print(cobra.change_skin())