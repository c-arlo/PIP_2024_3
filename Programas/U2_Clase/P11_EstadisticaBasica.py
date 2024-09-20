import statistics
import sys
from PyQt5 import uic, QtWidgets, QtGui
qtCreatorFile = "P11_EstadisticaBasica.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        
        # Área de los Signals
        self.btn_prom.clicked.connect(self.operacion)
        self.btn_med.clicked.connect(self.operacion)
        self.btn_desv.clicked.connect(self.operacion)
        self.btn_var.clicked.connect(self.operacion)
        self.btn_mayor.clicked.connect(self.operacion)
        self.btn_menor.clicked.connect(self.operacion)

        self.txt_datos.textChanged.connect(self.validar)

    # Área de los Slots

    def validar(self):
        v = self.txt_datos.text()
        perm = ["0","1","2","3","4","5",
                "6","7","8","9"," "]
        if "-" in v:
            m = QtWidgets.QMessageBox()
            m.setText("Favor de ingresar solo numeros y espacios")
            m.exec()

    def operacion(self):
        obj = self.sender()
        nombre_obj = obj.objectName()

        datos = self.txt_datos.text().split(" ")
        datos = [int(i) for i in datos]

        match nombre_obj:
            case "btn_prom":
                self.txt_res.setText(str(round(statistics.mean(datos), 2)))
            case "btn_med":
                self.txt_res.setText(str(round(statistics.median(datos), 2)))
            case "btn_desv":
                self.txt_res.setText(str(round(statistics.stdev(datos), 2)))
            case "btn_var":
                self.txt_res.setText(str(round(statistics.variance(datos), 2)))
            case "btn_mayor":
                self.txt_res.setText(str(max(datos)))
            case "btn_menor":
                self.txt_res.setText(str(min(datos)))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())