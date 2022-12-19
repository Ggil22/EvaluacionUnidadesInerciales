import matplotlib.pyplot as plt

import os

cwd = os.getcwd()  # Get the current working directory (cwd)
axiX = []
accY_x_minimu = []
accY_y_minimu = []
accY_z_minimu = []
accY_x_arduino = []
accY_y_arduino = []
accY_z_arduino = []
gyrY_x_minimu = []
gyrY_y_minimu = []
gyrY_z_minimu = []
gyrY_x_arduino = []
gyrY_y_arduino = []
gyrY_z_arduino = []
magY_x_minimu = []
magY_y_minimu = []
magY_z_minimu = []
word = []
lim = 0

fichero = cwd + '/ARCHIVOS_GUI/serial.txt'
'''
with open(fichero, 'r+') as fp:
    lines = fp.readlines()
    fp.seek(0)
    fp.truncate()
    fp.writelines(lines[1:])
'''
for line in open(fichero, 'r'):
    lines = [i for i in line.split(',')]
    if len(lines) >= 15:
        axiX.append(lim)
        accY_x_minimu.append(float(lines[0]))
        accY_y_minimu.append(float(lines[1]))
        accY_z_minimu.append(float(lines[2]))
        accY_x_arduino.append(float(lines[3]))
        accY_y_arduino.append(float(lines[4]))
        accY_z_arduino.append(float(lines[5]))
        gyrY_x_minimu.append(float(lines[6]))
        gyrY_y_minimu.append(float(lines[7]))
        gyrY_z_minimu.append(float(lines[8]))
        gyrY_x_arduino.append(float(lines[9]))
        gyrY_y_arduino.append(float(lines[10]))
        gyrY_z_arduino.append(float(lines[11]))
        magY_x_minimu.append(float(lines[12]))
        magY_y_minimu.append(float(lines[13]))
        magY_z_minimu.append(float(lines[14]))
        lim = lim+1

plt.title("Aceleracion MINIMU")
plt.xlabel('Tiempo')
plt.ylabel('Acc')
plt.plot(axiX, accY_x_minimu, label= 'Acc_X_minimu')
plt.plot(axiX, accY_y_minimu, label= 'Acc_Y_minimu')
plt.plot(axiX, accY_z_minimu, label= 'Acc_Z_minimu')
plt.legend(loc='lower right')
fichero = cwd + '/ARCHIVOS/AceleracionMinimu.jpg'
plt.savefig(fichero, bbox_inches='tight')
plt.show()

plt.title("Aceleracion ARDUINO")
plt.xlabel('Tiempo')
plt.ylabel('Acc')
plt.plot(axiX, accY_x_minimu, label= 'Acc_X_arduino')
plt.plot(axiX, accY_y_minimu, label= 'Acc_Y_arduino')
plt.plot(axiX, accY_z_minimu, label= 'Acc_Z_arduino')
plt.legend(loc='lower right')
fichero = cwd + '/ARCHIVOS/AceleracionArduino.jpg'
plt.savefig(fichero, bbox_inches='tight')
plt.show()

plt.title("Giroscopio MINIMU")
plt.xlabel('Tiempo')
plt.ylabel('gyr')
plt.plot(axiX, gyrY_x_minimu, label= 'gyr_X_minimu')
plt.plot(axiX, gyrY_y_minimu, label= 'gyr_Y_minimu')
plt.plot(axiX, gyrY_z_minimu, label= 'gyr_Z_minimu')
plt.legend(loc='lower right')
fichero = cwd + '/ARCHIVOS/GiroscopioMinimu.jpg'
plt.savefig(fichero, bbox_inches='tight')
plt.show()

plt.title("Giroscopio ARDUINO")
plt.xlabel('Tiempo')
plt.ylabel('gyr')
plt.plot(axiX, gyrY_x_minimu, label= 'gyr_X_arduino')
plt.plot(axiX, gyrY_y_minimu, label= 'gyr_Y_arduino')
plt.plot(axiX, gyrY_z_minimu, label= 'gyr_Z_arduino')
plt.legend(loc='lower right')
fichero = cwd + '/ARCHIVOS/GiroscopioArduino.jpg'
plt.savefig(fichero, bbox_inches='tight')
plt.show()

plt.title("Magnetometro MINIMU")
plt.xlabel('Tiempo')
plt.ylabel('mag')
plt.plot(axiX, magY_x_minimu, label= 'mag_X_minimu')
plt.plot(axiX, magY_y_minimu, label= 'mag_Y_minimu')
plt.plot(axiX, magY_z_minimu, label= 'mag_Z_minimu')
plt.legend(loc='lower right')
fichero = cwd + '/ARCHIVOS/MagnetometroMinimu.jpg'
plt.savefig(fichero, bbox_inches='tight')
plt.show()

