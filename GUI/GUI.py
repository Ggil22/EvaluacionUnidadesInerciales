from tkinter import *
from tkinter import ttk
from datetime import datetime
from tkinter import messagebox as MessageBox
from PIL import ImageTk, Image
import matplotlib.pyplot as plt
import os
import keyboard
import serial
from vpython import *
import numpy as np
import GUI_generar_graficas, GUI_minimu, GUI_arduino, GUI_steval
import subprocess
import serial

formato_letra = "Helvetica"
puerto = "Puerto: COM6"
baudrates = "Baudrates: 115200"
fecha = datetime.now().date()

def createLabels():
    titulo = Label(ventana, text="Comparativa IMUS")
    titulo.pack()
    titulo.config(font=(formato_letra,24,"bold"),fg="#FF5733")

    nombre = Label(ventana, text="Autor: Guillermo Gil Ochoa")
    nombre.place(x=1320, y=770)
    nombre.config(font=(formato_letra,10),fg="#FF5733")

    baud = Label(ventana, text=baudrates)
    baud.place(x=1200, y=770)
    baud.config(font=(formato_letra,10),fg="#FF5733")

    port = Label(ventana, text=puerto)
    port.place(x=1100, y=770)
    port.config(font=(formato_letra,10),fg="#FF5733")

    date = Label(ventana, text=fecha)
    date.place(x=1420, y=0)
    date.config(font=(formato_letra,10),fg="#FF5733")

    datos = Label(ventana, text="Datos a representar:")
    datos.place(x=60, y=150)
    datos.config(font=(formato_letra,10),fg="#FF5733")

    imus = Label(ventana, text="Imus a representar:")
    imus.place(x=60, y=190)
    imus.config(font=(formato_letra,10),fg="#FF5733")

def Salir():
    ventana.destroy()
    ventana.quit()
    print("proceso finalizado")

def open3D():
    MessageBox.showinfo(message="Cuando se cierre el 3d se cerrará el programa entero.", title="INFO")
    if datos_imu == "LSM303DyL3GD20H":
        GUI_minimu.Run()
    elif datos_imu == "LSM6DS3":
        GUI_arduino.Run()
    elif datos_imu == "LSM9DS1":
        GUI_steval.Run()
    else:
        MessageBox.showinfo(message="Elige primero una imu que desee representar.", title="INFO")
    print("abrir 3d")

def openGrafica():
    if datos_grafica == "Giroscopio":
        fondo1=Label(ventana,image=giro_minimu)
        fondo1.place(x = 400, y = 40)
        fondo2=Label(ventana,image=giro_arduino)
        fondo2.place(x = 950, y = 40)
        fondo3=Label(ventana,image=giro_steval)
        fondo3.place(x = 675, y = 400)
    elif datos_grafica == "Acelerometro":
        fondo1=Label(ventana,image=acc_minimu)
        fondo1.place(x = 400, y = 40)
        fondo2=Label(ventana,image=acc_arduino)
        fondo2.place(x = 950, y = 40)
        fondo3=Label(ventana,image=acc_steval)
        fondo3.place(x = 675, y = 400)
    elif datos_grafica == "Magnetometro":
        fondo1=Label(ventana,image=mag_minimu)
        fondo1.place(x = 400, y = 40)
        fondo2=Label(ventana,image=imagen1)
        fondo2.place(x = 950, y = 40)
        fondo3=Label(ventana,image=mag_steval)
        fondo3.place(x = 675, y = 400)
    elif datos_grafica == "Roll, Pitch y yaw":
        fondo1=Label(ventana,image=rpy_minimu)
        fondo1.place(x = 400, y = 40)
        fondo2=Label(ventana,image=rpy_arduino)
        fondo2.place(x = 950, y = 40)
        fondo3=Label(ventana,image=rpy_steval)
        fondo3.place(x = 675, y = 400)
    else:
        MessageBox.showinfo(message="Elige primero un dato que desee representar.", title="INFO")
    print("abrir grafica")

