from __init__ import TextBox, InputTextBox, Button, colorOrder
from page_elements.question_page.question_page_property_labels import QuestionPagePropertyLabels

# class to set and initialise input output elements for question page
# inherits from QuestionPagePropertyLabels class
class QuestionPagePropertyInOut(QuestionPagePropertyLabels):

    def __init__(self, width, height, mainWidth, mainHeight, margin, screen, Env):
        # inherits properties from parent class
        super().__init__(width, height, mainWidth, mainHeight, margin, screen)

        self.Env = Env

        # call methods to set input output elements for 2 particles
        self.p1Dim = self.setPropertyInOut(0)
        self.p2Dim = self.setPropertyInOut(1)

        # call methods to initialise input output elements for 2 particles
        p1InOut = self.initPropertyInOut(self.p1Dim, 1)
        p2InOut = self.initPropertyInOut(self.p2Dim, 2)
        self.pInputOutputList = [p1InOut, p2InOut]


    def setPropertyInOut(self, pIndex):
        # calculate positions of input output elements

        particleLabelPos = (self.propertiesPos[0]+self.margin/2, self.propertiesPos[1]+self.margin*4+self.particleLabelSize*pIndex+self.margin*0.5*pIndex)
        massInputPos = (self.massLabelPos[0], particleLabelPos[1])
        initialVInputPos = (self.massLabelPos[0]+self.margin*6, particleLabelPos[1])
        finalVPos = (initialVInputPos[0]+self.margin*5, particleLabelPos[1])
        decreaseSizePos = (finalVPos[0]+self.margin*5.5, particleLabelPos[1]+self.particleLabelSize/2-self.propertiesFontSize/2)
        increaseSizePos = (decreaseSizePos[0]+self.propertiesFontSize+self.margin*0.5, decreaseSizePos[1])
        initialMTextPos = (increaseSizePos[0]+self.margin*3, particleLabelPos[1])
        finalMTextPos = (initialMTextPos[0]+self.margin*5, particleLabelPos[1])
        impulseTextPos = (finalMTextPos[0]+self.margin*7.5, particleLabelPos[1])
        initialKETextPos = (impulseTextPos[0]+self.margin*7, particleLabelPos[1])
        finalKETextPos = (initialKETextPos[0]+self.margin*5, particleLabelPos[1])

        # return positions in a dictionary
        propertyInOutDim = {
            "particleLabelPos": particleLabelPos,
            "massInputPos": massInputPos,
            "initialVInputPos": initialVInputPos,
            "finalVPos": finalVPos,
            "decreaseSizePos": decreaseSizePos,
            "increaseSizePos": increaseSizePos,
            "initialMTextPos": initialMTextPos,
            "finalMTextPos": finalMTextPos,
            "impulseTextPos": impulseTextPos,
            "initialKETextPos": initialKETextPos,
            "finalKETextPos": finalKETextPos
        }

        return propertyInOutDim



    def initPropertyInOut(self, pDim, pIndex):
        # instantiate text box and input text box objects

        particleLabel = TextBox(width=self.particleLabelSize, height=self.particleLabelSize, pos=pDim["particleLabelPos"], screen=self.screen, text=str(pIndex), fontSize=self.propertiesFontSize, backColor=colorOrder.get(pIndex))
        massInputBox = InputTextBox(pos=pDim["massInputPos"], screen=self.screen, fontSize=self.propertiesFontSize, text="1.00", returnFunction=self.Env.setParticleMass, parameter=pIndex, rightClickFunction=self.Env.hideParticleMass, rightClickParam=pIndex)
        initialVInputBox = InputTextBox(pos=pDim["initialVInputPos"], screen=self.screen, fontSize=self.propertiesFontSize, text="0.00", parameter=pIndex, returnFunction=self.Env.setParticleInitialSpeed, rightClickFunction=self.Env.hideParticleInitialV, rightClickParam=pIndex)
        finalVInputBox = InputTextBox(pos=pDim["finalVPos"], screen=self.screen, text="0.00", fontSize=self.propertiesFontSize, typable=False, rightClickFunction=self.Env.hideParticleFinalV, rightClickParam=pIndex)
        decreaseSizeButton = Button(pos=pDim["decreaseSizePos"], screen=self.screen, width=self.propertiesFontSize, height=self.propertiesFontSize, text="-", onClickFunction=self.Env.decreaseParticleSize, parameter=pIndex, hoverColor=(50,50,50))
        increaseSizeButton = Button(pos=pDim["increaseSizePos"], screen=self.screen, fontSize=self.propertiesFontSize, width=self.propertiesFontSize, height=self.propertiesFontSize, text="+", onClickFunction=self.Env.increaseParticleSize, parameter=pIndex, hoverColor=(50,50,50))
        initialMInputBox = InputTextBox(pos=pDim["initialMTextPos"], screen=self.screen, text="0.00", fontSize=self.propertiesFontSize, typable=False, rightClickFunction=self.Env.hideParticleInitialM, rightClickParam=pIndex)
        finalMInputBox = InputTextBox(pos=pDim["finalMTextPos"], screen=self.screen, text="0.00", fontSize=self.propertiesFontSize, typable=False, rightClickFunction=self.Env.hideParticleFinalM, rightClickParam=pIndex)
        impulseInputBox = InputTextBox(pos=pDim["impulseTextPos"], screen=self.screen, text="0.00", fontSize=self.propertiesFontSize, typable=False, rightClickFunction=self.Env.hideParticleImpulse, rightClickParam=pIndex)
        initialKEInputBox = InputTextBox(pos=pDim["initialKETextPos"], screen=self.screen, text="0.00", fontSize=self.propertiesFontSize, typable=False, rightClickFunction=self.Env.hideParticleInitialKE, rightClickParam=pIndex)
        finalKEInputBox = InputTextBox(pos=pDim["finalKETextPos"], screen=self.screen, text="0.00", fontSize=self.propertiesFontSize, typable=False, rightClickFunction=self.Env.hideParticleFinalKE, rightClickParam=pIndex)

        # returns objects in a dictionary
        pInputOutput = {
            "particleLabel": particleLabel,
            "massInputBox": massInputBox,
            "initialVInputBox": initialVInputBox,
            "finalVInputBox": finalVInputBox,
            "decreaseSizeButton": decreaseSizeButton,
            "increaseSizeButton": increaseSizeButton,
            "initialMInputBox": initialMInputBox,
            "finalMInputBox": finalMInputBox,
            "impulseInputBox": impulseInputBox,
            "initialKEInputBox": initialKEInputBox,
            "finalKEInputBox": finalKEInputBox
        }

        return pInputOutput

    def drawPropertyInOut(self, events):
        # draws input output elements to the screen

        for i in range(2):
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
            self.pInputOutputList[i]["initialMInputBox"].update(str(self.Env.getParticleInitialMomentum(i+1)))

            self.pInputOutputList[i]["finalMInputBox"].displayText()
            self.pInputOutputList[i]["finalMInputBox"].updateInput(events)
            self.pInputOutputList[i]["finalMInputBox"].update(str(self.Env.getParticleMomentum(i+1)))

            self.pInputOutputList[i]["impulseInputBox"].displayText()
            self.pInputOutputList[i]["impulseInputBox"].updateInput(events)
            self.pInputOutputList[i]["impulseInputBox"].update(str(self.Env.getParticleImpulse(i+1)))

            self.pInputOutputList[i]["initialKEInputBox"].displayText()
            self.pInputOutputList[i]["initialKEInputBox"].updateInput(events)
            self.pInputOutputList[i]["initialKEInputBox"].update(str(self.Env.getParticleInitialKE(i+1)))

            self.pInputOutputList[i]["finalKEInputBox"].displayText()
            self.pInputOutputList[i]["finalKEInputBox"].updateInput(events)
            self.pInputOutputList[i]["finalKEInputBox"].update(str(self.Env.getParticleKE(i+1)))


    def updateVOutput(self):
        # updates displayed final and initial speeds
        for i in range(self.Env.getNoOfParticles()):
            self.pInputOutputList[i]["finalVInputBox"].update(str(round(self.Env.getParticleFromList(i).getSpeed(), 2)))
            self.pInputOutputList[i]["initialVInputBox"].update(str(round(self.Env.getParticleFromList(i).getInitialSpeed(), 2)))

