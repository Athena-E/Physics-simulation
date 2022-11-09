from environments.__init__ import random, colorOrder
from particles.particle1D import Particle1D
from environments.environment import Environment

# class for 1D Environment inherits from Envrionment class
class Environment1D(Environment):
    
    def __init__(self, screen, screenW, screenH, screenPos, maxParticles):
        # constructor to set environment properties
        # inherits all properties from parent class
        super().__init__(screen, screenW, screenH, screenPos, maxParticles)


    def addParticle(self): # override
        # adds new particle to set of particles and draws to screen

        if self._numOfParticles < self._maxParticles:

            self._numOfParticles += 1

            # gets random integers in the screen area for x and y positions
            x = random.randint(self._screenPos[0]+self._particleSize, self._boundaryX-self._particleSize)
            y = self._screenPos[1] + self._screenH/2

            # prevents particles overlapping
            while any((x2, y2, size2) for (x2, y2, size2) in self._particlePosSizeList if self.centerDistance(x, y, x2, y2) < self._particleSize + size2):
                # checks if distance between the centres of new and existing particles is less than the sum of the radii
                # gets new random integers for particle's position 
                x = random.randint(self._screenPos[0]+self._particleSize, self._boundaryX-self._particleSize)

            # adds position and size of new particle as a tuple to the list
            self._particlePosSizeList.append((x, y, self._particleSize))

            # instantiate 1D particle
            newParticle = Particle1D((x, y), self._particleSize, self._screen, self._screenW, self._screenH, self._screenPos, self._boundaryX, self._boundaryY, colorOrder[self._numOfParticles])
            self._particleList.append(newParticle)
