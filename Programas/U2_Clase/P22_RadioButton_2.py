import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P22_RadioButton_2.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        #self.rb_soltero.clicked.connect(self.soltero)
        #self.rb_casado.clicked.connect(self.casado)
        #self.rb_union.clicked.connect(self.union)

        self.rb_soltero.toggled.connect(self.soltero)
        self.rb_casado.toggled.connect(self.casado)
        self.rb_union.toggled.connect(self.union)

    # Área de los Slots
    def soltero(self):
        check = self.rb_soltero.isChecked()
        if check:
            print("Soltero")
        else:
            print("Se desmarco soltero")
    def casado(self):
        check = self.rb_casado.isChecked()
        if check:
            print("Casado")
    def union(self):
        check = self.rb_union.isChecked()
        if check:
            print("Union libre")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())