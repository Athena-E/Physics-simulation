from __init__ import Button, TextBox, pg
from page_elements.question_page.question_page_containers import QuestionPageContainers
from page2D import showPage2D

# class to set and initialise buttons fro question page
# inherts from QuestionPageContainers class
class QuestionPageButtons(QuestionPageContainers):

    def __init__(self, width, height, mainWidth, mainheight, margin, screen, Env):
        # inherits properties from parent class
        super().__init__(width, height, mainWidth, mainheight, margin, screen)

        self.Env = Env
        self.setButtons()
        self.initButtons()

    def setButtons(self):
        # calculates dimensions and positions of buttons

        self.controlButtonSize = self.mainHeight/17

        self.pausePos = (self.propertiesPos[0]+self.propertiesW+2*self.margin, self.propertiesPos[1])
        self.startPos = (self.pausePos[0]+self.controlButtonSize+self.margin/2, self.pausePos[1])
        self.stopPos = (self.startPos[0]+self.controlButtonSize+self.margin/2, self.startPos[1])

        self.deletePos = (self.pausePos[0], self.pausePos[1]+self.controlButtonSize+self.margin*2)
        self.addPos = (self.stopPos[0], self.stopPos[1]+self.controlButtonSize+self.margin*2)
        self.countPos = (self.startPos[0], self.startPos[1]+self.controlButtonSize+self.margin*2)

        self.saveButtonPos = (self.collisionPos[0]+self.collisionW+self.margin*2, self.collisionPos[1])
        self.backButtonPos = (self.saveButtonPos[0], self.saveButtonPos[1]+self.controlButtonSize+self.margin*2)

    def initButtons(self):
        # instantiate button objects

        pauseButton = Button(image=pg.image.load("app/img/pause_icon.png").convert_alpha(), width=self.controlButtonSize, height=self.controlButtonSize, pos=self.pausePos, screen=self.screen, onClickFunction=self.Env.pause)
        startButton = Button(image=pg.image.load("app/img/start_icon.png").convert_alpha(), width=self.controlButtonSize, height=self.controlButtonSize, pos=self.startPos, screen=self.screen, onClickFunction=self.Env.start)
        stopButton = Button(image=pg.image.load("app/img/stop_icon.png").convert_alpha(), width=self.controlButtonSize, height=self.controlButtonSize, pos=self.stopPos, screen=self.screen, onClickFunction=self.Env.stop)

        deleteButton = Button(text="-", pos=self.deletePos, width=self.controlButtonSize, height=self.controlButtonSize, fontSize=int(self.controlButtonSize), onClickFunction=self.Env.removeParticle, screen=self.screen, hoverColor=(50,50,50))
        addButton = Button(text="+", pos=self.addPos, width=self.controlButtonSize, height=self.controlButtonSize, fontSize=int(self.controlButtonSize), onClickFunction=self.Env.addParticle, screen=self.screen, hoverColor=(50,50,50))
    
        saveButton = Button(text="save question", pos=self.saveButtonPos, width=self.controlButtonSize*5, height=self.controlButtonSize*1.2, fontSize=int(self.controlButtonSize*0.75), screen=self.screen, color=(250, 215, 172), textColor=(0, 0, 0), onClickFunction=self.Env.onClickSave)
        backButton = Button(text="back", pos=self.backButtonPos, width=self.controlButtonSize*5, height=self.controlButtonSize*1.2, fontSize=int(self.controlButtonSize*0.75), screen=self.screen, color=(250, 215, 172), textColor=(0, 0, 0), onClickFunction=showPage2D)

        self.countBox = TextBox(pos=self.countPos, isBoxed=True, width=self.controlButtonSize, height=self.controlButtonSize, screen=self.screen, fontSize=int(self.controlButtonSize))

        self.buttons = [pauseButton, startButton, stopButton, deleteButton, addButton, saveButton, backButton]

    def drawButtons(self, events):
        # draws buttons to screen

        for button in self.buttons:
            button.displayButton(events)

        self.countBox.displayText()
        self.countBox.update(str(self.Env.getNoOfParticles()))
