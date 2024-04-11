from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton
from settings_dialog import SettingsDialog

class DescriptionWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Описание игры")
        self.setGeometry(100, 100, 400, 300)
        layout = QVBoxLayout()

        description_label = QLabel("Меняйте цвет фигуры. \nЗахватывайте поле!")
        layout.addWidget(description_label)

        start_button = QPushButton("Начать")
        start_button.clicked.connect(self.open_settings)
        layout.addWidget(start_button)

        self.setLayout(layout)

    def open_settings(self):
        self.close()
        self.settings_dialog = SettingsDialog()
        self.settings_dialog.exec_()
