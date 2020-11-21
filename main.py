import sys
import random
from PyQt5 import uic  # Импортируем uic
from PyQt5.QtGui import QPainter, QColor

from PyQt5.QtWidgets import QApplication, QMainWindow
from ui_file import Ui_MainWindow


# Наследуемся от виджета из PyQt5.QtWidgets и от класса с интерфейсом
class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)  # Загружаем дизайн
        self.push.clicked.connect(self.run)
        self.x, self.y = 600, 400

    def run(self):
        qp = QPainter()
        # Начинаем процесс рисования
        qp.begin(self)
        qp.setBrush(QColor(255, 255, 0))
        # Рисуем прямоугольник заданной кистью
        qp.drawEllipse(random.randrange(100), random.randrange(100), random.randrange(90, 600),
                       random.randrange(40, 400))
        # Завершаем рисование
        qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
