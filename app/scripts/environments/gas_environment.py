from environments.__init__ import pg, random, math
from particles.gas_particle import GasParticle
from environments.environment import Environment

# class for gas environment inherits from Environment class
class GasEnvironment(Environment):
    
    def __init__(self, screen, screenW, screenH, screenPos, maxParticles):
        # constructor method to set environment attributes
        # inherits all properties from parent class
        super().__init__(screen, screenW, screenH, screenPos, maxParticles)

        # define new attributes
        self._minParticleSize = int(self._screenH/40)
        self._particleSize = self._minParticleSize
        self._mouseParticle = GasParticle((0, 0), (0, 0), self._particleSize, self._screen, self._screenW, self._screenH, self._screenPos, self._boundaryX, self._boundaryY, (255, 0, 0))
        self._wall = pg.Rect(self._screenPos[0], self._screenPos[1], self._screenW, self._screenH/16)

        self._minV, self._maxV = 0.25, 8
        self._vRange = self._maxV - self._minV
        self._currentV = self._minV
        self._gravity = 0

        self._minElasticity, self._maxElasticity = 0.2, 1
        self._elasticityRange = self._maxElasticity - self._minElasticity
        self._elasticity = self._minElasticity

        self._temperatureRatio = 0
        self._elasticityRatio = 0
        self._sizeRatio = 0


    def setMaxParticleSize(self):

        # calculates maximum possible raidus of particles depending on the number of particles
        containerArea = self._screenW * (self._screenH-(self._wall.y+self._wall.height-self._screenPos[1]))
        # divides area of container into squares and square rooted to find the side length
        diameter = math.sqrt(math.floor(containerArea/self._numOfParticles))
        # divide diamter by two and uses 70% of calculated radius to still allow for room to move
        self.maxParticleSize = int(diameter/2 * 0.7)


    def addParticle(self):
        # adds particle to environment

        self._numOfParticles += 1
        # max particle size recaluclated as it must become smaller if more particles are added
        self.setMaxParticleSize()
        self.recalculateSize()

        # instantiate gas particle
        # dynamically generates GasParticle object
        particle = GasParticle((random.randint(self._particleSize, self._screenW-self._particleSize), 
        random.randint(self._particleSize, self._screenH-self._particleSize)), (random.uniform(-self._currentV, self._currentV), random.uniform(-self._currentV, self._currentV)), 
        self._particleSize, self._screen, self._screenW, self._screenH, self._screenPos, self._boundaryX, self._boundaryY, (0, 0, 0)) 
        self._particleList.append(particle)

        self.adjustWall()
        

    def removeParticle(self):
        # removes particles from environment
        
        if self._numOfParticles > 0:
            self._particleList.pop()
            self._numOfParticles -= 1

            # max particle size recalculated as it can become bigger if there are less particles
            self.setMaxParticleSize()
            self.recalculateSize()

    def update(self):
        # updates environment and particle interactions

        for particle in self._particleList:
            particle.move()
        for i, particle in enumerate(self._particleList):
            for p2 in self._particleList[i+1:]:
                particle.collide(p2)

            self.wallCollision(particle)
        
        self.display()

    def wallCollision(self, particle):
        # detects if particle has collided with a wall and calculates new velocities and positions

        # offset position to account for delay
        # reverse direction of travel in the opposite direction for an elastic collision
        if particle.getXPos() < self._screenPos[0] + particle.getSize():
            particle.setXPos(2*(self._screenPos[0] + particle.getSize()) - particle.getXPos())
            particle.setVx(particle.getVx() * -1 * self._elasticity)
        if particle.getXPos() > self._boundaryX - particle.getSize():
            particle.setXPos(2*(self._boundaryX - particle.getSize()) - particle.getXPos())
            particle.setVx(particle.getVx() * -1 * self._elasticity)
        if particle.getYPos() < self._wall.y + self._wall.height + particle.getSize():
            particle.setYPos(2*(particle.getSize() + self._wall.y + self._wall.height) - particle.getYPos())
            particle.setVy(particle.getVy() * -1 * self._elasticity)
        if particle.getYPos() > self._boundaryY - particle.getSize():
            particle.setYPos(2*(self._boundaryY - particle.getSize()) - particle.getYPos())
            particle.setVy(particle.getVy() * -1 * self._elasticity)


    def display(self):
        # draws particles, wall and cursor to screen

        for particle in self._particleList:
            pg.draw.circle(self._screen, particle._color, (int(particle._x), int(particle._y)), particle._size, particle._thickness)
        pg.draw.circle(self._screen, self._mouseParticle._color, (int(self._mouseParticle._x), int(self._mouseParticle._y)), self._mouseParticle._size, self._mouseParticle._thickness)
        pg.draw.rect(self._screen, (0, 0, 0), self._wall)


    def mouseInteraction(self):
        # moves a particle with the mouse to enable user interaction

        mousePos = pg.mouse.get_pos()

        if (self._screenPos[0] + self._particleSize < mousePos[0] < self._boundaryX - self._particleSize
        and self._screenPos[1] + self._particleSize < mousePos[1] < self._boundaryY - self._particleSize):

            self._mouseParticle._x = mousePos[0]
            self._mouseParticle._y = mousePos[1]


    def mouseCollision(self, vx, vy):
        # calculates new speed of particle if mouse collides with it

        for particle in self._particleList:

            dx, dy = self._mouseParticle._x - particle.getXPos(), self._mouseParticle._y - particle.getYPos()
            distanceOfCenters = math.hypot(dx, dy)

            if distanceOfCenters < particle.getSize() + self._particleSize:
                
                particle.setVx(particle.getVx()-vx*0.4)
                particle.setVy(particle.getVy()-vy*0.4)


    def selectWall(self):
        # flag to indicate when user has clicked on the wall

        mousePos = pg.mouse.get_pos()

        if self._wall.collidepoint(mousePos) and self._numOfParticles > 0:
            return True


    def getParticleDepth(self):
        # calculates the minimum height of the wall based on the number of particles and their size
        # calculates maximum number of layers of particles and calculates depth by multiplying with particle diameter
        layers = self._numOfParticles / (self._screenW/(2*self._particleSize)) 
        depth = layers*2*self._particleSize

        return depth


    def moveWall(self):
        # moves the wall with the mouse to change the container size

        mousePos = pg.mouse.get_pos()

        depth = self.getParticleDepth()

        # ensures y mouse position is within the valid range of the container and minimum height
        if self._screenPos[1] < mousePos[1] < self._screenPos[1] + self._screenH - depth - self._wall.height:

            self._wall = pg.Rect(self._screenPos[0], mousePos[1], self._screenW, self._screenH/16)
            self.setMaxParticleSize()

    
    def setSize(self, sizeRatio):
        # gets slider value as a ratio and sets the new particle size accordingly

        if sizeRatio != self._sizeRatio:

            self._sizeRatio = sizeRatio

            # multiplies ratio by maximum particle size and adds to minimum size to get the new size
            self._particleSize = int(self._minParticleSize + sizeRatio * self.maxParticleSize)
            self._mouseParticle._size = self._particleSize

            for particle in self._particleList:
                particle.setSize(self._particleSize)


    def recalculateSize(self):
        # method to recalculate size whenever number of particles is adjusted

        self._particleSize = int(self._minParticleSize + self._sizeRatio * self.maxParticleSize)
        self._mouseParticle._size = self._particleSize

        for particle in self._particleList:
            particle.setSize(self._particleSize)



    def adjustWall(self):
        # method to recalculate height of wall when particle size changes

        depth = self.getParticleDepth()
        maxYPos = self._screenPos[1] + self._screenH - depth - self._wall.height

        # if particles do not fit in the given space, y position of wall is decreased to the maximum y position
        if self._wall.y > maxYPos:
            self._wall = pg.Rect(self._screenPos[0], maxYPos, self._screenW, self._screenH/16)



    def setTemperatureV(self, temperatureRatio):
        # sets new velocity based on temperature

        if temperatureRatio != self._temperatureRatio:

            self._temperatureRatio = temperatureRatio

            # multiplies ratio by velocity range and adds to minimum velocity to set new velocity
            self._currentV = temperatureRatio * self._vRange + self._minV

            for particle in self._particleList:
                particle.setSpeed(self._currentV)
            
            # if temperature is greater than 50%, particles should float and act like gas
            if temperatureRatio > 0.5:
                gravity = 0
            # if temperature is 50% or less, particles should be drawn to the bottom of the screen like liquid
            else:
                gravity = 0.1
            for particle in self._particleList:
                particle.setGravity(gravity)


    def setElasticity(self, elasticityRatio):
        # set new collision elasticity based on given ratio

        if elasticityRatio != self._elasticityRatio:

            self._elasticityRatio = elasticityRatio
            self._elasticity = self._minElasticity + elasticityRatio * self._elasticityRange





        
