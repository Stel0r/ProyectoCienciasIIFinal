import sys
from PyQt5 import QtWidgets as QtW
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtGui

from ExternasView.FuncionesHash import TransfClaves
from ExternasView import BinariaSecuencial as BS


class ExternasView(QtW.QGroupBox):

    def __init__(self, p: QWidget):
        super().__init__(p)

        self.rango = None
        self.listaDatos = []
        self.registros = []
        self.cubetas = 0
        self.hash = None

        self.setStyleSheet("background-color:white")

        self.tabla = QtW.QTableWidget(self)
        self.tabla.setColumnCount(2)
        self.tabla.setHorizontalHeaderLabels(["Número", "Registro"])
        self.tabla.setGeometry(10, 190, 270, 480)
        self.tabla.horizontalScrollBar().setVisible(False)
        self.tabla.setColumnWidth(0, 100)
        self.tabla.setColumnWidth(1, 100)
        self.tabla.verticalHeader().setVisible(False)

        self.tablaBloques = QtW.QTableWidget(self)
        self.tablaBloques.setColumnCount(self.cubetas)
        self.tablaBloques.setGeometry(740, 20, 320, 650)
        self.tablaBloques.horizontalScrollBar().setVisible(True)
        self.tablaBloques.verticalHeader().setVisible(False)

        label = QtW.QLabel("Rango (Múltiplos de 10)", self)
        label.move(10, 10)
        label.setFont(QFont("Arial", 10, QFont.Bold))
        self.tamanoEstructura = QtW.QTextEdit(self)
        self.tamanoEstructura.setFrameStyle(1)
        self.tamanoEstructura.move(10, 40)
        self.tamanoEstructura.resize(140, 30)
        self.tamanoEstructura.setFont(QFont("Arial", 10))

        label = QtW.QLabel("Ingresar Regsitro (Registros numéricos)", self)
        label.move(10, 100)
        label.setFont(QFont("Arial", 10, QFont.Bold))
        self.ingresoDato = QtW.QTextEdit(self)
        self.ingresoDato.setFrameStyle(1)
        self.ingresoDato.move(10, 140)
        self.ingresoDato.resize(140, 30)
        self.ingresoDato.setFont(QFont("Arial", 10))

        self.opcionMetodoHash = QtW.QComboBox(self)
        self.opcionMetodoHash.addItems(["Mod", "Cuadratico", "Plegamiento", "Truncamiento", "Conversión bases"])
        self.opcionMetodoHash.move(560, 100)
        self.opcionMetodoHash.resize(170, 30)
        self.opcionMetodoHash.setFont(QFont("Arial", 10, QFont.Bold))

        self.labelWarning = QtW.QLabel("Error: ", self)
        self.labelWarning.move(310, 190)
        self.labelWarning.setFont(QFont("Arial", 10, QFont.Bold))
        self.labelWarning.resize(400, 35)
        self.labelWarning.setStyleSheet("color:red")

        self.labelSuccess = QtW.QLabel("Success: ", self)
        self.labelSuccess.move(310, 220)
        self.labelSuccess.setFont(QFont("Arial", 10, QFont.Bold))
        self.labelSuccess.resize(400, 30)
        self.labelSuccess.setStyleSheet("color:green")

        self.registroProcess = QtW.QTextEdit(self)
        self.registroProcess.setFrameStyle(1)
        self.registroProcess.move(310, 250)
        self.registroProcess.resize(400, 300)
        self.registroProcess.setReadOnly(True)
        self.registroProcess.setFont(QFont("Arial", 10))

        label = QtW.QLabel("Registro a buscar", self)
        label.move(360, 25)
        label.setFont(QFont("Arial", 10, QFont.Bold))
        self.txsecuencial = QtW.QTextEdit(self)
        self.txsecuencial.setFrameStyle(1)
        self.txsecuencial.move(510, 20)
        self.txsecuencial.resize(40, 30)
        self.txsecuencial.setFont(QFont("Arial", 10))

        label = QtW.QLabel("Registro a buscar", self)
        label.move(360, 65)
        label.setFont(QFont("Arial", 10, QFont.Bold))
        self.txbinario = QtW.QTextEdit(self)
        self.txbinario.setFrameStyle(1)
        self.txbinario.move(510, 60)
        self.txbinario.resize(40, 30)
        self.txbinario.setFont(QFont("Arial", 10))

        label = QtW.QLabel("Registro a buscar", self)
        label.move(360, 105)
        label.setFont(QFont("Arial", 10, QFont.Bold))
        self.txhash = QtW.QTextEdit(self)
        self.txhash.setFrameStyle(1)
        self.txhash.move(510, 100)
        self.txhash.resize(40, 30)
        self.txhash.setFont(QFont("Arial", 10))

        self.bnEstructura = QtW.QPushButton("Definir Rango", self)
        self.bnEstructura.setGeometry(160, 40, 130, 30)
        self.bnEstructura.setStyleSheet("QPushButton{background-color:#a4c3f5; border:1px solid black;}"
                                        "QPushButton::hover{background-color :#80a7e8;}"
                                        "QPushButton::pressed{background-color:#7499d6; }")
        self.bnEstructura.clicked.connect(self.testEstructure)

        self.bnIngresar = QtW.QPushButton("Agregar", self)
        self.bnIngresar.setGeometry(160, 140, 130, 30)
        self.bnIngresar.setStyleSheet("QPushButton{background-color:#a4c3a5; border:1px solid black;}"
                                      "QPushButton::hover{background-color :#80a7e8;}"
                                      "QPushButton::pressed{background-color:#7499d6; }")
        self.bnIngresar.clicked.connect(self.ingresarDato)
        self.bnIngresar.setEnabled(False)

        self.bnTerminar = QtW.QPushButton("Terminar", self)
        self.bnTerminar.setGeometry(300, 140, 130, 30)
        self.bnTerminar.setStyleSheet("QPushButton{background-color:#a4c3a5; border:1px solid black;}"
                                      "QPushButton::hover{background-color :#80a7e8;}"
                                      "QPushButton::pressed{background-color:#7499d6; }")
        self.bnTerminar.clicked.connect(self.terminar)
        self.bnTerminar.setEnabled(False)

        self.bnSecuencial = QtW.QPushButton("Secuencial", self)
        self.bnSecuencial.setGeometry(560, 20, 170, 30)
        self.bnSecuencial.setStyleSheet("QPushButton{background-color:#46D9F3; border:1px solid black;}"
                                        "QPushButton::hover{background-color :#80a7e8;}"
                                        "QPushButton::pressed{background-color:#7499d6; }")
        self.bnSecuencial.clicked.connect(self.secuencial)
        self.bnSecuencial.setEnabled(False)
        
        self.bnBinaria = QtW.QPushButton("Binaria", self)
        self.bnBinaria.setGeometry(560, 60, 170, 30)
        self.bnBinaria.setStyleSheet("QPushButton{background-color:#46D9F3; border:1px solid black;}"
                                        "QPushButton::hover{background-color :#80a7e8;}"
                                        "QPushButton::pressed{background-color:#7499d6; }")
        self.bnBinaria.clicked.connect(self.binario)
        self.bnBinaria.setEnabled(False)
        
        self.bnHASH = QtW.QPushButton("Función Hash", self)
        self.bnHASH.setGeometry(560, 140, 170, 30)
        self.bnHASH.setStyleSheet("QPushButton{background-color:#46D9F3; border:1px solid black;}"
                                      "QPushButton::hover{background-color :#80a7e8;}"
                                      "QPushButton::pressed{background-color:#7499d6; }")
        self.bnHASH.clicked.connect(self.funcionesHash)
        self.bnHASH.setEnabled(False)

        self.bnReiniciar = QtW.QPushButton("Reiniciar", self)
        self.bnReiniciar.setGeometry(420, 600, 170, 30)
        self.bnReiniciar.setStyleSheet("QPushButton{background-color:#f4c3a5; border:1px solid black;}"
                                      "QPushButton::hover{background-color :#80a7e8;}"
                                      "QPushButton::pressed{background-color:#7499d6; }")
        self.bnReiniciar.clicked.connect(self.reiniciar)
        self.bnReiniciar.setEnabled(False)

    def testEstructure(self):
        t = 0
        try:
            if(self.tamanoEstructura.toPlainText() != ''):
                t = int(self.tamanoEstructura.toPlainText())
            if(t % 10 != 0 or t > 1000 or t <= 0):
                self.errWarning("Por Favor ingrese un tamaño mayor a 0 o múltiplo de 10")
                return
        except:
            self.errWarning("Ingreso para tamaño caracteres no numericos")
            return

        self.rango = t
        self.processSuccess("Estructura definida")
        self.errWarning("")
        self.crearTabla()
        self.bnEstructura.setEnabled(False)
        self.bnIngresar.setEnabled(True)
        self.bnReiniciar.setEnabled(True)

    def ingresarDato(self):
        d = 0
        try:
            if(self.ingresoDato.toPlainText() != ''):
                d = int(self.ingresoDato.toPlainText())
            if(d <= 0):
                self.errWarning("Por Favor ingrese un registro mayor a 0")
                return
            if(len(self.listaDatos) > self.rango-1):
                self.errWarning("La estructura ya está llena")
                return
        except:
            self.errWarning("Ingreso para registro caracteres no numericos")
            return

        self.listaDatos.append(d)
        self.listaDatos.sort()
        self.processSuccess("Dato Ingresado (" + str(d) + ")")
        self.errWarning("")
        self.bnTerminar.setEnabled(True)
        self.cargarDatos()
        self.ingresoDato.setText("")
    
    def crearTabla(self):
        for i in range(0, self.rango):
            self.tabla.insertRow(i)
            self.tabla.setItem(i, 0, QtW.QTableWidgetItem(str(i + 1)))

    def errWarning(self, mensaje):
        self.labelWarning.setText("Error: " + mensaje)

    def processSuccess(self, mensaje):
        self.labelSuccess.setText("Success: " + mensaje)

    def reiniciar(self):
        self.rango = None
        self.listaDatos = []
        self.tabla.setRowCount(0)
        self.bnEstructura.setEnabled(True)
        self.opcionMetodoHash.setEnabled(True)
        self.tamanoEstructura.setEnabled(True)
        self.bnReiniciar.setEnabled(False)
        self.bnTerminar.setEnabled(False)
        self.bnSecuencial.setEnabled(False)
        self.bnBinaria.setEnabled(False)
        self.bnHASH.setEnabled(False)
        self.bnIngresar.setEnabled(False)
        self.registroProcess.setText("")

    def terminar(self):
        self.bnTerminar.setEnabled(False)
        self.bnSecuencial.setEnabled(True)
        self.bnBinaria.setEnabled(True)
        self.bnHASH.setEnabled(True)
        self.bnIngresar.setEnabled(False)
        self.registroProcess.setText("")
        self.ingresoDato.setText("")

    def cargarDatos(self):
        tablerow = 0
        for i in self.listaDatos:
            self.tabla.setItem(tablerow, 1, QtW.QTableWidgetItem(str(i)))
            tablerow += 1

    def secuencial(self):
        r = 0
        try:
            if(self.txsecuencial.toPlainText() != ''):
                r = int(self.txsecuencial.toPlainText())
        except:
            self.errWarning("Ingreso para registro caracteres no numericos")
            return
        
        multilista = self.cargarDatosSecuencialesBinarios()
        
        bloque, numeroBloque = BS.busqueda_por_bloques(multilista, int(r))
        ob = BS.Secuencial(bloque, numeroBloque, int(r))
        self.registroProcess.setText(BS.Secuencial.busqueda(ob))

        self.txsecuencial.setText("")

    def binario(self):
        r = 0
        try:
            if(self.txbinario.toPlainText() != ''):
                r = int(self.txbinario.toPlainText())
        except:
            self.errWarning("Ingreso para registro caracteres no numericos")
            return
        
        multilista = self.cargarDatosSecuencialesBinarios()

        bloque, numeroBloque = BS.busqueda_por_bloques(multilista, int(r))
        tt = BS.Binario(bloque, numeroBloque, int(r))
        self.registroProcess.setText(BS.Binario.busqueda(tt))

        self.txbinario.setText("")

    def cargarDatosSecuencialesBinarios(self):
        tamano_bloque = BS.calcular_tamano_bloques(self.rango)
        multilista = BS.guardar_en_bloques(self.listaDatos, tamano_bloque)

        for i, bloque in enumerate(multilista):
            self.cubetas = i + 1
            self.tablaBloques.setColumnCount(self.cubetas)

        self.tablaBloques.setRowCount(tamano_bloque)

        for i, bloque in enumerate(multilista):
            self.cubetas = i + 1
            tablerow = 0
            for elemento in bloque:
                self.tablaBloques.setItem(tablerow, i, QtW.QTableWidgetItem(str(elemento)))
                tablerow += 1
        return multilista


    def funcionesHash(self):
        try:
            if(self.txhash.toPlainText() != ''):
                r = int(self.txhash.toPlainText())
        except:
            self.errWarning("Ingreso para registro caracteres no numericos")
            return
        
        self.cubetas = self.rango
        self.hash = TransfClaves(self.opcionMetodoHash.currentText(), self.rango, 'Lineal')
        
        for registro in self.listaDatos:
            self.hash.ingresarValor(registro)

        self.crearTablaHash()

        self.txhash.setText("")

    def crearTablaHash(self):
        for i in range(0, self.rango):
            self.tablaBloques.insertColumn(i)
            self.tablaBloques.insertRow(i)
            self.tablaBloques.setHorizontalHeaderItem(i, QtW.QTableWidgetItem(str(i)))

        tablerow = 0
        for i in self.hash.estructura:
            self.tablaBloques.setItem(tablerow, i-1, QtW.QTableWidgetItem(str(self.hash.estructura[i])))

