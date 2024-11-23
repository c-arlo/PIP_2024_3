import serial as ser
import matplotlib.pyplot as plt

arduino = ser.Serial(port="COM6", baudrate=9600, timeout=1)
tot_lect = int(input("Ingresa el total de lecturas a procesar:"))
n = tot_lect
lecturas = []
while tot_lect>0:
    if arduino.inWaiting():
        c = arduino.readline().decode().strip()
        if c != "":
            print(c)
            lecturas.append(int(c))
            tot_lect -= 1
print("Lecturas obtenidas")
x = [i for i in range(0,n,1)]
print(x)
plt.plot(x,lecturas,marker="o", color="red")
plt.xticks(x)
plt.yticks(lecturas)
plt.grid(True)
plt.show()