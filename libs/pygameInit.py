import pygame, sys, time, math
from pygame.locals import *
from PIL import Image
from conf import *
from libs.common import *
from games.clock.showClock import *
from games.clock.showSingleChar import *
from games.tetris.tetris import *

class pygameInit():

    screen = None
    basicFont = None
    bigFont = None
    
    def __init__(self):
        x = PIXEL_X * SIZE
        y = PIXEL_Y * SIZE

        pygame.init()
        self.screen = pygame.display.set_mode((x, y))
        pygame.display.set_caption("Pi Games")

    def start(self):
        self.showLogo()
        self.showSelectGame()

    def startGame(self, gameNo):
        '''
        根据选择启动游戏
        :param gameNo:
        :return:
        '''
        for k, v in enumerate(GAMES):
            if (k == gameNo):
                if v == "clock":
                    clockInstance = showClock(self.screen, False)
                    return clockInstance.drawClock()
                if v == "number":
                    numberInstance = showSingleChar(self.screen, 'B')
                    return numberInstance.drawChar()
                if v == "tetris":
                    tetrisInstance = tetris(self.screen, False)
                    return tetrisInstance.gameStart()


    def drawSelectCursor(self, x, y):
        '''
        显示选择游标
        :param x:
        :param y:
        :return:
        '''
        if (y > GAME_PAGE_SIZE):
            y = GAME_PAGE_SIZE
        drawPixel(self.screen, x, y, "green")

    def drawGameSelect(self, gameNum, color):
        '''
        显示游戏选择图标
        :param num:
        :param color:
        :return:
        '''
        for i in range(1, gameNum + 1):
            for j in range(0, i):
                drawPixel(self.screen, j + 2, i - 1, color)

    def catchKeyOp(self, key):
        '''
        按键触发
        :param key:
        :return:
        '''
        # 键盘向下选择
        if key == K_q:
            self.showExit()
        if key == K_DOWN:
            self.initCursorPos += 1
            # 不能超过最大值。循环选择
            if self.initCursorPos > (self.realPageNum - 1):
                self.initCursorPos = 0
        # 键盘向上选择
        if key == K_UP:
            self.initCursorPos -= 1
            # 不能超过最小值。循环选择
            if self.initCursorPos < 0:
                self.initCursorPos = self.realPageNum - 1
        # 向右翻页
        if key == K_RIGHT:
            if self.realGameNum > 5 and self.currentPage < math.floor(self.realGameNum / GAME_PAGE_SIZE):
                self.currentPage += 1
                self.initCursorPos = 0
                self.realPageNum = GAME_PAGE_SIZE if (self.realGameNum - GAME_PAGE_SIZE * self.currentPage) >= GAME_PAGE_SIZE else self.realGameNum - GAME_PAGE_SIZE
        # 向左翻页
        if key == K_LEFT:
            if self.currentPage >= 1:
                self.currentPage -= 1
                self.initCursorPos = 0
                self.realPageNum = GAME_PAGE_SIZE

        # 当前选中游戏序号
        gameSelect = self.currentPage * GAME_PAGE_SIZE + self.initCursorPos
        print("current select: " + str(gameSelect))

        # 回车选中游戏，执行游戏
        if key == K_RETURN:
            self.startGame(gameSelect)


    def showLogo(self):
        '''
        显示LOGO
        :return:
        '''
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            drawImage(self.screen, LOGO_DIR, PIXEL_Y, PIXEL_X)
            updateScreen()
            time.sleep(3)
            break

    def showExit(self):
        '''
        显示结束LOGO，确认后退出游戏或取消退出
        :return:
        '''
        confirm = 0
        while True:
            pygame.event.pump()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        confirm = 1
                    if event.key == K_ESCAPE:
                        confirm = 2

            if confirm == 1:
                pygame.quit()
                sys.exit()
            elif confirm == 2:
                return

            drawImage(self.screen, SHUTDOWN_DIR, PIXEL_Y, PIXEL_X)
            updateScreen()
            time.sleep(0.5)


    def showSelectGame(self):
        '''
        游戏选择界面，按预定义顺序展示。
        由于可用像素较少，所以采用顺序选择的方式
        :return:
        '''
        gameColor0_5 = "orange"
        gameColor5_10 = "magenta"
        gameSelect = 0  # 游戏选择序号

        self.initCursorPos = 0 #游标位置
        self.currentPage = 0 # 当前页码
        self.realPageNum = GAME_PAGE_SIZE # 每页游戏数量
        self.realGameNum = len(GAMES) #游戏数量
        if self.realGameNum < GAME_PAGE_SIZE:
            self.realPageNum = self.realGameNum

        #游戏选择界面主循环
        while True:
            clearScreen(self.screen)
            pygame.event.pump()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                # 键盘按键触发
                if event.type == KEYDOWN:
                    self.catchKeyOp(event.key)
                # todo 手柄支持


            # todo 目前只支持10个及以内数量，可扩展
            if gameSelect < 5:
                self.drawGameSelect(self.realPageNum, gameColor0_5)
            elif 5 <= gameSelect < 10 :
                self.drawGameSelect(self.realPageNum, gameColor5_10)
            # elif 10 < gameSelect <= 15 :
            #

            self.drawSelectCursor(0, self.initCursorPos)
            updateScreen()


if __name__ == '__main__':
     game = pygameInit()
     game.start()


