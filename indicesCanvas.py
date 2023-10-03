import sys
from PyQt5 import QtWidgets as QtW
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import QtCore, QtGui;
from PyQt5.QtGui import QPaintEvent,QImage


class indiceCanvas(QtW.QWidget):
    def __init__(self,p:QtW.QWidget):
        super().__init__(p)


    def paintEvent(self, a0: QPaintEvent) -> None:
        super().paintEvent(a0)
        painter = QtGui.QPainter()
        #dibujar el fondo
        painter.begin(self)
        painter.fillRect(self.rect(),QtGui.QColorConstants.White)
        painter.setPen(QtGui.QPen(QtGui.QColorConstants.Black,3))
        painter.drawRect(self.rect())

    

