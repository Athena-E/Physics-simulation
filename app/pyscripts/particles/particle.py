from particles.__init__ import pg

# base class of all particle classes
class Particle(object):

    def __init__(self, position, size, screen, screenW, screenH, screenPos, boundaryX, boundaryY, color):
        # constructor to set particle properties
        self.MAX_SPEED = 0
        self.MAX_MASS = 0
        self.MIN_MASS = 0
        
        self._x, self._y = position
        self._size = size
        self._mass = self.MIN_MASS
        self._color = color
        self._thickness = 0
        self._speed = 0
        self._wallElasticity = 1

        # screen dimensions of collision container
        self._screen = screen
        self._width = screenW
        self._height = screenH
        self._screenPos = screenPos
        self._boundaryX, self._boundaryY = boundaryX, boundaryY

        # list to queue and store initial and final momentum so impulse can be calculated
        self._momenta = [0, 0]



    def display(self):
        # draws particle to the screen
        pg.draw.circle(self._screen, self._color, (int(self._x), int(self._y)), self._size, self._thickness)

    def move(self):
        # changes x position by adding value of speed
        self._x += self._speed

        # changes the direction of travel if particle collides with a boundary
        # offsets x position to account for delay
        if self._x > self._boundaryX - self._size:
            self._x = 2*(self._boundaryX-self._size) - self._x
            self._speed *= -self._wallElasticity 
        elif self._x < self._screenPos[0] + self._size:
            self._x = 2*(self._size +self._screenPos[0]) - self._x
            self._speed *= -self._wallElasticity 

    def validateSpeedInRange(self, value):
        # verifies user's input for speed is within range
        # if speed is out of range, speed is automatically set to the maximum
        speed = float(value)
        if abs(speed) > self.MAX_SPEED:
            return speed/abs(speed) * self.MAX_SPEED
        elif abs(speed) <= self.MAX_SPEED:
            return speed

    def validateMassInRange(self, value):
        # verifies user's input for mass is within range
        # if mass is out of range, mass is automatically set to the maximum/minimum
        mass = float(value)
        if mass > self.MAX_MASS:
            return self.MAX_MASS
        elif mass < self.MIN_MASS:
            return self.MIN_MASS
        else:
            return mass

    # set methods

    def setWallElasticity(self, value):
        self._wallElasticity = value

    def setMass(self, value):
        mass = self.validateMassInRange(value)
        self._mass = mass

    def setSize(self, value):
        self._size = value

    def setSpeed(self, value):
        speed = self.validateSpeedInRange(value)
        self._speed = speed

    def setXPos(self, value):
        self._x = value

    def setYPos(self, value):
        self._y = value


    # get methods

    def getSpeed(self):
        return self._speed

    def getSize(self):
        return self._size

    def getMass(self):
        return self._mass

    def getKineticEnergy(self):
        return 0.5*self._mass*(self._speed**2)

    def getMomentum(self):
        momentum = round(self._mass*self._speed, 2)
        # if new momentum is not equal to initial momentum
        if momentum != self._momenta[1]:
            # shift initial momentum to position 0 and append new momentum
            self._momenta = [self._momenta[1], momentum]
        return momentum

    def getImpulse(self):
        # impulse is equal to the change in momentum
        return round(self._momenta[1] - self._momenta[0], 2)

    def getMomentumMagnitude(self):
        return abs(self._momenta[1])

    def getSpeedMagnitude(self):
        return abs(self._speed)

    def getXPos(self):
        return self._x

    def getYPos(self):
        return self._y




