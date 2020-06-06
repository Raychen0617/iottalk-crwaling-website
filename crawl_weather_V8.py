# coding: utf-8
from bs4 import BeautifulSoup
from selenium import webdriver
import datetime
import globals

globals.initialize() 
region = 'Hshinchu'
#台南測站觀測資料
url = 'https://www.cwb.gov.tw/V8/C/W/OBS_Station.html?ID=46757'

#啟動模擬瀏覽器
driver = webdriver.Chrome()

#取得網頁代碼
driver.get(url)
open(region+'.html','wb').write(driver.page_source.encode('utf-8'))


#指定 lxml 作為解析器
soup = BeautifulSoup(driver.page_source, features='lxml')

# <tbody id='obstime'> 抓過去24小時資料
tbody = soup.find('tbody',{'id':'obstime'})

# <tbody>内所有<tr>標籤
trs = tbody.find_all('tr')

# 使用datetime取得時間年分
year = str(datetime.datetime.now().year)

# #對list中的每一項 <tr>
for tr in trs:
#   取時間, <tr>內的<th>, <th>內為時間 月/日<br>時:分
    d = tr.th.text
    d = year + d
#   字串轉為datetime格式
    #globals.initialize() 
    globals.date=(datetime.datetime.strptime(d, '%Y%m/%d %H:%M'))
    globals.temp=(tr.find('td',{'headers':'temp'}).text)
    #weather.append(tr.find('td',{'headers':'weather'}).find('img')['title'])
    ray = tr.find('td',{'headers':'weather'}).find('img')
    if ray is not None:    
        globals.weather = (ray['title'])
    else:    
        globals.weather = 0
    globals.wind_direction = (tr.find('td',{'headers':'w-1'}).text)
    globals.wind_speed = (tr.find('td',{'headers':'w-2'}).text)
    globals.gust_wind = (tr.find('td',{'headers':'w-3'}).text)
    if not globals.gust_wind.isdigit():
        globals.gust_wind = 0
    globals.visible = (tr.find('td',{'headers':'visible-1'}).text)
    globals.hum = (tr.find('td',{'headers':'hum'}).text)
    globals.pre = (tr.find('td',{'headers':'pre'}).text)
    globals.rain = (tr.find('td',{'headers':'rain'}).text)
    globals.sunlight = (tr.find('td',{'headers':'sunlight'}).text)
    if  globals.sunlight==0 and globals.hum==0 and globals.rain==0:
        print("all zero")
        continue
    else:
        break

#關閉模擬瀏覽器       
driver.quit()
# ---------------------------------------------------------------



"""
print("觀測時間: ",globals.date)
"溫度(°C): ",globals.temp,
"天氣: ",globals.weather)
"風向":globals.wind_direction,
"風力 (m/s)":globals.wind_speed,
"陣風 (m/s)":globals.gust_wind,
"能見度(公里)":globals.visible,
"相對溼度(%)":globals.hum,
"海平面氣壓(百帕)":globals.pre,
"當日累積雨量(毫米)":globals.rain,
"日照時數(小時)":globals.sunlight
)
"""