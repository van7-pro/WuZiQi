from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QTextEdit
from PyQt5.QtGui import QFont, QTextCursor
from PyQt5.QtCore import pyqtSignal


class StrategyWidget(QWidget):

    def __init__(self, width, height, gameLogit, parent=None):
        super(QWidget, StrategyWidget).__init__(self, parent)
        self.fixedWidth = width
        self.fixedHeight = height
        self.gameLogit = gameLogit
        self.initUI()

    def initUI(self):
        self.setFixedSize(self.fixedWidth, self.fixedHeight)
        gameStrategyLabel = QLabel("AI决策过程", self)
        gameStrategyLabel.move(145, 10)
        font = QFont()
        font.setFamily('微软雅黑')
        font.setBold(True)  # 设置加粗类型
        font.setPointSize(30)  # 设置字体大小
        font.setWeight(35)  # 设置字体粗细
        gameStrategyLabel.setFont(font)

        # Create the Button.
        # showButton = QPushButton('点击显示AI的决策过程\n(棋盘范围内单击可刷新决策过程！)', self)
        showHint = QLabel("棋盘范围内单击可刷新下方决策过程！", self)
        showHint.move(100, 70)
        showHint.resize(320, 75)
        font = QFont()
        font.setFamily('微软雅黑')
        font.setBold(True)  # 设置加粗类型
        font.setPointSize(15)  # 设置字体大小
        font.setWeight(35)  # 设置字体粗细
        showHint.setFont(font)
        # showHint.clicked.connect(self.showButtonClicked)

        # Create the text output widget.
        self.process = QTextEdit(self, readOnly=True)
        self.process.ensureCursorVisible()
        self.process.setLineWrapColumnOrWidth(350)  # 设置换行的固定宽度，即350个像素为一行，若该长度超出了窗口的长度，那么会产生一个水平的滚动条
        self.process.setLineWrapMode(QTextEdit.FixedPixelWidth)  # 按像素限制换行
        self.process.setFixedWidth(400)
        self.process.setFixedHeight(550)
        self.process.move(50, 150)
    '''
    def showButtonClicked(self):
        # 输出文本中的信息到文本窗口中
        try:
            with open('outputlog.txt', 'r+') as f:
                msg = f.read()
                self.process.setPlainText(msg)
                self.process.moveCursor(QTextCursor.End)  # 将滚动条固定至底部
        except:
            pass
    '''
    def refeshStrategyMessage(self, flag=0):
        if flag == 1:
            try:
                with open('outputlog.txt', 'r+') as f:
                    msg = f.read()
                    self.process.setPlainText(msg)
                    self.process.moveCursor(QTextCursor.End)  # 将滚动条固定至底部
            except:
                pass
