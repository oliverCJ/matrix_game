import pygame
from PIL import Image
from conf import *
from libs.common import numberFont, characterFont, mask
from games.tetris.shapeConf import PIECES_ORDER
'''
电脑屏幕显示
通用方法
'''

def drawImage(screen, filename, boardHeight, boardWidth):
    '''
    绘制图像
    :param filename:图像文件地址
    :param boardHeight:游戏窗口高度
    :param boardWidth:游戏窗口宽度
    :return:
    '''
    im = Image.open(filename)
    for row in range(0, boardHeight):
        for col in range(0, boardWidth):
            r, g, b = im.getpixel((col, row))
            pygame.draw.rect(screen, (r, g, b), (col * SIZE + 1, row * SIZE + 1, SIZE - 2, SIZE - 2))

def drawPixel(screen, x, y, color):
    '''
    绘制像素块，一个像素块由多个基本像素组成
    只能使用预定义颜色
    :param x:
    :param y:
    :param color:颜色元组
    :return:
    '''
    pygame.draw.rect(screen, COLORS[color], (x * SIZE + 1, y * SIZE + 1, SIZE - 2, SIZE - 2))

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
                drawPixel(screen, offsetx + x, offsety + y, color)



def drawCharacter(screen, number, offsetx, offsety, color):
    '''
    绘制字母
    :param screen:
    :param number:
    :param offsetx:
    :param offsety:
    :param color:
    :return:
    '''
    for x in range(0, 4):
        for y in range(0, 5):
            if characterFont[4 * number + x] & mask[y]:
                drawPixel(screen, offsetx + x, offsety + y, color)

def drawTetrisScoreAndNext(screen, score, level, lineCount, piece):
    '''
    俄罗斯方块的分数展示和下一个提示
    :param screen:
    :param score:
    :param level:
    :param piece:
    :return:
    '''
    print("---------tips--------")
    print("current score:" + str(score))
    print("current level:" + str(level))
    print("current lines:" + str(lineCount))
    for k, v in PIECES_ORDER.items():
        if (v == piece):
            print("next piece:" + k)
            break
