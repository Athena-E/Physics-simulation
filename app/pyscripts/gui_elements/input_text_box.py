from gui_elements.__init__ import pg
from gui_elements.textbox import TextBox
from gui_elements.colors import amber, lightGray, blue

# class for input text box to get user input
# inherits from TextBox class
class InputTextBox(TextBox):

    def __init__(self, **kargs):
        # set all input text box properties with keyword arguments or default values
        # inherits properties from parent text box class
        super().__init__(**kargs)

        self.activeColor = kargs.get("activeColor", amber)
        self.maxInputLength = kargs.get("maxInputLength", len(self.text))
        self.maxTextBoxSurface = self.font.render("_"*self.maxInputLength, True, self.textColor)
        self.maxTextWidth = self.maxTextBoxSurface.get_width()
        self.width = kargs.get("width", self.maxTextWidth + self.fontSize/2) # self.maxTextWidth*1.5
        self.height = kargs.get("height", self.fontSize*1.5) 
        self.textBoxRect = pg.Rect(self.x, self.y, self.width, self.height)

        self.returnFunction = kargs.get("returnFunction", None)
        self.parameter = kargs.get("parameter", None)

        self.active = False

        # input text box can be made unresponsive
        self.typable = kargs.get("typable", True)
        self.untypableColor = kargs.get("untypableColor", lightGray)

        # input text box can have a function to be called when right clicked
        self.rightClickFunction = kargs.get("rightClickFunction", None)
        self.rightClicked = False
        self.rightClickColor = kargs.get("rightClickColor", blue)
        self.rightClickParam = kargs.get("rightClickParam", None)

        # flag to indicate whether textbox is for a password to determine formatting of displayed text
        self.isPassword = kargs.get("isPassword", False)
        self.passwordString = ""

        self.isOnBox = False


    def displayText(self):
        # draws text and text box to screen

        self.screen.blit(self.textBoxSurface, (self.x+self.fontSize/4, self.y+self.height/2-self.fontSize/2))
        # changes text box border color depending on status
        if self.active:
            pg.draw.rect(self.screen, self.activeColor, self.textBoxRect, 1, border_radius=5)
        elif self.rightClicked:
            pg.draw.rect(self.screen, self.rightClickColor, self.textBoxRect, 1, border_radius=5)
        elif not self.typable:
            pg.draw.rect(self.screen, self.untypableColor, self.textBoxRect, 1, border_radius=5)
        else:
            pg.draw.rect(self.screen, self.boxColor, self.textBoxRect, 1, border_radius=5)


    def updateInput(self, events):
        # update text box when user enters text

        mousePos = pg.mouse.get_pos()

        for event in events:

            if self.typable:

                if self.textBoxRect.collidepoint(mousePos):
                    self.isOnBox = True
                else:
                    self.isOnBox = False

                if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                    # activates input text box when user left clicks on box
                    if self.textBoxRect.collidepoint(mousePos):
                        self.active = not self.active
                    else:
                        self.active = False
                    
                if event.type == pg.KEYDOWN and self.active:
                    # calls function when return key is pressed
                    if event.key == pg.K_RETURN:
                        self.active = False
                        try:
                            if self.returnFunction is None:
                                pass
                            elif self.parameter is None:
                                self.returnFunction(self.text)
                            else:
                                self.returnFunction(self.parameter, self.text)
                        except:
                            # exception when function is None
                            print("no return function")

                    # removes last letter from input text when backspace pressed
                    elif event.key == pg.K_BACKSPACE:
                        self.text = self.text[:-1]
                        if self.isPassword:
                            self.passwordString = self.passwordString[:-1]

                    # appends entered letter to input text 
                    elif len(self.text) < self.maxInputLength: 
                        self.text += event.unicode
                        # appends asterisk to password string to hide password when displayed
                        if self.isPassword and event.unicode != "":
                            self.passwordString += "*"

            # calls function when right clicked is detected
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 3 and self.rightClickFunction is not None and self.textBoxRect.collidepoint(mousePos):
                if not self.rightClicked:
                    self.active = False
                    self.rightClicked = True
                else:
                    self.rightClicked = False

                # pass parameters into function if applicable
                if self.rightClickParam is not None:
                    self.rightClickFunction(self.rightClickParam)
                else:
                    self.rightClickFunction()

        # renders text to surface
        if self.isPassword:
            self.textBoxSurface = self.font.render(self.passwordString, True, self.textColor)
        else:
            self.textBoxSurface = self.font.render(self.text, True, self.textColor)


    def update(self, value): # override
        # update text displayed in the text box with a new value
        if not self.active:
            self.text = value
            self.textBoxSurface = self.font.render(self.text, True, self.textColor)


    




