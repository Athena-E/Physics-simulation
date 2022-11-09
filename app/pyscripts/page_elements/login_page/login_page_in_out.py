from page_elements.login_page.login_page_buttons import LoginPageButtons
from __init__ import TextBox, InputTextBox, red

# class to set and initialise input output elements from login page
# inherits from LoginPageButtons
class LoginPageInOut(LoginPageButtons):

    def __init__(self, width, height, mainWidth, mainHeight, margin, screen, Env):
        # inherits properties from parent class
        super().__init__(width, height, mainWidth, mainHeight, margin, screen, Env)

        self.setInOut()
        self.initInOut()

    def setInOut(self):
        # calculate dimensions and positions of input output elements

        self.labelFontSize = int(self.smallButtonFontSize*0.75)
        self.userTypeLabelPos = (self.studentButtonPos[0], self.studentButtonPos[1]-self.labelFontSize-self.margin*0.75)

        self.usernameLabelPos = (self.studentButtonPos[0], self.studentButtonPos[1]+self.margin*2+self.bigButtonHeight)
        self.usernameInputBoxPos = (self.studentButtonPos[0], self.usernameLabelPos[1]+self.labelFontSize+self.margin*0.75)

        self.passwordLabelPos = (self.studentButtonPos[0], self.usernameInputBoxPos[1]+self.labelFontSize+self.margin*2)
        self.passwordInputBoxPos = (self.studentButtonPos[0], self.passwordLabelPos[1]+self.labelFontSize+self.margin*0.75)

        self.alertBoxPos = (self.studentButtonPos[0], self.goButtonPos[1]+self.bigButtonHeight+self.margin)

    def initInOut(self):
        # instantialise text box and input text box objects

        userTypeLabel = TextBox(pos=self.userTypeLabelPos, screen=self.screen, text="I am a:", fontSize=self.labelFontSize)
        usernameLabel = TextBox(pos=self.usernameLabelPos, screen=self.screen, text="Username", fontSize=self.labelFontSize)

        self.usernameInputBox = InputTextBox(pos=self.usernameInputBoxPos, screen=self.screen, fontSize=self.labelFontSize, maxInputLength=30)

        passwordLabel = TextBox(pos=self.passwordLabelPos, screen=self.screen, text="Password", fontSize=self.labelFontSize)

        self.passwordInputBox = InputTextBox(pos=self.passwordInputBoxPos, screen=self.screen, fontSize=self.labelFontSize, maxInputLength=30, isPassword=True)

        self.alertBox = TextBox(pos=self.alertBoxPos, screen=self.screen, fontSize=self.labelFontSize, textAlign="right", textColor=red)

        self.labels = [userTypeLabel, usernameLabel, passwordLabel]

    def drawInOut(self, events):
        # draws input output elements to screen

        for label in self.labels:
            label.displayText()

        self.usernameInputBox.displayText()
        self.usernameInputBox.updateInput(events)

        self.passwordInputBox.displayText()
        self.passwordInputBox.updateInput(events)

        self.alertBox.displayText()
        self.alertBox.update(self.Env.getErrorAlert())


