import math
# red : int
# green: int
# blue : int
class Color:
    MAX_DISTANCE = math.sqrt(math.pow(255, 2) + math.pow(255,2) + math.pow(255, 2))
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue
        self.fitness = 0.0
    def __str__(self):
         return str(self.fitness) 
    
    def getFitness(self, chrom):
        distance = self.MAX_DISTANCE - math.sqrt(math.pow(abs(chrom.red - self.red), 2) + 
                                math.pow(abs(chrom.green - self.green), 2) + 
                                math.pow(abs(chrom.blue - self.blue), 2)) 
        self.fitness = distance / self.MAX_DISTANCE
        return self.fitness