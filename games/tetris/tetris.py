import random, sys, time
from games.tetris.shapeConf import *
from libs.common import *


class tetris():

    def __init__(self, screen, isPi=False):
        self.screen = screen
        self.isPi = isPi

    def drawBoard(self, matrix):
        '''
        绘制游戏区域
        :param matrix:
        :return:
        '''
        for i in range(0, BOARDWIDTH):
            for j in range(0, BOARDHEIGHT):
                if matrix[i][j] == PIECES_BLANK:
                    color = "black"
                else:
                    color = matrix[i][j]
                drawPixel(self.screen, i, j, color)

    def drawPiece(self, piece, pixelx=None, pixely=None):
        '''
        绘制方块
        :param piece:
        :param pixelx:
        :param pixely:
        :return:
        '''
        shapeToDraw = PIECES[piece['shape']][piece['rotation']]
        if pixelx == None and pixely == None:
            pixelx = piece['x']
            pixely = piece['y']

        # 绘制方块
        for x in range(TEMPLATEWIDTH):
            for y in range(TEMPLATEHEIGHT):
                if shapeToDraw[y][x] != PIECES_BLANK:
                    drawPixel(self.screen, pixelx + x, pixely + y, piece['color'])

    def drawScoreAndNextPiece(self, score, level, lineCount, piece):
        '''
        绘制分数和下一个方块
        :param score:
        :param level:
        :param piece:
        :return:
        '''
        drawTetrisScoreAndNext(self.screen, score, level, lineCount, piece)


    def getBlankBoard(self):
        '''
        创建新的空白游戏区域
        :return:
        '''
        board = []
        for i in range(BOARDWIDTH):
            board.append([PIECES_BLANK] * BOARDHEIGHT)
        return board

    def getNewPiece(self):
        '''
        获取新的方块
        :return:
        '''
        shape = random.choice(list(PIECES.keys()))
        newPiece = {
            'shape': shape,
            'rotation': random.randint(0, len(PIECES[shape]) - 1),
            'x': int(BOARDWIDTH / 2) - int(TEMPLATEWIDTH / 2),
            'y': -2,
            'color': PIECES_COLOR.get(shape)
        }
        return newPiece

    def calculateLevelAndFallFreq(self, lines):
        '''
        基于清除的行数，返回游戏者的等级以及相应的下落速度
        :param score:
        :return:
        '''
        level = int(lines / LEVEL_UP_LINE) + 1 # 每消除LEVEL_UP_LINE行升一级
        if level > MAX_LEVEL:
            level = MAX_LEVEL
        fallFreq = FALLING_SPEED - (level * 0.05)
        if fallFreq <= 0.05:
            fallFreq = 0.05
        return level, fallFreq

    def addToBoard(self, board, piece):
        '''
        填充方块到游戏区域
        :param board:
        :param piece:
        :return:
        '''
        for x in range(TEMPLATEWIDTH):
            for y in range(TEMPLATEHEIGHT):
                if PIECES[piece['shape']][piece['rotation']][y][x] != PIECES_BLANK:
                    board[x + piece['x']][y + piece['y']] = piece['color']

    def removeCompleteLines(self, board):
        '''
        消除完成的行
        :param board:
        :return:
        '''
        numLinesRemoved = 0
        y = BOARDHEIGHT - 1
        while y >= 0:
            if self.isCompleteLine(board, y):
                # 消除后，上面所有行降一层
                for pullDownY in range(y, 0, -1):
                    for x in range(BOARDWIDTH):
                        board[x][pullDownY] = board[x][pullDownY - 1]
                # 将顶部清空
                for x in range(BOARDWIDTH):
                    board[x][0] = PIECES_BLANK
                numLinesRemoved += 1
            else :
                y -= 1
        return numLinesRemoved

    def isCompleteLine(self, board, y):
        '''
        检查行是否填充满
        :return:
        '''
        for x in range(BOARDWIDTH):
            if board[x][y] == PIECES_BLANK:
                return False
        return True

    def isOnBoard(self, x, y):
        '''
        判断是否在游戏区域内
        :param x:
        :param y:
        :return:
        '''
        return x >= 0 and x < BOARDWIDTH and y < BOARDHEIGHT

    def isValidPosition(self, board, piece, adjX=0, adjY=0):
        '''
        方块边缘检测，返回true表示没有碰撞
        :param board:
        :param piece:
        :param adjX:
        :param adjY:
        :return:
        '''
        for x in range(TEMPLATEWIDTH):
            for y in range(TEMPLATEHEIGHT):
                isAboveBoard = y + piece['y'] + adjY < 0
                if isAboveBoard or PIECES[piece['shape']][piece['rotation']][y][x] == PIECES_BLANK:
                    continue
                if not self.isOnBoard(x + piece['x'] + adjX, y + piece['y'] + adjY):
                    return False
                if board[x + piece['x'] + adjX][y + piece['y'] + adjY] != PIECES_BLANK:
                    return False
        return True

    def keyCatch(self, key, board, fallingPiece):
        '''
        键盘按键捕获
        :param key:
        :param board:
        :param fallingPiece:
        :return:
        '''
        if key == KEY_MAP['left'] and self.isValidPosition(board, fallingPiece, adjX=-1):
            fallingPiece['x'] -= 1
            self.movingLeft = True
            self.movingRight = False
            self.lastMoveSidewaysTime = time.time()

        if key == KEY_MAP['right'] and self.isValidPosition(board, fallingPiece, adjX=1):
            fallingPiece['x'] += 1
            self.movingLeft = False
            self.movingRight = True
            self.lastMoveSidewaysTime = time.time()
        if key == KEY_MAP['down']:
            self.movingDown = True
            if self.isValidPosition(board, fallingPiece, adjY=1):
                fallingPiece['y'] += 1
            self.lastMoveDownTime = time.time()
        if key == KEY_MAP['up'] or key == KEY_MAP['space']:
            fallingPiece['rotation'] = (fallingPiece['rotation'] + 1) % len(PIECES[fallingPiece['shape']])
            if not self.isValidPosition(board, fallingPiece):
                fallingPiece['rotation'] = (fallingPiece['rotation'] - 1) % len(PIECES[fallingPiece['shape']])

        return fallingPiece

    def gameStart(self):
        board = self.getBlankBoard()
        fallingPiece = self.getNewPiece()
        nextPiece = self.getNewPiece()
        level, fallFreq = self.calculateLevelAndFallFreq(0)

        self.movingDown = False
        self.movingLeft = False
        self.movingRight = False
        self.lastMoveDownTime = time.time()
        self.lastMoveSidewaysTime = time.time()
        self.lastFallTime = time.time()

        lineCount = 0
        score = 0
        oldScore = -1
        oldPiece = None

        while True:
            pygame.event.pump()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                # 键盘按键触发
                if event.type == KEYDOWN:
                    # 结束返回
                    if event.key == KEY_MAP['return']:
                        time.sleep(2)
                        return
                    # 检测按键动作
                    fallingPiece = self.keyCatch(event.key, board, fallingPiece)

                # todo 模拟器按键q

                # 键盘按键释放
                if event.type == KEYUP:
                    self.movingDown = False
                    self.movingLeft = False
                    self.movingRight = False

            # 重新产生方块，如果已经到顶部则结束游戏
            if fallingPiece == None:
                fallingPiece = nextPiece
                nextPiece = self.getNewPiece()

                # 新的方块与其他方块或游戏边框发生碰撞，则表示游戏区域已填满，游戏结束
                if not self.isValidPosition(board, fallingPiece):
                    time.sleep(2)
                    return

            # 持续按左右建
            if (self.movingLeft or self.movingRight) and time.time() - self.lastMoveSidewaysTime > MOVESIDEWAYSFREQ:
                if self.movingLeft and self.isValidPosition(board, fallingPiece, adjX = -1):
                    fallingPiece['x'] -= 1
                elif self.movingRight and self.isValidPosition(board, fallingPiece, adjX = 1):
                    fallingPiece['x'] += 1
                self.lastMoveSidewaysTime = time.time()

            # 持续按向下键
            if self.movingDown and \
                time.time() - self.lastMoveDownTime > MOVEDOWNFREQ and  \
                self.isValidPosition(board, fallingPiece, adjY=1):
                fallingPiece['y'] += 1
                self.lastMoveDownTime = time.time()

            # 下落
            if time.time() - self.lastFallTime > fallFreq:
                if not self.isValidPosition(board, fallingPiece, adjY=1):
                    # 落地
                    self.addToBoard(board, fallingPiece)
                    # 消除
                    remLine = self.removeCompleteLines(board)
                    # 统计总共消除的行数
                    lineCount += remLine
                    score += SCORES_BASE[remLine] * level
                    level, fallFreq = self.calculateLevelAndFallFreq(lineCount)
                    fallingPiece = None
                else:
                    # 继续下落
                    fallingPiece['y'] += 1
                    self.lastFallTime = time.time()

            clearScreen(self.screen)
            # 重绘游戏区域
            self.drawBoard(board)

            # 绘制下落的方块
            if fallingPiece != None:
                self.drawPiece(fallingPiece)

            # 绘制分数和下一个提示，为了避免一直刷新输出，增加判断分数或形状是否发生改变
            if score != oldScore or PIECES_ORDER.get(nextPiece['shape']) != oldPiece:
                self.drawScoreAndNextPiece(score, level, lineCount, PIECES_ORDER.get(nextPiece['shape']))
                oldScore = score
                oldPiece = PIECES_ORDER.get(nextPiece['shape'])


            updateScreen()
            time.sleep(0.05)