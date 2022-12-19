#include <Wire.h>
#include <Arduino_LSM6DS3.h>
#include <MadgwickAHRS.h>

bool rpy = true;
bool acc = true;
bool gyr = true;
bool magn = true;

/*VARIABLES PARA LA MINIMU v3*/
int SENSOR_SIGN[9] = {1,1,1,-1,-1,-1,1,1,1};

#define GRAVITY 256

#define M_X_MIN -1000
#define M_Y_MIN -1000
#define M_Z_MIN -1000
#define M_X_MAX +1000
#define M_Y_MAX +1000
#define M_Z_MAX +1000

#define STATUS_LED 13

float G_Dt=0.02;    // Ayda para el calculo de los datos

long timer=0;
long timer_old;
int AN[6]; //Array que guarda los datos gyro y accelerometer
int AN_OFFSET[6]={0,0,0,0,0,0}; //Array que guarda el Offset del sensors
//Variables auxiliares que ayudan al calculo de los datos
int gyro_x;
int gyro_y;
int gyro_z;
int accel_x;
int accel_y;
int accel_z;
int magnetom_x;
int magnetom_y;
int magnetom_z;
float c_magnetom_x;
float c_magnetom_y;
float c_magnetom_z;
float MAG_Heading;

// Variables rotacionales
float roll;
float pitch;
float yaw;

unsigned int counter=0;

const int MINIMU_mag_acc = 0x1D, MINIMU_gyr = 0x6B;

/*VARIABLES PARA LA IMU DE ARDUINO
Pagina que me ha ayudado https://www.joober.eu/angulos-de-rotacion-con-el-imu-de-arduino-nano-33-iot/ 
Pagina donde explica el filter https://ahrs.readthedocs.io/en/latest/filters/madgwick.html */
// initialize a Madgwick filter:
Madgwick filter;
// sensor's sample rate is fixed at 104 Hz:
const float sensorRate = 104.00;
// values for acceleration & rotation:
float xAcc_ARDUINO, yAcc_ARDUINO, zAcc_ARDUINO;
float xGyro_ARDUINO, yGyro_ARDUINO, zGyro_ARDUINO;
// values for orientation:
float roll_ARDUINO, pitch_ARDUINO, heading_ARDUINO;
/*VARIABLES PARA LA IMU DE POLOLU*/
// initialize a Madgwick filter:
Madgwick filter_POLOLU;
// values for acceleration & rotation:
float xAcc_POLOLU, yAcc_POLOLU, zAcc_POLOLU;
float xGyro_POLOLU, yGyro_POLOLU, zGyro_POLOLU;
float xMag_POLOLU, yMag_POLOLU, zMag_POLOLU;
// values for orientation:
float roll_POLOLU, pitch_POLOLU, heading_POLOLU;


void setup() {
  //Abrir puerto serie
  Serial.begin(115200);
  pinMode (STATUS_LED,OUTPUT);
  //Abrir puerto I2C
  I2C_Init();

  digitalWrite(STATUS_LED,LOW);
  delay(1500);
  
  // Empezamos la transmision con la minimu pero el chip del magnetometro y giroscopo L3GD20H
  Wire.beginTransmission(MINIMU_mag_acc);
  //Abrir la aceleracion de la pololu
  Accel_Init();
  Wire.endTransmission(true);
  // Empezamos la transmision con la minimu pero el chip del gyroscopio L3GD20H
  Wire.beginTransmission(MINIMU_gyr);
  //Abrir el giroscopo de la pololu
  Gyro_Init();
  Wire.endTransmission(true);

  delay(20);

  for(int i=0;i<32;i++)    // We take some readings...
    {
    //Lee los datos de la imu para ver si se puede escribir.
    Read_Gyro();
    //Lee los datos de la imu para ver si se puede escribir.
    Read_Accel();
    for(int y=0; y<6; y++)   // Obtencion del offset
      AN_OFFSET[y] += AN[y];
    delay(20);
    }
  // Obtencion del offset
  for(int y=0; y<6; y++)
    AN_OFFSET[y] = AN_OFFSET[y]/32;
  // Obtencion del offset junto con la gravedad
  AN_OFFSET[5]-=GRAVITY*SENSOR_SIGN[5];
  for(int y=0; y<6; y++)
    Serial.println(AN_OFFSET[y]);

  delay(2000);
  digitalWrite(STATUS_LED,HIGH);

  timer=millis();
  delay(20);
  counter=0;
  // Abre la imu de arduino
  if (!IMU.begin()) {
    Serial.println("Failed to initialize IMU");
    while (true);
  }
  //Inicia el filtro para el calculo de las variables rotacionales.
  filter.begin(sensorRate);
  filter_POLOLU.begin(sensorRate);
}


