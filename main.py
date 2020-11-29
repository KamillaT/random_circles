import sys

from random import randint
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication
from UI import Ui_Form


class MyWidget(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)


    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()


    def paint(self):
        self.do_paint = True
        self.repaint()


    def draw_flag(self, qp):
        a = randint(30, 100)
        r = randint(0, 256)
        g = randint(0, 256)
        b = randint(0, 256)
        qp.setBrush(QColor(r, g, b))
        qp.drawEllipse(a, a, a, a)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
