from particles.__init__ import math
from particles.particle import Particle

# class for 2D particle inherits from Particle class
# used in the main 2D environment linked through composition
# base class of gas particle 
class Particle2D(Particle):

    def __init__(self, position, size, screen, screenW, screenH, screenPos, boundaryX, boundaryY, color):
        # constructor to set particle properties
        # inherits all properties from parent class

        super().__init__(position, size, screen, screenW, screenH, screenPos, boundaryX, boundaryY, color)

        # define angle attribute measured in radians from the positive y-axis
        # +ve in clockwise direction, -ve in anti-clockwise direction
        self._angle = 0
        self._vx, self._vy = 0, 0

        # list to queue and store initial and final x and y components of momentum so impulse can be calculated
        self._momentaX = [0, 0]
        self._momentaY = [0, 0]

        self.MAX_SPEED = 5


    def calculateAngle(self):
        # calculates angle of travel using x and y components of velocity in tan function
        self._angle = math.atan2(self._vx, self._vy)

    def calculateSpeed(self): 
        self._speed = math.hypot(self._vx, self._vy)


    # set methods

    def setVx(self, value):
        vx = self.validateSpeedInRange(value)
        self._vx = vx 

    def setVy(self, value):
        vy = self.validateSpeedInRange(value)
        self._vy = vy

    def resetMomentaX(self):
        self._momentaX = [0, 0]
        
    def resetMomentaY(self):
        self._momentaY = [0, 0]

    def setVxVy(self):
        # trignometric functions used to calculate velocities
        self._vx = self._speed*math.sin(self._angle)
        self._vy = self._speed*math.cos(self._angle)

    def move(self): # override
        # changes x position by adding horizontal component of speed
        self._x += math.sin(self._angle) * self._speed
        # changes y position by adding vertical component of speed
        self._y -= math.cos(self._angle) * self._speed

        self.wallCollision()

    def wallCollision(self): # override
        # detects if particle collides with a boundary
        # calculates new angle of travel and speed using Netwon's Experimental Law and conservation of momentum for inelastic collisions
        # new speed calculated by equating the initial and final parallel components of velocity 

        initialAngle = self._angle

        # reflect particle off right wall
        if self._x > self._boundaryX - self._size:
            # offset x position to the left to account for delay
            self._x = 2*(self._boundaryX-self._size) - self._x
            # angle of travel equals angle of incidence when approaching from below the horizontal
            if 0 < self._angle <= math.pi/2 or -math.pi*2 < self._angle <= -math.pi*(3/2):
                self._angle = - (math.atan(self._wallElasticity*math.tan(self._angle)))
            # angle of incidence equals (π radians - +ve angle of travel) when approaching from above the horizontal
            else:
                self._angle = (math.atan(self._wallElasticity*math.tan(math.pi-self._angle))) + math.pi
            self._speed = (self._speed*math.cos(initialAngle))/math.cos(self._angle)*self._wallElasticity
            self.setVxVy()

        # reflect particle off left wall
        elif self._x < self._screenPos[0] + self._size:
            # offset x position to the right to account for delay
            self._x = 2*(self._size +self._screenPos[0]) - self._x
            if math.pi*(3/2) <= self._angle < math.pi*2 or -math.pi/2 <= self._angle < 0:
                self._angle = - (math.atan(self._wallElasticity*math.tan(self._angle)))
            else:
                self._angle = - ((math.atan(self._wallElasticity*math.tan(self._angle))) + math.pi)
            self._speed = (self._speed*math.cos(initialAngle))/math.cos(self._angle)*self._wallElasticity
            self.setVxVy()

       # reflect particle off bottom wall     
        elif self._y > self._boundaryY - self._size:
            # offset y position upwards to account for delay
            self._y = 2*(self._boundaryY - self._size) - self._y
            # angle of incidence equals (+ve angle of travel - π/2 radians) using alternate angle theorem
            if math.pi/2 < self._angle <= math.pi or -math.pi*(3/2) < self._angle <= -math.pi:
                self._angle = (math.pi/2 - math.atan(self._wallElasticity*math.tan(self._angle-math.pi/2)))
            else:
                self._angle = -(math.pi/2 - math.atan(self._wallElasticity*math.tan(math.pi*(3/2)-self._angle)))
            self._speed = (self._speed*math.cos(math.pi/2-initialAngle))/math.cos(self._angle-math.pi/2)*self._wallElasticity
            self.setVxVy()

        # reflect particle off top wall
        elif self._y < self._screenPos[1] + self._size:
            # offset y position downwards to account for delay
            self._y = 2*(self._size+self._screenPos[1]) - self._y
            # angle of incidence equals (π/2 radians - +ve angle of travel) using angles in a right angled triangle axiom
            if 0 <= self._angle < math.pi/2 or -math.pi*2 <= self._angle < -math.pi*(3/2):
                self._angle = (math.pi/2 + math.atan(self._wallElasticity*math.tan(math.pi/2 - self._angle)))
            else:
                self._angle = - (math.pi/2 + math.atan(self._wallElasticity*math.tan(math.pi/2 + self._angle)))
            self._speed = (self._speed*math.cos(math.pi/2-initialAngle))/math.cos(self._angle-math.pi/2)*self._wallElasticity
            self.setVxVy()


    # get methods

    def getMomentumX(self):
        # x component of momentum is 0 when particle is travelling vertically
        if self._angle == 0 or self._angle == math.pi or self._angle == -math.pi:
            momentumX = 0.00
        else:
            momentumX = round(self._mass*self._vx, 2)
        if momentumX != self._momentaX[1]:
            self._momentaX = [self._momentaX[1], momentumX]
        return momentumX

    def getMomentumY(self):
        # y component of momentum is 0 when particle is travelling horizontally
        if self._angle == math.pi/2 or self._angle == math.pi*(3/2) or self._angle == -math.pi/2 or self._angle == -math.pi*(3/2):
            momentumY = 0.00
        else:
            momentumY = round(self._mass*self._vy, 2)
        if momentumY != self._momentaY[1]:
            self._momentaY = [self._momentaY[1], momentumY]
        return momentumY

    def getImpulseX(self):
        return round(self._momentaX[1] - self._momentaX[0], 2)

    def getImpulseY(self):
        return round(self._momentaY[1] - self._momentaY[0], 2)

    def getMomentumMagnitude(self):
        return math.hypot(self._momentaX[1], self._momentaY[1])

    def getVx(self):
        return self._vx

    def getVy(self):
        return self._vy

    

    

