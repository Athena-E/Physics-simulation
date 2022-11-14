from page_elements.page_2D.page_2D_property_labels import PropertyLabels2D
from __init__ import pg, TextBox, InputTextBox, Button, colorOrder, red, time

# class to set and initialise input and output elements for 2D page
# inherits from PropertyLabels2D class
class PropertyInOut2D(PropertyLabels2D):

    def __init__(self, width, height, mainWidth, mainHeight, margin, screen, Env):
        # inherits properties from parent class
        super().__init__(width, height, mainWidth, mainHeight, margin, screen)

        # define new properties
        self.Env = Env
        self.inputBoxes = []
        self.inputButtons = []

        # properties to display error message with delay
        self.clock = pg.time.Clock()
        self.delay = 0

        # call method to set input output elements for 4 particles
        self.p1Dim = self.setPropertyInOut(0)
        self.p2Dim = self.setPropertyInOut(1)
        self.p3Dim = self.setPropertyInOut(2)
        self.p4Dim = self.setPropertyInOut(3)
        self.setOutputText()

        # call method to initialise input output elements from 4 particles
        p1InOut = self.initPropertyInputOutput(self.p1Dim, 1)
        p2InOut = self.initPropertyInputOutput(self.p2Dim, 2)
        p3InOut = self.initPropertyInputOutput(self.p3Dim, 3)
        p4InOut = self.initPropertyInputOutput(self.p4Dim, 4)
        self.pInputOutputList = [p1InOut, p2InOut, p3InOut, p4InOut]

        self.initOutputText()


    def setPropertyInOut(self, pIndex):
        # calculate positions for input output elements

        particleLabelPos = (self.propertiesPos[0]+self.margin/2, self.propertiesPos[1]+self.margin*4+self.particleLabelSize*pIndex+self.margin*0.5*pIndex)
        massInputPos = (self.massLabelPos[0], particleLabelPos[1])
        vxInputPos = (self.massLabelPos[0]+self.margin*5.5, particleLabelPos[1])
        vyInputPos = (vxInputPos[0]+self.margin*5, particleLabelPos[1])
        decreaseSizePos = (vyInputPos[0]+self.margin*5, particleLabelPos[1]+self.particleLabelSize/2-self.propertiesFontSize/2)
        increaseSizePos = (decreaseSizePos[0]+self.propertiesFontSize+self.margin*0.5, decreaseSizePos[1])
        mxTextPos = (decreaseSizePos[0]+self.margin*6, massInputPos[1])
        myTextPos = (mxTextPos[0]+self.margin*5, particleLabelPos[1])
        ixTextPos = (myTextPos[0]+self.margin*5, particleLabelPos[1])
        iyTextPos = (ixTextPos[0]+self.margin*5, particleLabelPos[1])

        # return positions as a dictionary
        propertyInOutDim = {
            "particleLabelPos": particleLabelPos,
            "massInputPos": massInputPos,
            "vxInputPos": vxInputPos,
            "vyInputPos": vyInputPos,
            "decreaseSizePos": decreaseSizePos,
            "increaseSizePos": increaseSizePos,
            "mxTextPos": mxTextPos,
            "myTextPos": myTextPos,
            "ixTextPos": ixTextPos,
            "iyTextPos": iyTextPos
        }

        return propertyInOutDim


    def setOutputText(self):
        # calculate position for kinetic energy text output

        self.KETextPos = (self.totalKELabelPos[0], self.totalKELabelPos[1]+self.propertiesFontSize)

        self.alertBoxPos = (self.collisionPos[0]+self.margin, self.collisionPos[1]+self.margin)


    def initOutputText(self):
        # instantiate kinetic energy text box object
    
        self.KEText = TextBox(pos=self.KETextPos, screen=self.screen, text="0.00", fontSize=self.propertiesFontSize)
        self.alertBox = TextBox(pos=self.alertBoxPos, screen=self.screen, fontSize=self.propertiesFontSize, textAlign="right", textColor=red, text="")


    def initPropertyInputOutput(self, pDim, pIndex):
        # instantiate particle input output text box and input text box objects
        
        particleLabel = TextBox(width=self.particleLabelSize, height=self.particleLabelSize, pos=pDim["particleLabelPos"], screen=self.screen, text=str(pIndex), fontSize=self.propertiesFontSize, backColor=colorOrder.get(pIndex))
        massInputBox = InputTextBox(pos=pDim["massInputPos"], screen=self.screen, fontSize=self.propertiesFontSize, text="1.00", returnFunction=self.Env.setParticleMass, parameter=pIndex)
        vxInputBox = InputTextBox(pos=pDim["vxInputPos"], screen=self.screen, fontSize=self.propertiesFontSize, text="0.00", returnFunction=self.Env.setParticleVx, parameter=pIndex)
        vyInputBox = InputTextBox(pos=pDim["vyInputPos"], screen=self.screen, fontSize=self.propertiesFontSize, text="0.00", returnFunction=self.Env.setParticleVy, parameter=pIndex)
        decreaseSizeButton = Button(pos=pDim["decreaseSizePos"], screen=self.screen, width=self.propertiesFontSize, height=self.propertiesFontSize, text="-", onClickFunction=self.Env.decreaseParticleSize, parameter=pIndex, hoverColor=(50,50,50))
        increaseSizeButton = Button(pos=pDim["increaseSizePos"], screen=self.screen, fontSize=self.propertiesFontSize, width=self.propertiesFontSize, height=self.propertiesFontSize, text="+", onClickFunction=self.Env.increaseParticleSize, parameter=pIndex, hoverColor=(50,50,50))
        mxText = TextBox(pos=pDim["mxTextPos"], screen=self.screen, text="0.00", fontSize=self.propertiesFontSize)
        myText = TextBox(pos=pDim["myTextPos"], screen=self.screen, text="0.00", fontSize=self.propertiesFontSize)
        ixText = TextBox(pos=pDim["ixTextPos"], screen=self.screen, text="0.00", fontSize=self.propertiesFontSize)
        iyText = TextBox(pos=pDim["iyTextPos"], screen=self.screen, text="0.00", fontSize=self.propertiesFontSize)
    
        # return input output objects as dictionary
        pInputOutput = {
            "particleLabel": particleLabel,
            "massInputBox": massInputBox,
            "vxInputBox": vxInputBox,
            "vyInputBox": vyInputBox,
            "decreaseSizeButton": decreaseSizeButton,
            "increaseSizeButton": increaseSizeButton,
            "mxText": mxText,
            "myText": myText,
            "ixText": ixText,
            "iyText": iyText
        }

        self.inputBoxes.extend([massInputBox, vxInputBox, vyInputBox])
        self.inputButtons.extend([decreaseSizeButton, increaseSizeButton])

        return pInputOutput


    def drawPropertyInOut(self, events):
        # draw all input output elements to the screen
        # handle user inputs to input text boxes
        # handle text updates in text boxes
        
        for i in range(4):
            self.pInputOutputList[i]["particleLabel"].displayText()
            self.pInputOutputList[i]["massInputBox"].displayText()
            self.pInputOutputList[i]["massInputBox"].updateInput(events)
            self.pInputOutputList[i]["vxInputBox"].displayText()
            self.pInputOutputList[i]["vxInputBox"].updateInput(events)
            self.pInputOutputList[i]["vyInputBox"].displayText()
            self.pInputOutputList[i]["vyInputBox"].updateInput(events)
            self.pInputOutputList[i]["decreaseSizeButton"].displayButton(events)
            self.pInputOutputList[i]["increaseSizeButton"].displayButton(events)
            
            # calls 2D environment methods to calculate momentum and impulse
            self.pInputOutputList[i]["mxText"].displayText()
            self.pInputOutputList[i]["mxText"].update(str(self.Env.getParticleMomentumX(i+1)))
            self.pInputOutputList[i]["myText"].displayText()
            self.pInputOutputList[i]["myText"].update(str(self.Env.getParticleMomentumY(i+1)))
            self.pInputOutputList[i]["ixText"].displayText()
            self.pInputOutputList[i]["ixText"].update(str(self.Env.getParticleImpulseX(i+1)))
            self.pInputOutputList[i]["iyText"].displayText()
            self.pInputOutputList[i]["iyText"].update(str(self.Env.getParticleImpulseY(i+1)))

            # calls 2D environment methods to update new velocities and mass as simulation runs
            self.pInputOutputList[i]["vxInputBox"].update(str(round(self.Env.getParticleVx(i+1), 2)))
            self.pInputOutputList[i]["vyInputBox"].update(str(round(self.Env.getParticleVy(i+1), 2)))
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













