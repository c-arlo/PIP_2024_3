import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "E1_ValorMayor.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("E1 - Obtener el valor mayor")
        # Área de los Signals
        try:
            self.btn_calc.clicked.connect(self.calcular)
        except Exception as e:
            print(e)

    # Área de los Slots
    def calcular(self):
        nums = self.txt_nums.text()
        list_nums = nums.split(",")
        mayor = max([int(i) for i in list_nums])
        self.txt_res.setText(str(mayor))
        print(mayor)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())