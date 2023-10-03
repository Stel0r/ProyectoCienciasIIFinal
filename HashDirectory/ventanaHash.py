import sys
from PyQt5 import QtWidgets as QtW
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtGui

from HashDirectory.Hash import TransfClaves

class HashView(QtW.QGroupBox):

    def __init__(self, p: QWidget):
        super().__init__(p)

        self.hash = None

        self.setStyleSheet("background-color:white")

        self.tabla = QtW.QTableWidget(self)
        self.tabla.setColumnCount(2)
        self.tabla.setHorizontalHeaderLabels(["Clave", "Valor"])
        self.tabla.setGeometry(780, 20, 270, 500)
        self.tabla.horizontalScrollBar().setVisible(False)
        self.tabla.setColumnWidth(0, 135)
        self.tabla.setColumnWidth(1, 135)
        self.tabla.verticalHeader().setVisible(False)

        # seccion de entradas
        label = QtW.QLabel("Metodo hash", self)
        label.move(10, 10)
        label.setFont(QFont("Arial", 10, QFont.Bold))
        self.opcionMetodoHash = QtW.QComboBox(self)
        self.opcionMetodoHash.addItems(["Mod", "Cuadratico", "Plegamiento", "Truncamiento"])
        self.opcionMetodoHash.move(10, 40)
        self.opcionMetodoHash.resize(150, 30)
        self.opcionMetodoHash.setFont(QFont("Arial", 10, QFont.Bold))

        label = QtW.QLabel("Metodo Solucion de Colisiones", self)
        label.move(190, 10)
        label.setFont(QFont("Arial", 10, QFont.Bold))
        self.opcionSolColision = QtW.QComboBox(self)
        self.opcionSolColision.addItems(["Lineal", "Cuadratico", "Doble Hash"])
        self.opcionSolColision.move(190, 40)
        self.opcionSolColision.resize(150, 30)
        self.opcionSolColision.setFont(QFont("Arial", 10, QFont.Bold))

        label = QtW.QLabel("Tamaño Estructura", self)
        label.move(400, 10)
        label.setFont(QFont("Arial", 10, QFont.Bold))
        self.tamanoEstructura = QtW.QTextEdit(self)
        self.tamanoEstructura.setFrameStyle(1)
        self.tamanoEstructura.move(400, 40)
        self.tamanoEstructura.resize(140, 30)
        self.tamanoEstructura.setFont(QFont("Arial", 10))

        label = QtW.QLabel("Ingresar Dato", self)
        label.move(10, 100)
        label.setFont(QFont("Arial", 10, QFont.Bold))
        self.ingresoDato = QtW.QTextEdit(self)
        self.ingresoDato.setFrameStyle(1)
        self.ingresoDato.move(10, 140)
        self.ingresoDato.resize(200, 30)
        self.ingresoDato.setFont(QFont("Arial", 10))

        self.labelWarning = QtW.QLabel("Error: ", self)
        self.labelWarning.move(10, 300)
        self.labelWarning.setFont(QFont("Arial", 10, QFont.Bold))
        self.labelWarning.resize(400, 30)
        self.labelWarning.setStyleSheet("color:red")

        self.labelSuccess = QtW.QLabel("Success: ", self)
        self.labelSuccess.move(10, 330)
        self.labelSuccess.setFont(QFont("Arial", 10, QFont.Bold))
        self.labelSuccess.resize(400, 30)
        self.labelSuccess.setStyleSheet("color:green")

        self.registroProcess = QtW.QTextEdit(self)
        self.registroProcess.setFrameStyle(1)
        self.registroProcess.move(10, 370)
        self.registroProcess.resize(700, 300)
        self.registroProcess.setReadOnly(True)
        self.registroProcess.setFont(QFont("Arial", 10))

        self.bnEstructura = QtW.QPushButton("Definir Estructura", self)
        self.bnEstructura.setGeometry(570, 40, 170, 30)
        self.bnEstructura.setStyleSheet("QPushButton{background-color:#a4c3f5; border:1px solid black;}"
                                        "QPushButton::hover{background-color :#80a7e8;}"
                                        "QPushButton::pressed{background-color:#7499d6; }")
        self.bnEstructura.clicked.connect(self.testEstructure)

        self.bnIngresar = QtW.QPushButton("Agregar", self)
        self.bnIngresar.setGeometry(220, 140, 170, 30)
        self.bnIngresar.setStyleSheet("QPushButton{background-color:#a4c3a5; border:1px solid black;}"
                                      "QPushButton::hover{background-color :#80a7e8;}"
                                      "QPushButton::pressed{background-color:#7499d6; }")
        self.bnIngresar.clicked.connect(self.ingresarDato)

    def testEstructure(self):
        t = 0
        try:
            if(self.tamanoEstructura.toPlainText() != ''):
                t = int(self.tamanoEstructura.toPlainText())
            if(t <= 0):
                self.errWarning("Por Favor ingrese un tamaño mayor a 0")
                return
        except:
            self.errWarning("Ingreso para tamaño caracteres no numericos")
            return

        self.hash = TransfClaves(self.opcionMetodoHash.currentText(), t, self.opcionSolColision.currentText())
        self.processSuccess("Estructura definida")
        self.errWarning("")

    def ingresarDato(self):
        d = 0
        if self.hash is None:
            self.errWarning("Estructura no definida")
            return
        try:
            if(self.ingresoDato.toPlainText() != ''):
                d = int(self.ingresoDato.toPlainText())
            if(d <= 0):
                self.errWarning("Por Favor ingrese un dato mayor a 0")
                return
        except:
            self.errWarning("Ingreso para dato caracteres no numericos")
            return

        self.hash.ingresarValor(d)
        self.processSuccess("Dato Ingresado (" + str(d) + ")")
        self.errWarning("")
        self.mostrarTabla()
        self.registrarProceso()
    def errWarning(self, mensaje):
        self.labelWarning.setText("Error: " + mensaje)

    def processSuccess(self, mensaje):
        self.labelSuccess.setText("Success: " + mensaje)

    def mostrarTabla(self):
        self.tabla.setRowCount(0)
        fila = 0
        for i in self.hash.estructura:
            self.tabla.insertRow(fila)
            self.tabla.setItem(fila, 0, QtW.QTableWidgetItem(str(i)))
            self.tabla.setItem(fila, 1, QtW.QTableWidgetItem(str(self.hash.estructura[i])))
            fila+=1

    def registrarProceso(self):
        if self.hash.mError != "":
            self.registroProcess.setText(self.registroProcess.toPlainText() + "\n> " + self.hash.mError)
        if self.hash.mIngreso != "":
            self.registroProcess.setText(self.registroProcess.toPlainText() + "\n> " + self.hash.mIngreso)
        if self.hash.mColision != "":
            self.registroProcess.setText(self.registroProcess.toPlainText() + "\n> " + self.hash.mColision)
        if self.hash.mSolColision != "":
            self.registroProcess.setText(self.registroProcess.toPlainText() + "\n> " + self.hash.mSolColision)