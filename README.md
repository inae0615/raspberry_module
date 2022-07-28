# thermal_camera_controls (with. raspberry pi)
## AMG8833
1. 라즈베리파이 GPIO 사용하기 

- git clone https://github.com/WiringPi/WiringPi

- cd WiringPi

- ./build

- gpio -v 

- gpio readall 



2.  라즈베리파이 AMG8833 모듈 설치 

- sudo pip3 install colour

- sudo i2cdetect -y 1

- sudo apt-get install -y build-essential python-pip python-dev python-smbus git

- git clone https://github.com/adafruit/Adafruit_Python_GPIO.git 

- cd Adafruit_Python_GPIO.git 

- sudo python setup.py install

- sudo apt-get install -y python-scipy python-pygame

- sudo pip install colour Adafruit_AMG88xx

- cd ~



3. Thermal camera AMG8833 사용하기 

- git clone https://github.com/adafruit/Adafruit_AMG88xx_python.git

- cd Adafruit_AMG88xx_python

- cd examples

- python thermal_cam.py

  (※python 실행을 중지해도 pygame window 창이 꺼지지 않음으로 코드 추가 편집필요 / https://github.com/inae0615/thermal_camera_controls 업로드함.)