void loop() {
  if((millis()-timer)>=20)  // Hace que se ejecute el loop a 50Hz
  {
    counter++;
    timer_old = timer;
    timer=millis();
    if (timer>timer_old)
    {
      G_Dt = (timer-timer_old)/1000.0;
      if (G_Dt > 0.2)
        G_Dt = 0;
    }
    else
      G_Dt = 0;
    // Empezamos la transmision con la minimu pero el chip del gyroscopio L3GD20H
    Wire.beginTransmission(MINIMU_gyr);
    // Leen los datos del giroscopio
    Read_Gyro();
    Wire.endTransmission(true);
    // Empezamos la transmision con la minimu pero el chip del magnetometro y giroscopo L3GD20H
    Wire.beginTransmission(MINIMU_mag_acc);
    // Lee los datos del acelerometro
    Read_Accel();

    if (counter > 5)  // Lee el magnetometro a 10 Hz
    {
      counter=0;
      Read_Compass();    // Lee I2C magnetomero
      Compass_Heading(); // Calcula el magnetometro
    }
    Wire.endTransmission(true);
    //Lee los datos de la imu y los mete en una variable.
    yAcc_POLOLU = AN[3];
    xAcc_POLOLU = AN[4];
    zAcc_POLOLU = AN[5];
    yGyro_POLOLU = AN[0];
    xGyro_POLOLU = AN[1];
    zGyro_POLOLU = AN[2];
    yMag_POLOLU = c_magnetom_x;
    xMag_POLOLU = c_magnetom_y;
    zMag_POLOLU = c_magnetom_z;
    //Utiliza el filtro para calcular las variables rotacionales.
    filter_POLOLU.update(xGyro_POLOLU, yGyro_POLOLU, zGyro_POLOLU, xAcc_POLOLU, yAcc_POLOLU, zAcc_POLOLU, xMag_POLOLU, yMag_POLOLU, zMag_POLOLU);
    // Obtiene las variables rotacionales.
    roll_POLOLU = filter_POLOLU.getRoll();
    pitch_POLOLU = filter_POLOLU.getPitch();
    heading_POLOLU = filter_POLOLU.getYaw();
  }

  // Comrpueba si se puede abrir la imu
  if (IMU.accelerationAvailable() && IMU.gyroscopeAvailable()) {
    // Lee el acelerometro y giroscopio:
    IMU.readAcceleration(xAcc_ARDUINO, yAcc_ARDUINO, zAcc_ARDUINO);
    IMU.readGyroscope(xGyro_ARDUINO, yGyro_ARDUINO, zGyro_ARDUINO);
    //Utiliza el filtro para calcular las variables rotacionales.
    filter.updateIMU(xGyro_ARDUINO, yGyro_ARDUINO, zGyro_ARDUINO, xAcc_ARDUINO, yAcc_ARDUINO, zAcc_ARDUINO);
    // Obtiene las variables rotacionales.
    roll_ARDUINO = filter.getRoll();
    pitch_ARDUINO = filter.getPitch();
    heading_ARDUINO = filter.getYaw();
  }
  // Pinta las variables rotacionales.
  printdata();
}
