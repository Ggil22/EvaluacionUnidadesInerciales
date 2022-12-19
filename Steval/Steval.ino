#include <Wire.h>
#include <SparkFunLSM9DS1.h>
#include <MadgwickAHRS.h>

bool rpy = true;
bool acc = true;
bool gyr = true;
bool magn = true;

//Inicializacion variables
LSM9DS1 imu;
#define PRINT_CALCULATED
#define PRINT_SPEED 250
static unsigned long lastPrint = 0;
#define DECLINATION -8.58

/*VARIABLES PARA LA IMU DE STEVAL*/
// Inicializacion madgwick
Madgwick filter_STEVAL;
// Valores que obtiene las imu
float xAcc_STEVAL, yAcc_STEVAL, zAcc_STEVAL;
float xGyro_STEVAL, yGyro_STEVAL, zGyro_STEVAL;
float xMag_STEVAL, yMag_STEVAL, zMag_STEVAL;
// Valores rotacionales
float roll_STEVAL, pitch_STEVAL, heading_STEVAL;

void setup()
{
  //Abrir puerto serie
  Serial.begin(115200);
  //Abrir puerto I2C
  Wire.begin();
  //Abrir la Imu
  if (imu.begin() == false)
  {
    Serial.println("Failed to communicate with LSM9DS1.");
    Serial.println("Double-check wiring.");
    Serial.println("Default settings in this sketch will " \
                   "work for an out of the box LSM9DS1 " \
                   "Breakout, but may need to be modified " \
                   "if the board jumpers are.");
    while (1);
  }
  //Inicia el filtro para el calculo de las variables rotacionales.
  filter_STEVAL.begin(sensorRate);
}

void loop()
{
  // Comprueba si se puede abrir la imu
  if ( imu.gyroAvailable() )
  {
    //Lee los datos de la imu para ver si se puede escribir.
    imu.readGyro();
  }
  // Comprueba si se puede abrir la imu
  if ( imu.accelAvailable() )
  {
    //Lee los datos de la imu para ver si se puede escribir.
    imu.readAccel();
  }
  // Comprueba si se puede abrir la imu
  if ( imu.magAvailable() )
  {
    //Lee los datos de la imu para ver si se puede escribir.
    imu.readMag();
  }
  //Lee los datos de la imu y los mete en una variable.
  xAcc_STEVAL = imu.calcAccel(imu.ax);
  yAcc_STEVAL = imu.calcAccel(imu.ay);
  zAcc_STEVAL = imu.calcAccel(imu.az);
  xGyro_STEVAL = imu.calcGyro(imu.gx);
  yGyro_STEVAL = imu.calcGyro(imu.gy);
  zGyro_STEVAL = imu.calcGyro(imu.gz);
  xMag_STEVAL = imu.calcMag(imu.mx);
  yMag_STEVAL = imu.calcMag(imu.my);
  zMag_STEVAL = imu.calcMag(imu.mz);
  //Utiliza el filtro para calcular las variables rotacionales.
  filter_STEVAL.update(xGyro_STEVAL, yGyro_STEVAL, zGyro_STEVAL, xAcc_STEVAL, yAcc_STEVAL, zAcc_STEVAL, xMag_STEVAL, yMag_STEVAL, zMag_STEVAL);
  // Obtiene las variables rotacionales.
  roll_STEVAL = filter_STEVAL.getRoll();
  pitch_STEVAL = filter_STEVAL.getPitch();
  heading_STEVAL = filter_STEVAL.getYaw();
  // Pinta las variables rotacionales.
  printdata();
  delay(200);
}

void printdata(void)
{
  if( rpy == true ){
    Serial.print(roll_STEVAL);
    Serial.print (",");
    Serial.print(pitch_STEVAL);
    Serial.print (",");
    Serial.print(heading_STEVAL);

    Serial.print (",");
  }
  if( acc == true ){ 
    Serial.print(xAcc_STEVAL);
    Serial.print (",");
    Serial.print(yAcc_STEVAL);
    Serial.print (",");
    Serial.print(zAcc_STEVAL);

    Serial.print(",");
  }
  if( gyr == true ){
    Serial.print(xGyro_STEVAL);
    Serial.print (",");
    Serial.print(yGyro_STEVAL);
    Serial.print (",");
    Serial.print(zGyro_STEVAL);

    Serial.print(",");
  }
  if( magn == true ){
    Serial.print(xMag_STEVAL);
    Serial.print (",");
    Serial.print(yMag_STEVAL);
    Serial.print (",");
    Serial.print(zMag_STEVAL);

    Serial.print (",");
  }
}
