import pygame
from conf import *


# 数字点阵编码 3*5
numberFont = [
        0x1F, 0x11, 0x1F, # 0
        0x00, 0x00, 0x1F, # 1
        0x1D, 0x15, 0x17, # 2
        0x15, 0x15, 0x1F, # 3
        0x07, 0x04, 0x1F, # 4
        0x17, 0x15, 0x1D, # 5
        0x1F, 0x15, 0x1D, # 6
        0x01, 0x01, 0x1F, # 7
        0x1F, 0x15, 0x1F, # 8
        0x17, 0x15, 0x1F # 9
]

# 字母点阵编码 4*5
characterFont = [
        0x1E, 0x05, 0x05, 0x1E, # A
        0x1F, 0x15, 0x15, 0x0A, # B
        0x78, 0x78, 0x1E, 0x1E, # S
        0x1E, 0x1E, 0x78, 0x78, # Z
        0x00, 0xFF, 0xFF, 0x00, # I
        0x06, 0x06, 0x7E, 0x7E, # J
        0x7E, 0x7E, 0x06, 0x06, # L
        0x3C, 0x3C, 0x3C, 0x3C, # O
        0x7E, 0x7E, 0x18, 0x18, # T
]

# 俄罗斯方块形状对应字符点阵
tetrisFont = [
        0x78, 0x78, 0x1E, 0x1E, #S
        0x1E, 0x1E, 0x78, 0x78, #Z
        0x00, 0xFF, 0xFF, 0x00, #I
        0x06, 0x06, 0x7E, 0x7E, #J
        0x7E, 0x7E, 0x06, 0x06, #L
        0x3C, 0x3C, 0x3C, 0x3C, #O
        0x7E, 0x7E, 0x18, 0x18, #T
]

# 汉字点阵编码
hanFont = [

]

# 按位取值
mask = bytearray([1, 2, 4, 8, 16, 32, 64, 128])

# 根据不同的输出设备，加载不同的方法
if SUPPORT_DISPLAY_DEVICE.__contains__(DISPLAY_DEVICE):
    if DISPLAY_DEVICE == 'ledMatrix_max7219':
        from libs.device.ledMatrix_max7219.common import *
    elif DISPLAY_DEVICE == 'screen':
        from libs.device.screen.common import *


def clearScreen(screen):
    '''
    填充屏幕背景色，等效于清除屏幕显示内容
    :return:
    '''
    screen.fill(BGCOLOR)


def updateScreen():
    '''
    显示图像
    :return:
    '''
    pygame.display.update()
