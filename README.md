## 像素游戏

> 项目使用python3, 基于pygame编写，主要是重构了一个开源树莓派项目的代码，目前支持2种输出设备（重构未完成）
> - 输出到电脑显示屏幕，只要系统能够运行python即可
> - 输出到WS2812B组成的LED像素屏(10*20)，分数或提示信息输出到MAX7219（8*32）点阵屏
> 开源树莓派项目地址:https://www.instructables.com/Wooden-LED-Gaming-Display-Powered-by-Raspberry-Pi-/

### 设置方式
```
配置文件：根目录/conf.py

# 输出设备设置
DISPLAY_DEVICE = 'screen' # 表示输出到电脑显示屏幕
DISPLAY_DEVICE = 'ledMatrix_max7219' # 表示输出到LED屏

# 显示像素
PIXEL_X = 10
PIXEL_Y = 20
#像素大小
#在电脑显示屏只因为单个像素很小，肉眼无法识别，所以增加像素大小配置，表示单个显示像素实际等于20*20个屏幕像素
SIZE = 20

```

### python依赖
```
# Neopixel驱动，pygame, max7219, libsdl
sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixels
sudo pip3 install pygame
sudo apt-get install libsdl1.2-dev
sudo pip3 install --upgrade luma.led_matrix

```

### 启动游戏
```
python3 main.py
```
- 启动后显示树莓派LOGO
- 3秒后进入游戏选择界面，由于像素屏显示效果有限，以顺序表示游戏：0时钟，1测试显示，2俄罗斯方块