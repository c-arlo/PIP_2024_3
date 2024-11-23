import sys
from PyQt5 import uic, QtWidgets, QtCore

qtCreatorFile3 = "Ventana_VisualizarDatos.ui"  # Nombre del archivo aquí.
Ui_dialog, QtBaseClass3 = uic.loadUiType(qtCreatorFile3)

class MyDialog(QtWidgets.QDialog, Ui_dialog):
    def __init__(self,  rPrincipal):
        QtWidgets.QDialog.__init__(self)
        Ui_dialog.__init__(self)
        self.setupUi(self)

        # Área de los Signals / Configuracion
        self.acceso = rPrincipal
        archivo = open("respaldo_interno.sebas")

        for fila in archivo:
            f = fila.split("/")
            c = ("Nombre: " + f[0] +
                 " | Parciales: " + f[1] + " / " + f[2] + " / " + f[3] +
                 " | Prom: " + f[4])
            self.listAlumnos.addItem(c)


    # Área de los Slots
