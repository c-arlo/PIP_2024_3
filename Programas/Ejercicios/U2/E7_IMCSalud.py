import sys

import numpy
from PyQt5 import uic, QtWidgets, QtGui

qtCreatorFile = "E7_IMCSalud.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.peso = 0
        self.altura = 0

        self.btn_calc.clicked.connect(self.calcular)
        self.cb_peso.currentIndexChanged.connect(self.cambiarMedida)
        self.cb_altura.currentIndexChanged.connect(self.cambiarMedida)

    # Área de los Slots
    def calcular(self):
        self.peso = float(self.txt_peso.text())
        self.altura = float(self.txt_altura.text())
        if self.peso == 0 or self.altura == 0:
            self.mensaje("Ingrese un peso y altura valida")
            return
        imc = self.peso / self.altura**2
        if self.cb_peso.currentIndex() == 1:
            imc *= 703
        recom = ""
        if imc < 18.5:
            recom = ("Su IMC es {0} lo que indica que su peso esta en la categoría de peso bajo "
                     "por lo que se recomendia comer con más frecuencia, elegir comer alimentos "
                     "más nutritivos, agregar carbohidratos y grasas saludables a tu dieta").format(round(imc, 1))
            self.lblIMC.setPixmap(QtGui.QPixmap(":/IMC/IMC_Bajo.png"))
        elif 18.5 < imc < 24.9:
            recom = ("Su IMC es {0} lo que indica que su peso esta en la categoría de peso saludable "
                     "por lo que se recomienda hacer ejercicio regularmente, mantener una dieta "
                     "equilibrada y controlar el consumo de grasas saturadas").format(round(imc, 1))
            self.lblIMC.setPixmap(QtGui.QPixmap(":/IMC/IMC_Normal.png"))
        elif 25.0 < imc < 29.9:
            recom = ("Su IMC es {0} lo que indica que su peso esta en la categoría de sobrepeso "
                     "por lo que se recomienda reducir el tamaño de porciones de comida, "
                     "comenzar a hacer ejercicio regularmente y modificar tu dieta para contener "
                     "alimentos nutritivos").format(round(imc, 1))
            self.lblIMC.setPixmap(QtGui.QPixmap(":/IMC/IMC_Sobrepeso.png"))
        elif 30 < imc:
            recom = ("Su IMC es {0} lo que indica que su peso esta en la categoría de obesidad "
                     "comenzar a hacer ejercicios adecuados, evitar el consumo de alimentos "
                     "procesados o que contengan grasas saturadas y reducir drasticamente "
                     "el tamaño de las porciones").format(round(imc, 1))
            self.lblIMC.setPixmap(QtGui.QPixmap(":/IMC/IMC_Obesidad.png"))
        self.txtIMC.setText(recom)


    def cambiarMedida(self):
        sender = self.sender().objectName()
        if sender == "cb_peso":
            self.cb_altura.setCurrentIndex(self.cb_peso.currentIndex())
            if self.cb_peso.currentIndex() == 0:
                self.peso = float(self.txt_peso.text())
                self.peso /= 2.205
                self.txt_peso.setText(str(round(self.peso, 2)))
            else:
                self.peso = float(self.txt_peso.text())
                self.peso *= 2.205
                self.txt_peso.setText(str(round(self.peso, 2)))
        else:
            self.cb_peso.setCurrentIndex(self.cb_altura.currentIndex())
            if self.cb_altura.currentIndex() == 0:
                self.altura = float(self.txt_altura.text())
                self.altura /= 39.37
                self.txt_altura.setText(str(round(self.altura, 2)))
            else:
                self.altura = float(self.txt_altura.text())
                self.altura *= 39.37
                self.txt_altura.setText(str(round(self.altura, 2)))

    def mensaje(self,texto):
        m = QtWidgets.QMessageBox()
        m.setText(texto)
        m.exec()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
