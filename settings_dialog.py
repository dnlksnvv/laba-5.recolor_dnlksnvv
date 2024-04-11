from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton
from game_window import GameWindow
from game import Game
from PyQt5.QtCore import QTimer

class SettingsDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("laba-5.recolor_dnlksnvv Settings")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        width_label = QLabel("Width of the field:")
        layout.addWidget(width_label)
        self.width_input = QLineEdit("12")
        layout.addWidget(self.width_input)

        height_label = QLabel("Height of the field:")
        layout.addWidget(height_label)
        self.height_input = QLineEdit("12")
        layout.addWidget(self.height_input)

        moves_label = QLabel("Number of moves:")
        layout.addWidget(moves_label)
        self.moves_input = QLineEdit("24")
        layout.addWidget(self.moves_input)

        start_button = QPushButton("Start laba-5.recolor_dnlksnvv")
        start_button.clicked.connect(self.start_game)
        layout.addWidget(start_button)

        self.setLayout(layout)

    def start_game(self):
        width = int(self.width_input.text())
        height = int(self.height_input.text())
        moves = int(self.moves_input.text())
        self.hide()  # Скрываем окно настроек вместо закрытия
        QTimer.singleShot(200, lambda: self.show_game_window(Game(width=width, height=height, moves_left=moves)))

    def show_game_window(self, game):
        self.game_window = GameWindow(game)
        self.game_window.show()

