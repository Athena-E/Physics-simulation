from particles.question_particle import QuestionParticle

# class for particle in test environment
# inherits from QuestionParticle class
class TestParticle(QuestionParticle):

    def __init__(self, position, size, screen, screenW, screenH, screenPos, boundaryX, boundaryY, color):
        # constructor to initialise class properties
        # inherits properties from parent class
        super().__init__(position, size, screen, screenW, screenH, screenPos, boundaryX, boundaryY, color)


    def setInitialProperties(self, particleProperties):
        # sets speed and mass of particle according to the fetched question particle properties
        self._initialSpeed = particleProperties.get("initialV")
        self._speed = self._initialSpeed
        self._mass = particleProperties.get("mass")

