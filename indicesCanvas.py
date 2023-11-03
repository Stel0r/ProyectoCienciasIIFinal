import math
import sys
from PyQt5 import QtWidgets as QtW
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import QtCore, QtGui;
from PyQt5.QtGui import QPaintEvent,QImage


class indiceCanvas(QtW.QWidget):
    def __init__(self,p:QtW.QWidget):
        super().__init__(p)
        self.resTabla = []
        #definicion de variables para el dibujo de la grafica
        self.activo = False
        self.Tipo = ""
        self.cantNivel = ""
        self.tamaBloque = 0
        self.cantRegistro = 0
        self.tamaRegistro = 0
        self.tamaRegistroIndice = 0
        self.cantIndices = 0
        self.cantEstructuras = 0

        self.regisXbloq = 0
        self.cantBloqRegis = 0
        self.indicXbloq = 0
        self.cantBloqIndic = 0


    def dibujarGrafico(self,T:str,cN:str,tB:int,cR:int,tR:int,tRI:int):
        self.setGeometry (0,0,720,500)
        self.activo = True
        self.resTabla = []
        #TO DO: Agregar un arreglo con la info que se mostrara en la tabla
        self.Tipo = T
        self.cantNivel = cN
        self.tamaBloque = tB
        self.cantRegistro = cR
        self.tamaRegistro = tR
        self.tamaRegistroIndice = tRI

        self.resTabla.append(["1","Cant.registros",str(self.cantRegistro)])
        self.regisXbloq = self.tamaBloque//self.tamaRegistro
        self.resTabla.append(["1","Reg. x Bloque",str(self.regisXbloq)])
        self.cantBloqRegis = math.ceil(self.cantRegistro/self.regisXbloq)
        self.resTabla.append(["1","Bloques",str(self.cantBloqRegis)])
        self.indicXbloq = self.tamaBloque//self.tamaRegistroIndice
        if(self.Tipo == "Primario"):
            self.cantIndices = self.cantBloqRegis
            self.cantBloqIndic = math.ceil(self.cantBloqRegis/self.indicXbloq)
        elif(self.Tipo == "Secundario"):
            self.cantIndices = self.cantRegistro
            self.cantBloqIndic = math.ceil(self.cantRegistro/self.indicXbloq)
        self.resTabla.append(["2","Cant. registros Indice",str(self.cantIndices)])
        self.resTabla.append(["2","Ind x Bloque",str(self.indicXbloq)])
        self.resTabla.append(["2","Cant. Bloques Indice",str(self.cantBloqIndic)])
        row = 2
        if(self.cantNivel == "Multinivel"):
            while self.cantBloqIndic != 1:
                row += 1
                #establecer la anterior estructura como los nuevos registros
                self.cantBloqRegis = self.cantBloqIndic
                #To Do: Termimnar de asignar los datos de cada subindice
                self.resTabla.append([str(row),"Cant. registros Indice",str(self.cantBloqRegis)])
                self.resTabla.append([str(row),"Ind x Bloque",str(self.indicXbloq)])
                self.cantBloqIndic = math.ceil(self.cantBloqRegis/self.indicXbloq)
                self.resTabla.append([str(row),"Cant. Bloques Indice",str(self.cantBloqIndic)])
        self.cantEstructuras = row
        self.update()
        return self.resTabla
        

    def paintEvent(self, a0: QPaintEvent) -> None:
        super().paintEvent(a0)
        painter = QtGui.QPainter()
        #dibujar el fondo
        painter.begin(self)
        painter.fillRect(self.rect(),QtGui.QColorConstants.White)
        painter.setPen(QtGui.QPen(QtGui.QColorConstants.Black,3))
        if(self.activo):
            separacion = 100
            diffEstructura = 30
            borde = 50
            anchoCanvas = self.rect().width()
            altoCanvas = self.rect().height()
            if(self.cantEstructuras <= 3):
                anchoEstructura = (anchoCanvas - (separacion*(self.cantEstructuras-1)) - (2*borde))//self.cantEstructuras
            else:
                anchoEstructura = 140
                self.resize((borde*2+(self.cantEstructuras*anchoEstructura)+((self.cantEstructuras-1)*separacion)),altoCanvas)
                anchoCanvas = self.rect().width()
            #creacion de la estructura indice
            estX = (anchoCanvas-borde-anchoEstructura)
            estY = borde
            painter.drawText(estX+(anchoEstructura//2),estY-20,"Principal")
            painter.drawRect(estX,estY,anchoEstructura,altoCanvas-(2*borde))
            #bordeSuperior
            painter.drawLine(estX,estY+10,estX+anchoEstructura,estY+10)
            painter.drawText(estX-12,estY,"1")
            painter.drawText(estX+(anchoEstructura//2),estY+35,"B1")
            painter.setPen(QtGui.QPen(QtGui.QColorConstants.Black,5))
            painter.drawLine(estX,estY+60,estX+anchoEstructura,estY+60) 
            painter.drawText(estX-((int(len(str(self.resTabla[1][2])))*6))-12,estY+60,str(self.resTabla[1][2])) 
            painter.setPen(QtGui.QPen(QtGui.QColorConstants.Black,3))
            painter.drawLine(estX,estY+50,estX+anchoEstructura,estY+50)
            #bordeInferior
            painter.setPen(QtGui.QPen(QtGui.QColorConstants.Black,5))
            painter.drawLine(estX,estY+(altoCanvas-(2*borde))-60,estX+anchoEstructura,estY+(altoCanvas-(2*borde))-60)
            painter.drawText(estX-((int(len(str(int(self.resTabla[0][2])-int(self.resTabla[1][2]))))*6))-12,estY+(altoCanvas-(2*borde))-60,str(int(self.resTabla[0][2])-int(self.resTabla[1][2]))) 
            painter.setPen(QtGui.QPen(QtGui.QColorConstants.Black,3))
            painter.drawText(estX+(anchoEstructura//2),estY+(altoCanvas-(2*borde))-30,"B"+self.resTabla[2][2])
            painter.drawLine(estX,estY+(altoCanvas-(2*borde))-10,estX+anchoEstructura,estY+(altoCanvas-(2*borde))-10)
            painter.drawText(estX-((int(len(str(self.resTabla[0][2])))*6))-12,estY+(altoCanvas-(2*borde))-10,self.resTabla[0][2])
            if(self.Tipo == "Primario"):
                estX = (anchoCanvas-borde-(2*anchoEstructura)-separacion)
                estY = borde+(diffEstructura//2)
                painter.drawText(estX+(anchoEstructura//2),estY-20,"Est. Indice")
                painter.drawRect(estX,estY,anchoEstructura,altoCanvas-(2*borde)-(diffEstructura))
                #bordeSuperior
                painter.drawLine(estX,estY+10,estX+anchoEstructura,estY+10)
                painter.drawText(estX-10,estY+7,"1")
                painter.drawText(estX+(anchoEstructura//2),estY+35,"B1")
                if self.cantBloqIndic != 1 or self.cantEstructuras != 2:
                    painter.setPen(QtGui.QPen(QtGui.QColorConstants.Black,5))
                    painter.drawLine(estX,estY+60,estX+anchoEstructura,estY+60) 
                    painter.drawText(estX-((int(len(str(self.resTabla[4][2])))*6))-12,estY+60,str(self.resTabla[4][2]))
                    painter.setPen(QtGui.QPen(QtGui.QColorConstants.Black,3))
                    painter.drawLine(estX,estY+50,estX+anchoEstructura,estY+50)
                    #bordeInferior
                    painter.setPen(QtGui.QPen(QtGui.QColorConstants.Black,5))
                    painter.drawLine(estX,estY+(altoCanvas-(2*borde)-(diffEstructura))-60,estX+anchoEstructura,estY+(altoCanvas-(2*borde)-(diffEstructura))-60)
                    painter.drawText(estX-((int(len(str(int(self.resTabla[3][2])-int(self.resTabla[4][2]))))*6))-12,estY+(altoCanvas-(2*borde)-(diffEstructura))-60,str(int(self.resTabla[3][2])-int(self.resTabla[4][2]))) 
                    painter.setPen(QtGui.QPen(QtGui.QColorConstants.Black,3))
                    painter.drawText(estX+(anchoEstructura//2),estY+(altoCanvas-(2*borde)-(diffEstructura))-30,"B"+self.resTabla[5][2])
                painter.drawLine(estX,estY+(altoCanvas-(2*borde)-(diffEstructura))-10,estX+anchoEstructura,estY+(altoCanvas-(2*borde)-diffEstructura)-10)
                painter.drawLine(estX+anchoEstructura,estY+5,estX+anchoEstructura+separacion,estY+15)
                painter.drawLine(estX+anchoEstructura,estY+(altoCanvas-(2*borde)-(diffEstructura))-5,estX+anchoEstructura+separacion,estY+(altoCanvas-(2*borde)-(diffEstructura))-15)
                painter.drawText(estX-((int(len(str(self.resTabla[3][2])))*6))-12,estY+(altoCanvas-(2*borde)-(diffEstructura))-3,self.resTabla[3][2])
            elif(self.Tipo == "Secundario"):
                estX = (anchoCanvas-borde-(2*anchoEstructura)-separacion)
                estY = borde
                painter.drawText(estX+(anchoEstructura//2),estY-20,"Est. Indice")
                painter.drawRect(estX,estY,anchoEstructura,altoCanvas-(2*borde))
                #bordeSuperior
                painter.drawLine(estX,estY+10,estX+anchoEstructura,estY+10)
                painter.drawText(estX-10,estY+7,"1")
                painter.drawText(estX+(anchoEstructura//2),estY+35,"B1")
                if self.cantBloqIndic!=1 or self.cantEstructuras != 2:
                    painter.setPen(QtGui.QPen(QtGui.QColorConstants.Black,5))
                    painter.drawLine(estX,estY+60,estX+anchoEstructura,estY+60) 
                    painter.drawText(estX-((int(len(str(self.resTabla[4][2])))*6))-12,estY+60,str(self.resTabla[4][2])) 
                    painter.setPen(QtGui.QPen(QtGui.QColorConstants.Black,3))
                    painter.drawLine(estX,estY+50,estX+anchoEstructura,estY+50)
                    #bordeInferior
                    painter.setPen(QtGui.QPen(QtGui.QColorConstants.Black,5))
                    painter.drawLine(estX,estY+(altoCanvas-(2*borde))-60,estX+anchoEstructura,estY+(altoCanvas-(2*borde))-60) 
                    painter.drawText(estX-((int(len(str(int(self.resTabla[3][2])-int(self.resTabla[4][2]))))*6))-12,estY+(altoCanvas-(2*borde))-60,str(int(self.resTabla[3][2])-int(self.resTabla[4][2])))
                    painter.setPen(QtGui.QPen(QtGui.QColorConstants.Black,3))
                    painter.drawText(estX+(anchoEstructura//2),estY+(altoCanvas-(2*borde))-30,"B"+self.resTabla[5][2])
                painter.drawLine(estX,estY+(altoCanvas-(2*borde))-10,estX+anchoEstructura,estY+(altoCanvas-(2*borde))-10)
                painter.drawLine(estX+anchoEstructura,estY+5,estX+anchoEstructura+separacion,estY+5)
                painter.drawLine(estX+anchoEstructura,estY+(altoCanvas-(2*borde))-5,estX+anchoEstructura+separacion,estY+(altoCanvas-(2*borde))-5)
                painter.drawText(estX-((int(len(str(self.resTabla[3][2])))*6))-12,estY+(altoCanvas-(2*borde))-3,self.resTabla[3][2])
            #creacion de las estructuras indices de multinivel
            if(self.cantNivel == "Multinivel"):
                row = 3
                for i in range(2,self.cantEstructuras):
                    estX = (anchoCanvas-borde-(row*anchoEstructura)-((row-1)*separacion))
                    estY = borde+(((row-1)*diffEstructura)//2) if altoCanvas-(2*borde)-((row-1)*diffEstructura) > 160 else 170
                    altura = altoCanvas-(2*borde)-((row-1)*diffEstructura) if altoCanvas-(2*borde)-((row-1)*diffEstructura) > 160 else 160
                    inclinacion = 15 if altoCanvas-(2*borde)-((row-1)*diffEstructura) > 160 else 25
                    painter.drawText(estX+(anchoEstructura//2),estY-20,"Est. Indice "+str(row-1))
                    painter.drawRect(estX,estY,anchoEstructura,altura)
                    #bordeSuperior
                    painter.drawLine(estX,estY+10,estX+anchoEstructura,estY+10)
                    painter.drawText(estX-15,estY+7,"1")
                    painter.drawText(estX+(anchoEstructura//2),estY+35,"B1")
                    if row!=self.cantEstructuras:
                        painter.setPen(QtGui.QPen(QtGui.QColorConstants.Black,5))
                        painter.drawLine(estX,estY+60,estX+anchoEstructura,estY+60)
                        painter.drawText(estX-((int(len(str(self.resTabla[(3*row)-2][2])))*6))-12,estY+60,str(self.resTabla[(3*row)-2][2])) 
                        painter.setPen(QtGui.QPen(QtGui.QColorConstants.Black,3))
                        painter.drawLine(estX,estY+50,estX+anchoEstructura,estY+50)
                        #bordeInferior
                        painter.setPen(QtGui.QPen(QtGui.QColorConstants.Black,5))
                        painter.drawLine(estX,estY+(altura)-60,estX+anchoEstructura,estY+(altura)-60) 
                        dato = int(self.resTabla[(3*row)-3][2])-int(self.resTabla[(3*row)-2][2])
                        dato = dato if dato >= int(self.resTabla[(3*row)-2][2]) else int(self.resTabla[(3*row)-2][2]) + 1
                        painter.drawText(estX-((int(len(str(dato)))*6))-12,estY+(altura)-60,str(dato)) 
                        painter.setPen(QtGui.QPen(QtGui.QColorConstants.Black,3))
                        painter.drawText(estX+(anchoEstructura//2),estY+(altura)-30,"B"+self.resTabla[(3*row)-1][2])
                    painter.drawLine(estX,estY+(altura)-10,estX+anchoEstructura,estY+(altura)-10)
                    painter.drawLine(estX+anchoEstructura,estY+5,estX+anchoEstructura+separacion,estY+inclinacion)
                    painter.drawLine(estX+anchoEstructura,estY+(altura)-5,estX+anchoEstructura+separacion,estY+(altura)-inclinacion)
                    painter.drawText(estX-((int(len(str(self.resTabla[(3*row)-3][2])))*6))-12,estY+(altura)-3,self.resTabla[(3*row)-3][2])
                    row += 1

        painter.end()

