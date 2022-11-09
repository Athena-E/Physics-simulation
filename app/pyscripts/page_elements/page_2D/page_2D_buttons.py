from page_elements.page_buttons import PageButtons
from __init__ import pg, Button, peach, darkPeach
from page1D import showPage1D
from gas_page import showGasPage
from question_page import showQuestionPage
from login_page import showLoginPage
from test_page import showTestPage
from manage_users.login.login_functions import showQuestionPageLoggedIn, logOut
import config

# class to set and initialise buttons for 2D Page
# inherits from PageButtons class
class Page2DButtons(PageButtons):

    def __init__(self, width, height, mainWidth, mainHeight, margin, screen, Env):
        # inherits properties from parent class
        super().__init__(width, height, mainWidth, mainHeight, margin, screen, Env)

        self.setButtons()
        self.initButtons()

    def setButtons(self): # extended method
        # calculate positions of buttons

        super(Page2DButtons, self).setButtons()

        self.page1DButtonPos = (self.showMomentumGraphPos[0], self.showMomentumGraphPos[1]+self.controlButtonSize+self.margin*4)
        self.gasPageButtonPos = (self.page1DButtonPos[0], self.page1DButtonPos[1]+self.controlButtonSize+self.margin*2)
        self.questionPageButtonPos = (self.gasPageButtonPos[0], self.gasPageButtonPos[1]+self.controlButtonSize+self.margin*4)
        self.testPageButtonPos = (self.questionPageButtonPos[0], self.questionPageButtonPos[1]+self.controlButtonSize+self.margin*2)

        self.loginButtonPos = (self.mainPos[0]+self.mainWidth-self.controlButtonSize*4, self.propertiesPos[1])


    def initButtons(self): # extended method
        # instantiate button objects

        super(Page2DButtons, self).initButtons()

        self.page1DButton = Button(text="1D collisions", pos=self.page1DButtonPos, width=self.controlButtonSize*5, height=self.controlButtonSize*1.2, fontSize=int(self.controlButtonSize*0.75), screen=self.screen, color=peach, textColor=(0, 0, 0), onClickFunction=showPage1D, hoverColor=darkPeach)
        self.gasPageButton = Button(text="gas collisions", pos=self.gasPageButtonPos, width=self.controlButtonSize*5, height=self.controlButtonSize*1.2, fontSize=int(self.controlButtonSize*0.75), screen=self.screen, color=peach, textColor=(0, 0, 0), onClickFunction=showGasPage, hoverColor=darkPeach)
        
        self.questionPageButton = Button(text="question creator", pos=self.questionPageButtonPos, width=self.controlButtonSize*5, height=self.controlButtonSize*1.2, fontSize=int(self.controlButtonSize*0.75), screen=self.screen, color=peach, textColor=(0, 0, 0), onClickFunction=showQuestionPageLoggedIn, hoverColor=darkPeach)
        self.testPageButton = Button(text="test mode", pos=self.testPageButtonPos, width=self.controlButtonSize*5, height=self.controlButtonSize*1.2, fontSize=int(self.controlButtonSize*0.75), screen=self.screen, color=(250, 215, 172), textColor=(0, 0, 0), onClickFunction=showTestPage, hoverColor=darkPeach)

        self.loginButton = Button(text="Log in", pos=self.loginButtonPos, width=self.controlButtonSize*3, height=self.controlButtonSize*1.2, fontSize=int(self.controlButtonSize*0.75), screen=self.screen, color=peach, textColor=(0, 0, 0), onClickFunction=showLoginPage, hoverColor=darkPeach)
        self.logoutButton = Button(text="Log out", pos=self.loginButtonPos, width=self.controlButtonSize*3, height=self.controlButtonSize*1.2, fontSize=int(self.controlButtonSize*0.75), screen=self.screen, color=peach, textColor=(0, 0, 0), onClickFunction=logOut, hoverColor=darkPeach)

        self.buttons.extend([self.page1DButton, self.gasPageButton])


    def drawButtons(self, events): # extended method
        # draw buttons to screen

        super(Page2DButtons, self).drawButtons(events)
        
        # display 'log in' button only if user is logged in
        if not config.isLoggedIn and self.loginButton not in self.buttons:
            #self.loginButton.displayButton(events)
            self.buttons.append(self.loginButton)
            self.buttons = [button for button in self.buttons if button is not self.logoutButton]
        elif config.isLoggedIn and self.logoutButton not in self.buttons:
            #self.logoutButton.displayButton(events)
            self.buttons.append(self.logoutButton)
            self.buttons = [button for button in self.buttons if button is not self.loginButton]

        # 'test page' button displayed if user is logged in as teacher/student
        if (config.isStudent or config.isTeacher) and self.testPageButton not in self.buttons:
            #self.testPageButton.displayButton(events)
            self.buttons.append(self.testPageButton)

        # display 'question page' button if user logged in is a teacher
        if config.isTeacher and self.questionPageButton not in self.buttons:
            #self.questionPageButton.displayButton(events)
            self.buttons.append(self.questionPageButton)

 
                





