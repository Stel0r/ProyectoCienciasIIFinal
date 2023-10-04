from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from ArbolesView.Nodo import Nodo

class ArbolesCanvas(QWidget):
    def __init__(self,p:QWidget):
        super().__init__(p)
        self.setGeometry(0,0,800,650)
        self.activo = False
        self.arbol:Nodo
        self.separacion = 60

    def paintEvent(self, a0: QPaintEvent) -> None:
        super().paintEvent(a0)
        painter = QPainter()
        painter.begin(self)
        painter.setPen(QPen(QColorConstants.Black,3))
        if(self.activo):
           self.dibujarNodo(self.arbol,self.rect().width()//2,30,painter) 
        painter.end()

                
    def dibujarNodo(self,nodo:Nodo,x,y,painter:QPainter,nivel = 0):
        
        painter.drawEllipse(x,y,30,30)
        painter.drawText(x+15,y+15,nodo.valor)
        if(len(nodo.hijos) == 0):
            return
        else:
            for n in range(len(nodo.hijos)):
                sep = (self.arbol.niveles-nivel)*(self.separacion)
                newX =x-sep + (n*((4*sep)//(len(nodo.hijos))))
                print(newX,n)
                self.dibujarNodo(nodo.hijos[n],newX,y+60,painter,nivel+1)