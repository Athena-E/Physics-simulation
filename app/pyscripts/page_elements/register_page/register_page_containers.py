from __init__ import pg
from page_elements.page_containers import PageContainers

# class to set and initialise page containers for registration page
# inherits from PageContainers class
class RegPageContainers(PageContainers):

    def __init__(self, width, height, mainWidth, mainHeight, margin, screen):
        # inherits properties from parent class
        super().__init__(width, height, mainWidth, mainHeight, margin, screen)


    def drawContainers(self):
        # draws container rects to the screen

        self.screen.fill((255, 255, 255))

        # main container
        pg.draw.rect(self.screen, (0, 0, 0), (self.mainPos[0], self.mainPos[1], self.mainWidth, self.mainHeight), 1)


