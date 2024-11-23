import sys
from PyQt5 import uic, QtWidgets, QtCore

qtCreatorFile3 = "Ventana_AgregarAlumno.ui"  # Nombre del archivo aquí.
Ui_dialog, QtBaseClass3 = uic.loadUiType(qtCreatorFile3)

class MyDialog(QtWidgets.QDialog, Ui_dialog):
    def __init__(self,  rPrincipal):
        QtWidgets.QDialog.__init__(self)
        Ui_dialog.__init__(self)
        self.setupUi(self)

        # Área de los Signals / Configuracion
        self.acceso = rPrincipal

        self.btnAgregar.clicked.connect(self.Agregar)

    # Área de los Slots
    def Agregar(self):
        n = self.txtNombre.text()

        self.acceso.datosAlumnos.append([n, [0, 0, 0], "NA"])
        self.acceso.listAlumnos.addItem(n)

        #self.acceso.usuario = None

        self.close()