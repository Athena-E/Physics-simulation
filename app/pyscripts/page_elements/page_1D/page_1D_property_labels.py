from __init__ import TextBox
from page_elements.page_containers import PageContainers

# class to set and initialise labels for 1D page
# inherits from PageContainers class
class PropertyLabels1D(PageContainers):

    def __init__(self, width, height, mainWidth, mainHeight, margin, screen):
        # inherits properties from parent class
        super().__init__(width, height, mainWidth, mainHeight, margin, screen)

        self.setPropertyLabels()
        self.initPropertyLabels()

    def setPropertyLabels(self):
        # calculate dimensions and positions of text labels

        self.particleLabelSize = self.propertiesH/7
        self.propertiesFontSize = int(self.particleLabelSize*3/4)

        self.massLabelPos = (self.propertiesPos[0]+self.margin*(7/2), self.propertiesPos[1]+self.margin*2)
        self.velocityLabelPos = (self.massLabelPos[0]+self.margin*6, self.massLabelPos[1])
        self.vSubscriptPos = (self.velocityLabelPos[0]+self.propertiesFontSize*4, self.massLabelPos[1])
        self.sizeLabelPos = (self.massLabelPos[0]+self.margin*15, self.massLabelPos[1])
        self.momentumLabelPos = (self.sizeLabelPos[0]+self.margin*4, self.massLabelPos[1])
        self.mSubscriptPos = (self.momentumLabelPos[0]+self.propertiesFontSize*6.25, self.massLabelPos[1])
        self.impulseLabelPos = (self.momentumLabelPos[0]+self.margin*11.5, self.massLabelPos[1])
        self.totalKELabelPos = (self.collisionPos[0]+self.collisionW+self.margin, self.collisionPos[1]+self.collisionH+self.margin)

    def initPropertyLabels(self):
        # instantiates text box objects
        
        massLabel = TextBox(pos=self.massLabelPos, screen=self.screen, text="mass/kg", fontSize=self.propertiesFontSize)
        velocityLabel = TextBox(pos=self.velocityLabelPos, screen=self.screen, text="velocity/ms", fontSize=self.propertiesFontSize)
        vSubscript = TextBox(pos=self.vSubscriptPos, screen=self.screen, text="-1", fontSize=int(self.propertiesFontSize*0.75))
        sizeLabel = TextBox(pos=self.sizeLabelPos, screen=self.screen, text="size", fontSize=self.propertiesFontSize)
        momentumLabel = TextBox(pos=self.momentumLabelPos, screen=self.screen, text="momentum/kgms", fontSize=self.propertiesFontSize)
        mSubscript = TextBox(pos=self.mSubscriptPos, screen=self.screen, text="-1", fontSize=int(self.propertiesFontSize*0.75))
        impulseLabel = TextBox(pos=self.impulseLabelPos, screen=self.screen, text="impulse/Ns", fontSize=self.propertiesFontSize)
        totalKELabel = TextBox(pos=self.totalKELabelPos, screen=self.screen, text="Kinetic Energy/J =", fontSize=self.propertiesFontSize)

        self.propertyLabels = [massLabel, velocityLabel, vSubscript, sizeLabel, momentumLabel, mSubscript, impulseLabel, totalKELabel]

    def drawPropertyLabels(self):
        # draws labels to the screen

        for label in self.propertyLabels:
            label.displayText()