from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from ArbolesView.ArbolesCanvas import ArbolesCanvas
from ArbolesView.Nodo import Nodo
import copy

class ArbolesView(QGroupBox):
    def __init__(self,p:QWidget):
        super().__init__(p)
        self.pasos:list[Nodo] = []

        self.alfabeto = {}

        self.canvas = ArbolesCanvas(None)
        self.canvas.setGeometry(0,0,1200,650)
        self.canvasArea = QScrollArea(self)
        self.canvasArea.setGeometry(40,20,802,652)
        self.canvasArea.setWidget(self.canvas)

        self.setStyleSheet("background-color:white")

        self.tabla = QTableWidget(self)
        self.tabla.setColumnCount(2)
        self.tabla.verticalHeader().setVisible(False)
        self.tabla.setHorizontalHeaderLabels(["Codigo","Letra"])
        self.tabla.setGeometry(860,20,200,250)
        self.tabla.setFont(QFont("Arial",7))
        self.tabla.horizontalScrollBar().setVisible(False)

        panelOpciones = QGroupBox(self)
        panelOpciones.setGeometry(860,290,200,380)
        panelOpciones.setStyleSheet("QGroupBox{border:1px solid black}")

        label = QLabel("Palabra",panelOpciones)
        label.move(80,30)
        label.setFont(QFont("Arial",10))
        self.campoPalabra = QTextEdit(panelOpciones)
        self.campoPalabra.setGeometry(30,50,140,30)
        self.campoPalabra.setFont(QFont("Arial",10))
        self.campoPalabra.setFrameStyle(1)
        
        label = QLabel("Tipo Arbol",panelOpciones)
        label.move(70,100)
        label.setFont(QFont("Arial",10))
        self.opcionTipoArbol = QComboBox(panelOpciones)
        self.opcionTipoArbol.setGeometry(30,130,140,30)
        self.opcionTipoArbol.setFont(QFont("Arial",10))
        self.opcionTipoArbol.addItems(["Digital","Residuos (TRIES)","Residuos multiples"])



        label = QLabel("paso",panelOpciones)
        label.move(35,265)
        label.setFont(QFont("Arial",10))
        self.opcionPasos = QComboBox(panelOpciones)
        self.opcionPasos.setGeometry(70,260,100,30)
        self.opcionPasos.setFont(QFont("Arial",10))
        self.opcionPasos.currentIndexChanged.connect(self.actualizarCanvas)

        botonGenerar = QPushButton("Generar",panelOpciones)
        botonGenerar.setGeometry(30,300,140,30)
        botonGenerar.setStyleSheet("QPushButton{background-color:#a4c3f5; border:1px solid black;}"
                                   "QPushButton::hover{background-color :#80a7e8;}"
                                   "QPushButton::pressed{background-color:#7499d6; }")
        botonGenerar.clicked.connect(self.generarArbol)
        
    def actualizarCanvas(self):
        if(self.opcionPasos.currentText() != ""):
            self.canvas.arbol = self.pasos[int(self.opcionPasos.currentText())-1]
            self.canvas.activo = True
            self.canvas.update()

    def generarArbol(self):
        #genera el diccionario de claves
        self.alfabeto = {}
        self.pasos = []
        for i in self.campoPalabra.toPlainText().upper():
            self.alfabeto[i] = bin(ord(i)-64).replace("0b","")
            self.alfabeto[i] = ("0"*(5-len(self.alfabeto[i])))+self.alfabeto[i]

        #genera el arbol segun estructura
        if self.opcionTipoArbol.currentText() == "Digital":
            raiz = Nodo()
            nodo = raiz
            for i in self.alfabeto:
                #generar arbol para paso
                digito = 0
                for x in self.alfabeto[i]:
                    digito += 1
                    if len(nodo.hijos) == 0:
                        nodo.hijos.append(Nodo())
                        nodo.hijos.append(Nodo())
                    if nodo.hijos[int(x)].valor == "":
                        nodo.hijos[int(x)].valor = i
                        nodo = raiz
                        break
                    else:
                        nodo = nodo.hijos[int(x)]
                        continue
                if digito  > raiz.niveles:
                    raiz.niveles = digito
                self.pasos.append(copy.deepcopy(raiz))
        elif self.opcionTipoArbol.currentText() == "Residuos (TRIES)":
            print("en desarrollo")
            
        self.opcionPasos.clear()
        for u in range(1,len(self.pasos)+1):
            self.opcionPasos.addItem(str(u))
                    



        

    
        
    
