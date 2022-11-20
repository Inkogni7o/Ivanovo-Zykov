import sys
from random import randint

from PyQt5 import QtGui
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton


class ExampleWidget(QWidget):
    def __init__(self):
        super(ExampleWidget, self).__init__()
        self.start_painting = False
        self.setGeometry(300, 500, 500, 500)
        self.btn = QPushButton('Создать кружок', self)
        self.btn.move(220, 220)
        self.btn.clicked.connect(self.draw_ellipse)

    def draw_ellipse(self):
        self.start_painting = True
        self.repaint()

    def paintEvent(self, event: QtGui.QPaintEvent) -> None:
        qp = QPainter()
        qp.begin(self)
        if self.start_painting:
            qp.setPen(QColor(204, 204, 0))
            radius = randint(5, 50)
            qp.drawEllipse(randint(1, 500), randint(1, 500), radius, radius)
        qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ExampleWidget()
    ex.show()
    sys.exit(app.exec())