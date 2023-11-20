from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from ui import Ui_MainWindow
import sys
import random

SCREEN_SIZE = [680, 480]


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.flag = False
        self.setWindowTitle('Git и желтые окружности')
        self.pushButton.clicked.connect(self.draw)

    def draw(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            color = (random.randint(0, 255), random.randint(
                0, 255), random.randint(0, 255))
            qp = QPainter()
            qp.begin(self)
            qp.setPen(QColor(*color))
            qp.setBrush(QColor(*color))
            for i in range(random.randint(0, 10)):
                size = random.randint(10, 100)
                self.x, self.y = random.randint(
                    100, SCREEN_SIZE[0] - 100), random.randint(100, SCREEN_SIZE[1] - 100)
                qp.drawEllipse(self.x, self.y, size, size)
            qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
