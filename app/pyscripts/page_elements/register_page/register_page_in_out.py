from page_elements.register_page.register_page_buttons import RegPageButtons
from __init__ import TextBox, InputTextBox, red

# class to set and initialise input output elements for registration page
# inherits from RegPageButtons class
class RegPageInOut(RegPageButtons):

    def __init__(self, width, height, mainWidth, mainHeight, margin, screen, Env):
        # inherits properties from parent class
        super().__init__(width, height, mainWidth, mainHeight, margin, screen, Env)

        self.setInOut()
        self.initInOut()


    def setInOut(self):
        # calculate dimensions and positions of input output elements

        self.labelFontSize = int(self.buttonFontSize*0.75)

        self.firstNameLabelPos = (self.loginButtonPos[0], self.loginButtonPos[1]+self.buttonHeight+self.margin*3)
        self.firstNameInputPos = (self.loginButtonPos[0], self.firstNameLabelPos[1]+self.labelFontSize+self.margin*0.75)

        self.lastNameLabelPos = (self.loginButtonPos[0], self.firstNameInputPos[1]+self.labelFontSize+self.margin*2)
        self.lastNameInputPos = (self.loginButtonPos[0], self.lastNameLabelPos[1]+self.labelFontSize+self.margin*0.75)

        self.codeLabelPos = (self.loginButtonPos[0], self.lastNameInputPos[1]+self.labelFontSize+self.margin*4)
        self.codeInputPos = (self.loginButtonPos[0]+self.mainWidth/4, self.codeLabelPos[1])

        self.usernameLabelPos = (self.loginButtonPos[0], self.codeLabelPos[1]+self.labelFontSize+self.margin*2)
        self.usernameTextPos = (self.usernameLabelPos[0]+self.margin*8, self.usernameLabelPos[1])

        self.emailLabelPos = (self.loginButtonPos[0], self.usernameLabelPos[1]+self.labelFontSize+self.margin*2)
        self.emailInputPos = (self.loginButtonPos[0], self.emailLabelPos[1]+self.labelFontSize+self.margin*0.75)

        self.passwordLabelPos = (self.registerButtonPos[0]+self.mainWidth/4, self.registerButtonPos[1])
        self.passwordInputPos = (self.passwordLabelPos[0], self.passwordLabelPos[1]+self.labelFontSize+self.margin*0.75)

        self.passwordReqLabelPos = (self.passwordLabelPos[0], self.passwordInputPos[1]+self.labelFontSize+self.margin)
        self.minCharLabelPos = (self.passwordLabelPos[0], self.passwordReqLabelPos[1]+self.labelFontSize+self.margin*0.25)
        self.letterCaseLabelPos = (self.passwordLabelPos[0], self.minCharLabelPos[1]+self.labelFontSize+self.margin*0.1)
        self.numLabelPos = (self.passwordLabelPos[0], self.letterCaseLabelPos[1]+self.labelFontSize+self.margin*0.1)
        self.symbolLabelPos = (self.passwordLabelPos[0], self.numLabelPos[1]+self.labelFontSize+self.margin*0.1)

        self.confirmPasswordLabelPos = (self.passwordLabelPos[0], self.symbolLabelPos[1]+self.labelFontSize+self.margin*2)
        self.confirmPasswordInputPos = (self.passwordLabelPos[0], self.confirmPasswordLabelPos[1]+self.labelFontSize+self.margin*0.75)

        self.alertBoxPos = (self.createAccountButtonPos[0], self.createAccountButtonPos[1]+self.buttonHeight+self.margin)


    def initInOut(self):
        # instantiate text box and input text box objects

        firstNameLabel = TextBox(pos=self.firstNameLabelPos, screen=self.screen, text="First name*", fontSize=self.labelFontSize)
        lastNameLabel = TextBox(pos=self.lastNameLabelPos, screen=self.screen, text="Last name*", fontSize=self.labelFontSize)
        codeLabel = TextBox(pos=self.codeLabelPos, screen=self.screen, text="Teacher code (teachers only):", fontSize=int(self.labelFontSize*0.9))
        usernameLabel = TextBox(pos=self.usernameLabelPos, screen=self.screen, text="Username:", fontSize=int(self.labelFontSize*0.9))
        emailLabel = TextBox(pos=self.emailLabelPos, screen=self.screen, text="Email*", fontSize=self.labelFontSize)
        passwordLabel = TextBox(pos=self.passwordLabelPos, screen=self.screen, text="Password*", fontSize=self.labelFontSize)
        confirmPasswordLabel = TextBox(pos=self.confirmPasswordLabelPos, screen=self.screen, text="Confirm password*", fontSize=self.labelFontSize)

        passwordReqLabel = TextBox(pos=self.passwordReqLabelPos, screen=self.screen, text="Password must contain at least:", fontSize=int(self.labelFontSize*0.9))
        minCharLabel = TextBox(pos=self.minCharLabelPos, screen=self.screen, text="- 6 characters", fontSize=int(self.labelFontSize*0.9))
        letterCaseLabel = TextBox(pos=self.letterCaseLabelPos, screen=self.screen, text="- 1 uppercase and lowercase", fontSize=int(self.labelFontSize*0.9))
        numLabel = TextBox(pos=self.numLabelPos, screen=self.screen, text="- 1 number", fontSize=int(self.labelFontSize*0.9))
        symbolLabel = TextBox(pos=self.symbolLabelPos, screen=self.screen, text="- 1 symbol", fontSize=int(self.labelFontSize*0.9))

        self.firstNameInputBox = InputTextBox(pos=self.firstNameInputPos, screen=self.screen, fontSize=self.labelFontSize, maxInputLength=30)
        self.lastNameInputBox = InputTextBox(pos=self.lastNameInputPos, screen=self.screen, fontSize=self.labelFontSize, maxInputLength=30)
        self.codeInputBox = InputTextBox(pos=self.codeInputPos, screen=self.screen, fontSize=self.labelFontSize, maxInputLength=8)
        self.usernameText = TextBox(pos=self.usernameTextPos, screen=self.screen, text="()", fontSize=int(self.labelFontSize*0.9), textAlign="right")
        self.emailInputBox = InputTextBox(pos=self.emailInputPos, screen=self.screen, fontSize=self.labelFontSize, maxInputLength=30)
        self.passwordInputBox = InputTextBox(pos=self.passwordInputPos, screen=self.screen, fontSize=self.labelFontSize, maxInputLength=30, isPassword=True)
        self.confirmPasswordInputBox = InputTextBox(pos=self.confirmPasswordInputPos, screen=self.screen, fontSize=self.labelFontSize, maxInputLength=30, isPassword=True)
        self.alertBox = TextBox(pos=self.alertBoxPos, screen=self.screen, text="hello", fontSize=self.labelFontSize, textAlign="right", textColor=red)

        self.labels = [firstNameLabel, lastNameLabel, codeLabel, usernameLabel, emailLabel, passwordLabel, passwordReqLabel, minCharLabel, 
        letterCaseLabel, numLabel, symbolLabel, confirmPasswordLabel]


    def drawInOut(self, events):
        # draw input output elements to screen and handle updates to text boxes

        for label in self.labels:
            label.displayText()

        self.firstNameInputBox.displayText()
        self.firstNameInputBox.updateInput(events)

        self.lastNameInputBox.displayText()
        self.lastNameInputBox.updateInput(events)

        self.codeInputBox.displayText()
        self.codeInputBox.updateInput(events)

        self.usernameText.displayText()

        self.emailInputBox.displayText()
        self.emailInputBox.updateInput(events)

        self.passwordInputBox.displayText()
        self.passwordInputBox.updateInput(events)

        self.confirmPasswordInputBox.displayText()
        self.confirmPasswordInputBox.updateInput(events)

        self.alertBox.displayText()
        self.alertBox.update(self.Env.getErrorAlert())
        
    
        
