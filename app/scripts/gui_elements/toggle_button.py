from gui_elements.__init__ import pg
from gui_elements.button import Button

# class for toggle button
# inherits from Button class
class ToggleButton(Button):
    def __init__(self, **kargs):
        # inherit properties from parent class
        super().__init__(**kargs)

        # accepts two functions to toggle between
        self.offClickFunction = kargs.get("offClickFunction", None)

        # flag to toggle functions
        self.clicked = False

        self.onClickColor = kargs.get("onClickColor", self.color)


    def displayButton(self, events): # override
        mousePos = pg.mouse.get_pos()

        if not self.image:
            # changes button color when clicked
            if self.clicked:
                self.buttonSurface.fill(self.onClickColor)
            else:
                self.buttonSurface.fill(self.color)


        if self.buttonRect.collidepoint(mousePos):

            self.isOnButton = True

            # changes button color when hovered over
            if not self.image and self.hoverColor is not None:
                self.buttonSurface.fill(self.hoverColor)
                
            for event in events:
                # detects when button has been clicked
                if event.type == pg.MOUSEBUTTONDOWN:
                    # calls functions when clicked
                    if not self.clicked:
                        try:
                            self.onClickFunction()
                            self.clicked = True
                        except TypeError:
                            # exception when no function is passed
                            print("No on click function")
                    else:
                        try:
                            self.offClickFunction()
                            self.clicked = False
                        except TypeError:
                            # exception when no function is passed
                            print("No off click function")

        else:
            self.isOnButton = False

        # draws button to screen
        if self.image:
            self.screen.blit(self.image, (self.buttonRect.x, self.buttonRect.y))
        else:
            self.buttonSurface.blit(self.buttonText, [
            self.buttonRect.width/2 - self.buttonText.get_rect().width/2,
            self.buttonRect.height/2 - self.buttonText.get_rect().height/2
            ])

            self.screen.blit(self.buttonSurface, self.buttonRect)