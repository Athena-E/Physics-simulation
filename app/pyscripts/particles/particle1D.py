from particles.particle import Particle

# class for 1D particle inherits from Particle class
# used in the direct collisions environment and test environment linked through composition
class Particle1D(Particle):

    def __init__(self, position, size, screen, screenW, screenH, screenPos, boundaryX, boundaryY, color):
        # constructor to set particle properties
        # inherits all properties from parent class
        super().__init__(position, size, screen, screenW, screenH, screenPos, boundaryX, boundaryY, color)

        self.MAX_SPEED = 7
        self.MAX_MASS = 10
        self.MIN_MASS = 1
    
        




