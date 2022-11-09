from __init__ import pg

# class to set and initialise rectangle containers
# base class of containers for each page
class PageContainers():

    def __init__(self, width, height, mainWidth, mainHeight, margin, screen):
        # constructor to set base properties

        self.width, self.height = width, height
        self.mainWidth, self.mainHeight = mainWidth, mainHeight
        self.margin = margin
        self.screen = screen

        self.setContainers()

    def setContainers(self):
        # calculate positions of containers

        self.mainPos = (int(self.width/2-self.mainWidth/2), int(self.height/2-self.mainHeight/2))
        
        self.collisionPos = (int(self.mainPos[0]+self.margin), int(self.mainPos[1]+self.margin))
        self.collisionW, self.collisionH = int(self.mainWidth*(2/3)), int(self.mainHeight*(2/3))

        self.propertiesPos = (self.collisionPos[0], self.collisionPos[1]+self.margin+self.collisionH)
        self.propertiesW, self.propertiesH = self.mainWidth/2+self.margin, self.mainHeight-3*self.margin-self.collisionH

    def drawContainers(self):
        # draws containers to screens
        
        self.screen.fill((255, 255, 255))

        # main container
        pg.draw.rect(self.screen, (0, 0, 0), (self.mainPos[0], self.mainPos[1], self.mainWidth, self.mainHeight), 1)
        # collision container
        pg.draw.rect(self.screen, (0, 0, 0), (self.collisionPos[0], self.collisionPos[1], self.collisionW, self.collisionH), 1)
        # properties container
        pg.draw.rect(self.screen, (0, 0, 0), (self.propertiesPos[0], self.propertiesPos[1], self.propertiesW, self.propertiesH), 1)


