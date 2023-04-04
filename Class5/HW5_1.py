# 引入 MIMEText 物件
from email.mime.text import MIMEText
# 如果想要在電子郵件中加入圖片，則需在Python專案中引用MIMEImage類別，並且引用pathlib函式庫來讀去照片
from email.mime.image import MIMEImage
from pathlib import Path
# 引入 MIMEMultipart 物件
from email.mime.multipart import MIMEMultipart
# Python專案中的電子郵件內容完成後，接下來就要設定Gmail的SMPT伺服器來寄送
import smtplib

# 建立 MIMEText 物件
text = MIMEText("我是江承軒Louie, 我喜歡打籃球, 我也喜歡打電動, 我最常打的電動是地平線5。我最喜歡的食物是牛排。")
image = MIMEImage(Path("/Users/Louie/Documents/Python_2023Spring/PotatoMan.png").read_bytes())

# 創建並設定 MIMEMultipart 物件
content = MIMEMultipart() # 建立 MIMEMultipart 物件
content["subject"] = "2023 春季班 自我介紹" # 郵件標題
content["from"] = "louiechiang907@gmail.com" # 寄件者
content["to"] = "kubetech.academy0524@gmail.com" # 收件者

# 郵件內容使用 MIMEMultipart 物件的 attach 方法 (Method) 進行設定
content.attach(text) # 郵件內容
content.attach(image) # 郵件圖片內容

# 建立 smtplib 物件 (host: 伺服器位置, port: 連接埠號)
smtp = smtplib.SMTP(host = "smtp.gmail.com", port = "587")

# 利用 with 來自動釋放資源
with open("Class5/password.txt", "r") as f:
    mailToken = f.read()

with smtp: # 利用 with 來自動釋放資源
    try:
        smtp.ehlo() # 驗證 SMTP 伺服器
        smtp.starttls() # 建立加密傳輸
        smtp.login("louiechiang907@gmail.com", mailToken)
        smtp.send_message(content) # 寄送郵件
        print("Your Email has been successfully sent")
        smtp.quit()
    except Exception as e:
        print("Errror message: ", e)