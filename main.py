from PyQt5.QtWidgets import QApplication
from description_window import DescriptionWindow
import sys

def main():
    app = QApplication(sys.argv)
    description_window = DescriptionWindow()
    description_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

