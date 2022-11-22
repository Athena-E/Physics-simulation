from __init__ import pg
from page_elements.page_containers import PageContainers

# class to set and initialise containers for login page
# inherits from PageContainers class
class LoginPageContainers(PageContainers):

    def __init__(self, width, height, mainWidth, mainHeight, margin, screen):
        # inherits properties from parent class
        super().__init__(width, height, mainWidth, mainHeight, margin, screen)

        self.setContainers()

    def setContainers(self): # extended method
        # calculates dimensions and positions of login container box
        super(LoginPageContainers, self).setContainers()

        self.loginBoxW, self.loginBoxH = int(self.mainWidth*0.5), int(self.mainWidth*0.5)
        self.loginBoxPos = (self.width/2-self.loginBoxW/2, self.height/2-self.loginBoxH/2)

    def drawContainers(self): # override
        # draws container rects to screen

        self.screen.fill((255, 255, 255))

        # main container
        pg.draw.rect(self.screen, (0, 0, 0), (self.mainPos[0], self.mainPos[1], self.mainWidth, self.mainHeight), 1)

        pg.draw.rect(self.screen, (0, 0, 0), (self.loginBoxPos[0], self.loginBoxPos[1], self.loginBoxW, self.loginBoxH), 1)


