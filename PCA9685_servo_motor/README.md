#servo_사용하기

$ sudo i2cdetect -y 1


---> PWM컨트롤러(PCA9685)의 I2C는 0x40과 0x70이라는 채널에 연결되어 있음을 알수 있습니다.

$ git clone https://github.com/adafruit/Adafruit_Python_PCA9685.git

$ cd Adafruit_Python_PCA9685

$ sudo python3 setup.py install

