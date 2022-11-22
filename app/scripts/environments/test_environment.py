from environments.__init__ import colorOrder
from environments.question_environment import QuestionEnvironment
from particles.test_particle import TestParticle

# class for test page environment
# inherits from QuestionEnvironment
class TestEnvironment(QuestionEnvironment):

    def __init__(self, screen, screenW, screenH, screenPos, maxParticles):
        # contructor to initialise properties
        # inherits properties from parent class
        super().__init__(screen, screenW, screenH, screenPos, maxParticles)

        # flags to indicate when buttons have been clicked
        self.nextClicked = False
        self.submitClicked = False
        self.revealClicked = False
        self.finishClicked = False

        self._isEndOfQuestion = False

        self._totalScore = 0
        self._maxScore = 0
        self._attempts = 0


    def addParticle(self, environmentData): # override
        # adds particles from question to test environment in the stored positions
        for i in range(1, self._numOfParticles+1):

            particlePos = environmentData.get(f"particlePos{i}")
            x, y = particlePos[0], particlePos[1]

            newParticle = TestParticle((x, y), int(self._screenH/10), self._screen, self._screenW, self._screenH, self._screenPos, self._boundaryX, self._boundaryY, colorOrder[i])
            self._particleList.append(newParticle)


    # methods to handle button clicks

    def onClickNext(self):
        self.nextClicked = True
        self._attempts = 0

    def onClickSubmit(self):
        self.submitClicked = True
        self._attempts += 1

    def onClickReveal(self):
        self.revealClicked = True

    def onClickFinish(self):
        self.finishClicked = True
        

    def start(self): # override
        # runs simulation if question is being shown and end of question simulation is not yet reached
        if self._numOfParticles != 0 and not self._isEndOfQuestion:
            self.run = True

    def stop(self): # override
        # stops and resets question simulation
        self.run = False
        self._isEndOfQuestion = False
        self.clear()
        self.setQuestionEnvProperties(self.environmentData)
        self.setQuestionParticleProperties(self.particleData)


    # set methods

    def setQuestionEnvProperties(self, environmentData):
        # store question environment properties to class attributes
        self.environmentData = environmentData

        self._numOfParticles = environmentData.get("noOfParticles")
        self._particleElasticity = environmentData.get("particleElasticity")
        self._wallElasticity = environmentData.get("wallElasticity")

        # add particles in the question
        self.addParticle(environmentData)

    def setQuestionParticleProperties(self, particleData):
        # set particle properties of each particle in the question
        self.particleData = particleData

        for particle, pIndex in zip(self._particleList, particleData):
            particle.setInitialProperties(particleData[pIndex])
            particle.setWallElasticity(self._wallElasticity)

    def setQuestionHiddenProperties(self, hiddenData):
        # store hidden question properties to class attribute
        self.hiddenData = hiddenData

    def setTotalScore(self, value):
        self._totalScore = value

    def setMaxScore(self, value):
        self._maxScore = value

    
    def checkAnswers(self, answerInput):
        # compares input answers with actual answers
        # returns dictionary of dictionaries of each particle's property keys and values; True if correct, False if incorrect

        answersCorrect = {}

        for particleNum in self.hiddenData:
            # create dictionary for each particle in answer dictionary
            answersCorrect[particleNum] = {}
            for hiddenProperty in self.hiddenData[particleNum]:
                if self._attempts == 1:
                    # increments maximum possible score for each available answer
                    self._maxScore += 1
                try:
                    # checks if answer is correct
                    if round(float(self.hiddenData[particleNum][hiddenProperty]), 2) == round(float(answerInput[particleNum][hiddenProperty]), 2):
                        answersCorrect[particleNum][hiddenProperty] = True
                    else:
                        answersCorrect[particleNum][hiddenProperty] = False
                except:
                    # exception raised if answer is null, so answer is incorrect by default
                    answersCorrect[particleNum][hiddenProperty] = False

        return answersCorrect

    def calculateScore(self, answersCorrect):
        # each correct property increments score by one
        # scores only counted on first attempt at question

        questionScore = 0
        if self._attempts == 1:
            for particleNum in answersCorrect:
                particleAnswer = answersCorrect[particleNum]
                for answer in particleAnswer:
                    if particleAnswer[answer]:
                        questionScore += 1
        
        # increment total score of all answered questions
        self._totalScore += questionScore


    # get methods

    def getTotalScore(self):
        return self._totalScore 

    def getMaxScore(self):
        return self._maxScore


    def compareV(self):
        # checks whether the current particle speed is equal to the final speed to signify end of question

        isEnd = True
        for particleNum, particle in zip(self.particleData, self._particleList):
            particleFinalV = self.particleData[particleNum]["finalV"]
            if particle.getSpeed() != particleFinalV:
                isEnd = False

        if isEnd:
            self.run = False
            self._isEndOfQuestion = True
                


