import sys
from PyQt5 import uic, QtWidgets, QtGui
qtCreatorFile = "P4_DatosDeImagenes_Completo.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Área de los Signals

        self.lista_imagenes = {
            0:":/Catos/duende.jpg", # 1
            1:":/Catos/5_peso.jpg", # 2
            2: ":/Frutas/banana.png", # 3
            3: ":/Frutas/pina.png" # 4
        }

        self.datos_imagenes = {
            0: ["nombre1","edad1","ocupacion1","pasatiempo1"],  # 1
            1: ["nombre2","edad2","ocupacion2","pasatiempo2"], # 2
            2: ["nombre3","edad3","ocupacion3","pasatiempo3"],
            3: ["nombre4","edad4","ocupacion4","pasatiempo4"]# 3
        }

        self.clave_imagen = 0
        self.Imagen.setPixmap(QtGui.QPixmap(self.lista_imagenes[self.clave_imagen]))
        self.btn_atras.clicked.connect(self.atras)
        self.btn_adelante.clicked.connect(self.adelante)

        self.txt_nombre.setText(self.datos_imagenes[self.clave_imagen][0])
        self.txt_edad.setText(self.datos_imagenes[self.clave_imagen][1])
        self.txt_ocupacion.setText(self.datos_imagenes[self.clave_imagen][2])
        self.txt_pasatiempo.setText(self.datos_imagenes[self.clave_imagen][3])

    def atras(self):
            if self.clave_imagen >= min(self.lista_imagenes)+1 : #self.clave_imagen >= 2 / no por indices
                self.clave_imagen -= 1
                self.Imagen.setPixmap(QtGui.QPixmap(self.lista_imagenes[self.clave_imagen]))
            self.txt_nombre.setText(self.datos_imagenes[self.clave_imagen][0])
            self.txt_edad.setText(self.datos_imagenes[self.clave_imagen][1])
            self.txt_ocupacion.setText(self.datos_imagenes[self.clave_imagen][2])
            self.txt_pasatiempo.setText(self.datos_imagenes[self.clave_imagen][3])

    def adelante(self):
        if self.clave_imagen < len(self.lista_imagenes)-1: #self.clave_imagen < 3 / no por indices
            self.clave_imagen += 1
            self.Imagen.setPixmap(QtGui.QPixmap(self.lista_imagenes[self.clave_imagen]))
            self.txt_nombre.setText(self.datos_imagenes[self.clave_imagen][0])
            self.txt_edad.setText(self.datos_imagenes[self.clave_imagen][1])
            self.txt_ocupacion.setText(self.datos_imagenes[self.clave_imagen][2])
            self.txt_pasatiempo.setText(self.datos_imagenes[self.clave_imagen][3])


    # Área de los Slots
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())