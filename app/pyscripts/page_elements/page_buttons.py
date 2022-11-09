from page_elements.page_containers import PageContainers
from __init__ import Button, TextBox, ToggleButton, pg, emeraldGreen, darkGray, peach, black, darkPeach
from graphs.speed_graph import showSpeedGraph
from graphs.momentum_graph import showMomentumGraph

# class to set and initialise buttons
# base class of buttons for each page
# inherits from PageContainers class
class PageButtons(PageContainers):

    def __init__(self, width, height, mainWidth, mainHeight, margin, screen, Env):
        # inherits properties from parent class
        super().__init__(width, height, mainWidth, mainHeight, margin, screen)

        self.Env = Env
        self.setButtons()
        self.initButtons()

    def setButtons(self):
        # calculate dimensions and positions of buttons
        
        self.controlButtonSize = self.mainHeight/17

        self.pausePos = (self.propertiesPos[0]+self.propertiesW+2*self.margin, self.propertiesPos[1])
        self.startPos = (self.pausePos[0]+self.controlButtonSize+self.margin/2, self.pausePos[1])
        self.stopPos = (self.startPos[0]+self.controlButtonSize+self.margin/2, self.startPos[1])

        self.deletePos = (self.pausePos[0], self.pausePos[1]+self.controlButtonSize+self.margin*2)
        self.addPos = (self.stopPos[0], self.stopPos[1]+self.controlButtonSize+self.margin*2)
        self.countPos = (self.startPos[0], self.startPos[1]+self.controlButtonSize+self.margin*2)

        self.showSpeedGraphPos = (self.collisionPos[0]+self.collisionW+self.margin*2, self.collisionPos[1])
        self.showMomentumGraphPos = (self.showSpeedGraphPos[0], self.showSpeedGraphPos[1]+self.controlButtonSize+self.margin*2)

        self.COMButtonPos = (self.pausePos[0], self.deletePos[1]+self.controlButtonSize+self.margin*2)

    def initButtons(self):
        # instatiate button objects
        
        pauseButton = Button(image=pg.image.load("app/img/pause_icon.png").convert_alpha(), width=self.controlButtonSize, height=self.controlButtonSize, pos=self.pausePos, screen=self.screen, onClickFunction=self.Env.pause)
        startButton = Button(image=pg.image.load("app/img/start_icon.png").convert_alpha(), width=self.controlButtonSize, height=self.controlButtonSize, pos=self.startPos, screen=self.screen, onClickFunction=self.Env.start)
        stopButton = Button(image=pg.image.load("app/img/stop_icon.png").convert_alpha(), width=self.controlButtonSize, height=self.controlButtonSize, pos=self.stopPos, screen=self.screen, onClickFunction=self.Env.stop)

        deleteButton = Button(text="-", pos=self.deletePos, width=self.controlButtonSize, height=self.controlButtonSize, fontSize=int(self.controlButtonSize), onClickFunction=self.Env.removeParticle, screen=self.screen, hoverColor=darkGray)
        addButton = Button(text="+", pos=self.addPos, width=self.controlButtonSize, height=self.controlButtonSize, fontSize=int(self.controlButtonSize), onClickFunction=self.Env.addParticle, screen=self.screen, hoverColor=darkGray)
        
        speedGraphButton = Button(text="speed graph", pos=self.showSpeedGraphPos, width=self.controlButtonSize*5, height=self.controlButtonSize*1.2, fontSize=int(self.controlButtonSize*0.75), onClickFunction=showSpeedGraph, screen=self.screen, color=peach, textColor=black, parameter=self.Env._maxParticles, hoverColor=darkPeach)
        momentumGraphButton = Button(text="momentum graph", pos=self.showMomentumGraphPos, width=self.controlButtonSize*5, height=self.controlButtonSize*1.2, fontSize=int(self.controlButtonSize*0.75), onClickFunction=showMomentumGraph, screen=self.screen, color=peach, textColor=black, parameter=self.Env._maxParticles, hoverColor=darkPeach)

        COMButton = ToggleButton(text="Centre of mass", pos=self.COMButtonPos, width=self.controlButtonSize*3+self.margin, height=self.controlButtonSize, fontSize=int(self.controlButtonSize*0.5), screen=self.screen, onClickFunction=self.Env.showHideCOM, offClickFunction=self.Env.showHideCOM, onClickColor=emeraldGreen)

        self.countBox = TextBox(pos=self.countPos, isBoxed=True, width=self.controlButtonSize, height=self.controlButtonSize, screen=self.screen, fontSize=int(self.controlButtonSize))

        self.buttons = [pauseButton, startButton, stopButton, deleteButton, addButton, speedGraphButton, momentumGraphButton, COMButton]

    def drawButtons(self, events):
        # draws buttons to screen

        for button in self.buttons:
            button.displayButton(events)

        self.countBox.displayText()
        self.countBox.update(str(self.Env.getNoOfParticles()))



        






