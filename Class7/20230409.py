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


# 大多數常用操作，只需要用到 Path 這個類別
from pathlib import Path

p = Path("Class7/20230409.py")
# p = Path() 

print(p.resolve())