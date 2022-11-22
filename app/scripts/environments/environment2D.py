from environments.__init__ import math, pg, colorOrder
from particles.particle2D import Particle2D
from environments.environment import Environment

# class for 1D Environment inherits from Envrionment class
# linked to particle2D class through composition
class Environment2D(Environment):
    
    def __init__(self, screen, screenW, screenH, screenPos, maxParticles):
        # constructor to set environment properties
        # inherits all properties from parent class
        super().__init__(screen, screenW, screenH, screenPos, maxParticles)


    def getVectorAngle(self, v1, v2):
        # calculates angle between two vectors using the cosine rule
        # angle returned is acute
        try:
            angle = math.acos((v1[0]*v2[0]+v1[1]*v2[1])/(math.hypot(v1[0], v1[1])*math.hypot(v2[0], v2[1])))
            if angle > math.pi/2:
                angle = math.pi - angle
            return angle
        except:
            return 0

    def getDirection(self, angle):
        # returns +ve if particle is moving to the right
        if 0 <= angle < math.pi or angle < -math.pi*(3/2):
            return 1
        # return -ve if particle is moving to the left
        elif math.pi <= angle < math.pi*2 or -math.pi*(3/2) < angle < 0:
            return -1

    def setParticleVx(self, id, newVx):
        # sets new x velocity for each existing particle and calculates its new angle and speed
        try:
            if id <= self._numOfParticles:
                self._particleList[id-1].setVx(newVx)
                self._particleList[id-1].resetMomentaX()
                self._particleList[id-1].calculateAngle()
                self._particleList[id-1].calculateSpeed()
        except:
            self.errorAlert = "invalid velocity"

    def setParticleVy(self, id, newVy):
        # sets new y velocity for each existing particle and calculates its new angle and speed
        try:
            if id <= self._numOfParticles:
                self._particleList[id-1].setVy(newVy)
                self._particleList[id-1].resetMomentaY()
                self._particleList[id-1].calculateAngle()
                self._particleList[id-1].calculateSpeed()
        except:
            self.errorAlert = "invalid velocity"


    def getParticleVx(self, id):
        if id <= self._numOfParticles:
            return self._particleList[id-1].getVx()
        else:
            return 0.00

    def getParticleVy(self, id):
        if id <= self._numOfParticles:
            return self._particleList[id-1].getVy()
        else:
            return 0.00

    def getParticleMomentumX(self, id):
        # gets x component of momentum if particle exists else returns default value
        if id <= self._numOfParticles:
            return self._particleList[id-1].getMomentumX()   
        else:
            return 0.00

    def getParticleMomentumY(self, id):
        # gets y component of momentum if particle exists else returns default value
        if id <= self._numOfParticles:
            return self._particleList[id-1].getMomentumY()   
        else:
            return 0.00

    def getParticleImpulseX(self, id):
        # gets x component of impulse if particle exists else returns default value
        if id <= self._numOfParticles:
            return self._particleList[id-1].getImpulseX()
        else:
            return 0.00

    def getParticleImpulseY(self, id):
        # gets y component of impulse if particle exists else returns default value
        if id <= self._numOfParticles:
            return self._particleList[id-1].getImpulseY()
        else:
            return 0.00


    def addParticle(self): # extended method

        if self._numOfParticles < self._maxParticles:
            # calls method of parent class to return available x, y position
            x, y = super().addParticle()

            # instantiate 2D particle
            newParticle = Particle2D((x, y), self._particleSize, self._screen, self._screenW, self._screenH, self._screenPos, self._boundaryX, self._boundaryY, colorOrder[self._numOfParticles])
            self._particleList.append(newParticle)
            

    def particleCollision(self, p1, p2): # override
        
        # detects when two particles have collided and calculates their new speeds and direction of travel

        # calculates the distance between the centres of two particles
        distanceOfCenters = self.centerDistance(p1.getXPos(), p1.getYPos(), p2.getXPos(), p2.getYPos())
        # stores direction vector of line of centres
        distanceVector = ((p1.getXPos()-p2.getXPos()), (p2.getYPos()-p1.getYPos()))

        if distanceOfCenters < p1.getSize() + p2.getSize():

            # calculates the incident angle by calculating the angle between the direction of travel and line of centres
            p1InAngle = self.getVectorAngle(distanceVector, (p1.getVx(), p1.getVy()))
            p2InAngle = self.getVectorAngle(distanceVector, (p2.getVx(), p2.getVy()))

            # calculates the initial x component of velocity using cosine
            # result is negative if particle is moving to the left, else remains positive
            p1ux = abs(p1.getSpeed()*math.cos(p1InAngle)) * self.getDirection(p1._angle)
            p2ux = abs(p2.getSpeed()*math.cos(p2InAngle)) * self.getDirection(p2._angle)

            # applies derived equations for conservation of momentum and Newton's experimental law to set new x component of velocity
            p1.setVx(((p1.getMass()*p1ux+p2.getMass()*p2ux-self._particleElasticity*p2.getMass()*(p1ux-p2ux))/(p1.getMass()+p2.getMass())))
            p2.setVx(((p1.getMass()*p1ux+p2.getMass()*p2ux+self._particleElasticity*p1.getMass()*(p1ux-p2ux))/(p1.getMass()+p2.getMass())))
            # final y component of velocity calculated from initial speed and incident angle with trigonometric sine
            p1.setVy(p1.getSpeed()*math.sin(p1InAngle))
            p2.setVy(p2.getSpeed()*math.sin(p2InAngle))

            # calculate and set new angles of travel and speed
            p1.calculateAngle()
            p2.calculateAngle()
            p1.calculateSpeed()
            p2.calculateSpeed()

            # offset x and y positions of both particles to account for delay
            # calculate angle of tilt of the line of centres to the horizontal
            tangent = math.atan2(p1.getYPos() - p2.getYPos(), p1.getXPos() - p2.getXPos())
            # add π/2 radians since angle of travel is measured from the positive y axis
            angle = math.pi/2 + tangent

            # offset positions by sine and cosine of angle
            p1X, p1Y = p1.getXPos() + math.sin(angle), p1.getYPos() - math.cos(angle)
            p2X, p2Y = p2.getXPos() - math.sin(angle), p2.getYPos() + math.cos(angle)
            p1.setXPos(p1X)
            p1.setYPos(p1Y)
            p2.setXPos(p2X)
            p2.setYPos(p2Y)


    def repositionParticle(self, particleIndex): # override
        # moves particle to the mouse's position if it has been selected

        particle = self._particleList[particleIndex]
        mousePos = pg.mouse.get_pos()
        self._particlePosSizeList[particleIndex] = (0, 0, 0)
        
        # ensures mouse is within collision container and does not overlap with exisiting particles
        if (self._screenPos[0] + particle.getSize() < mousePos[0] < self._screenPos[0] + self._screenW - particle.getSize() 
            and self._screenPos[1] + particle.getSize() < mousePos[1] < self._screenPos[1] + self._screenH - particle.getSize()
            and not any((x2, y2, size2) for (x2, y2, size2) in self._particlePosSizeList if self.centerDistance(mousePos[0], mousePos[1], x2, y2) < self._particleSize + size2)):
            # move particle to mouse's current position in both the x and y directions
            particle.setXPos(mousePos[0])
            particle.setYPos(mousePos[1])




