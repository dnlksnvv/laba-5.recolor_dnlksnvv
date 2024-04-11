from PyQt5.QtWidgets import QMainWindow, QLabel, QApplication
from PyQt5.QtGui import QPainter, QBrush, QColor
from game import Game

class GameWindow(QMainWindow):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.moves_label = QLabel(self)
        self.win_label = QLabel("WIN!", self)
        self.win_label.setStyleSheet("font-size: 20pt; color: green;")
        self.win_label.resize(100, 30)
        self.win_label.move(250, 620)
        self.win_label.hide()
        self.initUI()

    def initUI(self):
        cell_size = 50
        width = self.game.width * cell_size
        height = self.game.height * cell_size + 100
        self.setGeometry(300, 300, width, height)
        self.setWindowTitle('Color laba-5.recolor_dnlksnvv')
        self.moves_label.setText(f"Moves Left: {self.game.moves_left}")
        self.moves_label.move(10, self.game.height * cell_size + 20)
        self.moves_label.resize(200, 30)
        self.win_label.move(width // 2 - self.win_label.width() // 2, self.game.height * cell_size + 20)
        self.show()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawBoard(qp)
        qp.end()
        self.moves_label.setText(f"Moves Left: {self.game.moves_left}")
        if self.game.check_win_condition:
            self.win_label.show()
        else:
            self.win_label.hide()

    def drawBoard(self, qp):
        color_dict = {'red': QColor(255, 0, 0), 'orange': QColor(255, 165, 0), 'purple': QColor(128, 0, 128),
                      'blue': QColor(0, 0, 255), 'green': QColor(0, 128, 0), 'yellow': QColor(255, 255, 0)}
        cell_size = 50
        for i in range(self.game.height):
            for j in range(self.game.width):
                qp.setBrush(QBrush(color_dict[self.game.board[i][j]]))
                qp.drawRect(cell_size * j, cell_size * i, cell_size, cell_size)

    def mousePressEvent(self, event):
        cell_size = 50
        x = event.x() // cell_size
        y = event.y() // cell_size
        if x >= self.game.width or y >= self.game.height:
            return
        new_color = self.game.board[y][x]
        self.game.change_color(new_color)
        self.update()
