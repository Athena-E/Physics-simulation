from __init__ import Button
from page_elements.page_buttons import PageButtons
from page2D import showPage2D

# class to set and initialise buttons for 1D page
# inherits from PageButtons class
class Page1DButtons(PageButtons):

    def __init__(self, width, height, mainWidth, mainheight, margin, screen, Env):
        # inherits properties from parent class
        super().__init__(width, height, mainWidth, mainheight, margin, screen, Env)
        
        self.setButtons()
        self.initButtons()

    def setButtons(self): # extended method
        # calculate position of buttons

        super(Page1DButtons, self).setButtons()

        self.backButtonPos = (self.showMomentumGraphPos[0], self.showMomentumGraphPos[1]+self.controlButtonSize+self.margin*4)

    def initButtons(self): # extended method
        # instantiate button objects

        super(Page1DButtons, self).initButtons()

        self.backButton = Button(text="Back", pos=self.backButtonPos, width=self.controlButtonSize*5, height=self.controlButtonSize*1.2, fontSize=int(self.controlButtonSize*0.75), screen=self.screen, color=(177, 221, 240), textColor=(0, 0, 0), onClickFunction=showPage2D)

    def drawButtons(self, events): # extended method
        # draw buttons to screen
        
        super(Page1DButtons, self).drawButtons(events)

        self.backButton.displayButton(events)
