from conf import *


PIECES_BLANK = '.'
PIECES_LIGHT = '0'
S_SHAPE_TEMPLATE = [['.....',
                     '.....',
                     '..OO.',
                     '.OO..',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..OO.',
                     '...O.',
                     '.....']]

Z_SHAPE_TEMPLATE = [['.....',
                     '.....',
                     '.OO..',
                     '..OO.',
                     '.....'],
                    ['.....',
                     '..O..',
                     '.OO..',
                     '.O...',
                     '.....']]

I_SHAPE_TEMPLATE = [['..O..',
                     '..O..',
                     '..O..',
                     '..O..',
                     '.....'],
                    ['.....',
                     '.....',
                     'OOOO.',
                     '.....',
                     '.....']]

O_SHAPE_TEMPLATE = [['.....',
                     '.....',
                     '.OO..',
                     '.OO..',
                     '.....']]

J_SHAPE_TEMPLATE = [['.....',
                     '.O...',
                     '.OOO.',
                     '.....',
                     '.....'],
                    ['.....',
                     '..OO.',
                     '..O..',
                     '..O..',
                     '.....'],
                    ['.....',
                     '.....',
                     '.OOO.',
                     '...O.',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..O..',
                     '.OO..',
                     '.....']]

L_SHAPE_TEMPLATE = [['.....',
                     '...O.',
                     '.OOO.',
                     '.....',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..O..',
                     '..OO.',
                     '.....'],
                    ['.....',
                     '.....',
                     '.OOO.',
                     '.O...',
                     '.....'],
                    ['.....',
                     '.OO..',
                     '..O..',
                     '..O..',
                     '.....']]

T_SHAPE_TEMPLATE = [['.....',
                     '..O..',
                     '.OOO.',
                     '.....',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..OO.',
                     '..O..',
                     '.....'],
                    ['.....',
                     '.....',
                     '.OOO.',
                     '..O..',
                     '.....'],
                    ['.....',
                     '..O..',
                     '.OO..',
                     '..O..',
                     '.....']]

PIECES = {'S': S_SHAPE_TEMPLATE,
          'Z': Z_SHAPE_TEMPLATE,
          'I': I_SHAPE_TEMPLATE,
          'J': J_SHAPE_TEMPLATE,
          'L': L_SHAPE_TEMPLATE,
          'O': O_SHAPE_TEMPLATE,
          'T': T_SHAPE_TEMPLATE}

PIECES_ORDER = {'S': 0, 'Z': 1, 'I': 2, 'J': 3, 'L': 4, 'O': 5, 'T': 6}
PIECES_COLOR = {'S': 'blue', 'Z': 'green', 'I': 'red', 'J': 'yellow', 'L': 'cyan', 'O': 'magenta', 'T': 'orange'}

# 游戏区域大小
BOARDWIDTH = PIXEL_X
BOARDHEIGHT = PIXEL_Y
# 方块长宽最大
TEMPLATEWIDTH = 5
TEMPLATEHEIGHT = 5
# 横向移动刷新率
MOVESIDEWAYSFREQ = 0.15
# 下落刷新率
MOVEDOWNFREQ = 0.15
# 下拉速度,越小速度越快
FALLING_SPEED = 0.7

# 游戏最高等级，等级越高，速度越快，分值越高
MAX_LEVEL = 10
# 升级行数
LEVEL_UP_LINE = 20

# 分数，一次性消除的行对应不同分值
# 1行40分
# 2行100分
# ...
SCORES_BASE =(0,40,100,300,1200)