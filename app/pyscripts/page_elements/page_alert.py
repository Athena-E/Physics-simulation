from __init__ import pg, TextBox
from page_elements.page_containers import PageContainers

class PageAlert(PageContainers):

    def __init__(self, width, height, mainWidth, mainHeight, margin, screen):

        super().__init__(width, height, mainWidth, mainHeight, margin, screen)
        
        self.setAlertBox()


    def setAlertBox(self):

        self.alertBoxWidth, self.alertBoxHeight = self.width*0.7, self.height*0.25
        self.alertBoxPos = (self.width/2-self.alertBoxWidth/2, 0)

    def drawAlertBox(self):

        pg.draw.rect(self.screen, (0, 0, 0), (self.alertBoxPos[0], self.alertBoxPos[1], self.alertBoxWidth, self.alertBoxHeight), 0)


    