from __init__ import Button
from page2D import showPage2D
from login_page import showLoginPage
from page_elements.register_page.register_page_containers import RegPageContainers
from register_page import showRegisterPage

# class to set and initialise buttons for registration page
# inherits from RegPageContainers class
class RegPageButtons(RegPageContainers):

    def __init__(self, width, height, mainWidth, mainHeight, margin, screen, Env):
        # inherits properties from parent class
        super().__init__(width, height, mainWidth, mainHeight, margin, screen)

        self.Env = Env

        self.setButtons()
        self.initButtons()

    def setButtons(self):
        # calculate dimensions and positions of buttons

        self.buttonWidth, self.buttonHeight = self.mainWidth/6, self.mainHeight/15
        self.buttonFontSize = int(self.buttonHeight*0.8)

        self.loginButtonPos = (self.mainPos[0]+self.buttonWidth/2, self.mainPos[1]+self.mainHeight/6)
        self.registerButtonPos = (self.loginButtonPos[0]+self.buttonWidth+self.margin*3, self.loginButtonPos[1])

        self.createAccountButtonPos = (self.registerButtonPos[0]+self.mainWidth/4, self.loginButtonPos[1]+self.mainHeight*0.55)

        self.backButtonPos = (self.mainPos[0]+self.margin, self.mainPos[1]+self.margin)

    def initButtons(self):
        # instantiate button objects

        loginButton = Button(text="Login", pos=self.loginButtonPos, width=self.buttonWidth, height=self.buttonHeight, fontSize=self.buttonFontSize, screen=self.screen, onClickFunction=showLoginPage)
        registerButton = Button(text="Register", pos=self.registerButtonPos, width=self.buttonWidth, height=self.buttonHeight, fontSize=self.buttonFontSize, screen=self.screen, onClickFunction=showRegisterPage)
        createAccountButton = Button(text="Create account", pos=self.createAccountButtonPos, width=self.buttonWidth*1.4, height=self.buttonHeight, fontSize=self.buttonFontSize, screen=self.screen, onClickFunction=self.Env.onClickCreateAccount)

        backButton = Button(text="Back", pos=self.backButtonPos, width=self.buttonWidth, height=self.buttonHeight, fontSize=self.buttonFontSize, screen=self.screen, onClickFunction=showPage2D, color=(177, 221, 240), textColor=(0, 0, 0))

        self.buttons = [loginButton, registerButton, createAccountButton, backButton]

    def drawButtons(self, events):
        # draw buttons to screen

        for button in self.buttons:
            button.displayButton(events)
