from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from ArbolesView.Nodo import Nodo

class ArbolesCanvas(QWidget):
    def __init__(self,p:QWidget):
        super().__init__(p)
        self.activo = False
        self.arbol:Nodo
        self.separacion = 20

    def paintEvent(self, a0: QPaintEvent) -> None:
        super().paintEvent(a0)
        painter = QPainter()
        painter.begin(self)
        painter.setPen(QPen(QColorConstants.Black,3))
        if(self.activo):
            self.dibujarNodo(self.arbol,self.rect().width()//2,30,painter) 
        painter.end()

                
    def dibujarNodo(self,nodo:Nodo,x,y,painter:QPainter,nivel = 0,xPrev = 0, yPrev = 0):
        painter.drawEllipse(x,y,30,30)
        print(self.arbol.niveles)
        painter.drawText(x+10,y+20,nodo.valor)
        if(xPrev != 0 and yPrev != 0):
            painter.drawLine(x+15,y,xPrev+15,yPrev+30)
        if(len(nodo.hijos) == 0):
            return
        else:
            for n in range(len(nodo.hijos)):
                sep = self.separacion * (2**(self.arbol.niveles-nivel))
                print(sep,self.arbol.niveles)
                newX =int(x-sep + (n*((2*sep)//(len(nodo.hijos)-1))))
                self.dibujarNodo(nodo.hijos[n],newX,y+65,painter,nivel+1,x,y)
                painter.drawText(newX+10,y+50,str(n))