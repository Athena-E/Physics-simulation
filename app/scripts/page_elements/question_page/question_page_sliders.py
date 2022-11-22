from page_elements.page_sliders import PageSliders

# class to set and initialise sliders for question page
# inherits from PageSliders class
class QuestionPageSliders(PageSliders):

    def __init__(self, width, height, mainWidth, mainHeight, margin, screen, Env):
        # inherits properties from parent class
        super().__init__(width, height, mainWidth, mainHeight, margin, screen, Env)

        self.setSliders()
        self.initSliders()

    def setSliders(self): # extended method
        # calculate positions of sliders

        super(QuestionPageSliders, self).setSliders()

        self.wallElasticityPos = (self.collisionPos[0]+self.collisionW+self.margin*2, self.collisionPos[1]+self.collisionH/2)
        self.objectElasticityPos = (self.wallElasticityPos[0], self.wallElasticityPos[1]+self.margin*5)
        
        self.sliderFontSize = int(self.mainHeight/35)
        self.sliderTextPos = (self.wallElasticityPos[0], self.wallElasticityPos[1]-1.5*self.margin-self.sliderFontSize)
        
        self.wallInputTextPos = (self.sliderTextPos[0]+self.margin*9, self.wallElasticityPos[1]-1.5*self.margin-self.sliderFontSize)
        self.objectInputTextPos = (self.wallInputTextPos[0], self.wallInputTextPos[1]+self.margin*5)