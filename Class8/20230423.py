import requests

# # 不帶條件
# r = requests.get("https://www.google.com/")

# print(r.status_code)

# # 有帶條件
# payload = {"key1": "value1", "key2": "value2"}
# r = requests.get("https://www.google.com/", params = payload)

# r = requests.post("https://www.google.com/", data = {"key":"value"})

#------------------------------------------------------------------------------------------

url = "https://api.exchangerate-api.com/v4/latest/TWD"
res = requests.get(url)
data = res.json()
print("日幣對台幣的匯率為"+str(data["rates"]["JPY"]))
