import math
# red : int
# green: int
# blue : int
MAX_INT = 255
class Color:
    MAX_DISTANCE = math.sqrt(math.pow(255, 2) + math.pow(255,2) + math.pow(255, 2))
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue
    def __str__(self):
         return str(self.red) + " " + str(self.green) + " " + str(self.blue)
         
    def getFitness(self, target_color):
        distance = self.MAX_DISTANCE - math.sqrt(math.pow(abs(target_color.red - self.red), 2) + 
                                math.pow(abs(target_color.green - self.green), 2) + 
                                math.pow(abs(target_color.blue - self.blue), 2)) 
        return distance / self.MAX_DISTANCE

    def mutate(self):
        self.red = MAX_INT - self.red
        self.green = MAX_INT - self.green
        self.blue = MAX_INT - self.blue

    def equals(self, color):
        return (self.red == color.red) and (self.green == color.green) and (self.blue == color.blue)

