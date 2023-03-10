void Compass_Heading()
{
  // Ajuste del magnetometro por LSM303 con el offsets/sensitivity 
  c_magnetom_x = (float)(magnetom_x - SENSOR_SIGN[6]*M_X_MIN) / (M_X_MAX - M_X_MIN) - SENSOR_SIGN[6]*0.5;
  c_magnetom_y = (float)(magnetom_y - SENSOR_SIGN[7]*M_Y_MIN) / (M_Y_MAX - M_Y_MIN) - SENSOR_SIGN[7]*0.5;
  c_magnetom_z = (float)(magnetom_z - SENSOR_SIGN[8]*M_Z_MIN) / (M_Z_MAX - M_Z_MIN) - SENSOR_SIGN[8]*0.5;

//  // Tilt compensated Magnetic filed X:
//  MAG_X = c_magnetom_x*cos_pitch+c_magnetom_y*sin_roll*sin_pitch+c_magnetom_z*cos_roll*sin_pitch;
//  // Tilt compensated Magnetic filed Y:
//  MAG_Y = c_magnetom_y*cos_roll-c_magnetom_z*sin_roll;
//  // Magnetic Heading
//  MAG_Heading = atan2(-MAG_Y,MAG_X);
}
