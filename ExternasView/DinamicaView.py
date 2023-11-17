import sys
from PyQt5 import QtWidgets as QtW
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtGui

from ExternasView.FuncionesHash import TransfClaves
from ExternasView import Dinamica as D
from CamposView.Campos import Campos

class DinamicaView(QtW.QGroupBox):

    def __init__(self, p: QWidget):
        
        super().__init__(p)

        self.cubetas = 0
        self.registros = 0
        self.pExpaxion = 0
        self.pReduccion = 0
        self.estructura = None
        self.listaDatos = []
        self.campos = Campos()

        self.setStyleSheet("background-color:#DECCA6")

        label = QtW.QLabel("Lista de datos:", self)
        label.move(840, 240)
        label.setFont(QFont("Arial", 12, QFont.Bold))
        self.tabla = QtW.QTableWidget(self)
        self.tabla.setColumnCount(2)
        self.tabla.setHorizontalHeaderLabels(["Lista espera", "Registro"])
        self.tabla.setGeometry(840, 280, 200, 530)
        self.tabla.setFont(QFont("Arial", 12, QFont.Bold))
        self.tabla.horizontalScrollBar().setVisible(False)
        self.tabla.setColumnWidth(0, 100)
        self.tabla.setColumnWidth(1, 100)
        self.tabla.verticalHeader().setVisible(False)
        self.tabla.setStyleSheet("QTableWidget{border:1px solid black; background-color:#EBE6D2}")

        self.tablaBloques = QtW.QTableWidget(self)
        self.tablaBloques.setColumnCount(self.cubetas)
        self.tablaBloques.setGeometry(20, 20, 1290, 200)
        self.tablaBloques.setFont(QFont("Arial", 12, QFont.Bold))
        self.tablaBloques.horizontalScrollBar().setVisible(True)
        self.tablaBloques.verticalHeader().setVisible(False)
        self.tablaBloques.setStyleSheet("QTableWidget{border:1px solid black; background-color:#EBE6D2}")

        label = QtW.QLabel("Número de cubetas:", self)
        label.move(20, 240)
        label.setFont(QFont("Arial", 12, QFont.Bold))
        self.numcubeta = QtW.QTextEdit(self)
        self.numcubeta.setFrameStyle(1)
        self.numcubeta.move(20, 260)
        self.numcubeta.resize(140, 30)
        self.numcubeta.setFont(QFont("Arial", 12))
        self.numcubeta.setStyleSheet("background-color:#EBE6D2")

        label = QtW.QLabel("Número de registros:", self)
        label.move(180, 240)
        label.setFont(QFont("Arial", 12, QFont.Bold))
        self.numregistro = QtW.QTextEdit(self)
        self.numregistro.setFrameStyle(1)
        self.numregistro.move(180, 260)
        self.numregistro.resize(140, 30)
        self.numregistro.setFont(QFont("Arial", 12))
        self.numregistro.setStyleSheet("background-color:#EBE6D2")

        label = QtW.QLabel("D.O. de expansión:", self)
        label.move(20, 300)
        label.setFont(QFont("Arial", 12, QFont.Bold))
        self.doexpansion = QtW.QTextEdit(self)
        self.doexpansion.setFrameStyle(1)
        self.doexpansion.move(20, 320)
        self.doexpansion.resize(140, 30)
        self.doexpansion.setFont(QFont("Arial", 12))
        self.doexpansion.setStyleSheet("background-color:#EBE6D2")

        label = QtW.QLabel("D.O. de reducción:", self)
        label.move(180, 300)
        label.setFont(QFont("Arial", 12, QFont.Bold))
        self.doreduccion = QtW.QTextEdit(self)
        self.doreduccion.setFrameStyle(1)
        self.doreduccion.move(180, 320)
        self.doreduccion.resize(140, 30)
        self.doreduccion.setFont(QFont("Arial", 12))
        self.doreduccion.setStyleSheet("background-color:#EBE6D2")

        label = QtW.QLabel("Método:", self)
        label.move(340, 240)
        label.setFont(QFont("Arial", 12, QFont.Bold))
        self.opcionMetodo = QtW.QComboBox(self)
        self.opcionMetodo.addItems(["Total", "Parcial"])
        self.opcionMetodo.move(340, 260)
        self.opcionMetodo.resize(145, 30)
        self.opcionMetodo.setFont(QFont("Arial", 12, QFont.Bold))
        self.opcionMetodo.setStyleSheet("background-color:#EBE6D2")

        label = QtW.QLabel("Ingresar clave:", self)
        label.move(20, 360)
        label.setFont(QFont("Arial", 12, QFont.Bold))
        self.ingresoDato = QtW.QTextEdit(self)
        self.ingresoDato.setFrameStyle(1)
        self.ingresoDato.move(20, 380)
        self.ingresoDato.resize(140, 30)
        self.ingresoDato.setFont(QFont("Arial", 12))
        self.ingresoDato.setStyleSheet("background-color:#EBE6D2")

        label = QtW.QLabel("Ingresar nombre:", self)
        label.move(170, 360)
        label.setFont(QFont("Arial", 12, QFont.Bold))
        self.campoNombreA = QtW.QTextEdit(self)
        self.campoNombreA.setFrameStyle(1)
        self.campoNombreA.move(170, 380)
        self.campoNombreA.resize(140, 30)
        self.campoNombreA.setFont(QFont("Arial", 12))
        self.campoNombreA.setStyleSheet("background-color:#EBE6D2")

        label = QtW.QLabel("Ingresar edad:", self)
        label.move(320, 360)
        label.setFont(QFont("Arial", 12, QFont.Bold))
        self.campoEdadA = QtW.QTextEdit(self)
        self.campoEdadA.setFrameStyle(1)
        self.campoEdadA.move(320, 380)
        self.campoEdadA.resize(140, 30)
        self.campoEdadA.setFont(QFont("Arial", 12))
        self.campoEdadA.setStyleSheet("background-color:#EBE6D2")

        self.labelSuccess = QtW.QLabel("Proceso: ", self)
        self.labelSuccess.move(20, 420)
        self.labelSuccess.setFont(QFont("Arial", 12, QFont.Bold))
        self.labelSuccess.resize(400, 30)

        self.registroProcess = QtW.QTextEdit(self)
        self.registroProcess.setFrameStyle(1)
        self.registroProcess.move(20, 460)
        self.registroProcess.resize(730, 360)
        self.registroProcess.setReadOnly(True)
        self.registroProcess.setFont(QFont("Arial", 12))
        self.registroProcess.setStyleSheet("QTextEdit{border:1px solid black; background-color:#D0C0A7}")

        self.bnEstructura = QtW.QPushButton("Crear estructura", self)
        self.bnEstructura.setGeometry(470, 320, 130, 30)
        self.bnEstructura.setStyleSheet("QPushButton{background-color:#b0c9bb; border:1px solid black;}"
                                        "QPushButton::hover{background-color :#8fa89a;}"
                                        "QPushButton::pressed{background-color:#6e8679; }")
        self.bnEstructura.clicked.connect(self.testEstructure)

        self.bnIngresar = QtW.QPushButton("Agregar clave", self)
        self.bnIngresar.setGeometry(470, 380, 130, 30)
        self.bnIngresar.setStyleSheet("QPushButton{background-color:#b0c9bb; border:1px solid black;}"
                                        "QPushButton::hover{background-color :#8fa89a;}"
                                        "QPushButton::pressed{background-color:#6e8679; }")
        self.bnIngresar.clicked.connect(self.ingresarDato)
        self.bnIngresar.setEnabled(False)

        self.bnTerminar = QtW.QPushButton("Eliminar clave", self)
        self.bnTerminar.setGeometry(610, 380, 130, 30)
        self.bnTerminar.setStyleSheet("QPushButton{background-color:#b0c9bb; border:1px solid black;}"
                                        "QPushButton::hover{background-color :#8fa89a;}"
                                        "QPushButton::pressed{background-color:#6e8679; }")
        self.bnTerminar.clicked.connect(self.eliminarDato)
        self.bnTerminar.setEnabled(False)

        self.bnVerCampos = QtW.QPushButton("Ver campos clave", self)
        self.bnVerCampos.setGeometry(470, 420, 130, 30)
        self.bnVerCampos.setStyleSheet("QPushButton{background-color:#b0c9bb; border:1px solid black;}"
                                        "QPushButton::hover{background-color :#8fa89a;}"
                                        "QPushButton::pressed{background-color:#6e8679; }")
        self.bnVerCampos.clicked.connect(self.verDatos)
        self.bnVerCampos.setEnabled(False)

        self.bnReiniciar = QtW.QPushButton("Reiniciar", self)
        self.bnReiniciar.setGeometry(140, 840, 500, 30)
        self.bnReiniciar.setStyleSheet("QPushButton{background-color:#D7A184; border:1px solid black;}"
                                   "QPushButton::hover{background-color :#D4C2AD;}"
                                   "QPushButton::pressed{background-color:#EFDFCC; }")
        self.bnReiniciar.clicked.connect(self.reiniciar)
        self.bnReiniciar.setEnabled(False)

    # ---------------------------------------- Métodos ------------------------------------

    def testEstructure(self):
        cub = 0
        reg = 0
        exp = 0
        red = 0
        try:
            if self.numcubeta.toPlainText() != '' and self.numregistro.toPlainText() != '' and self.doexpansion.toPlainText() != '' and self.doreduccion.toPlainText() != '':
                cub = int(self.numcubeta.toPlainText())
                reg = int(self.numregistro.toPlainText())
                exp = int(self.doexpansion.toPlainText())
                red = int(self.doreduccion.toPlainText())
        except:
            self.imprimirTexto("Ingreso para tamaño caracteres no numericos")
            return

        self.cubetas = cub
        self.registros = reg
        self.doexpansion = exp
        self.doreduccion = red
        self.estructura = D.Dinamicas(self.cubetas, self.registros, self.doexpansion, self.doreduccion, self.opcionMetodo.currentText())
        self.imprimirTexto("Estructura definida")
        self.bnEstructura.setEnabled(False)
        self.bnIngresar.setEnabled(True)
        self.bnTerminar.setEnabled(True)
        self.bnReiniciar.setEnabled(True)
        self.bnVerCampos.setEnabled(True)

    def ingresarDato(self):
        d = 0
        try:
            if(self.ingresoDato.toPlainText() != ''):
                d = int(self.ingresoDato.toPlainText())
            if(d <= 0):
                self.imprimirTexto("Por Favor ingrese una clave mayor a 0")
                return
            nombre = self.campoNombreA.toPlainText()
            edad = self.campoEdadA.toPlainText()
            camposValidos = True
            if not nombre.strip():
                self.imprimirTexto("Por favor ingrese un nombre")
                camposValidos = False
            if not edad.isdigit():
                self.imprimirTexto("Por ingrese un número en la edad")
                camposValidos = False
            else:
                edad = int(edad)
                if edad<0:
                    self.imprimirTexto("La edad debe ser mayor a 0")
                    camposValidos = False
            if not camposValidos:
                return

            self.campos.insertar(d, nombre, edad)
            if d not in self.listaDatos:
                self.estructura.historico = []
                self.estructura.event = False
                self.listaDatos.append(d)
                self.estructura.insertClave(d)
                self.cargarDatos()
                self.imprimirTexto("Dato Ingresado (" + str(d) + ")")
                self.cargarDatos()
                self.ingresoDato.setText("")
                self.mostrarEstructura()
                if self.estructura.event:
                    self.estructura.event = False
                    self.warningError("La estructura se va a expandir")
                    self.mostrarEstructura()
            else:
                self.imprimirTexto("La clave ya se encuentra en la estructura")
                return
        except:
            self.imprimirTexto("La clave no puede tener caracteres no numericos")
            return
        
    def eliminarDato(self):
        d = 0
        try:
            if(self.ingresoDato.toPlainText() != ''):
                d = int(self.ingresoDato.toPlainText())
            if(d <= 0):
                self.imprimirTexto("Por Favor ingrese una clave mayor a 0")
                return
            if d not in self.listaDatos:
                self.imprimirTexto("La clave no se encuentra en la estructura")
                return
            else:
                self.listaDatos.remove(d)
                self.campos.eliminar(d)
                self.tabla.setRowCount(0)
                self.crearTabla()
                self.estructura.deleteClave(d)
                self.cargarDatos()
                self.mostrarEstructura()
                self.imprimirTexto("Dato Eliminado (" + str(d) + ")")
                self.ingresoDato.setText("")
                
        except:
            self.imprimirTexto("La clave no puede tener caracteres no numericos")
            return
        
    def crearTabla(self):
        for i in range(0, len(self.listaDatos)):
            self.tabla.insertRow(i)
            self.tabla.setItem(i, 0, QtW.QTableWidgetItem("Dentro"))
        
    def cargarDatos(self):
        self.tabla.setRowCount(0)
        self.crearTabla()
        tablerow = 0
        for i in self.estructura.ListClaves:
            self.tabla.setItem(tablerow, 1, QtW.QTableWidgetItem(str(i)))
            if i in self.estructura.ListEspera:
                self.tabla.setItem(tablerow, 0, QtW.QTableWidgetItem("Esperando"))
            tablerow += 1

    def mostrarEstructura(self):
        estructuraTemp = []
        if self.estructura.event:
            estructuraTemp = self.estructura.historico
        else:
            estructuraTemp = self.estructura.StructureDinamic

        self.tablaBloques.setColumnCount(0)
        self.tablaBloques.setRowCount(0)
        self.tablaBloques.setColumnCount(len(estructuraTemp[0]))
        self.tablaBloques.setHorizontalHeaderLabels([str(i) for i in range(0, len(estructuraTemp[0]))])
        self.tablaBloques.setVerticalHeaderLabels([str(i) for i in range(0, self.estructura.Registros)])
        for i in range(0, len(estructuraTemp)):
            self.tablaBloques.insertRow(i)
            for j in range(0, len(estructuraTemp[0])):
                x = str(estructuraTemp[i][j])
                if x == "0":
                    x = ""
                self.tablaBloques.setItem(i, j, QtW.QTableWidgetItem(str(x)))

    def reiniciar(self):
        self.rango = None
        self.listaDatos = []
        self.bnEstructura.setEnabled(True)
        self.opcionMetodo.setEnabled(True)
        self.bnReiniciar.setEnabled(False)
        self.bnTerminar.setEnabled(False)
        self.bnIngresar.setEnabled(False)
        self.bnVerCampos.setEnabled(False)
        self.registroProcess.setText("")
        
    def imprimirTexto(self,texto:str):
        self.registroProcess.setText(self.registroProcess.toPlainText()+"\n >"+texto)

    def warningError(self, msg: str):
        error = QtW.QMessageBox(self)
        error.setIcon(QtW.QMessageBox.Icon.Warning)
        error.setText(msg)
        error.setStyleSheet("background-color:white; border: 0pc solid white")
        error.setFont(QFont("Arial", 10, QFont.Bold))
        error.exec_()

    def verDatos(self):
        try:
            mensaje = self.campos.obtener(int(self.ingresoDato.toPlainText()))
        except:
            mensaje = 'Clave invalida'
        emergente = QtW.QMessageBox(self)
        emergente.setIcon(QtW.QMessageBox.Icon.Information)
        emergente.setText(mensaje)
        emergente.setStyleSheet("background-color:white; border: 0pc solid white")
        emergente.setFont(QFont("Arial", 10, QFont.Bold))
        emergente.exec_()