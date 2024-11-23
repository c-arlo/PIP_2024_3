import sys
from PyQt5 import uic, QtWidgets, QtCore
import serial

qtCreatorFile = "P6_ConexionArduino3.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btnAccion.clicked.connect(self.accion)
        self.btnLed.clicked.connect(self.controlLed)
        self.arduino = None
        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.lecturaArduino)
        self.estadoLed = 1

    # Área de los Slots
    def accion(self):
        texto = self.btnAccion.text()
        com = "COM" + self.txtCom.text()
        if texto == "CONECTAR" and self.arduino is None:  # CONECTAR
            self.arduino = serial.Serial(port=com, baudrate=9600, timeout=1)
            self.segundoPlano.start(10)
            self.btnAccion.setText("DESCONECTAR")
            self.txtEstado.setText("CONECTADO")
        elif texto == "DESCONECTAR" and self.arduino.isOpen():  # DESCONECTAR
            self.arduino.close()
            self.segundoPlano.stop()
            self.btnAccion.setText("RECONECTAR")
            self.txtEstado.setText("DESCONECTADO")
        else:  # RECONECTAR
            self.arduino.open()
            self.segundoPlano.start(10)
            self.btnAccion.setText("DESCONECTAR")
            self.txtEstado.setText("CONECTADO")

    def lecturaArduino(self):
        try:
            if not self.arduino is None and self.arduino.isOpen():
                if self.arduino.inWaiting():
                    cadena = self.arduino.readline()
                    cadena = cadena.decode()
                    cadena = cadena.strip()
                    if cadena != "":
                        self.datos.addItem(cadena)
                        self.datos.setCurrentRow(self.datos.count() - 1)
        except Exception as err:
            print(err)

    def controlLed(self):
        if self.arduino is not None and self.arduino.isOpen():
            if self.estadoLed == 0:
                self.btnLed.setText("PRENDER")
            else:
                self.btnLed.setText("APAGAR")
            val = "1" if self.estadoLed == 1 else "0" + "\n"
            print(val)
            self.arduino.write(val.encode())
            self.estadoLed = self.estadoLed * -1


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
