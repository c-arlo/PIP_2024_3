import serial as ser

arduino = ser.Serial(port="COM6", baudrate=9600, timeout=1)

while True:
    if arduino.inWaiting():
        c = arduino.readline().decode().strip()
        if c != "":
            print(c)