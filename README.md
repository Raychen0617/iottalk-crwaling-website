# iottalk-crwaling-website

using python to cwal dynamic website and then send it to iottalk's cyber  device

https://www.cwb.gov.tw/V8/C/W/OBS_Station.html?ID=46757

crwaling area: Hsinchu

setup:

For windows:

pip3 install selenium
pip3 install beautifulsoup4
pip3 install lxml

install chromedriver.exe and put it in the python's file

more info: references (teacher's code): https://github.com/IoTtalk/Crawler_CWB_V8

# UPDATE....

setting up a dash board in linux environment

簡易安裝說明

安裝 MySQL >= 5.7
sudo pip3 install -r requirements.txt 安裝相關需要套件
新增 MySQL 內的 user，允許連線 IP，與資料庫( db_name )，以及權限 (詳見下方注意2)
修改 config.py，根據內部註解依序填上資料
視情況修改 db_init.json (記得要設定 admin 密碼與 DB 初始 table 欄位)
執行 python3 db.py init  (注意3)
安裝好 tmux
執行 bash startup.sh  (注意4)

至此 Dashboard 已啟動完成，可用指令 tmux a 查看運行狀況
(按ctrl+b 1 / ctrl+b 2切換 dashboard 主程式與 DA 查看運行狀況)。

詳情請見:https://hackmd.io/5LqVk4MBSCinRXQderD_Jw

push the data into dashboaard 

result:


