from __init__ import TextBox
from page_elements.question_page.question_page_containers import QuestionPageContainers

# class to set and initialise text labels for question page
# inherits from QuestionPageContainers class
class QuestionPagePropertyLabels(QuestionPageContainers):

    def __init__(self, width, height, mainWidth, mainHeight, margin, screen):
        # inherits properties from parent class
        super().__init__(width, height, mainWidth, mainHeight, margin, screen)

        self.setPropertyLabels()
        self.initPropertyLabels()

    def setPropertyLabels(self):
        # calculate dimensions and positions of labels

        self.particleLabelSize = self.propertiesH/5
        self.propertiesFontSize = int(self.particleLabelSize*(3/4))

        self.massLabelPos = (self.propertiesPos[0]+self.margin*(7/2), self.propertiesPos[1]+self.margin*2)
        self.velocityLabelPos = (self.massLabelPos[0]+self.margin*7.25, self.propertiesPos[1]+self.margin*0.75)
        self.vSubscriptPos = (self.velocityLabelPos[0]+self.propertiesFontSize*4.2, self.velocityLabelPos[1])
        self.initialVLabelPos = (self.massLabelPos[0]+self.margin*7, self.massLabelPos[1])
        self.finalVLabelPos = (self.initialVLabelPos[0]+self.margin*5, self.massLabelPos[1])
        self.sizeLabelPos = (self.finalVLabelPos[0]+self.margin*5, self.massLabelPos[1])
        self.momentumLabelPos = (self.sizeLabelPos[0]+self.margin*4.25, self.velocityLabelPos[1])
        self.mSubscriptPos = (self.momentumLabelPos[0]+self.propertiesFontSize*6.25, self.momentumLabelPos[1])
        self.initialMLabelPos = (self.sizeLabelPos[0]+self.margin*5.5, self.massLabelPos[1])
        self.finalMLabelPos = (self.initialMLabelPos[0]+self.margin*5, self.massLabelPos[1])
        self.impulseLabelPos = (self.momentumLabelPos[0]+self.margin*12, self.sizeLabelPos[1])
        self.KELabelPos = (self.impulseLabelPos[0]+self.margin*8.25, self.velocityLabelPos[1])
        self.initialKELabelPos = (self.impulseLabelPos[0]+self.margin*9, self.impulseLabelPos[1])
        self.finalKELabelPos = (self.initialKELabelPos[0]+self.margin*5, self.impulseLabelPos[1])

    def initPropertyLabels(self):
        # instantiate text box objects

        massLabel = TextBox(pos=self.massLabelPos, screen=self.screen, text="mass/kg", fontSize=self.propertiesFontSize)
        velocityLabel = TextBox(pos=self.velocityLabelPos, screen=self.screen, text="velocity/ms", fontSize=self.propertiesFontSize)
        vSubscript = TextBox(pos=self.vSubscriptPos, screen=self.screen, text="-1", fontSize=int(self.propertiesFontSize*0.75))
        initialVLabel = TextBox(pos=self.initialVLabelPos, screen=self.screen, text=("initial"), fontSize=self.propertiesFontSize)
        finalVLabel = TextBox(pos=self.finalVLabelPos, screen=self.screen, text="final", fontSize=self.propertiesFontSize)
        sizeLabel = TextBox(pos=self.sizeLabelPos, screen=self.screen, text="size", fontSize=self.propertiesFontSize)
        momentumLabel = TextBox(pos=self.momentumLabelPos, screen=self.screen, text="momentum/kgms", fontSize=self.propertiesFontSize)
        mSubscript = TextBox(pos=self.mSubscriptPos, screen=self.screen, text="-1", fontSize=int(self.propertiesFontSize*0.75))
        initialMLabel = TextBox(pos=self.initialMLabelPos, screen=self.screen, text="initial", fontSize=self.propertiesFontSize)
        finalMLabel = TextBox(pos=self.finalMLabelPos, screen=self.screen, text="final", fontSize=self.propertiesFontSize)
        impulseLabel = TextBox(pos=self.impulseLabelPos, screen=self.screen, text="impulse/Ns", fontSize=self.propertiesFontSize)
        KELabel = TextBox(pos=self.KELabelPos, screen=self.screen, text="kinetic energy/J", fontSize=self.propertiesFontSize)
        initialKELabel = TextBox(pos=self.initialKELabelPos, screen=self.screen, text="initial", fontSize=self.propertiesFontSize)
        finalKELabel = TextBox(pos=self.finalKELabelPos, screen=self.screen, text="final", fontSize=self.propertiesFontSize)

        self.propertyLabels = [massLabel, velocityLabel, vSubscript, initialVLabel, finalVLabel, sizeLabel, momentumLabel, 
        mSubscript, initialMLabel, finalMLabel, impulseLabel, KELabel, initialKELabel, finalKELabel]

    def drawPropertyLabels(self):
        # draw labels to screen 

        for label in self.propertyLabels:
            label.displayText()


