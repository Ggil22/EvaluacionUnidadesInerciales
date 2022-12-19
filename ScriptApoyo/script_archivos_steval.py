import serial
import keyboard
def Run():
    '''arduino = serial.Serial('COM5', 115200, timeout=.1)
    f = open("ARCHIVOS/serial.txt", "w")'''
    arduino2 = serial.Serial('COM6', 115200, timeout=.1)
    f2 = open("ARCHIVOS/serial.txt", "w")
    terminate = False
    
    while terminate!=True:
        '''data = arduino.readline().decode('ISO-8859-1')
        final_data=data[:-3]
        print(final_data)
        f.write(final_data)
        f.write("\n")'''

        data2 = arduino2.readline().decode('ISO-8859-1')
        print(data2)
        final_data2=data2
        f2.write(final_data2)
        f2.write("\n")
        if keyboard.is_pressed('p'):
            terminate = True
        
    arduino2.close
    f2.close()

Run()
