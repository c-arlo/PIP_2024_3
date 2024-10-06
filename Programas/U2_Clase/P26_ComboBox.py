import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P26_ComboBox.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.dicc_alumnos = {
            "2206":["Fernando","IN",20],
            "REP01":["Sebastian","ISC",22],
            "MICA2":["Maciel","IC",21]
        }

        self.cb_alumnos.addItem("Fernando","2206")
        self.cb_alumnos.addItem("Sebastian","REP01")
        self.cb_alumnos.addItem("Maciel","MICA2")
        # (1) texto, (2) data - clave (3) index

        self.cambiaIndice()
        self.cb_alumnos.currentIndexChanged.connect(self.cambiaIndice)

    # Área de los Slots
    def cambiaIndice(self):
        texto = self.cb_alumnos.currentText()
        data = self.cb_alumnos.currentData()
        indice = self.cb_alumnos.currentIndex()
        #print(texto + " / " + data + " / " + str(indice))
        self.cargaDatos(data)

    def cargaDatos(self,clave):
        alumno = self.dicc_alumnos[clave]
        self.txt_nombre.setText(alumno[0])
        self.txt_carrera.setText(alumno[1])
        self.txt_edad.setText(str(alumno[2]))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())