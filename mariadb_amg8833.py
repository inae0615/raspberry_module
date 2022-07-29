import RPi.GPIO as GPIO
import sys
import time
import pymysql
from Adafruit_AMG88xx import Adafruit_AMG88xx

sensor = Adafruit_AMG88xx()
conn = pymysql.connect(host="0.0.0.0",user="",passwd="",db="")

try :
     with conn.cursor() as cur:

        while True :

            temperature = sensor.readThermistor()
            
            if temperature is not None:
                print('temp=%0.2f',temperature)
                print(type(temperature))

                cur.execute("insert into [tablename] (date_time, temperature) values(default, {0:0.2f})".format(temperature))
                conn.commit()
            else:
                print("Failed to get reading.")
            time.sleep(3)

except KeyboardInterrupt :
       exit()
finally:
       conn.close()