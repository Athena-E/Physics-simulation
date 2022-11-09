from gui_elements.__init__ import pg, math
from gui_elements.textbox import TextBox
from gui_elements.input_text_box import InputTextBox
from gui_elements.colors import black, lilac

# class for sliders
class Slider:

    def __init__(self, **kargs):
        # set all slider properties with keyword arguments or default values

        self.x, self.y = kargs.get("pos", (0, 0))
        self.width = kargs.get("width", 0)
        self.height = kargs.get("height", 0)
        self.cx, self.cy = self.x, self.y + self.height//2
        self.lineColor = kargs.get("lineColor", black)
        self.circleColor = kargs.get("circleColor", lilac)
        self.circleRadius = kargs.get("circleRadius", 0)

        self.sliderRect = pg.Rect(self.x, self.y, self.width, self.height)

        self.drag = False

        self.screen = kargs.get("screen", None)

        self.minValue = kargs.get("minValue", 0)
        self.maxValue = kargs.get("maxValue", 100)
        self.value = 0

        # sets properties for slider text box label
        self.sliderText = kargs.get("sliderText", "")
        self.sliderFontSize = kargs.get("sliderFontSize", 0)
        self.sliderTextPos = kargs.get("sliderTextPos", (0, 0))
        self.sliderTextBox = TextBox(text=self.sliderText, pos=self.sliderTextPos, screen=self.screen, fontSize=self.sliderFontSize)

        # sets properties if slider has a text box to display its value
        self.hasInput = kargs.get("hasInput", False)
        if self.hasInput:
            self.defaultText = kargs.get("defaultText", "")
            self.inputTextPos = kargs.get("inputTextPos", (0, 0))
            self.maxInputLength = kargs.get("maxInputLength", len(self.defaultText))
            self.sliderInputBox = InputTextBox(text=self.defaultText, pos=self.inputTextPos, screen=self.screen, fontSize=self.sliderFontSize, maxInputLength=self.maxInputLength)
        
        self.isOnSlider = False

        
    def displaySlider(self):
        # draws slider and text boxes to the screen

        pg.draw.rect(self.screen, self.lineColor, self.sliderRect, 0)
        pg.draw.circle(self.screen, self.circleColor, (self.cx, self.cy), self.circleRadius, 0)
        self.sliderTextBox.displayText()

        if self.hasInput:
            self.sliderInputBox.displayText()
            

    def collideCircle(self, mousePosX, mousePosY, circleX, circleY, radius):
        # returns flag to indicate whether mouse is inside the slider circle

        # calculates distance between mouse and circle centre using Pythagoras
        if math.hypot(mousePosX-circleX, mousePosY-circleY) <= radius:
            return True
        else:
            return False        


    def update(self, events):

        mousePos = pg.mouse.get_pos()
        
        for event in events:

            if self.collideCircle(mousePos[0], mousePos[1], self.cx, self.y, self.circleRadius):
                self.isOnSlider = True
                if event.type == pg.MOUSEBUTTONDOWN:
                    # flag to indicate user is dragging the slider
                    self.drag = True
            else:
                self.isOnSlider = False

            if event.type == pg.MOUSEMOTION:
                # change x position of slider circle when user drags
                if self.drag:
                    mousePos = pg.mouse.get_pos()
                    if mousePos[0] >= self.x and mousePos[0] <= self.x + self.width:
                        self.cx = mousePos[0]
                        self.updateSliderValue()

            if event.type == pg.MOUSEBUTTONUP:
                self.drag = False


        # call methods to update slider values based on text input
        if self.hasInput:
            self.sliderInputBox.updateInput(events)
            self.updateSliderPos()


    def updateSliderValue(self):
        # update displayed text in input box depending on position of slider circle

        posDiff = self.cx - self.x
        if posDiff == self.minValue:
            self.value = self.minValue
        elif posDiff >= self.width - 1:
            self.value = self.maxValue
        else:
            self.value = int(posDiff/self.width * self.maxValue)
        if self.hasInput:
            self.sliderInputBox.text = str(self.value)


    def updateSliderPos(self):
        # update the position of the slider circle depending on input into the text box

        self.value = self.sliderInputBox.text
        try:
            posDiff = int(self.value)/self.maxValue * self.width
        except:
            self.value = self.minValue

        posDiff = int(self.value)/self.maxValue * self.width 
        self.cx = posDiff + self.x

        if self.cx > self.x + self.width:
            self.cx = self.x + self.width
            self.sliderInputBox.text = str(self.maxValue)


    def getValue(self):
        # return slider value
        return self.value




