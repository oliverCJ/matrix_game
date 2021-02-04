'''
显示时间
'''
import time, sys
from libs.common import *

class showClock():

    screen = None

    def __init__(self, screen, isPi=False):
        self.isPi = isPi
        self.screen = screen

    def drawDispatch(self, c, x, y, color):
        if self.isPi:
            pass
        else:
            drawNumber(self.screen, c, x, y, color)


    def drawClock(self):
        while True:
            pygame.event.pump()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                # 键盘按键触发
                if event.type == KEYDOWN:
                    if event.key == KEY_MAP['return']:
                        return

            clearScreen(self.screen)
            hour = time.localtime().tm_hour
            minute = time.localtime().tm_min
            second = time.localtime().tm_sec

            self.drawDispatch(int(hour / 10), 2, 1, "blue")
            self.drawDispatch(int(hour % 10), 6, 1, "blue")
            self.drawDispatch(int(minute / 10), 2, 8, "blue")
            self.drawDispatch(int(minute % 10), 6, 8, "blue")
            self.drawDispatch(int(second / 10), 2, 15, "blue")
            self.drawDispatch(int(second % 10), 6, 15, "blue")
            updateScreen()
            time.sleep(.2)
            

if __name__ == '__main__':
    pass