def capturaDatos():
    MessageBox.showinfo(message="Para terminar la captura de datos, tendrás que clicar la tecla P.", title="INFO")
    terminate = False
    arduino = serial.Serial('COM6', 115200, timeout=.1)
    f = open("ARCHIVOS_GUI/serial.txt", "w")
    arduino2 = serial.Serial('COM5', 115200, timeout=.1)
    f2 = open("ARCHIVOS_GUI/serial_steval.txt", "w")
    terminate = False
    
    while terminate!=True:
        data = arduino.readline().decode('ISO-8859-1')
        final_data=data[:-3]
        f.write(final_data)
        f.write("\n")
        
        data2 = arduino2.readline().decode('ISO-8859-1')
        final_data2=data2[:-3]
        f2.write(final_data2)
        f2.write("\n")
        
        if keyboard.is_pressed('p'):
            terminate = True
        
    arduino.close
    f.close()
    arduino2.close
    f2.close()
    
    MessageBox.showinfo("INFO", "Proceso finalizado.")
    print("captura datos")

def generarGraficos():
    GUI_generar_graficas.Run()
    MessageBox.showinfo(message="Ya se han generado las graficas.", title="INFO")

    global giro_minimu
    imagen2_aux = Image.open("ARCHIVOS_GUI/GiroscopioMinimu.jpg")
    imagen2_aux = imagen2_aux.resize((450,350))
    giro_minimu = ImageTk.PhotoImage(imagen2_aux)

    global giro_arduino
    imagen3_aux = Image.open("ARCHIVOS_GUI/GiroscopioArduino.jpg")
    imagen3_aux = imagen3_aux.resize((450,350))
    giro_arduino = ImageTk.PhotoImage(imagen3_aux)

    global acc_minimu
    imagen4_aux = Image.open("ARCHIVOS_GUI/AceleracionMinimu.jpg")
    imagen4_aux = imagen4_aux.resize((450,350))
    acc_minimu = ImageTk.PhotoImage(imagen4_aux)

    global acc_arduino
    imagen5_aux = Image.open("ARCHIVOS_GUI/AceleracionArduino.jpg")
    imagen5_aux = imagen5_aux.resize((450,350))
    acc_arduino = ImageTk.PhotoImage(imagen5_aux)

    global mag_minimu
    imagen6_aux = Image.open("ARCHIVOS_GUI/MagnetometroMinimu.jpg")
    imagen6_aux = imagen6_aux.resize((450,350))
    mag_minimu = ImageTk.PhotoImage(imagen6_aux)

    global rpy_minimu
    imagen7_aux = Image.open("ARCHIVOS_GUI/RollPitchYawMinimu.jpg")
    imagen7_aux = imagen7_aux.resize((450,350))
    rpy_minimu = ImageTk.PhotoImage(imagen7_aux)

    global rpy_arduino
    imagen8_aux = Image.open("ARCHIVOS_GUI/RollPitchYawArduino.jpg")
    imagen8_aux = imagen8_aux.resize((450,350))
    rpy_arduino = ImageTk.PhotoImage(imagen8_aux)
    
    global mag_steval
    imagen9_aux = Image.open("ARCHIVOS_GUI/MagnetometroSteval.jpg")
    imagen9_aux = imagen9_aux.resize((450,350))
    mag_steval = ImageTk.PhotoImage(imagen6_aux)

    global rpy_steval
    imagen10_aux = Image.open("ARCHIVOS_GUI/RollPitchYawSteval.jpg")
    imagen10_aux = imagen10_aux.resize((450,350))
    rpy_steval = ImageTk.PhotoImage(imagen7_aux)
    
    global acc_steval
    imagen11_aux = Image.open("ARCHIVOS_GUI/AceleracionSteval.jpg")
    imagen11_aux = imagen11_aux.resize((450,350))
    acc_steval = ImageTk.PhotoImage(imagen4_aux)
    
    global giro_steval
    imagen12_aux = Image.open("ARCHIVOS_GUI/GiroscopioSteval.jpg")
    imagen12_aux = imagen12_aux.resize((450,350))
    giro_steval = ImageTk.PhotoImage(imagen2_aux)

    
    print("generar graficos")

def actualizarCombos():
    global datos_grafica
    datos_grafica = combo_datos.get()
    global datos_imu
    datos_imu = combo_imu.get()
    print(datos_imu)
    print("variables seleccionadas")

