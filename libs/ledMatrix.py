from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop

class ledMatrix():
    def __init__(self, isPi = False):
        if isPi:
            serial = spi(port=0, device=0, gpio=noop())
            self.device = max7219(serial, cascaded=4, blocks_arranged_in_reverse_order=True)


if __name__ == '__main__':
    pass

