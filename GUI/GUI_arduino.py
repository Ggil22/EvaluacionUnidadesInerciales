import serial
from vpython import *
import numpy as np
import keyboard

def Run():
    # Abre el puerto inmediatamente. Con el puerto COM6 que es donde se conecta el USB,
    # el budrate de 115200 que es el numero de objetos por segundo y con timeout de 0.1
    # que es la espera de lectura.
    arduino = serial.Serial('COM6', 115200, timeout=.1)
    scene.range=5
    # Variable que ayuda a transformar un numero decimal a radianes.
    toRad=2*np.pi/360
    # Vector que apunta en la misma dirección que la cámara mira.
    scene.forward=vector(-1,-1,-1)
    # Dibuja flechas en el 3D.
    xarrow=arrow(axis=vector(1,0,0), length=2, shaftwidth=.1,color=color.red)
    yarrow=arrow(axis=vector(0,1,0), length=2, shaftwidth=.1,color=color.green)
    zarrow=arrow(axis=vector(0,0,1), length=4, shaftwidth=.1,color=color.blue)
    frontArrow=arrow(length=4, shaftwidth=.1, color=color.purple, axis=vector(1,0,0))
    upArrow=arrow(length=1, shaftwidth=.1, color=color.magenta, axis=vector(0,1,0))
    sideArrow=arrow(length=2, shaftwidth=.1, color=color.orange, axis=vector(0,0,1))
    # Inicializa las variables donde calcularemos los datos.
    roll=0
    pitch=0
    yaw=0
    # Dibuja las cajas que representan los chips y protoboard.
    bBoard=box(length=6,width=2,height=.2,opacity=.8,pos=vector(0,0,0,))
    nano=box(length=1,width=.75,height=.1,pos=vector(2.3,.1+.05,0),color=color.blue)
    minimu=box(lenght=1.75,width=.6,height=.1,pos=vector(1,.1+.05,0),color=color.green)
    # Unimos los 3 componentes que se han creado antes como un solo objeto.
    myObj=compound([bBoard,nano,minimu])
    terminate = False
    while(terminate!=True):
        # Obtenemos la linea que devuelve arduino por el puerto serial.
        line = arduino.readline().decode('ISO-8859-1')
        # Partimos la linea y la guardamos en el array.
        words = line.split(",",21)
        # Calculamos el pitch, roll y yaw.
        roll = float(words[12])*toRad
        pitch = float(words[13])*toRad
        yaw = float(words[14])*toRad+np.pi
        # Calcula la posicion en la que se encuentra.
        k=vector(cos(yaw)*cos(pitch), sin(pitch), sin(yaw)*cos(pitch))
        # Calculamos la posicion a la que se esta dirigiendo.
        y=vector(0,1,0)
        s=cross(k,y)
        v=cross(s,k)
        # Formula de la teoría de la rotación tridimensional es un algoritmo eficiente
            # para rotar un vector en el espacio, dado un eje y un ángulo de rotación.
        vrot=v*cos(roll)+cross(k,v)*sin(roll)
        # Damos los valores calculados a las funciones axis que hacen que se mueva.
        frontArrow.axis=k
        sideArrow.axis=cross(k,vrot)
        upArrow.axis=vrot
        myObj.axis=k
        myObj.up=vrot
        frontArrow.length=4
        sideArrow.length=2
        upArrow.length=1
        if keyboard.is_pressed('p'):
            arduino.close
            terminate = True
    # Cerramos el puerto serie.
    arduino.close
