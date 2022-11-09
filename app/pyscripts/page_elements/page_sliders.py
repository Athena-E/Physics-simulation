from page_elements.page_buttons import PageButtons
from __init__ import Slider

# class to set and initialise sliders
# inherits from PageButtons class
class PageSliders(PageButtons):

    def __init__(self, width, height, mainWidth, mainHeight, margin, screen, Env):
        # inherits properties from parent class
        super().__init__(width, height, mainWidth, mainHeight, margin, screen, Env)

        self.setSliders()
        self.initSliders()


    def setSliders(self):
        # calculate dimensions and positions of sliders

        self.sliderWidth, self.sliderHeight = self.mainWidth/8, self.mainHeight/160
        self.circleRadius = self.sliderHeight*2.5

        self.wallElasticityPos = (self.width/2-self.mainWidth/2+2*self.margin+self.mainWidth*(2/3), self.addPos[1]+self.controlButtonSize)
        self.objectElasticityPos = (self.wallElasticityPos[0], self.wallElasticityPos[1]+self.margin*5)
        
        self.sliderFontSize = int(self.mainHeight/35)
        self.sliderTextPos = (self.wallElasticityPos[0], self.wallElasticityPos[1]-1.5*self.margin-self.sliderFontSize)
        
        self.wallInputTextPos = (self.sliderTextPos[0]+self.margin*9, self.wallElasticityPos[1]-1.5*self.margin-self.sliderFontSize)
        self.objectInputTextPos = (self.wallInputTextPos[0], self.wallInputTextPos[1]+self.margin*5)

    def initSliders(self):
        # instantiate slider objects
        
        self.wallElasticitySlider = Slider(width=self.sliderWidth, height=self.sliderHeight, circleRadius=self.circleRadius, screen=self.screen, 
        pos=self.wallElasticityPos, sliderText="wall elasticity:", sliderTextPos=self.sliderTextPos, sliderFontSize=self.sliderFontSize,
        inputTextPos=self.wallInputTextPos, defaultText="100", hasInput=True, maxInputLength=3)

        self.objectElasticitySlider = Slider(width=self.sliderWidth, height=self.sliderHeight, circleRadius=self.circleRadius, screen=self.screen, 
        pos=self.objectElasticityPos, sliderText="object elasticity:", sliderTextPos=(self.sliderTextPos[0], self.sliderTextPos[1]+self.margin*5), 
        sliderFontSize=self.sliderFontSize, inputTextPos=self.objectInputTextPos, defaultText="100", hasInput=True, maxInputLength=3)

        self.sliders = [self.wallElasticitySlider, self.objectElasticitySlider]

    def drawSliders(self, events):
        # draw sliders to screen and handle slider events
        
        self.wallElasticitySlider.displaySlider()
        self.wallElasticitySlider.update(events)
        wallElasticity = self.wallElasticitySlider.sliderInputBox.text
        self.Env.setWallElasticity(wallElasticity)

        self.objectElasticitySlider.displaySlider()
        self.objectElasticitySlider.update(events)
        objectElasticity = self.objectElasticitySlider.sliderInputBox.text
        self.Env.setParticleElasticity(objectElasticity)