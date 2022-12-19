void printdata(void)
{   
    if( rpy == true ){
      Serial.print(roll_POLOLU);
      Serial.print (",");
      Serial.print(pitch_POLOLU);
      Serial.print (",");
      Serial.print(heading_POLOLU);

      Serial.print (",");
    }
    if( acc == true ){ 
      Serial.print(xAcc_POLOLU/256);
      Serial.print (",");
      Serial.print(yAcc_POLOLU/256);
      Serial.print (",");
      Serial.print(zAcc_POLOLU/256);

      Serial.print(",");
    }
    if( gyr == true ){
      Serial.print(xGyro_POLOLU);
      Serial.print (",");
      Serial.print(yGyro_POLOLU);
      Serial.print (",");
      Serial.print(zGyro_POLOLU);

      Serial.print(",");
    }
    if( magn == true ){
      Serial.print(xMag_POLOLU);
      Serial.print (",");
      Serial.print(yMag_POLOLU);
      Serial.print (",");
      Serial.print(zMag_POLOLU);

      Serial.print (",");
    }
    if( rpy == true ){
      Serial.print(roll_ARDUINO);
      Serial.print (",");
      Serial.print(pitch_ARDUINO);
      Serial.print (",");
      Serial.print(heading_ARDUINO);
      Serial.print (",");
    }
    if( acc == true ){
      Serial.print(xAcc_ARDUINO);
      Serial.print (",");
      Serial.print(yAcc_ARDUINO);
      Serial.print (",");
      Serial.print(zAcc_ARDUINO);
      Serial.print (",");
    }
    if( gyr == true ){
      Serial.print(xGyro_ARDUINO);
      Serial.print (",");
      Serial.print(yGyro_ARDUINO);
      Serial.print (",");
      Serial.print(zGyro_ARDUINO);
      Serial.print (","); 
    }
      
      Serial.println();
      
}
