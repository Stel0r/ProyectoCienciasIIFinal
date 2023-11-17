import sys
from PyQt5 import QtWidgets as QtW
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtGui

from ExternasView.FuncionesHash import TransfClaves
from ExternasView import BinariaSecuencial as BS
from CamposView.Campos import Campos

class ExternasView(QtW.QGroupBox):

    def __init__(self, p: QWidget):
        
        super().__init__(p)

        # variable para simulacion
        self.campos=Campos()
        self.rango = None
        self.listaDatos = []
        self.registros = []
        self.cubetas = 0
        self.hash = None
        self.metodo = ""

        self.setStyleSheet("background-color:#DECCA6")

        label = QtW.QLabel("Lista de datos:", self)
        label.move(750, 340)
        label.setFont(QFont("Arial", 12, QFont.Bold))

        self.tabla = QtW.QTableWidget(self)
        self.tabla.setColumnCount(2)
        self.tabla.setFont(QFont("Arial", 12))
        self.tabla.setHorizontalHeaderLabels(["Número", "Registro"])
        self.tabla.setGeometry(750, 380, 550, 450)
        self.tabla.horizontalScrollBar().setVisible(False)
        self.tabla.setColumnWidth(0, 100)
        self.tabla.setColumnWidth(1, 100)
        self.tabla.verticalHeader().setVisible(False)
        self.tabla.setStyleSheet("QTableWidget{border:1px solid black; background-color:#EBE6D2}")

        self.tablaBloques = QtW.QTableWidget(self)
        self.tablaBloques.setColumnCount(self.cubetas)
        self.tablaBloques.setFont(QFont("Arial", 12))
        self.tablaBloques.setGeometry(750, 20, 550, 300)
        self.tablaBloques.horizontalScrollBar().setVisible(True)
        self.tablaBloques.verticalHeader().setVisible(False)
        self.tablaBloques.setStyleSheet("QTableWidget{border:1px solid black; background-color:#EBE6D2}")

        label = QtW.QLabel("Rango (Múltiplos de 10):", self)
        label.move(20, 20)
        label.setFont(QFont("Arial", 12, QFont.Bold))
        self.tamanoEstructura = QtW.QTextEdit(self)
        self.tamanoEstructura.setFrameStyle(1)
        self.tamanoEstructura.move(20, 50)
        self.tamanoEstructura.resize(140, 30)
        self.tamanoEstructura.setFont(QFont("Arial", 12))
        self.tamanoEstructura.setStyleSheet("background-color:#EBE6D2")

        label = QtW.QLabel("Ingresar clave:", self)
        label.move(20, 200)
        label.setFont(QFont("Arial", 12, QFont.Bold))
        self.ingresoDato = QtW.QTextEdit(self)
        self.ingresoDato.setFrameStyle(1)
        self.ingresoDato.move(20, 230)
        self.ingresoDato.resize(140, 30)
        self.ingresoDato.setFont(QFont("Arial", 12))
        self.ingresoDato.setStyleSheet("background-color:#EBE6D2")

        label = QtW.QLabel("Ingresar nombre:", self)
        label.move(170, 200)
        label.setFont(QFont("Arial", 12, QFont.Bold))
        self.campoNombreA = QtW.QTextEdit(self)
        self.campoNombreA.setFrameStyle(1)
        self.campoNombreA.move(170, 230)
        self.campoNombreA.resize(140, 30)
        self.campoNombreA.setFont(QFont("Arial", 12))
        self.campoNombreA.setStyleSheet("background-color:#EBE6D2")

        label = QtW.QLabel("Ingresar edad:", self)
        label.move(320, 200)
        label.setFont(QFont("Arial", 12, QFont.Bold))
        self.campoEdadA = QtW.QTextEdit(self)
        self.campoEdadA.setFrameStyle(1)
        self.campoEdadA.move(320, 230)
        self.campoEdadA.resize(140, 30)
        self.campoEdadA.setFont(QFont("Arial", 12))
        self.campoEdadA.setStyleSheet("background-color:#EBE6D2")

        label = QtW.QLabel("Tipo de búsqueda:", self)
        label.move(20, 110)
        label.setFont(QFont("Arial", 12, QFont.Bold))
        self.opcionMetodoHash = QtW.QComboBox(self)
        self.opcionMetodoHash.addItems(["Secuencial", "Binaria", "Mod", "Cuadratico", "Plegamiento", "Truncamiento"])
        self.opcionMetodoHash.move(20, 140)
        self.opcionMetodoHash.resize(145, 30)
        self.opcionMetodoHash.setFont(QFont("Arial", 12, QFont.Bold))
        self.opcionMetodoHash.setStyleSheet("background-color:#EBE6D2")

        self.labelSuccess = QtW.QLabel("Proceso: ", self)
        self.labelSuccess.move(20, 420)
        self.labelSuccess.setFont(QFont("Arial", 12, QFont.Bold))
        self.labelSuccess.resize(400, 30)

        self.registroProcess = QtW.QTextEdit(self)
        self.registroProcess.setFrameStyle(1)
        self.registroProcess.move(20, 450)
        self.registroProcess.resize(670, 370)
        self.registroProcess.setReadOnly(True)
        self.registroProcess.setFont(QFont("Arial", 16))
        self.registroProcess.setStyleSheet("QTextEdit{border:1px solid black; background-color:#D0C0A7}")

        label = QtW.QLabel("Clave a buscar:", self)
        label.move(20, 320)
        label.setFont(QFont("Arial", 12, QFont.Bold))
        self.txbuscar = QtW.QTextEdit(self)
        self.txbuscar.setFrameStyle(1)
        self.txbuscar.move(20, 350)
        self.txbuscar.resize(140, 30)
        self.txbuscar.setFont(QFont("Arial", 12))
        self.txbuscar.setStyleSheet("background-color:#EBE6D2")

        self.bnEstructura = QtW.QPushButton("Crear estructura", self)
        self.bnEstructura.setGeometry(180, 50, 130, 30)
        self.bnEstructura.setStyleSheet("QPushButton{background-color:#b0c9bb; border:1px solid black;}"
                                        "QPushButton::hover{background-color :#8fa89a;}"
                                        "QPushButton::pressed{background-color:#6e8679; }")
        self.bnEstructura.clicked.connect(self.testEstructure)

        self.bnIngresar = QtW.QPushButton("Agregar clave", self)
        self.bnIngresar.setGeometry(50, 270, 170, 30)
        self.bnIngresar.setStyleSheet("QPushButton{background-color:#b0c9bb; border:1px solid black;}"
                                        "QPushButton::hover{background-color :#8fa89a;}"
                                        "QPushButton::pressed{background-color:#6e8679; }")
        self.bnIngresar.clicked.connect(self.ingresarDato)
        self.bnIngresar.setEnabled(False)

        self.bnTerminar = QtW.QPushButton("Eliminar clave", self)
        self.bnTerminar.setGeometry(250, 270, 170, 30)
        self.bnTerminar.setStyleSheet("QPushButton{background-color:#b0c9bb; border:1px solid black;}"
                                        "QPushButton::hover{background-color :#8fa89a;}"
                                        "QPushButton::pressed{background-color:#6e8679; }")
        self.bnTerminar.clicked.connect(self.eliminarDato)
        self.bnTerminar.setEnabled(False)

        self.bnBuscar = QtW.QPushButton("Buscar", self)
        self.bnBuscar.setGeometry(180, 350, 130, 30)
        self.bnBuscar.setStyleSheet("QPushButton{background-color:#b0c9bb; border:1px solid black;}"
                                        "QPushButton::hover{background-color :#8fa89a;}"
                                        "QPushButton::pressed{background-color:#6e8679; }")
        self.bnBuscar.clicked.connect(self.buscar)
        self.bnBuscar.setEnabled(False)
        
        self.bnmetodo = QtW.QPushButton("Elegir método", self)
        self.bnmetodo.setGeometry(180, 140, 145, 30)
        self.bnmetodo.setStyleSheet("QPushButton{background-color:#b0c9bb; border:1px solid black;}"
                                        "QPushButton::hover{background-color :#8fa89a;}"
                                        "QPushButton::pressed{background-color:#6e8679; }")
        self.bnmetodo.clicked.connect(self.elegirBusqueda)
        self.bnmetodo.setEnabled(False)

        self.bnReiniciar = QtW.QPushButton("Reiniciar", self)
        self.bnReiniciar.setGeometry(20, 380, 500, 30)
        self.bnReiniciar.setStyleSheet("QPushButton{background-color:#D7A184; border:1px solid black;}"
                                   "QPushButton::hover{background-color :#D4C2AD;}"
                                   "QPushButton::pressed{background-color:#EFDFCC; }")
        self.bnReiniciar.clicked.connect(self.reiniciar)
        self.bnReiniciar.setEnabled(False)


    # ---------------------------------------- Métodos -----------------------------------------------------

    # Creación de la estructura ----------------------------------------------------------------------------

    # Rango

    def testEstructure(self):
        t = 0
        try:
            if(self.tamanoEstructura.toPlainText() != ''):
                t = int(self.tamanoEstructura.toPlainText())
            if(t % 10 != 0 or t > 1000 or t <= 0):
                self.imprimirTexto("Por Favor ingrese un tamaño mayor a 0 y menor a 10000, y múltiplo de 10")
                return
        except:
            self.imprimirTexto("El campo del rango está vacío o se ha ingresado caracteres no numéricos")
            return

        self.rango = t
        self.imprimirTexto("Estructura definida")
        self.crearTabla()
        self.bnEstructura.setEnabled(False)
        self.bnReiniciar.setEnabled(True)
        self.bnmetodo.setEnabled(True)

    # Método de busqueda

    def elegirBusqueda(self):
        self.metodo = self.opcionMetodoHash.currentText()
        if self.metodo != "Secuencial" and self.metodo != "Binaria":
            self.listaDatos.clear()
            self.tabla.setRowCount(0)
            self.tablaBloques.setRowCount(0)
            self.crearTabla()
        self.bnIngresar.setEnabled(True)
        self.bnTerminar.setEnabled(True)

    # Inicio CRUD -----------------------------------------------------------------------------------------

    # Ingresar

    def ingresarDato(self):
        self.bnBuscar.setEnabled(True)
        d = 0
        try:
            if self.ingresoDato.toPlainText() != '':

                d = int(self.ingresoDato.toPlainText())

            if d <= 0:

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

            if self.metodo == "Mod" or self.metodo == "Cuadratico" or self.metodo == "Plegamiento" or self.metodo == "Truncamiento":
                
                if len(str(d)) != 4:
                    self.imprimirTexto("La longitud de la clave debe ser 4")
                    return
                if d not in self.listaDatos:
                    self.listaDatos.append(d)
                    self.cargarDatos()
                    self.imprimirTexto("Dato Ingresado (" + str(d) + ")")
                    self.funcionesHash()
                    self.ingresoDato.setText("")
                    self.campoNombreA.setText('')
                    self.campoEdadA.setText('')
                    self.ingresoDato.setFocus()
                else:
                    self.imprimirTexto("La clave ya se encuentra en la estructura")
                    return
                
                return
            
            if self.metodo == "Secuencial" or self.metodo == "Binaria":
            
                if len(self.listaDatos) > self.rango-1:
                    self.imprimirTexto("La estructura ya está llena")
                    return
                if d not in self.listaDatos:
                    self.listaDatos.append(d)
                    self.cargarDatos()
                    self.cargarDatosSecuencialesBinarios()
                    self.imprimirTexto("Dato Ingresado (" + str(d) + ")")
                    self.ingresoDato.setText("")
                    self.campoNombreA.setText('')
                    self.campoEdadA.setText('')
                    self.ingresoDato.setFocus()
                else:
                    self.imprimirTexto("La clave ya se encuentra en la estructura")
                    return
                
        except:
            self.imprimirTexto("La clave no puede tener caracteres no numéricos")
            return
        
    # Eliminar

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
                self.cargarDatos()
                if self.metodo != "Secuencial" and self.metodo != "Binaria":
                    """self.funcionesHash()"""
                    return
                else:
                    self.cargarDatosSecuencialesBinarios()
                self.imprimirTexto("Dato Eliminado (" + str(d) + ")")
                self.ingresoDato.setText("")
                
        except:
            self.imprimirTexto("La clave no puede tener caracteres no numéricos")
            return

    # Buscar

    def buscar(self):

        r = 0
        try:
            if(self.txbuscar.toPlainText() != ''):
                r = int(self.txbuscar.toPlainText())
        except:
            self.imprimirTexto("Ingreso para registro caracteres no numericos")
            return

        if self.metodo  == "Binaria":
            self.binario(r)
        elif self.metodo == "Secuencial":
            self.secuencial(r)
        else:
            j = 0
            while j < self.rango - 1:
                bloque = 1
                for i in self.hash.buscarElemento(j):
                    if r == i:
                        self.imprimirTexto(f"El dato {r} se encuentra ubicado en la cubeta {j}, en el bloque {bloque}")
                        campos = self.campos.obtener(int(r))
                        if not campos.startswith('El registro con la clave'):
                            self.imprimirTexto(f"   {campos}")
                    bloque += 1
                j += 1
            return

    def secuencial(self, r):
        
        multilista = self.cargarDatosSecuencialesBinarios()
        
        bloque, numeroBloque = BS.busqueda_por_bloques(multilista, int(r))
        ob = BS.Secuencial(bloque, numeroBloque, int(r))
        self.registroProcess.setText(BS.Secuencial.busqueda(ob))
        campos = self.campos.obtener(int(r))
        if not campos.startswith('El registro con la clave'):
            self.imprimirTexto(f"   {campos}")

        self.txbuscar.setText("")

    def binario(self, r):
        
        multilista = self.cargarDatosSecuencialesBinarios()

        bloque, numeroBloque = BS.busqueda_por_bloques(multilista, int(r))
        tt = BS.Binario(bloque, numeroBloque, int(r))
        self.registroProcess.setText(BS.Binario.busqueda(tt))
        campos = self.campos.obtener(int(r))
        if not campos.startswith('El registro con la clave'):
            self.imprimirTexto(f"   {campos}")
        
        self.txbuscar.setText("")
    
    # Parte de la funciones HASH

    def funcionesHash(self):
        self.hash = TransfClaves(self.metodo, self.rango)
        
        for dato in self.listaDatos:
            clave = self.hash.obtenerClave(dato)
            self.hash.ingresarValor(clave, dato)

        self.tablaBloques.setRowCount(0)
        self.tablaBloques.setColumnCount(0)
        for i in range(0, self.rango):
            self.tablaBloques.insertColumn(i)
            self.tablaBloques.insertRow(i)
            self.tablaBloques.setHorizontalHeaderItem(i, QtW.QTableWidgetItem(str(i)))

        j = 0
        while j < self.rango - 1:
            tablerow = 0
            for i in self.hash.buscarElemento(j):
                self.tablaBloques.setItem(tablerow, j, QtW.QTableWidgetItem(str(i)))
                tablerow += 1
            j += 1
        return
        
    # Impresión en pantalla

    def imprimirTexto(self,texto:str):
        self.registroProcess.setText(self.registroProcess.toPlainText()+"\n >"+texto)

    # Visualización de las tablas

    def crearTabla(self):
        for i in range(0, self.rango):
            self.tabla.insertRow(i)
            self.tabla.setItem(i, 0, QtW.QTableWidgetItem(str(i + 1)))

    def cargarDatos(self):
        tablerow = 0
        for i in self.listaDatos:
            self.tabla.setItem(tablerow, 1, QtW.QTableWidgetItem(str(i)))
            tablerow += 1

    def cargarDatosSecuencialesBinarios(self):
        self.tablaBloques.setRowCount(0)
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

    # Botón reinicio

    def reiniciar(self):
        self.rango = None
        self.listaDatos = []
        self.bnEstructura.setEnabled(True)
        self.opcionMetodoHash.setEnabled(True)
        self.tamanoEstructura.setEnabled(True)
        self.bnReiniciar.setEnabled(False)
        self.bnTerminar.setEnabled(False)
        self.bnIngresar.setEnabled(False)
        self.registroProcess.setText("")

