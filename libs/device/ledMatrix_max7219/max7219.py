from libs.common import numberFont, tetrisFont, mask
import time
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT

serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=4, blocks_arranged_in_reverse_order=True)

def drawnumberMAX7219(number, offsetx, offsety, draw1):
    '''
    在MAX7219上显示数字
    :param number:
    :param offsetx:
    :param offsety:
    :param draw1:
    :return:
    '''
    for x in range(0,3):
        for y in range(0,5):
            if numberFont[3 * number + 2 - x] & mask[y]:
                drawScorePixel(offsetx + x, offsety + y, 1, draw1)
            elif numberFont[3 * number + 2 - x] & mask[y]:
                drawScorePixel(offsetx + x, offsety + y, 0, draw1)

def drawTetrisMAX7219(piece, offsetx, offsety, draw1):
    '''
    在MAX7219上显示俄罗斯方块对应的形状
    :param piece:
    :param offsetx:
    :param offsety:
    :param draw1:
    :return:
    '''
    for x in range(0, 4):
        for y in range(0, 8):
            if tetrisFont[4 * piece + x] & mask[y]:
                drawScorePixel(offsetx + x, offsety + y, 1, draw1)
            elif tetrisFont[4 * piece + x] & mask[y]:
                drawScorePixel(offsetx + x, offsety + y, 0, draw1)

def drawScorePixel(x, y, on, draw):
    draw.point((31 - x, y), fill="white")
    time.sleep(.01)