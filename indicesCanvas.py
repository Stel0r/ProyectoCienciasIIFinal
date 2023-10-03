import sys
from PyQt5 import QtWidgets as QtW
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import QtCore, QtGui;
from PyQt5.QtGui import QPaintEvent,QImage


class indiceCanvas(QtW.QWidget):
    def __init__(self,p:QtW.QWidget):
        super().__init__(p)
        #definicion de variables para el dibujo de la grafica
        self.Tipo = ""
        self.cantNivel = ""
        self.tamaBloque = 0
        self.cantRegistro = 0
        self.tamaRegistro = 0
        self.tamaRegistroIndice = 0

        self.regisXbloq = 0
        self.cantBloqRegis = 0
        self.indicXbloq = 0
        self.cantBloqIndic = 0


    def dibujarGrafico(self,T:str,cN:str,tB:int,cR:int,tR:int,tRI:int):
        #TO DO: Agregar un arreglo con la info que se mostrara en la tabla
        self.Tipo = T
        self.cantNivel = cN
        self.tamaBloque = tB
        self.cantRegistro = cR
        self.tamaRegistro = tR
        self.tamaRegistroIndice = tRI

        self.regisXbloq = self.tamaBloque/self.tamaRegistro
        self.cantBloqRegis = self.cantRegistro/self.regisXbloq
        self.indicXbloq = self.tamaBloque/self.tamaRegistroIndice
        if(self.Tipo == "Primario"):
            self.cantBloqIndic = self.cantBloqRegis/self.indicXbloq
        elif(self.Tipo == "Secundario"):
            self.cantBloqIndic = self.cantRegistro/self.indicXbloq
        if(self.cantNivel == "Multinivel"):
            #bucle para reducir los indices hasta un bloque
            return


    def paintEvent(self, a0: QPaintEvent) -> None:
        super().paintEvent(a0)
        painter = QtGui.QPainter()
        #dibujar el fondo
        painter.begin(self)
        painter.fillRect(self.rect(),QtGui.QColorConstants.White)
        painter.setPen(QtGui.QPen(QtGui.QColorConstants.Black,3))
        painter.drawRect(self.rect())
        #creacion de la estructura principal
        painter.drawRect(400,20,60,300)
        #creacion de la estructura indice
        if(self.Tipo == "Primario"):
            painter.drawRect(200,80,60,200)
        elif(self.Tipo == "Secundario"):
            painter.drawRect(200,20,60,300)
        #creacion de las estructuras indices de multinivel
        if(self.cantNivel == "Multinivel"):
                #logica creacion del resto de niveles
                painter.drawRect(100,20,60,300)


        painter.end()

