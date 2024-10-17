import random
import sys
from PyQt5 import uic, QtWidgets, QtCore

qtCreatorFile = "E12_ExamenAritmetica.ui"  # Nombre del archivo
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.diccOper = {
            0: "+",
            1: "-",
            2: "*",
        }
        self.name = ""
        self.calif = 0
        self.res = 0
        self.noper = 1

        # Signals
        self.btnStart.clicked.connect(self.start)
        self.btnResp.clicked.connect(self.respuesta)

    # Slots
    def start(self):
        o = self.btnStart.text()
        if o == "Iniciar":
            self.txtName.setEnabled(False)
            self.txtResp.setEnabled(True)
            self.btnResp.setEnabled(True)
            self.name = self.txtName.text()
            self.btnStart.setText("Reiniciar")
            self.operacion()
        else:
            self.txtName.setEnabled(True)
            self.txtResp.setEnabled(False)
            self.btnResp.setEnabled(False)
            self.name = ""
            self.txtName.setText("")
            self.txtResp.setText("")
            self.btnStart.setText("Iniciar")
            self.lbOper.setText("Ingrese su nombre para comenzar")
        self.calif = 0

    def operacion(self):
        x = random.randrange(1, 10)
        y = random.randrange(1, 10)
        o = random.randrange(0, 3)
        oper = str(x) + self.diccOper[o] + str(y)
        self.lbOper.setText(str(self.noper) + ") " + oper + " = ?")
        self.res = eval(oper)
        print(self.res)

    def respuesta(self):
        user = int(self.txtResp.text())
        if user == self.res:
            self.calif += 1
        self.noper += 1
        self.txtResp.setText("")
        if self.noper > 10:
            self.mensaje("Nombre: " + self.name +
                         "\nCalificacion: " + str(self.calif))
            self.start()
        else:
            self.operacion()

    def mensaje(self, texto):
        m = QtWidgets.QMessageBox()
        m.setText(texto)
        m.exec()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
