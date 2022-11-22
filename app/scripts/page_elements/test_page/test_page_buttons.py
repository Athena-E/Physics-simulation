from page_elements.question_page.question_page_buttons import QuestionPageButtons
from __init__ import Button, pg
from page2D import showPage2D

# class to set and initialise buttons fro test page
# inherits from QuestionPageButtons class
class TestPageButtons(QuestionPageButtons):

    def __init__(self, width, height, mainWidth, mainheight, margin, screen, Env):
        # inherits properties from parent class
        super().__init__(width, height, mainWidth, mainheight, margin, screen, Env)


    def setButtons(self): # extended method
        # calculate positions of buttons

        super(TestPageButtons, self).setButtons()

        self.backButtonPos = (self.collisionPos[0]+self.collisionW+self.margin*2, self.collisionPos[1])
        self.submitButtonPos = (self.backButtonPos[0], self.backButtonPos[1]+self.controlButtonSize+self.margin*4)
        self.revealButtonPos = (self.submitButtonPos[0], self.submitButtonPos[1]+self.controlButtonSize+self.margin*2)
        self.nextButtonPos = (self.revealButtonPos[0], self.revealButtonPos[1]+self.controlButtonSize+self.margin*2)
        self.finishButtonPos = (self.nextButtonPos[0], self.nextButtonPos[1]+self.controlButtonSize+self.margin*2)

    def initButtons(self): # override
        # instantiate button objects

        pauseButton = Button(image=pg.image.load("app/img/pause_icon.png").convert_alpha(), width=self.controlButtonSize, height=self.controlButtonSize, pos=self.pausePos, screen=self.screen, onClickFunction=self.Env.pause)
        startButton = Button(image=pg.image.load("app/img/start_icon.png").convert_alpha(), width=self.controlButtonSize, height=self.controlButtonSize, pos=self.startPos, screen=self.screen, onClickFunction=self.Env.start)
        stopButton = Button(image=pg.image.load("app/img/stop_icon.png").convert_alpha(), width=self.controlButtonSize, height=self.controlButtonSize, pos=self.stopPos, screen=self.screen, onClickFunction=self.Env.stop)

        backButton = Button(text="back", pos=self.backButtonPos, width=self.controlButtonSize*5, height=self.controlButtonSize*1.2, fontSize=int(self.controlButtonSize*0.75), screen=self.screen, color=(250, 215, 172), textColor=(0, 0, 0), onClickFunction=showPage2D)
        
        submitButton = Button(text="submit answer", pos=self.submitButtonPos, width=self.controlButtonSize*5, height=self.controlButtonSize*1.2, fontSize=int(self.controlButtonSize*0.75), screen=self.screen, color=(250, 215, 172), textColor=(0, 0, 0), onClickFunction=self.Env.onClickSubmit)
        revealButton = Button(text="reveal answer", pos=self.revealButtonPos, width=self.controlButtonSize*5, height=self.controlButtonSize*1.2, fontSize=int(self.controlButtonSize*0.75), screen=self.screen, color=(250, 215, 172), textColor=(0, 0, 0), onClickFunction=self.Env.onClickReveal)
        nextButton = Button(text="new question", pos=self.nextButtonPos, width=self.controlButtonSize*5, height=self.controlButtonSize*1.2, fontSize=int(self.controlButtonSize*0.75), screen=self.screen, color=(250, 215, 172), textColor=(0, 0, 0), onClickFunction=self.Env.onClickNext)
        finishButton = Button(text="finish", pos=self.finishButtonPos, width=self.controlButtonSize*5, height=self.controlButtonSize*1.2, fontSize=int(self.controlButtonSize*0.75), screen=self.screen, color=(250, 215, 172), textColor=(0, 0, 0), onClickFunction=self.Env.onClickFinish)

        self.buttons = [pauseButton, startButton, stopButton, backButton, submitButton, revealButton, nextButton, finishButton]

    def drawButtons(self, events): # override
        # draw buttons to screen
        
        for button in self.buttons:
            button.displayButton(events)

