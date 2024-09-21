import sys, random as rnd
from PyQt5 import uic, QtWidgets, QtCore

qtCreatorFile = "P18_ExamenTablas.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.lista_nombres = [
            "Angel S.", "Jazmin", "Carolina", "Fernando", "Dilan", "Maciel", "Yahir", "Carlos", "Angel A."
        ]
        self.index_nombre = 0
        self.txt_nombre.setText(self.lista_nombres[self.index_nombre])
        self.txt_nombre.setEnabled(False)

        self.btn_control.clicked.connect(self.control)

        self.hiloSegundoPlano = QtCore.QTimer()
        self.hiloSegundoPlano.timeout.connect(self.contar)

        self.txt_tabla.setEnabled(False)
        self.txt_numero.setEnabled(False)
        self.txt_resultado.setEnabled(False)
        self.btn_validar.setEnabled(False)
        self.txt_resultado.setText("")

        self.resp_validada = 1
        self.btn_validar.clicked.connect(self.valida)

    def valida(self):
        resultado = self.tabla * self.numero
        resp_usuario = int(self.txt_resultado.text())
        if resultado == resp_usuario:
            self.mensaje("Respuesta Correcta")
            self.resp_validada = 1
        else:
            self.mensaje("Respuesta incorrecta")
            self.resp_validada = 0

    def mensaje(self, m):
        msj = QtWidgets.QMessageBox()
        msj.setText(m)
        msj.exec()

    def control(self):
        texto_boton = self.btn_control.text()
        if texto_boton == "INICIAR" and self.resp_validada == 1:
            self.index_nombre = 0
            self.hiloSegundoPlano.start(10) #inicia el hilo en segundo plano
            self.btn_control.setText("DETENER")
            self.txt_resultado.setText("")
        elif texto_boton == "INICIAR" and self.resp_validada == 0:
            self.index_nombre = 0
            self.hiloSegundoPlano.start(10)  # inicia el hilo en segundo plano
            self.btn_control.setText("DETENER")
            self.txt_resultado.setText("")
            self.txt_resultado.setEnabled(False)
            self.btn_validar.setEnabled(False)
        else:
            self.hiloSegundoPlano.stop()
            self.btn_control.setText("INICIAR")
            self.txt_resultado.setEnabled(True)
            self.btn_validar.setEnabled(True)
            self.genera_pregunta()
            self.resp_validada = 0

    def genera_pregunta(self):
        self.tabla = -1
        self.numero = -1
        self.tabla = rnd.randint(1, 10)
        self.numero = rnd.randint(1, 10)
        self.txt_tabla.setText(str(self.tabla))
        self.txt_numero.setText(str(self.numero))

    def contar(self):
        self.index_nombre += 1
        self.index_nombre %= len(self.lista_nombres)
        self.txt_nombre.setText(self.lista_nombres[self.index_nombre])

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

