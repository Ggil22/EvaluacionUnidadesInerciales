import serial
import collections
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.lines import Line2D

def getSerialData(self,Samples,numData,serialConnection, lines):
  # Obtenemos la linea que devuelve arduino por el puerto serial.
  line = serialConnection.readline().decode('ISO-8859-1')
  # Partimos la linea y la guardamos en el array.
  words = line.split(",",6)
  # Actualizamos las variables donde vamos a ir guardando los datos obtenidos.
  for i in range(numData):
      # Guarda lectura en la última posición.
      data[i].append(float(words[i]))
      # Dibujar nueva linea.
      lines[i].set_data(range(Samples),data[i])

# Puerto serial arduino.
serialPort = 'COM6'
# Baudios (número de símbolos por segundo).
baudRate = 115200
# Abre el puerto inmediatamente. Con el puerto COM6 que es donde se conecta el USB,
# el budrate de 115200 que es el numero de objetos por segundo y con timeout de 0.1
# que es la espera de lectura.
serialConnection = serial.Serial(serialPort, baudRate)
# Muestras.
Samples = 50
# Tiempo de muestreo. En este caso es cero para que se muestre en tiempo real.
sampleTime = 0
# Numero de datos que queremos representar en las graficas.
numData = 3
# Limites de los ejes.
xmin = 0
xmax = Samples
ymin = [-750,-750,-750]
ymax = [750,750,750]
lines = []
data = []
# Inicializamos las variables donde vamos a ir guardando los datos obtenidos.
for i in range(numData):
    # Creamos una tabla doblemente enlazada.
    data.append(collections.deque([0] * Samples, maxlen=Samples))
    # Cree una instancia de Line2D con datos x e y en secuencias de xdata, ydata.
    lines.append(Line2D([], [], color='blue'))
# Creamos la ventana para representar las gráficas.
fig = plt.figure("ACC IMU")
# Creamos la grafica, le ponemos titulo y ponemos que variable es la que quiere estar 
# leyendo.
ax1 = fig.add_subplot(2, 2, 1,xlim=(xmin, xmax), ylim=(ymin[0] , ymax[0]))
ax1.title.set_text('ACC X:')
ax1.add_line(lines[0])
# Creamos la grafica, le ponemos titulo y ponemos que variable es la que quiere estar 
# leyendo.
ax2 = fig.add_subplot(2, 2, 2,xlim=(xmin, xmax), ylim=(ymin[1] , ymax[1]))
ax2.title.set_text('ACC Y:')
ax2.add_line(lines[1])
# Creamos la grafica, le ponemos titulo y ponemos que variable es la que quiere estar 
# leyendo.
ax3 = fig.add_subplot(2, 2, 3,xlim=(xmin, xmax), ylim=(ymin[2] , ymax[2]))
ax3.title.set_text("ACC Z:")
ax3.add_line(lines[2])
# Crea una animacion (en este caso las graficas) llamando a una funcion repetitivamente.
# Se quiere representar en la figura fig, utilizando la funcion getSerialData que es la
# encargada de obtener los datos, se le pasa los parametros fargs que tambien es donde
# se los guarda y ponemos interval que en este caso es 0.
anim = animation.FuncAnimation(fig,getSerialData, fargs=(Samples,numData,serialConnection,lines), interval=sampleTime)
# Enseñamos las graficas.
plt.show()
# Cerramos el puerto serie.
serialConnection.close()
 

