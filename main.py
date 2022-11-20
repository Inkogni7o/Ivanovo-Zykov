import sys

from PyQt5.QtWidgets import QApplication
from example_class import ExampleWidget


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ExampleWidget()
    ex.show()
    sys.exit(app.exec())