# Evaluación de Unidades Inerciales para el Monitoreo de la Actividad Física y Deportiva

Trabajo Fin de Grado (TFG) de **Guillermo Gil Ochoa** en la Universidad Autónoma de Madrid.

El proyecto compara tres unidades de medida inercial (IMU) de bajo coste para valorar cuál es más adecuada para monitorizar la actividad física y deportiva. Para ello se capturan los datos de acelerómetro, giroscopio y magnetómetro de cada sensor, se calcula su orientación (*roll*, *pitch* y *yaw*) con el filtro de **Madgwick**, y se evalúan sus características metrológicas mediante pruebas a distintos ángulos.

## IMUs evaluadas

| Nombre en el proyecto | Sensor | Placa | Sensores |
|-----------------------|--------|-------|----------|
| **Arduino** | LSM6DS3 | IMU integrada en la placa Arduino | Acelerómetro + giroscopio |
| **Pololu / MinIMU** | LSM303D + L3GD20H | Pololu MinIMU-9 | Acelerómetro + giroscopio + magnetómetro |
| **Steval** | LSM9DS1 | STMicroelectronics STEVAL-MKI159V1 | Acelerómetro + giroscopio + magnetómetro |

Todas las placas se comunican por I²C con un Arduino y envían los datos al PC por puerto serie a 115200 baudios.

## Estructura del repositorio

```
├── Pololu/          # Firmware Arduino: lee la IMU integrada (LSM6DS3) y la MinIMU-9 y aplica Madgwick
├── Steval/          # Firmware Arduino para la STEVAL (LSM9DS1) con Madgwick
├── GUI/             # Aplicación de escritorio para capturar, visualizar y comparar los datos
│   ├── GUI.py                    # Ventana principal (Tkinter)
│   ├── GUI_arduino.py            # Visualización 3D de la IMU del Arduino
│   ├── GUI_minimu.py             # Visualización 3D de la MinIMU-9
│   ├── GUI_steval.py             # Visualización 3D de la STEVAL
│   ├── GUI_generar_graficas.py   # Generación de gráficas a partir de los datos capturados
│   └── ARCHIVOS_GUI/             # Datos capturados y gráficas generadas
├── ScriptApoyo/     # Scripts independientes usados durante el desarrollo (captura, gráficas y 3D)
└── Pruebas/         # Resultados experimentales
    ├── 0, 30, 45, 60, 90, 120, 160, 180, 230/   # Capturas de cada IMU a cada ángulo (º)
    ├── Fotos/                                   # Capturas de pantalla de las pruebas
    ├── TFG_PruebasCalibracion.xlsx              # Curvas de calibración
    └── tablas.xlsx                              # Tablas comparativas de resultados
```

## Aplicación GUI

La interfaz (`GUI/GUI.py`) permite:

- **Captura de datos**: lee simultáneamente los dos puertos serie (Arduino + MinIMU en `COM6` y STEVAL en `COM5`) y guarda los datos en `ARCHIVOS_GUI/`. La captura termina al pulsar la tecla `P`.
- **Generar gráficas**: crea las gráficas de aceleración, giroscopio, magnetómetro y *roll/pitch/yaw* de cada IMU.
- **Abrir gráfica**: muestra en paralelo las gráficas de las tres IMUs para el tipo de dato seleccionado.
- **Abrir 3D**: representa en tiempo real la orientación de la IMU seleccionada en un modelo 3D (VPython, se abre en el navegador).

## Evaluación

Las IMUs se colocaron a 0º, 30º, 45º, 60º, 90º, 120º, 160º, 180º y 230º. Con esos datos se obtuvieron curvas de calibración y se compararon el campo de medida, el alcance, la sensibilidad, la resolución, la deriva y la repetibilidad de cada sensor. Los resultados están en la carpeta `Pruebas/`.

## Requisitos

### Hardware
- Placa Arduino con IMU LSM6DS3 integrada
- Pololu MinIMU-9 (LSM303D + L3GD20H)
- STEVAL-MKI159V1 (LSM9DS1) con un segundo Arduino

### Firmware (Arduino IDE)
Librerías: `Arduino_LSM6DS3`, `MadgwickAHRS`, `LSM303`, `L3G` (Pololu) y `SparkFun LSM9DS1`.

1. Cargar `Pololu/Pololu.ino` (con el resto de ficheros `.ino` de la carpeta) en el Arduino conectado a la MinIMU-9.
2. Cargar `Steval/Steval.ino` en el Arduino conectado a la STEVAL.

### Software (Python 3)
```bash
pip install pyserial vpython numpy matplotlib pillow keyboard
cd GUI
python GUI.py
```

> **Nota:** los puertos `COM5` y `COM6` están fijados en el código; ajústalos a los de tu equipo. `GUI.py` también carga dos imágenes de la carpeta `GUI/IMAGENES/` (`logo-uam.png` y `defecto_grafica.jpg`) que no están en el repositorio; hay que añadirlas para que la ventana arranque.

## Autor

**Guillermo Gil Ochoa** — [GitHub](https://github.com/Ggil22)
