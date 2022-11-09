from environments.__init__ import random, pg, math

# base class of all environment classes
class Environment(object):

    def __init__(self, screen, screenW, screenH, screenPos, maxParticles):
        # constructor to set environment properties

        self._particleList = []
        self._particleElasticity = 1
        self._wallElasticity = 1
        self._numOfParticles = 0

        self._screen = screen
        self._screenW = screenW
        self._screenH = screenH
        self._screenPos = screenPos

        self._centerOfMass = (0, 0)
        self._COMsize = int(self._screenH/30)
        self._showCenterOfMass = False

        # public attribute to indicate if simulation is running
        self.run = False
        
        self._particleSize = int(self._screenH/10)

        # actual x and y positions of the particle container's far boundaries
        self._boundaryX, self._boundaryY = self._screenW + self._screenPos[0], self._screenH + self._screenPos[1]

        # list of tuples storing each particle's positions and sizes
        self._particlePosSizeList = []

        self._speedTimePoints = [[],[],[],[]]
        self._momentumTimePoints = [[],[],[],[]]
        self._maxParticles = maxParticles


    def centerDistance(self, x1, y1, x2, y2):
        # calculates distance between two particles' centres using Pythagors
        return math.hypot((x1-x2), (y1-y2))

        
    def addParticle(self):
        # adds new particle to set of particles and draws to screen

        self._numOfParticles += 1

        # gets random integers in the screen area for x and y positions
        x = random.randint(self._screenPos[0]+self._particleSize, self._boundaryX-self._particleSize)
        y = random.randint(self._screenPos[1]+self._particleSize, self._boundaryY - self._particleSize)

        # prevents particles overlapping
        while any((x2, y2, size2) for (x2, y2, size2) in self._particlePosSizeList if self.centerDistance(x, y, x2, y2) < self._particleSize + size2):
            # checks if distance between the centres of new and existing particles is less than the sum of the radii
            # gets new random integers for particle's position 
            x = random.randint(self._screenPos[0]+self._particleSize, self._boundaryX-self._particleSize)
            y = random.randint(self._screenPos[1]+self._particleSize, self._boundaryY - self._particleSize)

        # adds position and size of new particle as a tuple to the list
        self._particlePosSizeList.append((x, y, self._particleSize))

        return x, y


    def particleCollision(self, p1, p2):
        # detects when two particles have collided directly in 1D
        if abs(p1._x - p2._x) < p1.getSize() + p2.getSize():

            p1Speed, p2Speed = p1.getSpeed(), p2.getSpeed()

            p1Speed, p2Speed = (p1.getMass()*p1Speed + p2.getMass()*p2Speed - self._particleElasticity*p2.getMass()*(p1Speed-p2Speed))/(p1.getMass()+p2.getMass()), (p1.getMass()*p1Speed + p2.getMass()*p2Speed + self._particleElasticity*p2.getMass()*(p1Speed-p2Speed))/(p1.getMass()+p2.getMass())

            p1.setSpeed(p1Speed)
            p2.setSpeed(p2Speed)


    def update(self):
        # updates environment and particle interactions
        for i, particle in enumerate(self._particleList):
            if self.run:
                particle.move()
                for particle2 in self._particleList[i+1:]:
                    self.particleCollision(particle, particle2)
            particle.display()

        self.displayCOM()



    def removeParticle(self):
        # removes particle from environment
        if self._numOfParticles > 0:
            self._particleList.pop()
            self._particlePosSizeList.pop()
            self._numOfParticles -= 1

    def clear(self):
        # clears environment of particles and resets attributes
        self._particleList.clear()
        self._particlePosSizeList.clear()
        self._numOfParticles = 0
        self._speedTimePoints = [[],[],[],[]]
        self._momentumTimePoints = [[],[],[],[]]


    # set methods

    def setWallElasticity(self, wallElasticity):
        # sets new wall elasticity from user input
        try:
            wallElasticity = int(wallElasticity)/100
        except:
            wallElasticity = 0
        self._wallElasticity = wallElasticity
        for particle in self._particleList:
            particle.setWallElasticity(self._wallElasticity)

    def setParticleElasticity(self, particleElasticity):
        # sets new particle elasticity from user input
        try:
            particleElasticity = int(particleElasticity)/100
        except:
            particleElasticity = 0
        self._particleElasticity = particleElasticity

    def setParticleMass(self, id, value):
        if id <= self._numOfParticles:
            self._particleList[id-1].setMass(float(value))

    def setParticleSpeed(self, id, value):
        if id <= self._numOfParticles:
            self._particleList[id-1].setSpeed(float(value))


    # get methods

    def getParticleMass(self, id):
        # returns particle mass for existing particles else return default value
        if id <= self._numOfParticles:
            return self._particleList[id-1].getMass()
        else:
            return 1.00

    def getParticleMomentum(self, id):
        # returns particle momentum for existing particles else return default value
        if id <= self._numOfParticles:
            return self._particleList[id-1].getMomentum()   
        else:
            return 0.00

    def getParticleImpulse(self, id):
        # returns particle impulse for existing particles else returns default value
        if id <= self._numOfParticles:
            return self._particleList[id-1].getImpulse()
        else:
            return 0.00

    def getParticleSpeed(self, id):
        # returns particle speed for existing particles else returns default value
        if id <= self._numOfParticles:
            return self._particleList[id-1].getSpeed()
        else:
            return 0.00


    def getTotalKineticEnergy(self):
        # sums the kinetic energies for each particle
        totalKE = 0
        for particle in self._particleList:
            totalKE += particle.getKineticEnergy()
        return round(totalKE, 2)

    def getSpeedTimePoints(self):
        return self._speedTimePoints

    def getMomentumTimePoints(self):
        return self._momentumTimePoints

    def getParticleFromList(self, index):
        return self._particleList[index]

    def getWallElasticity(self):
        return self._wallElasticity

    def getParticleElasticity(self):
        return self._particleElasticity
    
    def getNoOfParticles(self):
        return self._numOfParticles

    def getCenterOfMass(self):
        return self._centerOfMass

    def getMaxParticles(self):
        return self._maxParticles
        

    def calculateCenterOfMass(self):
        # calculates center of mass by finding the average of the sum of the products of each particle's mass and position
        totalMass, xMomentSum, yMomentSum = 0, 0, 0

        for particle in self._particleList:
            totalMass += particle.getMass()
            xMomentSum += particle.getMass()*particle.getXPos()
            yMomentSum += particle.getMass()*particle.getYPos()

        self._centerOfMass = (xMomentSum/totalMass, yMomentSum/totalMass)

    def displayCOM(self):
        # draws centre of mass of the system to the screen
        if self._numOfParticles > 0 and self._showCenterOfMass:
            self.calculateCenterOfMass()
            pg.draw.circle(self._screen, (0, 0, 0), self._centerOfMass, self._COMsize, 0)

    def showHideCOM(self):
        self._showCenterOfMass = not self._showCenterOfMass


    def increaseParticleSize(self, id):
        # sets new particle size 
        if id <= self._numOfParticles:
            particleSize = self._particleList[id-1].getSize()
            if particleSize < self._screenH/5:
                newSize = particleSize + 5 # 5 pixels
                self._particleList[id-1].setSize(newSize)

                particlePosSize = self._particlePosSizeList[id-1]
                self._particlePosSizeList[id-1] = (particlePosSize[0], particlePosSize[1], newSize)
        
    def decreaseParticleSize(self, id):
        # sets new particle size
        if id <= self._numOfParticles:
            particleSize = self._particleList[id-1].getSize()
            if particleSize > self._screenH/10:
                newSize = particleSize - 5 # 5 pixels
                self._particleList[id-1].setSize(newSize)

                particlePosSize = self._particlePosSizeList[id-1]
                self._particlePosSizeList[id-1] = (particlePosSize[0], particlePosSize[1], newSize)

    
    def start(self):
        # runs simulation
        if self._numOfParticles != 0:
            self.run = True

    def stop(self):
        # stops simulation and clears environment
        self.run = False
        self.clear()

    def pause(self):
        # pauses simulation
        self.run = False


    def storeSpeedPoint(self, value, index):
        # adds new point for speed-time graph to a list
        self._speedTimePoints[index].append([len(self._speedTimePoints[index])+1, value])

    def storeMomentumPoint(self, value, index):
        # adds new point for momentum-time graph to a list
        self._momentumTimePoints[index].append([len(self._momentumTimePoints[index])+1, value])


    def updateParticlePosSizeList(self):
        # update list of particle positions and sizes
        for i, particle in enumerate(self._particleList):
            self._particlePosSizeList[i] = (particle._x, particle._y, particle.getSize())

    def selectParticle(self):
        # checks to see if mouse is within the area of a particle
        for particle in self._particleList:
            mousePos = pg.mouse.get_pos()
            if math.hypot(particle._x - mousePos[0], particle._y - mousePos[1]) <= particle.getSize():
                return self._particleList.index(particle)
        return None

    def repositionParticle(self, particleIndex):
        # updates particle x position to mouse's position in 1D
        particle = self._particleList[particleIndex]
        mousePos = pg.mouse.get_pos()
        self._particlePosSizeList[particleIndex] = (0, 0, 0)
        # ensures that mouse is within the collision boundary
        if (self._screenPos[0] + particle.getSize() < mousePos[0] < self._screenPos[0] + self._screenW - particle.getSize()
            and not any((x2, y2, size2) for (x2, y2, size2) in self._particlePosSizeList if self.centerDistance(mousePos[0], mousePos[1], x2, y2) < self._particleSize + size2)):
            particle.setXPos(mousePos[0])



    



