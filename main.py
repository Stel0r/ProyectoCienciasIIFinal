import sys
from PyQt5 import QtWidgets as QtW
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import QtCore, QtGui;

def window():
    app = QApplication(sys.argv)
    w = QtW.QMainWindow()
    
    panelOpciones = QtW.QGroupBox(w)
    panelOpciones.setGeometry(0,0,200,200)
    panelOpciones.setStyleSheet("background-color:blue")

    w.setGeometry(300,300,1080,720)
    w.setWindowTitle("Proyecto Ciencias")
    w.show()
    sys.exit(app.exec_())
	
if __name__ == '__main__':
    window()