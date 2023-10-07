import sys
from PyQt5 import QtWidgets as QtW
from PyQt5.QtWidgets import QApplication
from ArbolesView.ArbolesView import ArbolesView
from BusquedasInView.BusquedasInView import BusquedasInView
from ExternasView.ExternasView import ExternasView

from ventanaIndices import IndicesView
from HashDirectory.ventanaHash import HashView


def window():
    app = QApplication(sys.argv)
    w = QtW.QMainWindow()
    w.setGeometry(100, 100, 1080, 720)
    w.setFixedSize(1080, 720)

    panelOpciones = IndicesView(None)
    panelHash = HashView(None)
    panelArboles = ArbolesView(None)
    panelBusqIn = BusquedasInView(None)
    panelBusqEx = ExternasView(None)

    ventanaTabs = QtW.QTabWidget(w)
    ventanaTabs.setGeometry(0, 0, 1080, 730)
    ventanaTabs.addTab(panelOpciones, "Indices")
    ventanaTabs.addTab(panelHash, "Hash")
    ventanaTabs.addTab(panelArboles, "Arboles")
    ventanaTabs.addTab(panelBusqIn, "Busq. Interna")
    ventanaTabs.addTab(panelBusqEx, "Busq. Externas")
    ventanaTabs.setStyleSheet(
        "QTabBar::Tab{background-color:#F3F3F3;} QTabBar::Tab::hover{background-color:#E5E5E5;} QTabBar::Tab::selected{background-color:#CCCCCC;} ")

    w.show()
    app.exec()


if __name__ == '__main__':
    window()
