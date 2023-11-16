from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from BusquedasInView.Estructuras.Binario import Binario

from BusquedasInView.Estructuras.EstructuraInterna import EstructuraInterna
from BusquedasInView.Estructuras.Secuencial import Secuencial

class BusquedasInView(QGroupBox):
    def __init__(self, p:QWidget):
        super().__init__(p)

        #variables logicas
        self.estructura:EstructuraInterna = None
        self.datoBuscado : int = None

        self.setStyleSheet("background-color:#DECCA6")

        self.tabla = QTableWidget(self)
        self.tabla.setColumnCount(1)
        self.tabla.setHorizontalHeaderLabels(["Clave"])
        self.tabla.setFont(QFont("Arial",12,QFont.Bold))
        self.tabla.setGeometry(1100, 20, 220, 850)
        self.tabla.horizontalScrollBar().setVisible(False)
        self.tabla.setColumnWidth(0, 200)
        self.tabla.setStyleSheet("QTableWidget{border:1px solid black; background-color:#EBE6D2}")

        panelEstructura = QGroupBox(self)
        panelEstructura.setGeometry(10,20,1060,320)
        panelEstructura.setStyleSheet("QGroupBox{border:1px solid black}")

        label = QLabel("Creacion Estructura",panelEstructura)
        label.setFont(QFont("Arial",12,QFont.Bold))
        label.move(120,60)

        #seccion de entradas
        label = QLabel("Tipo de Busqueda",self)
        label.move(80,125)
        label.setFont(QFont("Arial",12,QFont.Bold))
        self.opcionTipoBusq = QComboBox(self)
        self.opcionTipoBusq.addItems(["Secuencial","Binaria"])
        self.opcionTipoBusq.move(235,120)
        self.opcionTipoBusq.resize(120,30)
        self.opcionTipoBusq.setFont(QFont("Arial",12,QFont.Bold))
        self.opcionTipoBusq.setStyleSheet("background-color:#EBE6D2")

        label = QLabel("Rango",self)
        label.move(385,125)
        label.setFont(QFont("Arial",12,QFont.Bold))
        self.campoRango = QTextEdit(self)
        self.campoRango.setFrameStyle(1)
        self.campoRango.move(450,120)
        self.campoRango.resize(80,30)
        self.campoRango.setFont(QFont("Arial",12))
        self.campoRango.setStyleSheet("background-color:#EBE6D2")

        label = QLabel("Digitos Clave",self)
        label.move(555,125)
        label.setFont(QFont("Arial",12,QFont.Bold))
        self.campoDigitos = QTextEdit(self)
        self.campoDigitos.setFrameStyle(1)
        self.campoDigitos.move(665,120)
        self.campoDigitos.resize(80,30)
        self.campoDigitos.setFont(QFont("Arial",12))
        self.campoDigitos.setStyleSheet("background-color:#EBE6D2")

        botonGenerar = QPushButton("Generar",panelEstructura)
        botonGenerar.setGeometry(780,100,120,30)
        botonGenerar.setFont(QFont("Arial",12))
        botonGenerar.setStyleSheet("QPushButton{background-color:#b0c9bb; border:1px solid black;}"
                                        "QPushButton::hover{background-color :#8fa89a;}"
                                        "QPushButton::pressed{background-color:#6e8679; }")
        botonGenerar.setCursor(QCursor(Qt.PointingHandCursor))
        botonGenerar.clicked.connect(self.GenerarEstructura)
        
        self.labelTitIng = QLabel("Ingresar/Buscar",panelEstructura)
        self.labelTitIng.move(120,160)
        self.labelTitIng.setFont(QFont("Arial",12,QFont.Bold))
        self.labelTitIng.setVisible(False)
        
        self.labelCampResNum = QLabel("Clave Numerica",panelEstructura)
        self.labelCampResNum.move(200,205)
        self.labelCampResNum.setFont(QFont("Arial",12,QFont.Bold))
        self.labelCampResNum.setVisible(False)
        self.campoCampResNum = QTextEdit(self)
        self.campoCampResNum.setFrameStyle(1)
        self.campoCampResNum.move(350,220)
        self.campoCampResNum.resize(80,30)
        self.campoCampResNum.setFont(QFont("Arial",12))
        self.campoCampResNum.setVisible(False)
        self.campoCampResNum.setStyleSheet("background-color:#EBE6D2")

        self.botonIngresar = QPushButton("Ingresar",panelEstructura)
        self.botonIngresar.setGeometry(480,200,120,30)
        self.botonIngresar.setStyleSheet("QPushButton{background-color:#b0c9bb; border:1px solid black;}"
                                        "QPushButton::hover{background-color :#8fa89a;}"
                                        "QPushButton::pressed{background-color:#6e8679; }")
        self.botonIngresar.setCursor(QCursor(Qt.PointingHandCursor))
        self.botonIngresar.clicked.connect(self.ingresarDato)
        self.botonIngresar.setFont(QFont("Arial",12))
        self.botonIngresar.setVisible(False)
        
        
        self.botonBuscar = QPushButton("Buscar",panelEstructura)
        self.botonBuscar.setGeometry(610,200,120,30)
        self.botonBuscar.setStyleSheet("QPushButton{background-color:#b0c9bb; border:1px solid black;}"
                                        "QPushButton::hover{background-color :#8fa89a;}"
                                        "QPushButton::pressed{background-color:#6e8679; }")
        self.botonBuscar.setCursor(QCursor(Qt.PointingHandCursor))
        self.botonBuscar.setFont(QFont("Arial",12))
        self.botonBuscar.clicked.connect(self.buscarDato)
        self.botonBuscar.setVisible(False)

        #Consola de salida

        self.registroProcess = QTextEdit(self)
        self.registroProcess.setFrameStyle(1)
        self.registroProcess.setGeometry(10, 350,1060, 520)
        self.registroProcess.setReadOnly(True)
        self.registroProcess.setFont(QFont("Arial", 16))
        self.registroProcess.setStyleSheet("QTextEdit{border:1px solid black; background-color:#D0C0A7}")

        
    def GenerarEstructura(self):
        try:
            if self.estructura != None:
                matriz = self.estructura.matriz
            else:
                matriz = []
            if(self.opcionTipoBusq.currentText() == "Secuencial"):
                self.estructura = Secuencial(matriz,int(self.campoRango.toPlainText()),int(self.campoDigitos.toPlainText()))
            elif(self.opcionTipoBusq.currentText() == "Binaria"):
                self.estructura = Binario(matriz,int(self.campoRango.toPlainText()),int(self.campoDigitos.toPlainText()))
            self.tabla.setRowCount(0)
            for x in range(int(self.campoRango.toPlainText())):
                self.tabla.insertRow(x)
            self.labelTitIng.setVisible(True)
            self.labelCampResNum.setVisible(True)
            self.campoCampResNum.setVisible(True)
            self.botonIngresar.setVisible(True)
            self.botonBuscar.setVisible(True)
            self.imprimirTexto("Se ha creado la estructura exitosamente")
            self.refrescarTabla()
        except Exception as e:
            error = QMessageBox()
            error.setText("Los datos no son validos, deben ser Numericos")
            error.setIcon(QMessageBox.Icon.Critical)
            print(e)
            error.exec()

    def deshabilitar(self):
        self.tabla.setRowCount(0)
        self.GenerarEstructura()
        self.refrescarTabla()

    def imprimirTexto(self,texto:str):
        self.registroProcess.setText(self.registroProcess.toPlainText()+"\n >"+texto)

    def ingresarDato(self):
        try:
            res = self.estructura.ingresarDato(int(self.campoCampResNum.toPlainText()))
            self.imprimirTexto(res)
            self.refrescarTabla()
        except Exception as e:
            error = QMessageBox()
            error.setText("La clave debe ser Numerica")
            error.setIcon(QMessageBox.Icon.Critical)
            print(e)
            error.exec()
    

    def buscarDato(self):
        try:
            res = self.estructura.busqueda(int(self.campoCampResNum.toPlainText()))
            self.imprimirTexto(res)
            self.datoBuscado = int(self.campoCampResNum.toPlainText())
            self.refrescarTabla()
        except Exception as e:
            error = QMessageBox()
            error.setText("la clave debe ser Numerico")
            error.setIcon(QMessageBox.Icon.Critical)
            print(e)
            error.exec()
    
    def refrescarTabla(self):
        for i in range(len(self.estructura.matriz)):
            itemTabla = QTableWidgetItem(("0"*(self.estructura.digitos - len(str(self.estructura.matriz[i]))))+str(self.estructura.matriz[i]))
            if (self.estructura.matriz[i] == self.datoBuscado):
                print("cambiando color")
                itemTabla.setBackground(QColorConstants.Green)
            self.tabla.setItem(i,0,itemTabla)
        self.datoBuscado = None