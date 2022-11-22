from particles.__init__ import math, colorGradient, random
from particles.particle2D import Particle2D

# class for gas particle inherits from Particle2D class
# used in the gas environment
class GasParticle(Particle2D):
    
    def __init__(self, position, velocity, size, screen, screenW, screenH, screenPos, boundaryX, boundaryY, color):
        # constructor to set particle properties
        # inherits properties from parent class
        super().__init__(position, size, screen, screenW, screenH, screenPos, boundaryX, boundaryY, color)

        self._vx, self._vy = velocity[0], velocity[1]
        self.MAX_SPEED = 8

        self._gravity = 0.1
        self._elasticity = 1


    def centerDistance(self, x1, y1, x2, y2):
        # calculates distance between two particles' centres using Pythagors
        return math.hypot((x1-x2), (y1-y2))

    def move(self):
        # change y component of velocity by gravity value
        # if gravity > 0 particles will settle at the bottom of the container
        self._vy += self._gravity

        self._x += self._vx
        self._y += self._vy

        self.setColor()

    def collide(self, p2):
        # detects if two particles have collided and calculates their new speeds for an elastic collision

        # gets difference in x and y of particle positions
        dx, dy = self._x - p2.getXPos(), self._y - p2.getYPos()
        distanceOfCenters = self.centerDistance(self._x, self._y, p2.getXPos(), p2.getYPos())

        if distanceOfCenters < self._size + p2.getSize():
            # calculate difference in components of velocity
            dvx, dvy = self._vx - p2.getVx(), self._vy - p2.getVy()

            # calculates sine and cosine of the angle of travel
            sin, cos = dx/distanceOfCenters, dy/distanceOfCenters
            # offset x and y positions to account for delay
            offset = (self._size + p2.getSize() - distanceOfCenters)/2
            dx2, dy2 = sin*offset, cos*offset

            self._x += dx2
            self._y += dy2
            p2.setXPos(p2.getXPos()-dx2)
            p2.setYPos(p2.getYPos()-dy2)

            # calculates new speed using the dot product of the difference in positions and difference in velocities
            newV = (dx * dvx + dy * dvy) / distanceOfCenters
            # resolves speed into its components using the sine and cosine of the angle of travel
            new_dvx, new_dvy = -newV * sin * self._elasticity, -newV * cos * self._elasticity

            self._vx += new_dvx
            self._vy += new_dvy
            p2.setVx(p2.getVx()-new_dvx)
            p2.setVy(p2.getVy()-new_dvy)


    # get methods

    def getSpeed(self):
        # calculates new speed using Pythagoras by taking the hypotenuse of the x and y velocities
        speed = math.hypot(self._vx, self._vy)

        if speed > self.MAX_SPEED:
            speed = self.MAX_SPEED
        return speed

    def getColor(self, scale):
        # returns particle color corresponding to speed
        return colorGradient[scale]


    # set methods

    def setColor(self):
        # sets particle color based on speed 
        speed = self.getSpeed()
        self._color = self.getColor(int((speed/8)*15 - 1))

    def calculateSpeed(self, newV):
        # sets a random x and y velocity within the given range
        self._vx = random.uniform(-newV, newV)
        self._vy = random.uniform(-newV, newV)

    def setGravity(self, gravity):
        self._gravity = gravity

    def setVx(self, value):
        self._vx = value

    def setVy(self, value):
        self._vy = value
    




