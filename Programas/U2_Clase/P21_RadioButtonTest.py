import sys
from PyQt5 import uic, QtWidgets
import P20_ProcesarPreguntas as p20

qtCreatorFile = "P21_RadioButtonTest.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.preguntas = p20.procesar_preguntas()
        self.index = 0
        self.opcion = "Nada"
        self.calif = 0

        self.rb_opcionA.toggled.connect(self.getOpcion)
        self.rb_opcionB.toggled.connect(self.getOpcion)
        self.rb_opcionC.toggled.connect(self.getOpcion)
        self.rb_opcionD.toggled.connect(self.getOpcion)
        self.btn_validar.clicked.connect(self.validar)
        self.cambiar_preguntas()


    # Área de los Slots
    def cambiar_preguntas(self):
        self.txt_pregunta.setText(self.preguntas[self.index][0])
        self.rb_opcionA.setText(self.preguntas[self.index][2][0])
        self.rb_opcionB.setText(self.preguntas[self.index][2][1])
        self.rb_opcionC.setText(self.preguntas[self.index][2][2])
        self.rb_opcionD.setText(self.preguntas[self.index][2][3])

    def getOpcion(self):
        obj = self.sender()
        self.opcion = obj.text()

    def validar(self):
        #print(self.preguntas)
        if self.opcion == self.preguntas[self.index][1]:
            self.calif += 1
        else:
            pass
        self.index += 1
        if self.index >= len(self.preguntas):
            m = "Obtuvo una calificacion de {0}/10".format(self.calif)
            self.mensaje(m)
            sys.exit()
        else:
            self.cambiar_preguntas()

    def mensaje(self, m):
        msj = QtWidgets.QMessageBox()
        msj.setText(m)
        msj.exec()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

