from page_elements.gas_page.gas_page_containers import GasPageContainers
from __init__ import Slider, TextBox, GASENV_MAX_PARTICLES

# class to set and initialise sliders for gas page
# inherits from GasPageContainers class
class GasPageSliders(GasPageContainers):

    def __init__(self, width, height, mainWidth, mainHeight, margin, screen, Env):
        # inherits properties from parent class
        super().__init__(width, height, mainWidth, mainHeight, margin, screen)

        self.Env = Env

        self.setSliders()
        self.initSliders()

        self.setSliderLabels()
        self.initSliderLabels()


    def setSliders(self):
        # calculates dimensions and positions of sliders

        self.sliderWidth, self.sliderHeight = self.propertiesW*0.6, self.mainHeight/120
        self.circleRadius = self.sliderHeight*2.5

        self.tempPos = (self.propertiesPos[0]+self.propertiesW*0.25, self.propertiesPos[1]+self.margin*3)
        self.elasticityPos = (self.tempPos[0], self.tempPos[1]+self.circleRadius+self.margin*2)
        self.noOfParticlesPos = (self.tempPos[0], self.elasticityPos[1]+self.circleRadius+self.margin*2)
        self.sizePos = (self.tempPos[0], self.noOfParticlesPos[1]+self.circleRadius+self.margin*2)

        self.sliderFontSize = int(self.mainHeight/35)
        self.sizeLabelPos = (self.sizePos[0]-self.margin*4, self.sizePos[1])

    def setSliderLabels(self):
        # calculate dimensions and positions of slider labels

        self.sliderFontSize = int(self.mainHeight/35)
        self.tempLabelPos = (self.tempPos[0]-self.margin*10, self.tempPos[1]-self.sliderFontSize/2)
        self.elasticityLabelPos = (self.elasticityPos[0]-self.margin*8, self.elasticityPos[1]-self.sliderFontSize/2)
        self.noOfParticlesLabelPos = (self.noOfParticlesPos[0]-self.margin*8, self.noOfParticlesPos[1]-self.sliderFontSize/2)
        self.sizeLabelPos = (self.sizePos[0]-self.margin*5.5, self.sizePos[1]-self.sliderFontSize/2)

    def initSliderLabels(self):
        # instantiate text box objects

        tempLabel = TextBox(pos=self.tempLabelPos, screen=self.screen, text="Temperature", fontSize=self.sliderFontSize)
        elasticityLabel = TextBox(pos=self.elasticityLabelPos, screen=self.screen, text="Elasticity", fontSize=self.sliderFontSize)
        noOfParticlesLabel = TextBox(pos=self.noOfParticlesLabelPos, screen=self.screen, text="Particles", fontSize=self.sliderFontSize)
        sizeLabel = TextBox(pos=self.sizeLabelPos, screen=self.screen, text="Size", fontSize=self.sliderFontSize)

        self.sliderLabels = [tempLabel, elasticityLabel, noOfParticlesLabel, sizeLabel]

    def initSliders(self):
        # instantiate slider objects

        self.tempSlider = Slider(width=self.sliderWidth, height=self.sliderHeight, circleRadius=self.circleRadius, screen=self.screen,
        pos=self.tempPos)

        self.elasticitySlider = Slider(width=self.sliderWidth, height=self.sliderHeight, circleRadius=self.circleRadius, screen=self.screen,
        pos=self.elasticityPos)

        self.noOfParticlesSlider = Slider(width=self.sliderWidth, height=self.sliderHeight, circleRadius=self.circleRadius, screen=self.screen,
        pos=self.noOfParticlesPos)

        self.sizeSlider = Slider(width=self.sliderWidth, height=self.sliderHeight, circleRadius=self.circleRadius, screen=self.screen,
        pos=self.sizePos)

    def drawSlidersAndLabels(self, events):
        # draw sliders and labels to screen
        
        self.tempSlider.displaySlider()
        self.tempSlider.update(events)
        tempValue = float(self.tempSlider.getValue()/100)
        self.Env.setTemperatureV(tempValue)

        self.elasticitySlider.displaySlider()
        self.elasticitySlider.update(events)
        elasticity = float(self.elasticitySlider.getValue() / 100)
        self.Env.setElasticity(elasticity)

        self.noOfParticlesSlider.displaySlider()
        self.noOfParticlesSlider.update(events)
        noOfParticles = int(self.noOfParticlesSlider.getValue() / 100 * GASENV_MAX_PARTICLES)
        if noOfParticles > self.Env.getNoOfParticles():
            self.Env.addParticle()
        elif noOfParticles < self.Env.getNoOfParticles():
            self.Env.removeParticle()

        self.sizeSlider.displaySlider()
        self.sizeSlider.update(events)
        newSize = float(self.sizeSlider.getValue() / 100)
        self.Env.setSize(newSize)


        for label in self.sliderLabels:
            label.displayText()

