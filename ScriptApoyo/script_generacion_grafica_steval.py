import matplotlib.pyplot as plt
import os
def Run():
    cwd = os.getcwd()  # Get the current working directory (cwd)
    axiX = []
    accY_x_minimu = []
    accY_y_minimu = []
    accY_z_minimu = []
    gyrY_x_minimu = []
    gyrY_y_minimu = []
    gyrY_z_minimu = []
    magY_x_minimu = []
    magY_y_minimu = []
    magY_z_minimu = []

    lim = 0

    fichero = cwd + '/ARCHIVOS/serial.txt'

    for line in open(fichero, 'r'):
        lines = [i for i in line.split(',')]
        if len(lines) >= 10:
            axiX.append(lim)
            accY_x_minimu.append(float(lines[0]))
            accY_y_minimu.append(float(lines[1]))
            accY_z_minimu.append(float(lines[2]))
            
            gyrY_x_minimu.append(float(lines[3]))
            gyrY_y_minimu.append(float(lines[4]))
            gyrY_z_minimu.append(float(lines[5]))
            
            magY_x_minimu.append(float(lines[6]))
            magY_y_minimu.append(float(lines[7]))
            magY_z_minimu.append(float(lines[8]))
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

Run()
