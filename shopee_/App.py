
import pyautogui
import time
from datetime import datetime
import pyautogui
import pyperclip
import pandas as pd
import os
import requests
import json

path_file = os.getcwd();
name_file = path_file+"\download\\test.csv";
header_csv = [
    "รหัสสินค้า",
    "ชื่อสินค้า",
    "ราคา",
    "ขาย",
    "ชื่อร้านค้า",
    "อัตราค่าคอมมิชชัน",
    "คอมมิชชัน",
    "ลิงก์สินค้า",
    "ลิงก์ข้อเสนอ"
]
head_key = {
    "รหัสสินค้า":"item_id",
    "ชื่อสินค้า":"product_name",
    "ราคา": "sale_price",
    "ขาย":"sold",
    "ชื่อร้านค้า":"name_seller",
    "อัตราค่าคอมมิชชัน":"commission_rate",
    "คอมมิชชัน":"commission",
    "ลิงก์สินค้า":"product_url",
    "ลิงก์ข้อเสนอ":"promo_link"
}
def Timer_():
    current_time = datetime.now()
    formatted_time = current_time.strftime("[%H:%M:%S]")
    return formatted_time

def Info(type):
    valueinfo = Timer_()
    if(type=="info"):
        valueinfo+=" [INFO] :"
    elif(type=="warning"):
        valueinfo+=" [WARNING] :"
    elif(type=="error"):
        valueinfo+=" [ERROR] :"
    return valueinfo

def Read_csv():
    df = pd.read_csv(name_file)
    num_rows, num_columns = df.shape
    for i in range(num_rows):
        data_send = {
            "item_id":None, #String
            "product_name":None,#String
            "sale_price":None, #Float
            "sold":None, #String
            "name_seller":None, #String
            "product_url":None, #String
            "commission_rate":None, #String
            "commission":None, #Float
            "promo_link":None, #String
            "place":None, #String
            "market":"Shopee" #String
        }
        for j in range(len(header_csv)):
             data_input = str(df[header_csv[j]][i])
             data_send[head_key[header_csv[j]]] = data_input;

             print(Info("info"),i+1," :",header_csv[j],"=",data_send[head_key[header_csv[j]]]);




def api_check(value):
    url = "http://api.openchinaapi.com/v1/shopee/products/"+value+"?nation=th"
    payload={}
    headers = {
        'Authorization':'Token ca7dfebc52c73cbbc88645bad1db57eafb68ef8f'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    data = json.loads(response.text);
    print(Info("info")+"Check Data");
    return data
 
# Read_csv();

print(api_check("13457251239"));
