from State.state import State
from Components.button import Button
import pygame
import csv
# Nowe elementy:
class Editor(State):
    def __init__(self,game):
        super().__init__(game)
        self.TILESIZE = 32
        self.LOWERMARGIN = 100
        self.SIDEMARGIN = 200
        self.COLS = 30
        self.ROWS = (self.game.DISPLAY_WIDTH - self.SIDEMARGIN) // self.TILESIZE
        self.scrollLeft = False
        self.scrollRight = False
        self.leftShift = False
        self.scroll = 0
        self.scrollSpeed = 1
        self.keyBackspace = False
        self.cloudImage = pygame.image.load('./Sprites/Background/sky_cloud.png').convert_alpha()
        self.skyImage = pygame.image.load('./Sprites/Background/sky.png').convert_alpha()
        #self.skyRect = self.skyImage.get_rect()
        self.mountainImage = pygame.image.load('./Sprites/Background/mountain2.png').convert_alpha()
        #self.mountainRect = self.mountainImage.get_rect()
        self.pineForestImg1 = pygame.image.load('./Sprites/Background/pine2.png').convert_alpha()
        #self.pineRect1 = self.pineForestImg1.get_rect()
        self.pineForestImg2 = pygame.image.load('./Sprites/Background/pine1.png').convert_alpha()
        #self.pineRect2 = self.pineForestImg2.get_rect()
        self.TILE_COUNT = 16
        # Nowe elementy:
        self.level = 0
        self.saveButtonImg = ''
        self.loadButtonImg = ''
        self.worldData = []
        self.buttonList = []
        self.currentTile = 0
        self.init = True # Przerobic na kontrolke.
        self.mousePos = 0
        self.mousePosX = 0
        self.mousePosY = 0
        # INIT
        #self.InitTiles() # TODO: Przeniesc to
        #self.InitWorldData()
    def InitImg(self): # ZMIENIC NAZWE NA INIT IMG
        self.saveButtonImg = pygame.image.load('img/saveButton.png').convert_alpha()
        self.loadButtonImg = pygame.image.load('img/loadButton.png').convert_alpha()
        self.imgList = []
        for x in range(5):
            img = pygame.image.load(f'Sprites/Tiles/grass_{x+1}.png')
            img = pygame.transform.scale(img,(self.TILESIZE,self.TILESIZE))
            self.imgList.append(img)
        for x in range(11):
            img = pygame.image.load(f'Sprites/Tiles/ground_{x+1}.png')
            img = pygame.transform.scale(img, (self.TILESIZE, self.TILESIZE))
            self.imgList.append(img)
        print(self.imgList)
    def InitWorldData(self):
        for row in range(self.ROWS):
            r = [-1] * self.COLS
            self.worldData.append(r)
        print(self.worldData)
    def InitButtons(self):
        buttonCol = 0
        buttonRow = 0
        for i in range(len(self.imgList)):
            tileButton = Button(
                self.game.DISPLAY_WIDTH - self.SIDEMARGIN + (40 * buttonCol) + 30,
                40 * buttonRow + 30,
                self.imgList[i],
                1
            )
            self.buttonList.append(tileButton)
            buttonCol += 1
            if buttonCol == 3:
                buttonRow += 1
                buttonCol = 0
        self.saveButton = Button(0.02 * self.game.DISPLAY_WIDTH, self.game.DISPLAY_HEIGHT - self.LOWERMARGIN + 40, self.saveButtonImg, 0.35)
        self.loadButton = Button(0.02 * self.game.DISPLAY_WIDTH + 75, self.game.DISPLAY_HEIGHT - self.LOWERMARGIN + 40, self.loadButtonImg, 0.35)
        print(self.buttonList)
    def InitEditorSettings(self):
        self.InitImg()
        self.InitWorldData()
        self.InitButtons()
    def CheckMouseMotion(self):
        self.mousePos = pygame.mouse.get_pos()
        self.mousePosX = (self.mousePos[0] + self.scroll) // self.TILESIZE
        self.MousePosY = self.mousePos[1] // self.TILESIZE
    def CheckTileArea(self):
        if self.mousePos[0] < self.game.DISPLAY_WIDTH - self.SIDEMARGIN and self.mousePos[1] < self.game.DISPLAY_HEIGHT - self.LOWERMARGIN:
            # update tile value
            if pygame.mouse.get_pressed()[0] == 1:
                if self.worldData[self.mousePosY][self.MousePosY] != self.currentTile:
                    self.worldData[self.MousePosY][self.mousePosX] = self.currentTile
                    print("OK")
                else:
                    print(" NIE OK ")
        print(self.mousePosX)
        print(self.mousePosY)
    # KONIEC NOWYCH
    def ResetKeys(self):
        self.keyBackspace = False
    def CheckInput(self):
        if (self.keyBackspace):
            print("Backspace")
        if (self.scrollLeft and self.scroll > 10):
            self.scroll -= 5 * self.scrollSpeed
        if (self.scrollRight):
            self.scroll += 5 * self.scrollSpeed
        if (self.leftShift):
            self.scrollSpeed = 5
        if (self.leftShift == False):
            self.scrollSpeed = 1

    def UpdateEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.runDisplay = False
                self.game.start = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.keyBackspace = True
                    print(self.keyBackspace)
                if event.key == pygame.K_LEFT:
                    self.scrollLeft = True
                if event.key == pygame.K_RIGHT:
                    self.scrollRight = True
                if event.key == pygame.K_LSHIFT:
                    self.leftShift = True
                # NOWE
                if event.key == pygame.K_UP:
                    self.level += 1
                if event.key == pygame.K_DOWN and self.level > 0:
                    self.level -= 1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.scrollLeft = False
                if event.key == pygame.K_RIGHT:
                    self.scrollRight = False
                if event.key == pygame.K_LSHIFT:
                    self.leftShift = False
    def Update(self):
        self.UpdateEvents()
        self.CheckInput()
        self.CheckMouseMotion()
        self.CheckTileArea()
        # TODO: ZROBIC NOWA FUNKCJE DO OBSLUGI CSV:

        if self.saveButton.Draw(self.game.display):
            # save level data
            with open(f'level{self.level}_data.csv', 'w', newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=',')
                for row in self.worldData:
                    writer.writerow(row)
        if self.loadButton.Draw(self.game.display):
            # load in level data
            # reset scrol lback to teh start of the level
            self.scroll = 0
            with open(f'level{self.level}_data.csv', newline='') as csvfile:
                reader = csv.reader(csvfile, delimiter=',')
                for x, row in enumerate(reader):
                    for y, tile in enumerate(row):
                        self.worldData[x][y] = int(tile)
        self.ResetKeys()
        pygame.display.update()
    def DrawBg(self):
        self.game.display.fill(self.game.COLORS["gray"])
        width = self.skyImage.get_width()
        for x in range(4):
            self.game.display.blit(self.cloudImage, ((x * width)-self.scroll * 0.5,0))
            self.game.display.blit(self.skyImage, ((x * width)-self.scroll * 0.6, self.game.DISPLAY_HEIGHT - self.skyImage.get_height() - 250))
            self.game.display.blit(self.mountainImage,((x * width)-self.scroll * 0.7, self.game.DISPLAY_HEIGHT - self.mountainImage.get_height() - 250))
            self.game.display.blit(self.pineForestImg2, ((x * width)-self.scroll * 0.8,self.game.DISPLAY_HEIGHT - self.pineForestImg2.get_height() - 180))
            self.game.display.blit(self.pineForestImg1, ((x * width)-self.scroll * 0.9,self.game.DISPLAY_HEIGHT - self.pineForestImg2.get_height() - 150))
    def DrawGrid(self):
        for i in range(self.COLS):
            pygame.draw.line(self.game.display,self.game.COLORS["white"],(i * self.TILESIZE - self.scroll,0),(i*self.TILESIZE - self.scroll,self.game.DISPLAY_HEIGHT- self.LOWERMARGIN))
        for i in range(self.ROWS):
            pygame.draw.line(self.game.display,self.game.COLORS["white"],(0,i * self.TILESIZE),(self.game.DISPLAY_WIDTH - self.SIDEMARGIN,i * self.TILESIZE))
    def DrawWorld(self):
        for y, row in enumerate(self.worldData):
            for x, tile in enumerate(row):
                if tile >= 0:
                    # screen.blit(imgList[tile],(x * TILESIZE - scroll,y * tile))
                    self.game.display.blit(self.imgList[tile], (x * self.TILESIZE - self.scroll, y * self.TILESIZE))
                    # screen.blit(imgList[tile],(x * TILESIZE - scroll,SCREEN_HEIGHT - TILESIZE))
    def DrawEditorPanel(self):
        pygame.draw.rect(self.game.display,self.game.COLORS['black'],(self.game.DISPLAY_WIDTH - self.SIDEMARGIN,0,self.SIDEMARGIN,self.game.DISPLAY_HEIGHT + self.LOWERMARGIN))
        pygame.draw.rect(self.game.display,self.game.COLORS["black"],(0,self.game.DISPLAY_HEIGHT - self.LOWERMARGIN,self.game.DISPLAY_WIDTH,self.game.DISPLAY_HEIGHT - self.LOWERMARGIN))
        for buttonCount, i in enumerate(self.buttonList):
            if i.Draw(self.game.display):
                self.currentTile = buttonCount
        # highlight the selected tile
        pygame.draw.rect(self.game.display, self.game.COLORS['white'], self.buttonList[self.currentTile].rect, 3)
        self.game.DrawText(f'Level - {self.level}', 20, 0.25 * self.game.DISPLAY_WIDTH,self.game.DISPLAY_HEIGHT - self.LOWERMARGIN // 2 + 5,self.game.COLORS["white"])
        self.game.DrawText(f'Press UP or DOWN to change level', 20, 0.35 * self.game.DISPLAY_WIDTH + 100,self.game.DISPLAY_HEIGHT - self.LOWERMARGIN // 2 + 5,self.game.COLORS["white"])
        self.saveButton.Draw(self.game.display)
        self.loadButton.Draw(self.game.display)

    def Render(self):
        self.DrawBg()
        self.DrawGrid()
        self.DrawWorld()
        self.DrawEditorPanel()
        self.BlitScreen()
    def DisplayState(self):
        print("Jestem w edytorze.")
        if (self.init == True):
            self.InitEditorSettings()
            self.init = False
        while self.runDisplay:
            self.Update()
            self.Render()
            # ZEGAR
            self.game.clock.tick( self.game.FPS )