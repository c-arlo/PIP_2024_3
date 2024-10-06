import sys
from PyQt5 import uic, QtWidgets, QtGui
qtCreatorFile = "E6_CambioUnidades.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.txtMm.editingFinished.connect(self.cambiarLong)
        self.txtCm.editingFinished.connect(self.cambiarLong)
        self.txtM.editingFinished.connect(self.cambiarLong)
        self.txtKm.editingFinished.connect(self.cambiarLong)

        self.txtMg.editingFinished.connect(self.cambiarMasa)
        self.txtG.editingFinished.connect(self.cambiarMasa)
        self.txtKg.editingFinished.connect(self.cambiarMasa)
        self.txtT.editingFinished.connect(self.cambiarMasa)

        self.txtCel.editingFinished.connect(self.cambiarTemp)
        self.txtFar.editingFinished.connect(self.cambiarTemp)
        self.txtKel.editingFinished.connect(self.cambiarTemp)

    # Área de los Slots
    def cambiarLong(self):
        obj = self.sender().objectName()
        match obj:
            case "txtMm":
                long = float(self.txtMm.text())
                self.txtCm.setText(str(round(long*10**-1, 10)))
                self.txtM.setText(str(round(long*10**-3, 10)))
                self.txtKm.setText(str(round(long*10**-6, 10)))
            case "txtCm":
                long = float(self.txtCm.text())
                self.txtMm.setText(str(round(long*10**1, 10)))
                self.txtM.setText(str(round(long*10**-2, 10)))
                self.txtKm.setText(str(round(long*10**-5, 10)))
            case "txtM":
                long = float(self.txtM.text())
                self.txtMm.setText(str(round(long*10**3, 10)))
                self.txtCm.setText(str(round(long*10**2, 10)))
                self.txtKm.setText(str(round(long*10**-3, 10)))
            case "txtKm":
                long = float(self.txtKm.text())
                self.txtMm.setText(str(round(long*10**6, 10)))
                self.txtCm.setText(str(round(long*10**5, 10)))
                self.txtM.setText(str(round(long*10**3, 10)))

    def cambiarMasa(self):
        obj = self.sender().objectName()
        match obj:
            case "txtMg":
                long = float(self.txtMg.text())
                self.txtG.setText(str(round(long*10**-3, 10)))
                self.txtKg.setText(str(round(long*10**-6, 10)))
                self.txtT.setText(str(round(long*10**-9, 10)))
            case "txtG":
                long = float(self.txtG.text())
                self.txtMg.setText(str(round(long*10**3, 10)))
                self.txtKg.setText(str(round(long*10**-3, 10)))
                self.txtT.setText(str(round(long*10**-6, 10)))
            case "txtKg":
                long = float(self.txtKg.text())
                self.txtMg.setText(str(round(long*10**6, 10)))
                self.txtG.setText(str(round(long*10**3, 10)))
                self.txtT.setText(str(round(long*10**-3, 10)))
            case "txtT":
                long = float(self.txtT.text())
                self.txtMg.setText(str(round(long*10**9, 10)))
                self.txtG.setText(str(round(long*10**6, 10)))
                self.txtKg.setText(str(round(long*10**3, 10)))

    def cambiarTemp(self):
        obj = self.sender().objectName()
        match obj:
            case "txtCel":
                temp = float(self.txtCel.text())
                self.txtFar.setText(str(round(9*temp/5+32, 2)))
                self.txtKel.setText(str(round(temp+273.15, 2)))
            case "txtFar":
                temp = float(self.txtFar.text())
                self.txtCel.setText(str(round(5*(temp-32)/9, 2)))
                self.txtKel.setText(str(round(5*(temp-32)/9+273.15, 2)))
            case "txtKel":
                temp = float(self.txtKel.text())
                self.txtCel.setText(str(round(temp-273.15, 2)))
                self.txtFar.setText(str(round(9*(temp-273.15)/5+32, 2)))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())