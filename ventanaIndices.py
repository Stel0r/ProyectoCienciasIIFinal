import sys
from PyQt5 import QtWidgets as QtW
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtGui

from indicesCanvas import indiceCanvas

class IndicesView(QtW.QGroupBox):

    def generarGrafica():
        self.canvas

    def __init__(self,p:QWidget):
        super().__init__(p)
        self.canvas = indiceCanvas(self)
        self.canvas.setGeometry (40,20,720,500)
        
        self.setStyleSheet("background-color:white")

        self.tabla = QtW.QTableWidget(self)
        self.tabla.setColumnCount(3)
        self.tabla.setHorizontalHeaderLabels(["N. Estr","Var","Valor"])
        self.tabla.setGeometry(780,20,270,500)
        self.tabla.horizontalScrollBar().setVisible(False)
        self.tabla.setColumnWidth(0,70)
        self.tabla.setColumnWidth(1,100)
        self.tabla.setColumnWidth(2,100)

        #seccion de entradas
        label = QtW.QLabel("Tipo de Indice",self)
        label.move(120,565)
        label.setFont(QFont("Arial",10,QFont.Bold))
        opcionTipoIndice = QtW.QComboBox(self)
        opcionTipoIndice.addItems(["Primario","Secundario"])
        opcionTipoIndice.move(220,560)
        opcionTipoIndice.resize(120,30)
        opcionTipoIndice.setFont(QFont("Arial",10,QFont.Bold))

        label = QtW.QLabel("Cantidad de Niveles",self)
        label.move(380,565)
        label.setFont(QFont("Arial",10,QFont.Bold))
        opcionNiveles = QtW.QComboBox(self)
        opcionNiveles.addItems(["Un Nivel","Multinivel"])
        opcionNiveles.move(520,560)
        opcionNiveles.resize(120,30)
        opcionNiveles.setFont(QFont("Arial",10,QFont.Bold))

        label = QtW.QLabel("Tamaño Bloque (kb)",self)
        label.move(680,565)
        label.setFont(QFont("Arial",10,QFont.Bold))
        campoTamBloque = QtW.QTextEdit(self)
        campoTamBloque.setFrameStyle(1)
        campoTamBloque.move(820,560)
        campoTamBloque.resize(140,30)
        campoTamBloque.setFont(QFont("Arial",10))

        label = QtW.QLabel("Cant. Registros",self)
        label.move(120,605)
        label.setFont(QFont("Arial",10,QFont.Bold))
        campoCantReg = QtW.QTextEdit(self)
        campoCantReg.setFrameStyle(1)
        campoCantReg.move(220,600)
        campoCantReg.resize(140,30)
        campoCantReg.setFont(QFont("Arial",10))

        label = QtW.QLabel("Tamaño Registro (Kb)",self)
        label.move(380,605)
        label.setFont(QFont("Arial",10,QFont.Bold))
        campoTamReg = QtW.QTextEdit(self)
        campoTamReg.setFrameStyle(1)
        campoTamReg.move(520,600)
        campoTamReg.resize(140,30)
        campoTamReg.setFont(QFont("Arial",10))

        label = QtW.QLabel("Tamaño Reg. Indice (Kb)",self)
        label.move(680,605)
        label.setFont(QFont("Arial",10,QFont.Bold))
        campoTamReg = QtW.QTextEdit(self)
        campoTamReg.setFrameStyle(1)
        campoTamReg.move(850,600)
        campoTamReg.resize(140,30)
        campoTamReg.setFont(QFont("Arial",10))

        botonGenerar = QtW.QPushButton("Generar",self)
        botonGenerar.setGeometry(520,650,120,30)
        botonGenerar.setStyleSheet("QPushButton{background-color:#a4c3f5; border:1px solid black;}"
                                   "QPushButton::hover{background-color :#80a7e8;}"
                                   "QPushButton::pressed{background-color:#7499d6; }")
        botonGenerar.clicked.connect = generarGrafica

    


        


        
        
        



   

    
