import sys
from PyQt5 import uic, QtWidgets, QtCore

qtCreatorFile3 = "Ventana_CalcularPromedio.ui"  # Nombre del archivo aquí.
Ui_dialog, QtBaseClass3 = uic.loadUiType(qtCreatorFile3)

class MyDialog(QtWidgets.QDialog, Ui_dialog):
    def __init__(self,  rPrincipal):
        QtWidgets.QDialog.__init__(self)
        Ui_dialog.__init__(self)
        self.setupUi(self)

        # Área de los Signals / Configuracion
        self.acceso = rPrincipal

        self.lblNombre.setText(self.acceso.datosAlumnos[self.acceso.index][0])

        self.btnCalcular.clicked.connect(self.Calcular)

    # Área de los Slots
    def Calcular(self):
        p1 = int(self.txtParcial1.text())
        p2 = int(self.txtParcial2.text())
        p3 = int(self.txtParcial3.text())
        prom = round((p1 + p2 + p3) / 3,2)
        self.acceso.datosAlumnos[self.acceso.index][1] = [p1, p2, p3]
        self.acceso.datosAlumnos[self.acceso.index][2] = prom

        #self.acceso.listAlumnos.clear()
        #for i in self.acceso.datosAlumnos:
            #print(i)
            #self.acceso.listAlumnos.addItem(str(i))
        self.close()