import os
from pygame.locals import *
'''
配置项
'''

# 支持的输出设备：电脑屏幕，LED点阵
SUPPORT_DISPLAY_DEVICE = ('screen', 'ledMatrix_max7219')
# 当前输出设备，必须是支持输出设备中的值
DISPLAY_DEVICE = 'screen'


#项目根目录
ROOT_DIR = os.path.dirname(__file__)

#常用颜色预定义
#                   R    G    B
WHITE           = (255, 255, 255)
GRAY            = (185, 185, 185)
BLACK           = (0,   0,   0)
RED             = (255,   0,   0)
LIGHTRED        = (175,  20,  20)
GREEN           = (0, 255,   0)
LIGHTGREEN      = (20, 175,  20)
BLUE            = (0,   0, 255)
LIGHTBLUE       = (20,  20, 175)
YELLOW          = (255, 255,   0)
LIGHTYELLOW     = (175, 175,  20)
CYAN            = (0, 255, 255)
MAGENTA         = (255,   0, 255)
ORANGE          = (255, 100,   0)

#背景颜色
BGCOLOR = BLACK
# 可用颜色字典
COLORS = {
    "blue":     BLUE,
    "green":    GREEN,
    "red":      RED,
    "yellow":   YELLOW,
    "cyan":     CYAN,
    "magenta":  MAGENTA,
    "orange":   ORANGE,
    "black":    BLACK
}

LOGO_DIR = ROOT_DIR + "/statics/pi.bmp"
SHUTDOWN_DIR = ROOT_DIR + "/statics/shutdown.bmp"

#高宽
PIXEL_X = 10
PIXEL_Y = 20
#像素大小
SIZE = 20

#每页游戏数量
GAME_PAGE_SIZE = 5
#游戏
GAMES = ["clock", "number", "tetris"]

#键盘
KEY_MAP = {
    "return":   K_q,
    "left":     K_LEFT,
    "right":    K_RIGHT,
    "down":     K_DOWN,
    "up":       K_UP,
    "space":    K_SPACE
}

#手柄