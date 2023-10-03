import sys
from PyQt5 import QtWidgets as QtW
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import QtCore, QtGui

from ventanaIndices import IndicesView

def window():
    app = QApplication(sys.argv)
    w = QtW.QMainWindow()
    w.setGeometry(100,100,1080,720)


    panelOpciones = IndicesView(None)

    ventanaTabs = QtW.QTabWidget(w)
    ventanaTabs.setGeometry(0,0,1080,720)
    ventanaTabs.addTab(panelOpciones,"Indices")
    ventanaTabs.setStyleSheet("QTabBar::Tab{background-color:#F3F3F3;} QTabBar::Tab::hover{background-color:#E5E5E5;} QTabBar::Tab::selected{background-color:#CCCCCC;} ")

    w.show()
    app.exec()

    
	
if __name__ == '__main__':
    window()