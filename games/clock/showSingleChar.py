'''
显示数字或字母
主要用于测试显示数字,0-2位数字
'''
import pygame, time, sys

from libs.common import *


class showSingleChar():
    screen = None
    characterTup = ('A', 'B', 'C', 'D', 'E', 'F')
    character = ""

    def __init__(self, screen, character):
        self.screen = screen
        self.character = character

    def drawDispatch(self, c, x, y, color):
        if c.isdigit():
            drawNumber(self.screen, c, x, y, color)
        elif c.isalpha():
            drawCharacter(self.screen, self.characterTup.index(c), x, y, color)


    def drawChar(self):
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
            if self.character != "" :
                if self.character.isdigit():
                    self.drawDispatch(int(self.character / 10), 2, 1, "blue")
                    self.drawDispatch(int(self.character % 10), 6, 1, "blue")
                elif self.character.isalpha() :
                    self.drawDispatch(self.character, 1, 1, "green")
            updateScreen()
            time.sleep(.2)


if __name__ == '__main__':
    pass
