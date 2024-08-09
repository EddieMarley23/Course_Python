class Triangle:
    def __init__(self,side1,side2,side3, base, height):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.base = base
        self.height = height
    def area(self):
        return(self.base * self.height)/ 2


    def tipo(self):
        if self.side1 == self.side2 or self.side1 == self.side3 or self.side2 == self.side3:
            return 'Triângulo isóceles'
        elif self.side1 > self.side2 + self.side3:
            return 'não é um triângulo'
        else:
            return 'outro tipo de triângulo'




