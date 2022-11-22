from __init__ import pg
from page_elements.page_containers import PageContainers

# class to set and initialise container rectangles for question page
# inherits from PageContainers class
class QuestionPageContainers(PageContainers):

    def __init__(self, width, height, mainWidth, mainHeight, margin, screen):
         # inherits properties from parent class
        super().__init__(width, height, mainWidth, mainHeight, margin, screen)

        self.setContainers()
    
    def setContainers(self): # extended method
        # calculate dimensions for properties container

        super(QuestionPageContainers, self).setContainers()

        self.propertiesW, self.propertiesH = self.collisionW, self.mainHeight-3*self.margin-self.collisionH*1.1


