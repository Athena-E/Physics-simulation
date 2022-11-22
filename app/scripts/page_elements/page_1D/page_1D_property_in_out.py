from page_elements.page_1D.page_1D_property_labels import PropertyLabels1D
from __init__ import pg, TextBox, InputTextBox, Button, colorOrder, red

# class to set and initialise input output elements for 1D page
# inherits from PropertyLabels1D class
class PropertyInOut1D(PropertyLabels1D):

    def __init__(self, width, height, mainWidth, mainHeight, margin, screen, Env):
        # inherits properties from parent class
        super().__init__(width, height, mainWidth, mainHeight, margin, screen)

        self.Env = Env

        # properties to display error message with delay 
        self.clock = pg.time.Clock()
        self.delay = 0

        # call methods to set input output elements for 2 particles
        self.p1Dim = self.setPropertyInOut(0)
        self.p2Dim = self.setPropertyInOut(1)
        
        # call methods to initialise input output elements for 2 particles
        p1InOut = self.initPropertyInOut(self.p1Dim, 1)
        p2InOut = self.initPropertyInOut(self.p2Dim, 2)
        self.pInputOutputList = [p1InOut, p2InOut]

        self.setOutputText()
        self.initOutputText()
        

    def setOutputText(self):
        # calculate position of kinetic energy output text

        self.KETextPos = (self.totalKELabelPos[0], self.totalKELabelPos[1]+self.propertiesFontSize)
        self.alertBoxPos = (self.collisionPos[0]+self.margin, self.collisionPos[1]+self.margin)

    def initOutputText(self):
        # instantiate kinetic energy text box object
    
        self.KEText = TextBox(pos=self.KETextPos, screen=self.screen, text="0.00", fontSize=self.propertiesFontSize)
        self.alertBox = TextBox(pos=self.alertBoxPos, screen=self.screen, fontSize=self.propertiesFontSize, textAlign="right", textColor=red, text="")


    def setPropertyInOut(self, pIndex):
        # calculate positions for input output elements

        particleLabelPos = (self.propertiesPos[0]+self.margin/2, self.propertiesPos[1]+self.margin*4+self.particleLabelSize*pIndex+self.margin*0.5*pIndex)
        massInputPos = (self.massLabelPos[0], particleLabelPos[1])
        vInputPos = (self.velocityLabelPos[0]+self.margin, particleLabelPos[1])
        decreaseSizePos = (vInputPos[0]+self.margin*7.25, particleLabelPos[1]+self.particleLabelSize/2-self.propertiesFontSize/2)
        increaseSizePos = (decreaseSizePos[0]+self.propertiesFontSize+self.margin*0.5, decreaseSizePos[1])
        mTextPos = (increaseSizePos[0]+self.margin*6.5, particleLabelPos[1])
        iTextPos = (mTextPos[0]+self.margin*9.5, particleLabelPos[1])

        # returns positions in dictionary
        propertyInOutDim = {
            "particleLabelPos": particleLabelPos,
            "massInputPos": massInputPos,
            "vInputPos": vInputPos,
            "decreaseSizePos": decreaseSizePos,
            "increaseSizePos": increaseSizePos,
            "mTextPos": mTextPos,
            "iTextPos": iTextPos
        }

        return propertyInOutDim

    def initPropertyInOut(self, pDim, pIndex):
        # instantiate text box and input text box objects

        particleLabel = TextBox(width=self.particleLabelSize, height=self.particleLabelSize, pos=pDim["particleLabelPos"], screen=self.screen, text=str(pIndex), fontSize=self.propertiesFontSize, backColor=colorOrder.get(pIndex))
        massInputBox = InputTextBox(pos=pDim["massInputPos"], screen=self.screen, fontSize=self.propertiesFontSize, text="1.00", returnFunction=self.Env.setParticleMass, parameter=pIndex)
        vInputBox = InputTextBox(pos=pDim["vInputPos"], screen=self.screen, fontSize=self.propertiesFontSize, text="0.00", returnFunction=self.Env.setParticleSpeed, parameter=pIndex)
        decreaseSizeButton = Button(pos=pDim["decreaseSizePos"], screen=self.screen, width=self.propertiesFontSize, height=self.propertiesFontSize, text="-", onClickFunction=self.Env.decreaseParticleSize, parameter=pIndex)
        increaseSizeButton = Button(pos=pDim["increaseSizePos"], screen=self.screen, fontSize=self.propertiesFontSize, width=self.propertiesFontSize, height=self.propertiesFontSize, text="+", onClickFunction=self.Env.increaseParticleSize, parameter=pIndex)
        mText = TextBox(pos=pDim["mTextPos"], screen=self.screen, text="0.00", fontSize=self.propertiesFontSize)
        iText = TextBox(pos=pDim["iTextPos"], screen=self.screen, text="0.00", fontSize=self.propertiesFontSize)

        # return objects as a dictionary
        pInputOutput = {
            "particleLabel": particleLabel,
            "massInputBox": massInputBox,
            "vInputBox": vInputBox,
            "decreaseSizeButton": decreaseSizeButton,
            "increaseSizeButton": increaseSizeButton,
            "mText": mText,
            "iText": iText
        }

        return pInputOutput

    def drawPropertyInOut(self, events):
        # draws input output elements to the screen

        for i in range(2):
            self.pInputOutputList[i]["particleLabel"].displayText()
            self.pInputOutputList[i]["massInputBox"].displayText()
            self.pInputOutputList[i]["massInputBox"].updateInput(events)
            self.pInputOutputList[i]["vInputBox"].displayText()
            self.pInputOutputList[i]["vInputBox"].updateInput(events)
            self.pInputOutputList[i]["decreaseSizeButton"].displayButton(events)
            self.pInputOutputList[i]["increaseSizeButton"].displayButton(events)
            self.pInputOutputList[i]["mText"].displayText()
            self.pInputOutputList[i]["mText"].update(str(self.Env.getParticleMomentum(1)))
            self.pInputOutputList[i]["iText"].displayText()
            self.pInputOutputList[i]["iText"].update(str(self.Env.getParticleImpulse(1)))

            self.pInputOutputList[i]["vInputBox"].update(str(round(self.Env.getParticleSpeed(i+1), 2)))
            self.pInputOutputList[i]["massInputBox"].update(str(round(self.Env.getParticleMass(i+1), 2)))

        self.KEText.displayText()
        self.KEText.update(str(self.Env.getTotalKineticEnergy()))

        self.alertBox.displayText()
        
        errorAlert = self.Env.getParticleErrorAlert()
        self.alertBox.update(errorAlert)

        if errorAlert != "":
            dt = self.clock.tick()
            self.delay += dt

            if self.delay > 8000:
                self.Env.resetParticleErrorAlert()
                self.delay = 0
