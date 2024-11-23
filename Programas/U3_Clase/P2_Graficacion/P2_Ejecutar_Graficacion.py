import sys
from PyQt5 import uic, QtWidgets
import Plantilla_Grafica as interfaz
import matplotlib.pyplot as plt

class MyApp(QtWidgets.QMainWindow, interfaz.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        interfaz.Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btnGraficar.clicked.connect(self.graficar)
        self.btnEstablecer.clicked.connect(self.titulo)
        self.btnGrilla.clicked.connect(self.grilla)
        self.btnLimpiar.clicked.connect(self.limpiar)

        # Estilos Linea
                              # text      , data
        self.cbEstiloL.addItem("Estilo: :", ":")
        self.cbEstiloL.addItem("Estilo: -", "-")
        self.cbEstiloL.addItem("Estilo: --", "--")
        self.cbEstiloL.addItem("Estilo: -.", "-.")
        self.cbEstiloL.currentIndexChanged.connect(self.estiloLinea)

        self.cbColorL.addItem("Negro", "black")
        self.cbColorL.addItem("Rojo", "red")
        self.cbColorL.addItem("Azul", "blue")
        self.cbColorL.addItem("Verde", "green")
        self.cbColorL.currentIndexChanged.connect(self.colorLinea)

        self.sbAnchoL.setValue(1)
        self.sbAnchoL.setMaximum(10)
        self.sbAnchoL.setMinimum(1)
        self.sbAnchoL.setSingleStep(1)
        self.sbAnchoL.valueChanged.connect(self.anchoLinea)

        self.cbEstiloP.addItem("Estilo: cuadrada", "projecting")
        self.cbEstiloP.addItem("Estilo: redondeada", "round")
        self.cbEstiloP.addItem("Estilo: colilla", "butt")
        self.cbEstiloP.currentIndexChanged.connect(self.estiloPunta)

        self.cbEstiloU.addItem("Estilo: redondeada", "round")
        self.cbEstiloU.addItem("Estilo: inglete", "miter")
        self.cbEstiloU.addItem("Estilo: bisel", "bevel")
        self.cbEstiloU.currentIndexChanged.connect(self.estiloUnion)

        # Default linea
        self.estiloLinea = ":"
        self.colorLinea = "black"
        self.anchoLinea = 1
        self.estiloP = "projecting"
        self.estiloU = "round"

        # Estilos marker
        self.cbEstiloM.addItem("Estilo: punto", ".")
        self.cbEstiloM.addItem("Estilo: circulo", "o")
        self.cbEstiloM.addItem("Estilo: estrella", "*")
        self.cbEstiloM.addItem("Estilo: x", "x")
        self.cbEstiloM.addItem("Estilo: diamante", "D")
        self.cbEstiloM.currentIndexChanged.connect(self.estiloMarcador)

        self.cbColorM.addItem("Negro", "black")
        self.cbColorM.addItem("Rojo", "red")
        self.cbColorM.addItem("Azul", "blue")
        self.cbColorM.addItem("Verde", "green")
        self.cbColorM.currentIndexChanged.connect(self.colorMarcador)

        self.sbTamM.setValue(1)
        self.sbTamM.setMaximum(10)
        self.sbTamM.setMinimum(1)
        self.sbTamM.setSingleStep(1)
        self.sbTamM.valueChanged.connect(self.tamMarcador)

        self.cbColorB.addItem("Azul", "blue")
        self.cbColorB.addItem("Negro", "black")
        self.cbColorB.addItem("Rojo", "red")
        self.cbColorB.addItem("Verde", "green")
        self.cbColorB.currentIndexChanged.connect(self.colorBorde)

        self.sbAnchuraB.setValue(1)
        self.sbAnchuraB.setMaximum(10)
        self.sbAnchuraB.setMinimum(1)
        self.sbAnchuraB.setSingleStep(1)
        self.sbAnchuraB.valueChanged.connect(self.tamBorde)

        #Default marcador
        self.estiloM = "."
        self.colorM = "black"
        self.tamMarc = 1
        self.colorB = "blue"
        self.tamB = 1

        # Valores X
        self.sbXmin.setValue(0)
        self.sbXmin.setMaximum(10000)
        self.sbXmin.setMinimum(-10000)
        self.sbXmin.setSingleStep(1)
        self.sbXmin.valueChanged.connect(self.minX)

        self.sbXmax.setValue(10)
        self.sbXmax.setMaximum(10000)
        self.sbXmax.setMinimum(-10000)
        self.sbXmax.setSingleStep(1)
        self.sbXmax.valueChanged.connect(self.maxX)

        self.sbXDiv.setValue(1)
        self.sbXDiv.setMaximum(10)
        self.sbXDiv.setMinimum(1)
        self.sbXDiv.setSingleStep(1)
        self.sbXDiv.valueChanged.connect(self.divisionesX)

        # Valores Y
        self.sbYmin.setValue(0)
        self.sbYmin.setMaximum(10000)
        self.sbYmin.setMinimum(-10000)
        self.sbYmin.setSingleStep(1)
        self.sbYmin.valueChanged.connect(self.minY)

        self.sbYmax.setValue(10)
        self.sbYmax.setMaximum(10000)
        self.sbYmax.setMinimum(-10000)
        self.sbYmax.setSingleStep(1)
        self.sbYmax.valueChanged.connect(self.maxY)

        self.sbYDiv.setValue(1)
        self.sbYDiv.setMaximum(10)
        self.sbYDiv.setMinimum(1)
        self.sbYDiv.setSingleStep(1)
        self.sbYDiv.valueChanged.connect(self.divisionesY)

        # Default X & Y
        self.xMax = 10
        self.xMin = 0
        self.xDivisiones = 1
        self.yMax = 10
        self.yMin = 0
        self.yDivisiones = 1

        # Grilla
        self.btnGrilla.setText("ON")

    # Área de los Slots
    #X Slots
    def minX(self):
        self.xMin = self.sbXmin.value()  # obtiene el nuevo valor para el argumento
        #self.limpiar()  # borra grafica anterior
        self.graficar()  # genera la nueva grafica

    def maxX(self):
        self.xMax = self.sbXmax.value()
        self.sbXDiv.setMaximum(self.xMax)
        self.graficar()

    def divisionesX(self):
        self.xDivisiones = self.sbXDiv.value()
        self.graficar()

    #Y Slots
    def minY(self):
        self.yMin = self.sbYmin.value()
        self.graficar()

    def maxY(self):
        self.yMax = self.sbYmax.value()
        self.sbYDiv.setMaximum(self.yMax)
        self.graficar()

    def divisionesY(self):
        self.yDivisiones = self.sbYDiv.value()
        self.graficar()

    #Slots linea
    def estiloLinea(self):
        estilo = self.cbEstiloL.currentData()
        self.estiloLinea = estilo
        self.graficar()

    def colorLinea(self):
        color = self.cbColorL.currentData()
        self.colorLinea = color
        self.graficar()

    def anchoLinea(self):
        ancho = self.sbAnchoL.value()
        self.anchoLinea = ancho
        self.graficar()

    def estiloPunta(self):
        punta = self.cbEstiloP.currentData()
        self.estiloP = punta
        self.graficar()

    def estiloUnion(self):
        union = self.cbEstiloU.currentData()
        self.estiloU = union
        print(self.estiloU)
        self.graficar()

    #Slots marcador
    def estiloMarcador(self):
        m = self.cbEstiloM.currentData()
        self.estiloM = m
        self.graficar()

    def colorMarcador(self):
        c = self.cbColorM.currentData()
        self.colorM = c
        self.graficar()

    def tamMarcador(self):
        t = self.sbTamM.value()
        self.tamMarc = t
        self.graficar()

    def colorBorde(self):
        c = self.cbColorB.currentData()
        self.colorB = c
        self.graficar()

    def tamBorde(self):
        t = self.sbAnchuraB.value()
        self.tamB = t
        self.graficar()

    #Slots general
    def limpiar(self):
        plt.cla()  # borra_todo
        self.canvas.draw()  # vuelve a dibujar

    def titulo(self):
        t = self.txtTitulo.text()
        self.ax.set_title(t)  # establece el titulo
        self.canvas.draw()  # aplica los cambios

    def grilla(self):
        texto = self.btnGrilla.text()
        if texto == "OFF":
            self.btnGrilla.setText("ON")
            plt.grid(False)
        else:  # ON
            self.btnGrilla.setText("OFF")
            plt.grid(True)
        self.canvas.draw()

    def graficar(self):
        self.limpiar()

        polinomio = self.txtPoli.text()  # Ej: 2x^2+3x+4
        polinomio = polinomio.replace("^", "**")  # 2x**2+3x+4

        # tabular...  valores de X con base en los cuales pueda obtener los valores de y
        X = [i for i in range(self.xMin, self.xMax + 1)]  # lista de comprension
        #print("Valores de X: ")
        #print(X)

        # self.sbXmax.setValue(X[-1])

        # y = polinomio.replace("x","*("+str(x[0])+")")
        y = [eval(polinomio.replace("x", "*(" + str(x) + ")")) for x in X]
        #print("Valores de Y: ")
        #print(y)

        # self.sbYmax.setValue(y[-1])

        self.ax.plot(X, y,
                     linestyle=self.estiloLinea,  #: - -- -.
                     color=self.colorLinea,  # color de la linea
                     linewidth=self.anchoLinea,  # tamaño de la linea
                     dash_capstyle=self.estiloP,  # dash or solid : "butt" "round" "projecting"
                     dash_joinstyle=self.estiloU,
                     #marker_joinstyle=self.estiloU,# dash or solid : "miter" "round" "bevel"
                     marker=self.estiloM,  # o . *  x   1
                     markersize=self.tamMarc,
                     markerfacecolor=self.colorM,  # color interno del marcador
                     markeredgewidth=self.tamB,  # tamaño del borde del marcador
                     markeredgecolor=self.colorB  # color del borde del marcador
                     )

        # Establecer los limites
        self.ax.set_xlim(self.xMin, self.xMax)
        self.ax.set_ylim(self.yMin, self.yMax)

        self.ax.set_xlabel("Eje X")
        self.ax.set_ylabel("Eje Y")

        # totalelementosenX/totaldivisionesDeseadas = 8
        # mediante un ciclo se obtiene:

        # si comienzo con xmin en 0 seria:
        # xtick = [0, 10, 20, 30, 40, 50, 60, 70, 80]

        # si comienzo con xmin en n seria:
        xtick = []
        #for i in range(self.xMin, self.xMax, self.xDivisiones):
        #    xtick.append(i)
        #print(self.xMax/self.xDivisiones)
        for i in range(self.xMin, self.xMax, int(self.xMax/self.xDivisiones)):
            xtick.append(i)

        #print("Ticks para X: ")
        #print(xtick)

        # xtick = [2, 5, 15, 25, 35, 45, 55, 65, 75, 85]

        self.ax.set_xticks(xtick)

        ytick = []
        #for i in range(self.yMin, self.yMax, self.yDivisiones):
        #    ytick.append(i)
        for i in range(self.yMin, self.yMax, int(self.yMax/self.yDivisiones)):
            ytick.append(i)
        #print("Ticks para Y: ")
        #print(ytick)

        self.ax.set_yticks(ytick)  # NOTA.. CHECK!

        # una posibilidad para establecer los ticks sería:
        # Tomar el conjunto y dividirlo entre el total de "divisiones" que el usuario desee

        self.canvas.draw()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())