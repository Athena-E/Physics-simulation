from __init__ import TextBox
from page_elements.page_containers import PageContainers

# class to set and initialise text labels for 2D page
# inherits from PageContainers class
class PropertyLabels2D(PageContainers):

    def __init__(self, width, height, mainWidth, mainHeight, margin, screen):
        # inherits properties from parent class
        super().__init__(width, height, mainWidth, mainHeight, margin, screen)

        self.setPropertyLabels()
        self.initPropertyLabels()
    

    def setPropertyLabels(self):
        # calculate dimensions and positions of text labels

        self.particleLabelSize = self.propertiesH/7
        self.propertiesFontSize = int(self.particleLabelSize*(3/4))

        self.massLabelPos = (self.propertiesPos[0]+self.margin*(7/2), self.propertiesPos[1]+self.margin*2)
        self.velocityLabelPos = (self.massLabelPos[0]+self.margin*6, self.propertiesPos[1]+self.margin*0.75)
        self.vSubscriptPos = (self.velocityLabelPos[0]+self.propertiesFontSize*4, self.velocityLabelPos[1])
        self.vxLabelPos = (self.massLabelPos[0]+self.margin*7, self.massLabelPos[1])
        self.vyLabelPos = (self.vxLabelPos[0]+self.margin*5, self.massLabelPos[1])
        self.sizeLabelPos = (self.vxLabelPos[0]+self.margin*9.25, self.massLabelPos[1])
        self.momentumLabelPos = (self.sizeLabelPos[0]+self.margin*4, self.velocityLabelPos[1])
        self.mSubscriptPos = (self.momentumLabelPos[0]+self.propertiesFontSize*6.25, self.momentumLabelPos[1])
        self.mxLabelPos = (self.sizeLabelPos[0]+self.margin*6, self.massLabelPos[1])
        self.myLabelPos = (self.mxLabelPos[0]+self.margin*5, self.massLabelPos[1])
        self.impulseLabelPos = (self.momentumLabelPos[0]+self.margin*11.5, self.velocityLabelPos[1])
        self.ixLabelPos = (self.myLabelPos[0]+self.margin*5, self.massLabelPos[1])
        self.iyLabelPos = (self.ixLabelPos[0]+self.margin*5, self.massLabelPos[1])
        self.totalKELabelPos = (self.collisionPos[0]+self.collisionW+self.margin, self.collisionPos[1]+self.collisionH+self.margin)

    def initPropertyLabels(self):
        # instantialise text box objects

        massLabel = TextBox(pos=self.massLabelPos, screen=self.screen, text="mass/kg", fontSize=self.propertiesFontSize)
        velocityLabel = TextBox(pos=self.velocityLabelPos, screen=self.screen, text="velocity/ms", fontSize=self.propertiesFontSize)
        vSubscript = TextBox(pos=self.vSubscriptPos, screen=self.screen, text="-1", fontSize=int(self.propertiesFontSize*0.75))
        vxLabel = TextBox(pos=self.vxLabelPos, screen=self.screen, text=("x"), fontSize=self.propertiesFontSize)
        vyLabel = TextBox(pos=self.vyLabelPos, screen=self.screen, text="y", fontSize=self.propertiesFontSize)
        sizeLabel = TextBox(pos=self.sizeLabelPos, screen=self.screen, text="size", fontSize=self.propertiesFontSize)
        momentumLabel = TextBox(pos=self.momentumLabelPos, screen=self.screen, text="momentum/kgms", fontSize=self.propertiesFontSize)
        mSubscript = TextBox(pos=self.mSubscriptPos, screen=self.screen, text="-1", fontSize=int(self.propertiesFontSize*0.75))
        mxLabel = TextBox(pos=self.mxLabelPos, screen=self.screen, text="x", fontSize=self.propertiesFontSize)
        myLabel = TextBox(pos=self.myLabelPos, screen=self.screen, text="y", fontSize=self.propertiesFontSize)
        impulseLabel = TextBox(pos=self.impulseLabelPos, screen=self.screen, text="impulse/Ns", fontSize=self.propertiesFontSize)
        ixLabel = TextBox(pos=self.ixLabelPos, screen=self.screen, text="x", fontSize=self.propertiesFontSize)
        iyLabel = TextBox(pos=self.iyLabelPos, screen=self.screen, text="y", fontSize=self.propertiesFontSize)
        totalKELabel = TextBox(pos=self.totalKELabelPos, screen=self.screen, text="Kinetic Energy/J =", fontSize=self.propertiesFontSize)

        self.propertyLabels = [massLabel, velocityLabel, vSubscript, vxLabel, vyLabel, sizeLabel, momentumLabel, 
        mSubscript, mxLabel, myLabel, impulseLabel, ixLabel, iyLabel, totalKELabel]

    def drawPropertyLabels(self):
        # draw labels to screen

        for label in self.propertyLabels:
            label.displayText()






