import serial
import datetime
import keyboard

arduino = serial.Serial('COM6', 115200, timeout=.1)
x = datetime.datetime.now()
fecha = str(x.hour) + "." + str(x.minute) + "." + str(x.second) + "-" + str(x.day) + "." + str(x.month) + "." + str(x.year)
#f = open("/ARCHIVOS/serial" + ahora + ".txt", "w")
f = open("ARCHIVOS/serial123.txt", "w")
terminate = False
while terminate!=True:
    data = arduino.readline().decode('ISO-8859-1')
    final_data=data[:-3]
    print(final_data)
    f.write(final_data)
    f.write("\n")
    if keyboard.is_pressed('p'):
        terminate = True
    
arduino.close
f.close()
