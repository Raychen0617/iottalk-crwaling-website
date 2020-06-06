# DAI2.py  -- new version of Dummy Device DAI.py, modified by tsaiwn@cs.nctu.edu.tw
# you can get from here:  https://goo.gl/6jtP41   ; Search dummy + iottalk  for other files
import time, DAN, requests, random 
import threading, sys
import os
import globals
import importlib

# ServerURL = 'http://Your_server_IP_or_DomainName:9999' #with no secure connection
# ServerURL = 'http://192.168.20.101:9999' #with no secure connection
#  注意你用的 IoTtalk 伺服器網址或 IP 
ServerURL = 'https://6.iottalk.tw' #with SSL secure connection
# ServerURL = 'https://Your_DomainName' #with SSL connection  (IP can not be used with https)
Reg_addr = None  #if None, Reg_addr = MAC address

mac_addr = 'C86208BD219'  # put here for easy to modify;;  the mac_addr in DAN.py is NOT used
# Copy DAI.py to DAI2.py and then modify the above mac_addr, then you can have two dummy devices
Reg_addr = mac_addr   # Otherwise, the mac addr generated in DAN.py will always be the same !

DAN.profile['dm_name']='Weather_dummy'   # you can change this but should also add the DM in server
DAN.profile['df_list']=['Pressure_L', 'Humidity', 'Rain_L',' SunHrID-I', 'Temperature_L', 'Visibility','Weather','SunHrID-I','Dummy_Control'] 
DAN.profile['d_name']='0716230_weather'
DAN.device_registration_with_retry(ServerURL, Reg_addr)

# global gotInput, date
gotInput=False
date="haha"
allDead=False

###################################
#doRead read input from user
###################################


def doRead( ):    
    global gotInput, date, allDead, temp, weather, wind_direction, wind_speed, gust_wind, visible, hum, pre, rain, sunlight
    while True:
        
        print("crawling.....................")
        import crawl_weather_V8
        print("finish crawling website......")
        date =  crawl_weather_V8.globals.date   
        temp = crawl_weather_V8.globals.temp
        weather = crawl_weather_V8.globals.weather 
        wind_direction = crawl_weather_V8.globals.wind_direction
        wind_speed = crawl_weather_V8.globals.wind_speed
        gust_wind = crawl_weather_V8.globals.gust_wind
        visible = crawl_weather_V8.globals.visible
        hum = crawl_weather_V8.globals.hum
        pre = crawl_weather_V8.globals.pre
        rain = crawl_weather_V8.globals.rain
        sunlight = crawl_weather_V8.globals.sunlight
        
        print("觀測時間: ",globals.date,
         "\n溫度(°C): ",globals.temp,
         "\n天氣: ",globals.weather,
         "\n風向: ",globals.wind_direction,
         "\n風力 (m/s): ",globals.wind_speed,
         "\n陣風 (m/s): ",globals.gust_wind,
         "\n能見度(公里): ",globals.visible,
         "\n相對溼度(%): ",globals.hum,
         "\n海平面氣壓(百帕):　",globals.pre,
         "\n當日累積雨量(毫米): ",globals.rain,
         "\n日照時數(小時):", globals.sunlight
         )

        gotInput=True
        

        if gotInput:
           time.sleep(30) # 30 second execute one time
           importlib.reload(crawl_weather_V8)
        
        



#creat a thread to do Input data from keyboard, by tsaiwn@cs.nctu.edu.tw
threadx = threading.Thread(target=doRead)
threadx.daemon = True
threadx.start()

while True:
    try:
    #Pull data from a device feature called "test_weather"
        value1=DAN.pull('Dummy_Control')
        if value1 != None:
            print (value1[0])
    #Push data to a device feature called "Dummy_Sensor" 
        if gotInput:
           
           value2= pre
           value3 = hum
           
           gotInput=False   # so that you can input again 
           if(allDead): break
           DAN.push ('Pressure_L', value2,  value2)
           time.sleep(1)
           DAN.push ('Humidity', value3,  value3)
           time.sleep(1)
           DAN.push ('Rain_L', rain, rain)
           time.sleep(1)
           DAN.push ('Temperature_L', temp, temp)
           time.sleep(1)
           DAN.push ('Visibility', visible, visible)
           time.sleep(1)
           DAN.push ('Weather', wind_speed, wind_speed)
           time.sleep(1)
           DAN.push ('SunHrID-I', sunlight,sunlight)
           
           



    except Exception as e:
        print(e)
        if str(e).find('mac_addr not found:') != -1:
            print('Reg_addr is not found. Try to re-register...')
            DAN.device_registration_with_retry(ServerURL, Reg_addr)
        else:
            print('Connection failed due to unknow reasons.')
            time.sleep(1)    
    try:
       time.sleep(0.2)
    except KeyboardInterrupt:
       break
time.sleep(0.5)
try: 
   DAN.deregister()
except Exception as e:
   print("===")
print("Bye ! --------------", flush=True)
sys.exit( )