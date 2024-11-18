
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

def process_split(value):
    product_id = value.split('/')[4]  
    print(Info("info")+"split ");
    return product_id

def sender_api_main(data):
    # main
    url_Api = "http://26.49.17.12:8080/0eea90b98ea1129c8f7c16af9bca09820d5564ac93678c9766000941f5444ade"
    payload = {
        "key":"5a3dec84301206e275f7ca7fa119796c8a5be05d100a2d23ba3a4f189876d03a",
        "datas":data 
    }

    try:
        response = requests.request("POST",url_Api,data=payload)
        return response.status_code
    except:
        return {"status":404,"message":"POST API ERROR."}
def sender_api_detail(data):
    # main
    url_Api = "http://26.49.17.12:8080/5564ac93678c9766000941f5444ade0eea90b98ea1129c8f7c16af9bca09820d"
    payload = {
        "key":"5a3dec84301206e275f7ca7fa119796c8a5be05d100a2d23ba3a4f189876d03a",
        "datas":data 
    }
    
    try:
        response = requests.request("POST",url_Api,data=payload)
        return response.status_code
    except:
        return {"status":404,"message":"POST API ERROR."}
    
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
            "shop_id":None,#String
            "market":"shopee" #String
        }
        for j in range(len(header_csv)):
            data_input = str(df[header_csv[j]][i])
            data_send[head_key[header_csv[j]]] = data_input;
             
            if(j==7):    
                data_send['shop_id'] = process_split(data_input);
                print(Info("info"),i+1," :","รหัสร้านค้า","=",data_send['shop_id']);
            print(Info("info"),i+1," :",header_csv[j],"=",data_send[head_key[header_csv[j]]]);
        data_detail = api_check(data_send[ "item_id"],data_send['shop_id']);
        
        # print( sender_api_main(json.dumps(data_send)))
        print(sender_api_detail(json.dumps(data_detail['data'])));
             
             

def api_check(id_product,shop_id):
    url = "http://api.openchinaapi.com/v1/shopee/products/"+id_product+"/?shop_id="+shop_id+"&nation=th"
    payload={}
    headers = {
        'Authorization':'Token ca7dfebc52c73cbbc88645bad1db57eafb68ef8f'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    data = json.loads(response.text);
    print(Info("info")+"Check Data");
    return data
  
Read_csv();


     

   

# http://api.openchinaapi.com/v1/shopee/products/23624785285/?shop_id=388007409&nation=th

# ลองแบบนี้นะครับว่าได้ไหมครับ

# http://api.openchinaapi.com/v1/shopee/products/ใส่ตัวหลัง/?shop_id=ใส่ตัวหน้า&nation=th

# https://shopee.co.th/product/388007409(ตัวหน้า)/23624785285(ตัวหลัง)
# api.openchinaapi.com