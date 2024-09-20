import sys
from PyQt5 import uic, QtWidgets, QtGui
qtCreatorFile = "P7_EjemploVerticalSlider.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Área de los Signals
        self.vSlider.setMinimum(0)
        self.vSlider.setMaximum(255)
        self.vSlider.setSingleStep(1)
        self.vSlider.setValue(0)

        self.vSlider.valueChanged.connect(self.cambiarValor)
        self.txt_valor.setText(str(self.vSlider.value()))

    def cambiarValor(self):
        self.txt_valor.setText(str(self.vSlider.value()))

    # Área de los Slots
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())