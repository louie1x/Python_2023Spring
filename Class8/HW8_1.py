import requests
import pygsheets

gc = pygsheets.authorize(service_file="Project/causal-scarab-383206-d3edf987cf5e.json")
sht = gc.open_by_url("https://docs.google.com/spreadsheets/d/1mpgr_6vPS_pSIxFawYWXU9czJPpZq4Q-c9j7y5wlYHM/edit#gid=0")
ws = sht[0]
ws = sht.worksheet_by_title("Homework 8_1")

url = "https://api.exchangerate-api.com/v4/latest/TWD"
res = requests.get(url)
data = res.json()

ws.update_value("A2", "美國")
ws.update_value("A3", "日本")
ws.update_value("A4", "香港")

ws.update_value("B2", data["rates"]["USD"])
ws.update_value("B3", data["rates"]["JPY"])
ws.update_value("B4", data["rates"]["HKD"])