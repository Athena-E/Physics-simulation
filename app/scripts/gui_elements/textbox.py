from gui_elements.__init__ import pg
from gui_elements.colors import black

# class for text box to display text
# parent class for input text box
class TextBox:

    def __init__(self, **kargs):
        # set all text box properties with keyword arguments or default values
        self.x, self.y = kargs.get("pos", (0, 0))
        self.screen = kargs.get("screen", None)

        self.text = kargs.get("text", "")
        self.textColor = kargs.get("textColor", black)
        self.boxColor = kargs.get("boxColor", black)
        self.backColor = kargs.get("backColor", None)
        # default center text alignment
        self.textAlign = kargs.get("textAlign", "center")
        
        self.fontStyle = kargs.get("fontStyle", "Helvetica")
        self.fontSize = kargs.get("fontSize", int(self.screen.get_height()/20))
        self.height = kargs.get("height", self.fontSize)
        self.font = pg.font.SysFont(self.fontStyle, self.fontSize)

        self.textBoxSurface = self.font.render(self.text, True, self.textColor)
        self.textWidth = self.textBoxSurface.get_width()
        self.width = kargs.get("width", self.textWidth)
        self.textBoxRect = pg.Rect(self.x, self.y, self.width, self.height)

        self.isBoxed = kargs.get("isBoxed", False)


    def displayText(self):
        # draws text to screen 

        if self.backColor is not None:
            pg.draw.rect(self.screen, self.backColor, self.textBoxRect) 
        if self.textAlign == "right":
            self.screen.blit(self.textBoxSurface, (self.x, self.y))
        elif self.textAlign == "center":
            self.textWidth = self.textBoxSurface.get_width()
            self.screen.blit(self.textBoxSurface, (self.x+self.width/2-self.textWidth/2, self.y+self.height/2-self.fontSize/2))

        # draws border to screen if applicable
        if self.isBoxed:
            pg.draw.rect(self.screen, self.boxColor, self.textBoxRect, 1, border_radius=5)

    def update(self, value):
        # updates text displayed in text box
        self.text = value
        self.textBoxSurface = self.font.render(self.text, True, self.textColor)

    def getText(self):
        return self.text

