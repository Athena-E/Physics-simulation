from page_elements.gas_page.gas_page_containers import GasPageContainers
from __init__ import Button
from page2D import showPage2D

# class to set and initialise buttons for gas page
# inherits from GasPageContainers class
class GasPageButtons(GasPageContainers):

    def __init__(self, width, height, mainWidth, mainHeight, margin, screen, Env):
        # inherits properties from parent class
        super().__init__(width, height, mainWidth, mainHeight, margin, screen)
        self.Env = Env

        self.setButtons()
        self.initButtons()

    def setButtons(self):
        # calculate dimensions and positions of buttons

        self.controlButtonSize = self.mainHeight/17

        self.backButtonPos = (self.propertiesPos[0]+self.propertiesW+2*self.margin, self.propertiesPos[1])

    def initButtons(self):
        # instantiate button object

        self.backButton = Button(text="Back", pos=self.backButtonPos, width=self.controlButtonSize*5, height=self.controlButtonSize*1.2, fontSize=int(self.controlButtonSize*0.75), screen=self.screen, color=(177, 221, 240), textColor=(0, 0, 0), onClickFunction=showPage2D)

    def drawButtons(self, events):
        # draw button to screen

        self.backButton.displayButton(events)
        

