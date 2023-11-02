import sys
from PyQt5 import QtWidgets as QtW
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtGui

from indicesCanvas import indiceCanvas

class IndicesView(QtW.QGroupBox):

    def generarGrafica(self):
        try:
            self.tabla.setRowCount(0)
            tablaRes = self.canvas.dibujarGrafico(self.opcionTipoIndice.currentText(),self.opcionNiveles.currentText(),int(self.campoTamBloque.toPlainText()),int(self.campoCantReg.toPlainText()),int(self.campoTamReg.toPlainText()),int(self.campoTamRegIn.toPlainText()))
            row = 0
            for i in tablaRes:
                self.tabla.insertRow(row)
                for column in range(len(i)):
                    self.tabla.setItem(row,column,QtW.QTableWidgetItem(tablaRes[row][column]))
                row += 1
        except:
            error = QtW.QMessageBox(self)
            error.setIcon(QtW.QMessageBox.Icon.Warning)
            error.setText("Datos Mal Ingresados")
            error.exec_()


    def __init__(self,p:QWidget):
        super().__init__(p)

        self.canvas = indiceCanvas(None)
        self.canvas.setGeometry (0,0,720,500)
        self.canvas.setStyleSheet("background-color:#EBE6D2")

        self.ventanaCanvas = QtW.QScrollArea(self)
        self.ventanaCanvas.setGeometry(40,20,722,502)
        self.ventanaCanvas.setWidget(self.canvas)
        self.ventanaCanvas.verticalScrollBar().setVisible(False)
        self.ventanaCanvas.verticalScrollBar().setEnabled(False)
        self.ventanaCanvas.setStyleSheet("background-color:#EBE6D2")
        self.ventanaCanvas.setFrameStyle(1)


        self.setStyleSheet("background-color:#DECCA6")

        self.tabla = QtW.QTableWidget(self)
        self.tabla.setColumnCount(3)
        self.tabla.verticalHeader().setVisible(False)
        self.tabla.setHorizontalHeaderLabels(["N. Est","Variable","Valor"])
        self.tabla.setGeometry(775,20,290,500)
        self.tabla.setFont(QFont("Arial",7))
        self.tabla.horizontalScrollBar().setVisible(False)
        self.tabla.setColumnWidth(0,30)
        self.tabla.setColumnWidth(1,130)
        self.tabla.setColumnWidth(2,120)
        self.tabla.setStyleSheet("QTableWidget{border:1px solid black; background-color:#EBE6D2}")

        #seccion de entradas
        label = QtW.QLabel("Tipo de Indice",self)
        label.move(120,565)
        label.setFont(QFont("Arial",9,QFont.Bold))
        self.opcionTipoIndice = QtW.QComboBox(self)
        self.opcionTipoIndice.addItems(["Primario","Secundario"])
        self.opcionTipoIndice.move(240,560)
        self.opcionTipoIndice.resize(120,30)
        self.opcionTipoIndice.setFont(QFont("Arial",9,QFont.Bold))
        self.opcionTipoIndice.setStyleSheet("background-color:#EBE6D2")

        label = QtW.QLabel("Cantidad de Niveles",self)
        label.move(380,565)
        label.setFont(QFont("Arial",9,QFont.Bold))
        self.opcionNiveles = QtW.QComboBox(self)
        self.opcionNiveles.addItems(["Un Nivel","Multinivel"])
        self.opcionNiveles.move(540,560)
        self.opcionNiveles.resize(120,30)
        self.opcionNiveles.setFont(QFont("Arial",9,QFont.Bold))
        self.opcionNiveles.setStyleSheet("background-color:#EBE6D2")

        label = QtW.QLabel("Tamaño Bloque (b)",self)
        label.move(680,565)
        label.setFont(QFont("Arial",9,QFont.Bold))
        self.campoTamBloque = QtW.QTextEdit(self)
        self.campoTamBloque.setFrameStyle(1)
        self.campoTamBloque.move(840,560)
        self.campoTamBloque.resize(140,30)
        self.campoTamBloque.setFont(QFont("Arial",9))
        self.campoTamBloque.setStyleSheet("background-color:#EBE6D2")

        label = QtW.QLabel("Cant. Registros",self)
        label.move(120,605)
        label.setFont(QFont("Arial",9,QFont.Bold))
        self.campoCantReg = QtW.QTextEdit(self)
        self.campoCantReg.setFrameStyle(1)
        self.campoCantReg.move(240,600)
        self.campoCantReg.resize(140,30)
        self.campoCantReg.setFont(QFont("Arial",9))
        self.campoCantReg.setStyleSheet("background-color:#EBE6D2")

        label = QtW.QLabel("Tamaño Registro (b)",self)
        label.move(380,605)
        label.setFont(QFont("Arial",9,QFont.Bold))
        self.campoTamReg = QtW.QTextEdit(self)
        self.campoTamReg.setFrameStyle(1)
        self.campoTamReg.move(540,600)
        self.campoTamReg.resize(140,30)
        self.campoTamReg.setFont(QFont("Arial",9))
        self.campoTamReg.setStyleSheet("background-color:#EBE6D2")

        label = QtW.QLabel("Tamaño Regi. Indice (b)",self)
        label.move(680,605)
        label.setFont(QFont("Arial",9,QFont.Bold))
        self.campoTamRegIn = QtW.QTextEdit(self)
        self.campoTamRegIn.setFrameStyle(1)
        self.campoTamRegIn.move(870,600)
        self.campoTamRegIn.resize(140,30)
        self.campoTamRegIn.setFont(QFont("Arial",9))
        self.campoTamRegIn.setStyleSheet("background-color:#EBE6D2")

        botonGenerar = QtW.QPushButton("Generar",self)
        botonGenerar.setGeometry(520,650,120,30)
        botonGenerar.setStyleSheet("QPushButton{background-color:#b0c9bb; border:1px solid black;}"
                                        "QPushButton::hover{background-color :#8fa89a;}"
                                        "QPushButton::pressed{background-color:#6e8679; }")
        botonGenerar.clicked.connect(self.generarGrafica)

        self.campoCantReg.setText("700000")
        self.campoTamBloque.setText("1024")
        self.campoTamRegIn.setText("12")
        self.campoTamReg.setText("20")

    


        


        
        
        



   

    
