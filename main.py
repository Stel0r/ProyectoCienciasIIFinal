import sys
from PyQt5 import QtWidgets as QtW
from PyQt5.QtWidgets import QApplication

from ventanaIndices import IndicesView
from HashDirectory.ventanaHash import HashView


def window():
    app = QApplication(sys.argv)
    w = QtW.QMainWindow()
    w.setGeometry(100, 100, 1080, 720)

    panelOpciones = IndicesView(None)
    panelHash = HashView(None)

    ventanaTabs = QtW.QTabWidget(w)
    ventanaTabs.setGeometry(0, 0, 1080, 730)
    ventanaTabs.addTab(panelOpciones, "Indices")
    ventanaTabs.addTab(panelHash, "Hash")
    ventanaTabs.setStyleSheet(
        "QTabBar::Tab{background-color:#F3F3F3;} QTabBar::Tab::hover{background-color:#E5E5E5;} QTabBar::Tab::selected{background-color:#CCCCCC;} ")

    w.show()
    app.exec()


if __name__ == '__main__':
    window()
