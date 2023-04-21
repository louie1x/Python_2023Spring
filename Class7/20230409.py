# from twilio.rest import Client

# account_sid = 'ACcec416adbfcdcad6d6e9747226a31bf5'
# auth_token = 'bd9d9c370aba7787914cce37d0343ed5'
# client = Client(account_sid, auth_token)

# message = client.messages.create(
#     messaging_service_sid='MG0b78f4bc3e04e98bf5afdd04db2406ff',
#     body='你好，你已經成功傳送簡訊 :D',
#     to='+886988321612'
# )

# print(message.sid)

#-----------------------

# # 大多數常用操作，只需要用到 Path 這個類別
# from pathlib import Path
# p = Path("Class7/20230409.py")
# # p = Path() 

# print(p.resolve())

#-----------------------

import pygsheets

# 設定 google cloud 用戶：讓 google sheet 知道你的身份
gc = pygsheets.authorize(service_file="Project/causal-scarab-383206-d3edf987cf5e.json")
# 連接試算表：讓 google sheet 知道要更改哪一個試算表
sht = gc.open_by_url("https://docs.google.com/spreadsheets/d/1mpgr_6vPS_pSIxFawYWXU9czJPpZq4Q-c9j7y5wlYHM/edit#gid=0")

# 利用 Index 選取工作表
ws = sht[0]
# 利用名字選取工作表
ws = sht.worksheet_by_title("Sheet1")

# 讀取表中內容
value = ws.get_value("A1")
A1 = ws.cell("A1")
print("A1's value: "+value)

# 清除sheet內所有值
ws.clear()
# for i in range(100):
#     ws.update_value("A"+str(i), "耶依")