import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P21_RadioButtonTest.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_validar.clicked.connect(self.validar)

    # Área de los Slots
    def validar(self):
        opciones = [
            self.rb_opcionA.isChecked(),
            self.rb_opcionB.isChecked(),
            self.rb_opcionC.isChecked(),
            self.rb_opcionD.isChecked()
        ]
        print(opciones)
        if max(opciones) == 1:
            index = opciones.index(1)
            print(index)
        else:
            print("Debes seleccionar una opcion..")






if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

