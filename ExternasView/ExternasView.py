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

        self.setStyleSheet("background-color:#DECCA6")

        label = QtW.QLabel("Lista de datos:", self)
        label.move(550, 340)
        label.setFont(QFont("Arial", 10, QFont.Bold))

        self.tabla = QtW.QTableWidget(self)
        self.tabla.setColumnCount(2)
        self.tabla.setHorizontalHeaderLabels(["Número", "Registro"])
        self.tabla.setGeometry(550, 380, 500, 290)
        self.tabla.horizontalScrollBar().setVisible(False)
        self.tabla.setColumnWidth(0, 100)
        self.tabla.setColumnWidth(1, 100)
        self.tabla.verticalHeader().setVisible(False)
        self.tabla.setStyleSheet("QTableWidget{border:1px solid black; background-color:#EBE6D2}")

        self.tablaBloques = QtW.QTableWidget(self)
        self.tablaBloques.setColumnCount(self.cubetas)
        self.tablaBloques.setGeometry(550, 20, 500, 300)
        self.tablaBloques.horizontalScrollBar().setVisible(True)
        self.tablaBloques.verticalHeader().setVisible(False)
        self.tablaBloques.setStyleSheet("QTableWidget{border:1px solid black; background-color:#EBE6D2}")

        label = QtW.QLabel("Rango (Múltiplos de 10):", self)
        label.move(20, 20)
        label.setFont(QFont("Arial", 10, QFont.Bold))
        self.tamanoEstructura = QtW.QTextEdit(self)
        self.tamanoEstructura.setFrameStyle(1)
        self.tamanoEstructura.move(20, 50)
        self.tamanoEstructura.resize(140, 30)
        self.tamanoEstructura.setFont(QFont("Arial", 10))
        self.tamanoEstructura.setStyleSheet("background-color:#EBE6D2")

        label = QtW.QLabel("Ingresar clave (Claves numéricas):", self)
        label.move(20, 110)
        label.setFont(QFont("Arial", 10, QFont.Bold))
        self.ingresoDato = QtW.QTextEdit(self)
        self.ingresoDato.setFrameStyle(1)
        self.ingresoDato.move(20, 140)
        self.ingresoDato.resize(140, 30)
        self.ingresoDato.setFont(QFont("Arial", 10))
        self.ingresoDato.setStyleSheet("background-color:#EBE6D2")

        self.opcionMetodoHash = QtW.QComboBox(self)
        self.opcionMetodoHash.addItems(["Mod", "Cuadratico", "Plegamiento", "Truncamiento", "Conversión bases"])
        self.opcionMetodoHash.move(180, 330)
        self.opcionMetodoHash.resize(145, 30)
        self.opcionMetodoHash.setFont(QFont("Arial", 10, QFont.Bold))
        self.opcionMetodoHash.setStyleSheet("background-color:#EBE6D2")

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

        label = QtW.QLabel("Dirección a buscar:", self)
        label.move(20, 210)
        label.setFont(QFont("Arial", 10, QFont.Bold))
        self.txbuscar = QtW.QTextEdit(self)
        self.txbuscar.setFrameStyle(1)
        self.txbuscar.move(20, 250)
        self.txbuscar.resize(140, 30)
        self.txbuscar.setFont(QFont("Arial", 10))
        self.txbuscar.setStyleSheet("background-color:#EBE6D2")

        self.bnEstructura = QtW.QPushButton("Crear estructura", self)
        self.bnEstructura.setGeometry(180, 50, 130, 30)
        self.bnEstructura.setStyleSheet("QPushButton{background-color:#b0c9bb; border:1px solid black;}"
                                        "QPushButton::hover{background-color :#8fa89a;}"
                                        "QPushButton::pressed{background-color:#6e8679; }")
        self.bnEstructura.clicked.connect(self.testEstructure)

        self.bnIngresar = QtW.QPushButton("Agregar", self)
        self.bnIngresar.setGeometry(180, 140, 130, 30)
        self.bnIngresar.setStyleSheet("QPushButton{background-color:#b0c9bb; border:1px solid black;}"
                                        "QPushButton::hover{background-color :#8fa89a;}"
                                        "QPushButton::pressed{background-color:#6e8679; }")
        self.bnIngresar.clicked.connect(self.ingresarDato)
        self.bnIngresar.setEnabled(False)

        self.bnTerminar = QtW.QPushButton("Eliminar clave", self)
        self.bnTerminar.setGeometry(320, 140, 130, 30)
        self.bnTerminar.setStyleSheet("QPushButton{background-color:#b0c9bb; border:1px solid black;}"
                                        "QPushButton::hover{background-color :#8fa89a;}"
                                        "QPushButton::pressed{background-color:#6e8679; }")
        #self.bnTerminar.clicked.connect()
        self.bnTerminar.setEnabled(False)

        self.bnSecuencial = QtW.QPushButton("Secuencial", self)
        self.bnSecuencial.setGeometry(180, 250, 300, 30)
        self.bnSecuencial.setStyleSheet("QPushButton{background-color:#b0c9bb; border:1px solid black;}"
                                        "QPushButton::hover{background-color :#8fa89a;}"
                                        "QPushButton::pressed{background-color:#6e8679; }")
        self.bnSecuencial.clicked.connect(self.secuencial)
        self.bnSecuencial.setEnabled(False)
        
        self.bnBinaria = QtW.QPushButton("Binaria", self)
        self.bnBinaria.setGeometry(180, 290, 300, 30)
        self.bnBinaria.setStyleSheet("QPushButton{background-color:#b0c9bb; border:1px solid black;}"
                                        "QPushButton::hover{background-color :#8fa89a;}"
                                        "QPushButton::pressed{background-color:#6e8679; }")
        self.bnBinaria.clicked.connect(self.binario)
        self.bnBinaria.setEnabled(False)
        
        self.bnHASH = QtW.QPushButton("Función Hash", self)
        self.bnHASH.setGeometry(335, 330, 145, 30)
        self.bnHASH.setStyleSheet("QPushButton{background-color:#b0c9bb; border:1px solid black;}"
                                        "QPushButton::hover{background-color :#8fa89a;}"
                                        "QPushButton::pressed{background-color:#6e8679; }")
        self.bnHASH.clicked.connect(self.funcionesHash)
        self.bnHASH.setEnabled(False)

        self.bnReiniciar = QtW.QPushButton("Reiniciar", self)
        self.bnReiniciar.setGeometry(20, 640, 500, 30)
        self.bnReiniciar.setStyleSheet("QPushButton{background-color:#D7A184; border:1px solid black;}"
                                   "QPushButton::hover{background-color :#D4C2AD;}"
                                   "QPushButton::pressed{background-color:#EFDFCC; }")
        self.bnReiniciar.clicked.connect(self.reiniciar)
        self.bnReiniciar.setEnabled(False)


    # ---------------------------------------- Métodos ------------------------------------

    def testEstructure(self):
        t = 0
        try:
            if(self.tamanoEstructura.toPlainText() != ''):
                t = int(self.tamanoEstructura.toPlainText())
            if(t % 10 != 0 or t > 1000 or t <= 0):
                self.imprimirTexto("Por Favor ingrese un tamaño mayor a 0 o múltiplo de 10")
                return
        except:
            self.imprimirTexto("Ingreso para tamaño caracteres no numericos")
            return

        self.rango = t
        self.imprimirTexto("Estructura definida")
        self.crearTabla()
        self.bnEstructura.setEnabled(False)
        self.bnIngresar.setEnabled(True)
        self.bnReiniciar.setEnabled(True)

    def crearTabla(self):
        for i in range(0, self.rango):
            self.tabla.insertRow(i)
            self.tabla.setItem(i, 0, QtW.QTableWidgetItem(str(i + 1)))

    def ingresarDato(self):
        d = 0
        try:
            if(self.ingresoDato.toPlainText() != ''):
                d = int(self.ingresoDato.toPlainText())
            if(d <= 0):
                self.imprimirTexto("Por Favor ingrese una clave mayor a 0")
                return
            if(len(self.listaDatos) > self.rango-1):
                self.imprimirTexto("La estructura ya está llena")
                return
            if d not in self.listaDatos:
                self.listaDatos.append(d)
                self.cargarDatos()
                self.cargarDatosSecuencialesBinarios()
                self.imprimirTexto("Dato Ingresado (" + str(d) + ")")
            else:
                self.imprimirTexto("La clave ya se encuentra en la estructura")
                return
        except:
            self.errWarning("La clave no puede tener caracteres no numericos")
            return
        
        self.ingresoDato.setText("")


    def cargarDatos(self):
        tablerow = 0
        for i in self.listaDatos:
            self.tabla.setItem(tablerow, 1, QtW.QTableWidgetItem(str(i)))
            tablerow += 1

    def reiniciar(self):
        self.rango = None
        self.listaDatos = []
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

    def imprimirTexto(self,texto:str):
        self.registroProcess.setText(self.registroProcess.toPlainText()+"\n >"+texto)

