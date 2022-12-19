import matplotlib.pyplot as plt
import os

def Run():
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

    rpyY_x_minimu = []
    rpyY_y_minimu = []
    rpyY_z_minimu = []
    rpyY_x_arduino = []
    rpyY_y_arduino = []
    rpyY_z_arduino = []
    
    accY_x_steval = []
    accY_y_steval = []
    accY_z_steval = []
    gyrY_x_steval = []
    gyrY_y_steval = []
    gyrY_z_steval = []
    magY_x_steval = []
    magY_y_steval = []
    magY_z_steval = []
    rpyY_x_steval = []
    rpyY_y_steval = []
    rpyY_z_steval = []
    axiX2 = []
    lim = 0

    fichero = cwd + '/ARCHIVOS_GUI/serial.txt'
    fichero2 = cwd + '/ARCHIVOS_GUI/serial_steval.txt'

    for line in open(fichero, 'r'):
        lines = [i for i in line.split(',')]
        if len(lines) >= 21:
            axiX.append(lim)

            rpyY_x_minimu.append(float(lines[0]))
            rpyY_y_minimu.append(float(lines[1]))
            rpyY_z_minimu.append(float(lines[2]))
            
            accY_x_minimu.append(float(lines[3]))
            accY_y_minimu.append(float(lines[4]))
            accY_z_minimu.append(float(lines[5]))
            
            gyrY_x_minimu.append(float(lines[6]))
            gyrY_y_minimu.append(float(lines[7]))
            gyrY_z_minimu.append(float(lines[8]))
            
            magY_x_minimu.append(float(lines[9]))
            magY_y_minimu.append(float(lines[10]))
            magY_z_minimu.append(float(lines[11]))

            rpyY_x_arduino.append(float(lines[12]))
            rpyY_y_arduino.append(float(lines[13]))
            rpyY_z_arduino.append(float(lines[14]))
            
            accY_x_arduino.append(float(lines[15]))
            accY_y_arduino.append(float(lines[16]))
            accY_z_arduino.append(float(lines[17]))
            
            gyrY_x_arduino.append(float(lines[18]))
            gyrY_y_arduino.append(float(lines[19]))
            gyrY_z_arduino.append(float(lines[20]))
            lim = lim+1
    
    lim = 0
    for line in open(fichero2, 'r'):
        lines = [i for i in line.split(',')]
        if len(lines) >= 12:
            axiX2.append(lim)
            rpyY_x_steval.append(float(lines[0]))
            rpyY_y_steval.append(float(lines[1]))
            rpyY_z_steval.append(float(lines[2]))
            
            accY_x_steval.append(float(lines[3]))
            accY_y_steval.append(float(lines[4]))
            accY_z_steval.append(float(lines[5]))
            
            gyrY_x_steval.append(float(lines[6]))
            gyrY_y_steval.append(float(lines[7]))
            gyrY_z_steval.append(float(lines[8]))
            
            magY_x_steval.append(float(lines[9]))
            magY_y_steval.append(float(lines[10]))
            magY_z_steval.append(float(lines[11]))
            lim = lim+1

    plt.title("Roll, pitch y yaw MINIMU")
    plt.xlabel('Tiempo')
    plt.ylabel('RPY')
    plt.plot(axiX, rpyY_x_minimu, label= 'rpy_X_minimu')
    plt.plot(axiX, rpyY_y_minimu, label= 'rpy_Y_minimu')
    plt.plot(axiX, rpyY_z_minimu, label= 'rpy_Z_minimu')
    plt.legend(loc='lower right')
    fichero = cwd + '/ARCHIVOS_GUI/RollPitchYawMinimu.jpg'
    plt.savefig(fichero, bbox_inches='tight')
    plt.show()

    plt.title("Roll, pitch y yaw ARDUINO")
    plt.xlabel('Tiempo')
    plt.ylabel('RPY')
    plt.plot(axiX, rpyY_x_arduino, label= 'rpy_X_arduino')
    plt.plot(axiX, rpyY_y_arduino, label= 'rpy_Y_arduino')
    plt.plot(axiX, rpyY_z_arduino, label= 'rpy_Z_arduino')
    plt.legend(loc='lower right')
    fichero = cwd + '/ARCHIVOS_GUI/RollPitchYawArduino.jpg'
    plt.savefig(fichero, bbox_inches='tight')
    plt.show()
    
    plt.title("Aceleracion MINIMU")
    plt.xlabel('Tiempo')
    plt.ylabel('g')
    plt.plot(axiX, accY_x_minimu, label= 'Acc_X_minimu')
    plt.plot(axiX, accY_y_minimu, label= 'Acc_Y_minimu')
    plt.plot(axiX, accY_z_minimu, label= 'Acc_Z_minimu')
    plt.legend(loc='lower right')
    fichero = cwd + '/ARCHIVOS_GUI/AceleracionMinimu.jpg'
    plt.savefig(fichero, bbox_inches='tight')
    plt.show()

    plt.title("Aceleracion ARDUINO")
    plt.xlabel('Tiempo')
    plt.ylabel('g')
    plt.plot(axiX, accY_x_arduino, label= 'Acc_X_arduino')
    plt.plot(axiX, accY_y_arduino, label= 'Acc_Y_arduino')
    plt.plot(axiX, accY_z_arduino, label= 'Acc_Z_arduino')
    plt.legend(loc='lower right')
    fichero = cwd + '/ARCHIVOS_GUI/AceleracionArduino.jpg'
    plt.savefig(fichero, bbox_inches='tight')
    plt.show()

    plt.title("Giroscopio MINIMU")
    plt.xlabel('Tiempo')
    plt.ylabel('dps')
    plt.plot(axiX, gyrY_x_minimu, label= 'gyr_X_minimu')
    plt.plot(axiX, gyrY_y_minimu, label= 'gyr_Y_minimu')
    plt.plot(axiX, gyrY_z_minimu, label= 'gyr_Z_minimu')
    plt.legend(loc='lower right')
    fichero = cwd + '/ARCHIVOS_GUI/GiroscopioMinimu.jpg'
    plt.savefig(fichero, bbox_inches='tight')
    plt.show()

    plt.title("Giroscopio ARDUINO")
    plt.xlabel('Tiempo')
    plt.ylabel('dps')
    plt.plot(axiX, gyrY_x_arduino, label= 'gyr_X_arduino')
    plt.plot(axiX, gyrY_y_arduino, label= 'gyr_Y_arduino')
    plt.plot(axiX, gyrY_z_arduino, label= 'gyr_Z_arduino')
    plt.legend(loc='lower right')
    fichero = cwd + '/ARCHIVOS_GUI/GiroscopioArduino.jpg'
    plt.savefig(fichero, bbox_inches='tight')
    plt.show()

    plt.title("Magnetometro MINIMU")
    plt.xlabel('Tiempo')
    plt.ylabel('gauss')
    plt.plot(axiX, magY_x_minimu, label= 'mag_X_minimu')
    plt.plot(axiX, magY_y_minimu, label= 'mag_Y_minimu')
    plt.plot(axiX, magY_z_minimu, label= 'mag_Z_minimu')
    plt.legend(loc='lower right')
    fichero = cwd + '/ARCHIVOS_GUI/MagnetometroMinimu.jpg'
    plt.savefig(fichero, bbox_inches='tight')
    plt.show()

    plt.title("Roll, pitch y yaw STEVAL")
    plt.xlabel('Tiempo')
    plt.ylabel('RPY')
    plt.plot(axiX2, rpyY_x_steval, label= 'rpy_X_steval')
    plt.plot(axiX2, rpyY_y_steval, label= 'rpy_Y_steval')
    plt.plot(axiX2, rpyY_z_steval, label= 'rpy_Z_steval')
    plt.legend(loc='lower right')
    fichero = cwd + '/ARCHIVOS_GUI/RollPitchYawSteval.jpg'
    plt.savefig(fichero, bbox_inches='tight')
    plt.show()
    
    plt.title("Aceleracion STEVAL")
    plt.xlabel('Tiempo')
    plt.ylabel('g')
    plt.plot(axiX2, accY_x_steval, label= 'Acc_X_steval')
    plt.plot(axiX2, accY_y_steval, label= 'Acc_Y_steval')
    plt.plot(axiX2, accY_z_steval, label= 'Acc_Z_steval')
    plt.legend(loc='lower right')
    fichero = cwd + '/ARCHIVOS_GUI/AceleracionSteval.jpg'
    plt.savefig(fichero, bbox_inches='tight')
    plt.show()
    
    plt.title("Giroscopio STEVAL")
    plt.xlabel('Tiempo')
    plt.ylabel('dps')
    plt.plot(axiX2, gyrY_x_steval, label= 'gyr_X_steval')
    plt.plot(axiX2, gyrY_y_steval, label= 'gyr_Y_steval')
    plt.plot(axiX2, gyrY_z_steval, label= 'gyr_Z_steval')
    plt.legend(loc='lower right')
    fichero = cwd + '/ARCHIVOS_GUI/GiroscopioSteval.jpg'
    plt.savefig(fichero, bbox_inches='tight')
    plt.show()
    
    plt.title("Magnetometro STEVAL")
    plt.xlabel('Tiempo')
    plt.ylabel('gauss')
    plt.plot(axiX2, magY_x_steval, label= 'mag_X_steval')
    plt.plot(axiX2, magY_y_steval, label= 'mag_Y_steval')
    plt.plot(axiX2, magY_z_steval, label= 'mag_Z_steval')
    plt.legend(loc='lower right')
    fichero = cwd + '/ARCHIVOS_GUI/MagnetometroSteval.jpg'
    plt.savefig(fichero, bbox_inches='tight')
    plt.show()
