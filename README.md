# Python crwaling dynamic website 

## push data into dashboard

## iottalk-crwaling-website

[weather website](https://www.cwb.gov.tw/V8/C/W/OBS_Station.html?ID=46757)

crwaling area: Hsinchu

## setup:

For windows:<br>
pip3 install selenium <br>
pip3 install beautifulsoup4 <br>
pip3 install lxml <br>
install chromedriver.exe and put it in the python's file <br>
[more info: references (teacher's code)](https://github.com/IoTtalk/Crawler_CWB_V8) <br>

## UPDATE....

### setting up a dashboard in linux environment

* setup

  * install MySQL >= 5.7 <br>
  * sudo pip3 install -r requirements.txt <br>
  * 新增 MySQL 內的 user，允許連線 IP，與資料庫( db_name )，以及權限 (詳見下方注意2) <br>
  * modify `config.py`，根據內部註解依序填上資料 <br>
  * 視情況修改 `db_init.json` (記得要設定 admin 密碼與 DB 初始 table 欄位) <br>
  * 執行 `python3 db.py init`  (don't execute more than one time !!) <br>
  * install tmux <br>
  * execute bash startup.sh (whenever you change anything, execute one time) <br> 

至此 Dashboard 已啟動完成，可用指令 tmux a 查看運行狀況 <br>
(press ctrl+b 1 / ctrl+b 2切換 dashboard 主程式與 DA 查看運行狀況)。

## reference
[more info](https://hackmd.io/5LqVk4MBSCinRXQderD_Jw)

then push the data into dashboaard 

[result vedio](https://youtu.be/n1s-N4cdDXI)


