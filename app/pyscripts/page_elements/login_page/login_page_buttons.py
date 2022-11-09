from page_elements.login_page.login_page_containers import LoginPageContainers
from __init__ import Button, emeraldGreen, black, lightBlue, darkGray
from page2D import showPage2D
from login_page import showLoginPage
from register_page import showRegisterPage
import config

# class to set and initialise buttons for login page
# inherits from LoginPageContainers class
class LoginPageButtons(LoginPageContainers):

    def __init__(self, width, height, mainWidth, mainHeight, margin, screen, Env):
        # inherits properties from parent class
        super().__init__(width, height, mainWidth, mainHeight, margin, screen)

        self.Env = Env
        self.setButtons()
        self.initButtons()

    def setButtons(self):
        # calculates button dimensions and positions

        self.bigButtonWidth, self.bigButtonHeight = self.loginBoxW/3, self.loginBoxH/11
        self.bigButtonFontSize = int(self.bigButtonHeight*0.8)

        self.loginButtonPos = (self.width/2 - self.bigButtonWidth - self.margin*3, self.loginBoxPos[1]+self.loginBoxW/12)

        self.registerButtonPos = (self.loginButtonPos[0]+self.bigButtonWidth+self.margin*6, self.loginButtonPos[1])

        self.smallButtonWidth, self.smallButtonHeight = self.loginBoxW/5, self.loginBoxH/13
        self.smallButtonFontSize = int(self.smallButtonHeight*0.8)

        self.studentButtonPos = (self.loginButtonPos[0], self.loginButtonPos[1]+self.bigButtonHeight+self.loginBoxW/10)
        self.teacherButtonPos = (self.studentButtonPos[0]+self.smallButtonWidth+self.margin*2, self.studentButtonPos[1])

        self.goButtonPos = (self.studentButtonPos[0], self.teacherButtonPos[1]+self.loginBoxH*0.5)

        self.backButtonPos = (self.mainPos[0]+self.margin, self.mainPos[1]+self.margin)

    def initButtons(self):
        # instantiates button objects

        loginButton = Button(text="Login", pos=self.loginButtonPos, width=self.bigButtonWidth, height=self.bigButtonHeight, fontSize=self.bigButtonFontSize, screen=self.screen, onClickFunction=showLoginPage, hoverColor=darkGray)
        registerButton = Button(text="Register", pos=self.registerButtonPos, width=self.bigButtonWidth, height=self.bigButtonHeight, fontSize=self.bigButtonFontSize, screen=self.screen, onClickFunction=showRegisterPage, hoverColor=darkGray)
        goButton = Button(text="Go", pos=self.goButtonPos, width=self.smallButtonWidth, height=self.smallButtonHeight, fontSize=self.smallButtonFontSize, screen=self.screen, onClickFunction=self.Env.onClickGo, hoverColor=darkGray)
        backButton = Button(text="Back", pos=self.backButtonPos, width=self.bigButtonWidth, height=self.bigButtonHeight, fontSize=self.bigButtonFontSize, screen=self.screen, onClickFunction=showPage2D, color=lightBlue, textColor=black)

        self.studentButton = Button(text="Student", pos=self.studentButtonPos, width=self.smallButtonWidth, height=self.smallButtonHeight, fontSize=self.smallButtonFontSize, screen=self.screen, onClickFunction=self.Env.onClickStudent, hoverColor=emeraldGreen)
        self.teacherButton = Button(text="Teacher", pos=self.teacherButtonPos, width=self.smallButtonWidth, height=self.smallButtonHeight, fontSize=self.smallButtonFontSize, screen=self.screen, onClickFunction=self.Env.onClickTeacher, hoverColor=emeraldGreen)

        self.buttons = [loginButton, registerButton, goButton, backButton, self.studentButton, self.teacherButton]

    def drawButtons(self, events):
        # draws buttons to screen

        # changes color of student and teacher based on user type
        if self.Env.isStudent:
            self.studentButton.color = emeraldGreen
            self.teacherButton.color = black
        if self.Env.isTeacher:
            self.teacherButton.color = emeraldGreen
            self.studentButton.color = black

        for button in self.buttons:
            button.displayButton(events)




