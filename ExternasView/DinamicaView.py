import sys
from PyQt5 import QtWidgets as QtW
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtGui

from ExternasView.FuncionesHash import TransfClaves
from ExternasView import BinariaSecuencial as BS


class DinamicaView(QtW.QGroupBox):

    def __init__(self, p: QWidget):
        
        super().__init__(p)

        self.rango = None
        self.listaDatos = []
        self.registros = []
        self.cubetas = 0
        self.hash = None

        self.setStyleSheet("background-color:#DECCA6")

        label = QtW.QLabel("Lista de datos:", self)
        label.move(550, 240)
        label.setFont(QFont("Arial", 10, QFont.Bold))
        self.tabla = QtW.QTableWidget(self)
        self.tabla.setColumnCount(2)
        self.tabla.setHorizontalHeaderLabels(["Número", "Registro"])
        self.tabla.setGeometry(550, 280, 500, 390)
        self.tabla.horizontalScrollBar().setVisible(False)
        self.tabla.setColumnWidth(0, 100)
        self.tabla.setColumnWidth(1, 100)
        self.tabla.verticalHeader().setVisible(False)
        self.tabla.setStyleSheet("QTableWidget{border:1px solid black; background-color:#EBE6D2}")

        self.tablaBloques = QtW.QTableWidget(self)
        self.tablaBloques.setColumnCount(self.cubetas)
        self.tablaBloques.setGeometry(20, 20, 1030, 200)
        self.tablaBloques.horizontalScrollBar().setVisible(True)
        self.tablaBloques.verticalHeader().setVisible(False)
        self.tablaBloques.setStyleSheet("QTableWidget{border:1px solid black; background-color:#EBE6D2}")

        label = QtW.QLabel("Número de cubetas:", self)
        label.move(20, 240)
        label.setFont(QFont("Arial", 10, QFont.Bold))
        self.numcubeta = QtW.QTextEdit(self)
        self.numcubeta.setFrameStyle(1)
        self.numcubeta.move(20, 260)
        self.numcubeta.resize(140, 30)
        self.numcubeta.setFont(QFont("Arial", 10))
        self.numcubeta.setStyleSheet("background-color:#EBE6D2")

        label = QtW.QLabel("Número de registros:", self)
        label.move(180, 240)
        label.setFont(QFont("Arial", 10, QFont.Bold))
        self.numregistro = QtW.QTextEdit(self)
        self.numregistro.setFrameStyle(1)
        self.numregistro.move(180, 260)
        self.numregistro.resize(140, 30)
        self.numregistro.setFont(QFont("Arial", 10))
        self.numregistro.setStyleSheet("background-color:#EBE6D2")

        label = QtW.QLabel("Ingresar clave:", self)
        label.move(20, 300)
        label.setFont(QFont("Arial", 10, QFont.Bold))
        self.ingresoDato = QtW.QTextEdit(self)
        self.ingresoDato.setFrameStyle(1)
        self.ingresoDato.move(20, 320)
        self.ingresoDato.resize(140, 30)
        self.ingresoDato.setFont(QFont("Arial", 10))
        self.ingresoDato.setStyleSheet("background-color:#EBE6D2")

        self.labelSuccess = QtW.QLabel("Proceso: ", self)
        self.labelSuccess.move(20, 390)
        self.labelSuccess.setFont(QFont("Arial", 10, QFont.Bold))
        self.labelSuccess.resize(400, 30)

        self.registroProcess = QtW.QTextEdit(self)
        self.registroProcess.setFrameStyle(1)
        self.registroProcess.move(20, 420)
        self.registroProcess.resize(500, 200)
        self.registroProcess.setReadOnly(True)
        self.registroProcess.setFont(QFont("Arial", 10))
        self.registroProcess.setStyleSheet("QTextEdit{border:1px solid black; background-color:#D0C0A7}")

        self.bnEstructura = QtW.QPushButton("Crear estructura", self)
        self.bnEstructura.setGeometry(340, 260, 130, 30)
        self.bnEstructura.setStyleSheet("QPushButton{background-color:#b0c9bb; border:1px solid black;}"
                                        "QPushButton::hover{background-color :#8fa89a;}"
                                        "QPushButton::pressed{background-color:#6e8679; }")
        #self.bnEstructura.clicked.connect(self.testEstructure)

        self.bnIngresar = QtW.QPushButton("Agregar clave", self)
        self.bnIngresar.setGeometry(180, 320, 130, 30)
        self.bnIngresar.setStyleSheet("QPushButton{background-color:#b0c9bb; border:1px solid black;}"
                                        "QPushButton::hover{background-color :#8fa89a;}"
                                        "QPushButton::pressed{background-color:#6e8679; }")
        #self.bnIngresar.clicked.connect(self.ingresarDato)
        self.bnIngresar.setEnabled(False)

        self.bnTerminar = QtW.QPushButton("Eliminar clave", self)
        self.bnTerminar.setGeometry(320, 320, 130, 30)
        self.bnTerminar.setStyleSheet("QPushButton{background-color:#b0c9bb; border:1px solid black;}"
                                        "QPushButton::hover{background-color :#8fa89a;}"
                                        "QPushButton::pressed{background-color:#6e8679; }")
        #self.bnTerminar.clicked.connect()
        self.bnTerminar.setEnabled(False)

        self.bnReiniciar = QtW.QPushButton("Reiniciar", self)
        self.bnReiniciar.setGeometry(20, 640, 500, 30)
        self.bnReiniciar.setStyleSheet("QPushButton{background-color:#D7A184; border:1px solid black;}"
                                   "QPushButton::hover{background-color :#D4C2AD;}"
                                   "QPushButton::pressed{background-color:#EFDFCC; }")
        #self.bnReiniciar.clicked.connect(self.reiniciar)
        self.bnReiniciar.setEnabled(False)
