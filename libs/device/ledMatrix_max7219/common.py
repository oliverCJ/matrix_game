from libs.common import numberFont, tetrisFont, mask
from libs.device.ledMatrix_max7219.max7219 import *
from PIL import Image
from conf import *
import time
import board
import neopixel
import subprocess
'''
LED ws2812点阵显示图像（20*10）
max7219显示分数或文字内容（8*32）
'''

def drawImage(filename, boardHeight, boardWidth):
    '''
    绘制图像
    :param filename:
    :param boardHeight:
    :param boardWidth:
    :return:
    '''
    im = Image.open(filename)
    for row in range(0, boardHeight):
        for col in range(0, boardWidth):
            r, g, b = im.getpixel((col, row))
            drawPixel(col, row, (r, g, b))

def drawPixel(x, y, color):
    pixels = []
    if (x >= 0 and y >= 0):
        if x % 2 == 1:
            pixels[x * PIXEL_Y + y] = color
        else:
            pixels[x * PIXEL_Y + (PIXEL_Y - 1 - y)] = color
    return pixels

def drawNumber(screen, number, offsetx, offsety, color):
    '''
    绘制数字
    :param screen:
    :param number:
    :param offsetx:
    :param offsety:
    :param color:
    :return:
    '''
    for x in range(0, 3):
        for y in range(0, 5):
            if numberFont[3 * number + x] & mask[y]:
                drawPixel(offsetx + x, offsety + y, color)

def drawTetrisScoreAndNext(screen, score, level, lineCount, piece):
    '''
    绘制俄罗斯方块的分数和下一个方块
    :param screen:
    :param score:
    :param level:
    :param piece:
    :return:
    '''
    _score = score
    if _score > 999999:
        _score = 999999

    with canvas(device) as draw1:
        # for i in range(0, level):
        #     drawScorePixel(i * 2, 7, 1, draw1)

        for i in range(0, 6):
            drawnumberMAX7219(_score % 10, i * 4, 0, draw1)
            _score //= 10

        drawTetrisMAX7219(piece, 27, 0, draw1)
        device.show()