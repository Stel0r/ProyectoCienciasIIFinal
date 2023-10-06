from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from BusquedasInView.Estructuras.EstructuraInterna import EstructuraInterna

class BusquedasInView(QGroupBox):
    def __init__(self, p:QWidget):
        super().__init__(p)

        #variables logicas
        self.estructura:EstructuraInterna = None

        self.tabla = QTableWidget(self)
        self.tabla.setColumnCount(1)
        self.tabla.setHorizontalHeaderLabels(["Valor"])
        self.tabla.setGeometry(880, 20, 170, 650)
        self.tabla.horizontalScrollBar().setVisible(False)
        self.tabla.setColumnWidth(0, 170)

        panelEstructura = QGroupBox(self)
        panelEstructura.setGeometry(10,20,860,420)
        panelEstructura.setStyleSheet("QGroupBox{border:1px solid black}")

        label = QLabel("Creacion Estructura",panelEstructura)
        label.move(20,10)

        #seccion de entradas
        label = QLabel("Tipo de Busqueda",self)
        label.move(35,65)
        label.setFont(QFont("Arial",9,QFont.Bold))
        self.opcionTipoIndice = QComboBox(self)
        self.opcionTipoIndice.addItems(["Secuencial","Binaria"])
        self.opcionTipoIndice.move(150,60)
        self.opcionTipoIndice.resize(120,30)
        self.opcionTipoIndice.setFont(QFont("Arial",9,QFont.Bold))

        label = QLabel("Rango",self)
        label.move(295,65)
        label.setFont(QFont("Arial",9,QFont.Bold))
        self.campoTamBloque = QTextEdit(self)
        self.campoTamBloque.setFrameStyle(1)
        self.campoTamBloque.move(340,60)
        self.campoTamBloque.resize(80,30)
        self.campoTamBloque.setFont(QFont("Arial",9))

        