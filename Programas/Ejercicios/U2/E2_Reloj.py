import sys
from PyQt5 import uic, QtWidgets, QtCore

qtCreatorFile = "E2_Reloj.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.hora = 0
        self.minutos = 0

        self.lcdHora.setNumDigits(2)
        self.lcdMinutos.setNumDigits(2)
        self.lcdHora.display(self.hora)
        self.lcdMinutos.display(self.minutos)

        self.sbHora.setMinimum(0)
        self.sbHora.setMaximum(23)
        self.sbHora.setSingleStep(1)
        self.sbHora.setValue(0)

        self.sbMinutos.setMinimum(0)
        self.sbMinutos.setMaximum(59)
        self.sbMinutos.setSingleStep(1)
        self.sbMinutos.setValue(0)

        self.sbHora.valueChanged.connect(self.cambiarPeriodo)

        self.horaAlarma = -1
        self.minAlarma = -1
        self.btnAgregar.clicked.connect(self.setAlarma)

        self.tiempo = QtCore.QTimer()
        self.tiempo.timeout.connect(self.contarMin)
        self.tiempo.start(10)

    # Área de los Slots
    def setAlarma(self):
        if self.btnAgregar.text() == "AGREGAR":
            self.horaAlarma = int(self.sbHora.value())
            self.minAlarma = int(self.sbMinutos.value())
            self.sbHora.setEnabled(False)
            self.sbMinutos.setEnabled(False)
            self.btnAgregar.setText("ELIMINAR")
        else:
            self.horaAlarma = -1
            self.minAlarma = -1
            self.sbHora.setEnabled(True)
            self.sbMinutos.setEnabled(True)
            self.btnAgregar.setText("AGREGAR")

    def cambiarPeriodo(self):
        if self.sbHora.value() < 13:
            self.lblPeriodo2.setText("A.M.")
        else:
            self.lblPeriodo2.setText("P.M.")

    def contarMin(self):
        self.lcdMinutos.display(self.minutos)
        self.lcdHora.display(self.hora)
        self.minutos += 1
        if self.minutos == 60:
            self.minutos = 0
            self.hora += 1
        if self.hora == 24:
            self.hora = 0
        if self.hora < 13:
            self.lblPeriodo1.setText("A.M.")
        else:
            self.lblPeriodo1.setText("P.M.")
        if self.hora == self.horaAlarma and self.minutos == self.minAlarma:
            self.mensaje("Alarma")


    def mensaje(self,texto):
        m = QtWidgets.QMessageBox()
        m.setText(texto)
        m.exec()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

