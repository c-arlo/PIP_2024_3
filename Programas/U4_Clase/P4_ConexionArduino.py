import sys
from PyQt5 import uic, QtWidgets
import serial

qtCreatorFile = "P4_ConexionArduino.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btnAccion.clicked.connect(self.accion)
        self.arduino = None

    # Área de los Slots
    def accion(self):
        texto = self.btnAccion.text()
        com = self.txtCom.text()
        if texto == "CONECTAR" and self.arduino is None:
            self.arduino = serial.Serial(port=com, baudrate=9600, timeout=1)
            self.btnAccion.setText("DESCONECTAR")
            self.txtEstado.setText("CONECTADO")
        elif texto == "DESCONECTAR" and self.arduino.isOpen():
            self.arduino.close()
            self.btnAccion.setText("RECONECTAR")
            self.txtEstado.setText("DESCONECTADO")
        else:
            self.arduino.open()
            self.btnAccion.setText("DESCONECTAR")
            self.txtEstado.setText("CONECTADO")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())