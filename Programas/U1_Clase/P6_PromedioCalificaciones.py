import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P6_PromedioCalificaciones.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("P6_PromedioCalificaciones")

        # Área de los Signals (Eventos)
        try:
            self.btn_calcular.clicked.connect(self.calcular)
        except Exception as e:
            print(e)


    # Área de los Slots (Funciones)
    def calcular(self):
        calif = self.txt_calificaciones.text() #str
        lista_calif = calif.split(" ") #separa cadena en lista de strs
        lista_calif = [int(i) for i in lista_calif] #lista str a lista de int
        r = sum(lista_calif) / len(lista_calif)
        self.txt_resultado.setText(str(r))

    """
    def mensaje(self,texto):
        m = QtWidgets.QMessageBox()
        m.setWindowTitle("Resultado")
        m.setText(texto)
        m.exec()
    """

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())