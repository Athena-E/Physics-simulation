from environments.__init__ import random, colorOrder, json
from particles.question_particle import QuestionParticle
from environments.environment1D import Environment1D

# class for question envrionment inherits from Environment1D
class QuestionEnvironment(Environment1D):

    def __init__(self, screen, screenW, screenH, screenPos, maxParticles):
        # constructor to set environment properties
        # inherits properties from parent class
        super().__init__(screen, screenW, screenH, screenPos, maxParticles)

        # defines new properties

        # methods for when 'save' and 'start' buttons are clicked
        self._saveClicked = False
        self._startClicked = False

        # dictionary to store environment properties of the question
        self._envProperties = {}


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
            newParticle = QuestionParticle((x, y), self._particleSize, self._screen, self._screenW, self._screenH, self._screenPos, self._boundaryX, self._boundaryY, colorOrder[self._numOfParticles])
            self._particleList.append(newParticle)


    # get methods

    def getParticleInitialMomentum(self, id):
        # returns initial momentum of existing particles else returns default value 
        if id <= self._numOfParticles:
            return self._particleList[id-1].getInitialMomentum()
        else:
            return 0.00

    def getParticleInitialKE(self, id):
        # returns initial kinetic energy of existing particles else returns default value 
        if id <= self._numOfParticles:
            return round(self._particleList[id-1].getInitialKE(), 2)
        else:
            return 0.00

    def getParticleKE(self, id):
        # returns current kinetic energy of existing particles else returns default value 
        if id <= self._numOfParticles:
            return round(self._particleList[id-1].getKE(), 2)
        else:
            return 0.00   

    
    def onClickSave(self):
        self._saveClicked = True


    # methods to hide particle property and store as a hidden property

    def hideParticleMass(self, id):
        if id <= self._numOfParticles:
            self._particleList[id-1].hideMass()

    def hideParticleInitialV(self, id):
        if id <= self._numOfParticles:
            self._particleList[id-1].hideInitialV()

    def hideParticleFinalV(self, id):
        if id <= self._numOfParticles:
            self._particleList[id-1].hideFinalV()

    def hideParticleInitialM(self, id):
        if id <= self._numOfParticles:
            self._particleList[id-1].hideInitialM()

    def hideParticleFinalM(self, id):
        if id <= self._numOfParticles:
            self._particleList[id-1].hideFinalM()

    def hideParticleImpulse(self, id):
        if id <= self._numOfParticles:
            self._particleList[id-1].hideImpulse()

    def hideParticleInitialKE(self, id):
        if id <= self._numOfParticles:
            self._particleList[id-1].hideInitialKE()

    def hideParticleFinalKE(self, id):
        if id <= self._numOfParticles:
            self._particleList[id-1].hideFinalKE()


    def getDisplayedParticleProperties(self):
        # returns properties of particle that will be displayed in the question as a json

        particleProperties = {}

        for i, particle in enumerate(self._particleList, start=1):
            particleProperties[f"particle{i}"] = particle.getDisplayedProperties()
        
        return json.dumps(particleProperties)


    def getHiddenParticleProperties(self):
        # return properties of particle that will be hidden in the question as a json

        particleProperties = {}

        for i, particle in enumerate(self._particleList, start=1):
            particleProperties[f"particle{i}"] = particle.getHiddenProperties()
        
        return json.dumps(particleProperties)


    def getEnvProperties(self):
        # returns environment properties of question as a json

        newEnvProperties = {
            "noOfParticles": self._numOfParticles,
            "particleElasticity": self._particleElasticity,
            "wallElasticity": self._wallElasticity
        }

        self._envProperties.update(newEnvProperties)

        return json.dumps(self._envProperties)

    
    def start(self): # override
        if self._numOfParticles != 0:
            self.run = True
            self._startClicked = True

    def stop(self): # override
        self.run = False
        self.clear()
        self._startClicked = False
        self._envProperties.clear()


    def setInitialPos(self):
        # set the starting position of each particle in the question

        for i, particle in enumerate(self._particleList, start=1):

            self._envProperties[f"particlePos{i}"] = (particle._x, particle._y)

    def setParticleInitialSpeed(self, id, value):
        if id <= self._numOfParticles:
            self._particleList[id-1].setInitialSpeed(float(value))


    def removeParticle(self): # extended method
        super(QuestionEnvironment, self).removeParticle()
        self._envProperties.popitem()