def Help():
    ayuda_ventana = Toplevel(ventana)
    ayuda_ventana.title("Ayuda")
    ayuda_ventana.geometry("600x300")
    Label(ayuda_ventana,text ="Botones:\n\n" +
                              "- ABRIR 3D: abre en su browser el 3d. Termina cuando se cierra el browser.\n" +
                              "- ABRIR GRAFICA: abre las gráficas de las 3 imus pero de los datos seleccionados.\n" +
                              "- CAPTURAR DATOS: captura en un fichero los movimietnos que hagas.\n" +
                              "- GENERAR GRAFICA: con los datos capturados, genera las graficas en una imagen.\n" +
                              "- SALIR: sale de la aplicacion.\n\n" +
                              "Listas:\n\n" +
                              "- Datos a representar: elegir entre acc, gyr, mag y rotacionales.\n" +
                              "- Imus a representar: elegir entres las 3 imus que tenemos.\n\n" +
                              "AVISO: Despues de abrir un 3d, se tendrá que cerrar el otro.\n"
          , font = (formato_letra, 10),justify="left").pack()
    print("help")


def createButtons():
    salir = Button(command= Salir, width=9 ,text= "SALIR",bg="#FF5733", font=(formato_letra,10,"bold"),justify="center")
    salir.place(x=25, y=760)

    abrir3d = Button(command= open3D, width=20 ,text= "ABRIR 3D",bg="#FF5733", font=(formato_letra,10,"bold"),justify="center")
    abrir3d.place(x=130, y=500)

    abrir_grafica = Button(command= openGrafica, width=20 ,text= "ABRIR GRAFICA",bg="#FF5733", font=(formato_letra,10,"bold"),justify="center")
    abrir_grafica.place(x=130, y=550)

    capturar_datos = Button(command= capturaDatos, width=20 ,text= "CAPTURA DATOS",bg="#FF5733", font=(formato_letra,10,"bold"),justify="center")
    capturar_datos.place(x=130, y=600)

    generar_graficos = Button(command= generarGraficos, width=20 ,text= "GENERAR GRAFICOS",bg="#FF5733", font=(formato_letra,10,"bold"),justify="center")
    generar_graficos.place(x=130, y=650)

    ayuda = Button(command= Help, width=9 ,text= "AYUDA",bg="#FF5733", font=(formato_letra,10,"bold"),justify="center")
    ayuda.place(x=120, y=760)

    aceptar = Button(command= actualizarCombos, width=9 ,text= "ACEPTAR",bg="#FF5733", font=(formato_letra,10,"bold"),justify="center")
    aceptar.place(x=130, y=230)

def createCombos():
    global combo_datos
    combo_datos = ttk.Combobox(state="readonly",values=["Acelerometro", "Magnetometro", "Giroscopio", "Roll, Pitch y yaw"])
    combo_datos.place(x=200, y=150)
    combo_datos.current(1)

    global combo_imu
    combo_imu = ttk.Combobox(state="readonly",values=["LSM9DS1", "LSM6DS3", "LSM303DyL3GD20H"])
    combo_imu.place(x=200, y=190)
    combo_imu.current(1)

def inizializarImagenes():
    global imagen1
    imagen1_aux = Image.open("IMAGENES/defecto_grafica.jpg")
    imagen1_aux = imagen1_aux.resize((450,350))
    imagen1 = ImageTk.PhotoImage(imagen1_aux)

    global logo
    logo_aux = Image.open("IMAGENES/logo-uam.png")
    logo_aux = logo_aux.resize((100,100))
    logo = ImageTk.PhotoImage(logo_aux)

ventana =Tk()
ventana.geometry("1500x800")
ventana.title("TFG")
icono = PhotoImage(file="IMAGENES/logo-uam.png")
ventana.iconphoto(True, icono)
ventana.resizable(0,0)

inizializarImagenes()

logoImage=Label(ventana,image=logo)
logoImage.place(x = 0, y = 0)

fondo1=Label(ventana,image=imagen1)
fondo1.place(x = 400, y = 40)

fondo2=Label(ventana,image=imagen1)
fondo2.place(x = 950, y = 40)

fondo3=Label(ventana,image=imagen1)
fondo3.place(x = 675, y = 400)

createLabels()
createButtons()
createCombos()

ventana.mainloop()
