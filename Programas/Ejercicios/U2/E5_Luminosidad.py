import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "E5_Luminosidad.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.valor_lumi.setMinimum(0)
        self.valor_lumi.setMaximum(255)
        self.valor_lumi.setSingleStep(1)
        self.valor_lumi.setValue(0)
        self.valor_lumi.valueChanged.connect(self.cambiarLumi)

        self.lumi = 0

        self.cambiarLumi()
        self.blur_effect = QtWidgets.QGraphicsBlurEffect()
        self.blur_effect.setBlurRadius(15)
        self.lbl_lumi.setGraphicsEffect(self.blur_effect)

        # Área de los Slots

    def cambiarLumi(self):
        self.lumi = self.valor_lumi.value()
        # background-color: rgb(97, 80, 255);
        estilo = ("background-color: rgb(" + str(self.lumi) +
                  "," + str(self.lumi) + "," + str(self.lumi) + "); border-radius:90px")
        self.lbl_lumi.setStyleSheet(estilo)
        self.txt_lumi.setText(str(self.lumi))


    # Área de los Slots
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

