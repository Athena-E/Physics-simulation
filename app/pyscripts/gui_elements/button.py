from gui_elements.__init__ import pg
from gui_elements.colors import black, white

# class for single-click button
# parent class of toggle button
class Button():
    def __init__(self, **kargs):
        # set all button properties with keyword arguments or default values
        self.x, self.y = kargs.get("pos", (0, 0))
        self.width = kargs.get("width", 0)
        self.height = kargs.get("height", 0)
        
        self.color = kargs.get("color", black)
        self.textColor = kargs.get("textColor", white)
        self.hoverColor = kargs.get("hoverColor", None)

        self.onClickFunction = kargs.get("onClickFunction", None)
        self.parameter = kargs.get("parameter", None)

        self.text = kargs.get("text", "")
        self.fontStyle = kargs.get("fontStyle", "Helvetica")
        self.fontSize = kargs.get("fontSize", 10)
        self.font = pg.font.SysFont(self.fontStyle, self.fontSize)

        self.image = kargs.get("image", None)

        self.screen = kargs.get("screen", None)

        self.isOnButton = False

        # scales image onto button if image is used
        if self.image:
            self.image = pg.transform.scale(self.image, (self.width, self.height))
            self.buttonRect = self.image.get_rect()
            self.buttonRect.topleft = (self.x, self.y)
        # initialises surface for button Rect object and button text
        else:
            self.buttonSurface = pg.Surface((self.width, self.height))
            self.buttonRect = pg.Rect(self.x, self.y, self.width, self.height)
            self.buttonText = self.font.render(self.text, True, self.textColor)


    def displayButton(self, events):
        # draw button to the screen and handle button events
        
        mousePos = pg.mouse.get_pos()

        if not self.image:
            self.buttonSurface.fill(self.color)

        # detects if mouse is within the button region
        if self.buttonRect.collidepoint(mousePos):
            
            self.isOnButton = True
            # changes button color when hovered over
            if not self.image and self.hoverColor is not None:
                self.buttonSurface.fill(self.hoverColor)

            for event in events:
                # calls function when button is clicked
                if event.type == pg.MOUSEBUTTONDOWN:
                    try:
                        if self.parameter is None:
                            self.onClickFunction()
                        else:
                            self.onClickFunction(self.parameter)
                    except TypeError:
                        # exception when no function has been passed as an argument
                        print("no button function")

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

