from page_elements.question_page.question_page_property_in_out import QuestionPagePropertyInOut
from __init__ import TextBox

# class to set and initialise input output elements for test page
# inherits from QuestionPagePropertyInOut
class TestPagePropertyInOut(QuestionPagePropertyInOut):

    def __init__(self, width, height, mainWidth, mainHeight, margin, screen, Env):
        # inherits properties from parent class
        super().__init__(width, height, mainWidth, mainHeight, margin, screen, Env)

        self.setOutputText()
        self.initOutputText()

    def setOutputText(self):
        # calculates positions of text output elements
        self.scoreTextPos =  (self.collisionPos[0]+self.collisionW+self.margin*2, self.collisionH*0.8)
        self.wallElasticityTextPos = (self.propertiesPos[0]+self.propertiesW+self.margin*2, self.propertiesPos[1]+self.propertiesH*0.5)
        self.particleElasticityTextPos = (self.wallElasticityTextPos[0], self.wallElasticityTextPos[1]+self.propertiesFontSize+self.margin*0.5)

    def initOutputText(self):
        # instantiates text box objects
        self.scoreText = TextBox(width=self.particleLabelSize, height=self.particleLabelSize, pos=self.scoreTextPos, screen=self.screen, text="0/0", fontSize=self.propertiesFontSize, textAlign="right")
        self.wallElasticityText = TextBox(width=self.particleLabelSize, height=self.particleLabelSize, pos=self.wallElasticityTextPos, screen=self.screen, fontSize=self.propertiesFontSize, textAlign="right")
        self.particleElasticityText = TextBox(width=self.particleLabelSize, height=self.particleLabelSize, pos=self.particleElasticityTextPos, screen=self.screen, fontSize=self.propertiesFontSize, textAlign="right")


    def hidePropertyInOut(self, hiddenData):
        # formats input text boxes that users can view/edit

        # deactivates input text boxes
        for pInOut in self.pInputOutputList:
            for property in pInOut:
                pInOut[property].rightClickFunction = None
                pInOut[property].typable = False
                pInOut[property].returnFunction = None

        # activates input text boxes that require an answer
        for i, pIndex in enumerate(hiddenData):
            particleHiddenProperties = hiddenData[pIndex]
            for property in particleHiddenProperties:
                self.pInputOutputList[i][f"{property}InputBox"].typable = True
                self.pInputOutputList[i][f"{property}InputBox"].text = ""


    def drawPropertyInOut(self, events, hiddenData):
        # draws input output elements to the screen

        self.scoreText.displayText()
        self.scoreText.update(f"Total score: {self.Env.getTotalScore()}/{self.Env.getMaxScore()}")

        self.wallElasticityText.displayText()
        self.wallElasticityText.update(f"wall elasticity = {self.Env.getWallElasticity()}")

        self.particleElasticityText.displayText()
        self.particleElasticityText.update(f"particle elasticity = {self.Env.getParticleElasticity()}")
        

        for i in range(self.Env._numOfParticles):

            self.pInputOutputList[i]["particleLabel"].displayText()

            self.pInputOutputList[i]["massInputBox"].displayText()
            self.pInputOutputList[i]["massInputBox"].updateInput(events)

            self.pInputOutputList[i]["initialVInputBox"].displayText()
            self.pInputOutputList[i]["initialVInputBox"].updateInput(events)

            self.pInputOutputList[i]["finalVInputBox"].displayText()
            self.pInputOutputList[i]["finalVInputBox"].updateInput(events)

            self.pInputOutputList[i]["decreaseSizeButton"].displayButton(events)
            self.pInputOutputList[i]["increaseSizeButton"].displayButton(events)

            self.pInputOutputList[i]["initialMInputBox"].displayText()
            self.pInputOutputList[i]["initialMInputBox"].updateInput(events)
            if "initialM" not in hiddenData[f"particle{i+1}"]:
                self.pInputOutputList[i]["initialMInputBox"].update(f"{self.Env.getParticleInitialMomentum(i+1)}")

            self.pInputOutputList[i]["finalMInputBox"].displayText()
            self.pInputOutputList[i]["finalMInputBox"].updateInput(events)
            if "finalM" not in hiddenData[f"particle{i+1}"]:
                self.pInputOutputList[i]["finalMInputBox"].update(f"{self.Env.getParticleMomentum(i+1)}")

            self.pInputOutputList[i]["impulseInputBox"].displayText()
            self.pInputOutputList[i]["impulseInputBox"].updateInput(events)
            if "impulse" not in hiddenData[f"particle{i+1}"]:
                self.pInputOutputList[i]["impulseInputBox"].update(f"{self.Env.getParticleImpulse(i+1)}")

            self.pInputOutputList[i]["initialKEInputBox"].displayText()
            self.pInputOutputList[i]["initialKEInputBox"].updateInput(events)
            if "initialKE" not in hiddenData[f"particle{i+1}"]:
                self.pInputOutputList[i]["initialKEInputBox"].update(f"{self.Env.getParticleInitialKE(i+1)}")

            self.pInputOutputList[i]["finalKEInputBox"].displayText()
            self.pInputOutputList[i]["finalKEInputBox"].updateInput(events)
            if "finalKE" not in hiddenData[f"particle{i+1}"]:
                self.pInputOutputList[i]["finalKEInputBox"].update(f"{self.Env.getParticleKE(i+1)}")

        


    def updateVOutput(self, hiddenData):
        # updates displayed initial and final speeds if properties are not hidden
        for i in range(self.Env._numOfParticles):
            if "finalV" not in hiddenData[f"particle{i+1}"]:
                self.pInputOutputList[i]["finalVInputBox"].update(f"{round(self.Env._particleList[i]._speed, 2)}")
            if "initialV" not in hiddenData[f"particle{i+1}"]:
                self.pInputOutputList[i]["initialVInputBox"].update(f"{round(self.Env._particleList[i]._initialSpeed, 2)}")

    
    def getAnswerInput(self, hiddenData):
        # returns user answers as a dictionary with property as key and answer as value

        answerInput = {}

        for i, pIndex in enumerate(hiddenData):
            particleHiddenProperties = hiddenData[pIndex]
            answerInput[pIndex] = {}
            for property in particleHiddenProperties:
                answerInput[pIndex][f"{property}"] = self.pInputOutputList[i][f"{property}InputBox"].text

        return answerInput


    def markAnswerInput(self, answersCorrect):
        # formats text boxes containing answers
        # text box is green for correct answers
        # text box is red for incorrect answers

        for i, pIndex in enumerate(answersCorrect):
            particleAnswersCorrect = answersCorrect[pIndex]
            for property in particleAnswersCorrect:
                if particleAnswersCorrect[property]:
                    self.pInputOutputList[i][f"{property}InputBox"].boxColor = (0, 255, 0)
                else:
                    self.pInputOutputList[i][f"{property}InputBox"].boxColor = (255, 0, 0)

    def revealAnswers(self, hiddenData):
        # reveals all answers in green text box

        for i, pIndex in enumerate(hiddenData):
            particleHiddenProperties = hiddenData[pIndex]
            for property in particleHiddenProperties:
                self.pInputOutputList[i][f"{property}InputBox"].typable = False
                self.pInputOutputList[i][f"{property}InputBox"].untypableColor = (0, 255, 0)
                self.pInputOutputList[i][f"{property}InputBox"].text = str(round(float(particleHiddenProperties[property]), 2))

