from particles.particle1D import Particle1D

# class for question particle used in Question Environment
# inherits from Particle1D class
class QuestionParticle(Particle1D):

    def __init__(self, position, size, screen, screenW, screenH, screenPos, boundaryX, boundaryY, color):
        # constructor to initialise particle properties
        # inherits properties from parent class
        super().__init__(position, size, screen, screenW, screenH, screenPos, boundaryX, boundaryY, color)

        # define new properties

        self._initialSpeed = 0
        self._initialMomentum = 0
        self._initialKE = 0
        
        # list of names of particle properties
        self._hiddenProperties = ["mass", "initialV", "finalV", "initialM", "finalM", "impulse", "initialKE", "finalKE"]
        self._allProperties = ["mass", "initialV", "finalV", "initialM", "finalM", "impulse", "initialKE", "finalKE"]


    # set methods

    def setInitialSpeed(self, value):
        self._speed = value
        self._initialSpeed = value

    # get methods

    def getInitialMomentum(self):
        self._initialMomentum = round(self._mass*self._initialSpeed, 2)
        return self._initialMomentum

    def getInitialKE(self):
        self._initialKE = 0.5 * self._mass * self._initialSpeed ** 2
        return self._initialKE

    def getKE(self):
        # implements kinetic energy equation 
        return 0.5 * self._mass * self._speed ** 2

    def getInitialSpeed(self):
        return self._initialSpeed

    def getDisplayedProperties(self):
        # creates and returns dictionary of displayed properties

        displayedProperties = {}

        if "mass" in self._allProperties:
            displayedProperties["mass"] = self._mass
        if "initialV" in self._allProperties:
            displayedProperties["initialV"] = self._initialSpeed
        if "finalV" in self._allProperties:
            displayedProperties["finalV"] = self._speed
        if "initialM" in self._allProperties:
            displayedProperties["initialM"] = self._initialMomentum
        if "finalM" in self._allProperties:
            displayedProperties["finalM"] = self._momenta[1]
        if "impulse" in self._allProperties:
            displayedProperties["impulse"] = self.getImpulse()
        if "initialKE" in self._allProperties:
            displayedProperties["initialKE"] = self._initialKE
        if "finalKE" in self._allProperties:
            displayedProperties["finalKE"] = self.getKE()

        return displayedProperties

    def getHiddenProperties(self):
        # creates and returns dictionary of hidden properties
    
        hiddenProperties = {}

        if "mass" not in self._hiddenProperties:
            hiddenProperties["mass"] = self._mass
        if "initialV" not in self._hiddenProperties:
            hiddenProperties["initialV"] = self._initialSpeed
        if "finalV" not in self._hiddenProperties:
            hiddenProperties["finalV"] = self._speed
        if "initialM" not in self._hiddenProperties:
            hiddenProperties["initialM"] = self._initialMomentum
        if "finalM" not in self._hiddenProperties:
            hiddenProperties["finalM"] = self._momenta[1]
        if "impulse" not in self._hiddenProperties:
            hiddenProperties["impulse"] = self.getImpulse()
        if "initialKE" not in self._hiddenProperties:
            hiddenProperties["initialKE"] = self._initialKE
        if "finalKE" not in self._hiddenProperties:
            hiddenProperties["finalKE"] = self.getKE()

        return hiddenProperties


    # methods to store property as a hidden property if they have been right-clicked

    def hideMass(self):
        # toggle function of removing and adding property name to list
        if "mass" in self._hiddenProperties:
            self._hiddenProperties.remove("mass")
        else:
            self._hiddenProperties.append("mass")

    def hideInitialV(self):
        if "initialV" in self._hiddenProperties:
            self._hiddenProperties.remove("initialV")
        else:
            self._hiddenProperties.append("initialV")

    def hideFinalV(self):
        if "finalV" in self._hiddenProperties:
            self._hiddenProperties.remove("finalV")
        else:
            self._hiddenProperties.append("finalV")

    def hideInitialM(self):
        if "initialM" in self._hiddenProperties:
            self._hiddenProperties.remove("initialM")
        else:
            self._hiddenProperties.append("initialM")

    def hideFinalM(self):
        if "finalM" in self._hiddenProperties:
            self._hiddenProperties.remove("finalM")
        else:
            self._hiddenProperties.append("finalM")

    def hideImpulse(self):
        if "impulse" in self._hiddenProperties:
            self._hiddenProperties.remove("impulse")
        else:
            self._hiddenProperties.append("impulse")

    def hideInitialKE(self):
        if "initialKE" in self._hiddenProperties:
            self._hiddenProperties.remove("initialKE")
        else:
            self._hiddenProperties.append("initialKE")

    def hideFinalKE(self):
        if "finalKE" in self._hiddenProperties:
            self._hiddenProperties.remove("finalKE")
        else:
            self._hiddenProperties.append("finalKE")