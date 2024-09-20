import sys
from PyQt5 import uic, QtWidgets, QtGui
qtCreatorFile = "P9_OperacionesAritmeticas.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Área de los Signals
        self.btn_sumar.clicked.connect(self.sumar)
        self.btn_restar.clicked.connect(self.restar)
        self.btn_multiplicar.clicked.connect(self.multiplicar)
        self.btn_dividir.clicked.connect(self.dividir)

    # Área de los Slots
    def sumar(self):
        a = int(self.txt_a.text())
        b = int(self.txt_b.text())
        self.txt_res.setText(str(a+b))

    def restar(self):
        a = int(self.txt_a.text())
        b = int(self.txt_b.text())
        self.txt_res.setText(str(a-b))

    def multiplicar(self):
        a = int(self.txt_a.text())
        b = int(self.txt_b.text())
        self.txt_res.setText(str(a*b))

    def dividir(self):
        a = int(self.txt_a.text())
        b = int(self.txt_b.text())
        self.txt_res.setText(str(a/b))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())