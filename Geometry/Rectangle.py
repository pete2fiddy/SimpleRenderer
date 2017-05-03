

class Rectangle(object):
    
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
    @classmethod
    def init_from_center(cls, center, width, height):
        x = center[0]-width//2
        y = center[1]-height//2
        return Rectangle(x, y, width, height)
    
    def fill(self, image, color):
        for x in range(self.x, self.x+self.width):
            for y in range(self.y, self.y+self.height):
                image[x,y] = color