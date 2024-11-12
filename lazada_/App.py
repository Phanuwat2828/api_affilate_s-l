# version 0.0.2

import pyautogui
import time
from datetime import datetime
import pyautogui
import pyperclip
import pandas as pd
import os
import requests
import json

parth_image = "./image/"
id_product  = "1231231412"
api_check_product = "http://api.openchinaapi.com/v1/lazada/products/"+id_product+"?nation=th"
url = "https://adsense.lazada.co.th/index.htm#!/offer/product_offer"
# ชื่อไฟล์ภาพที่ต้องการค้นหาบนหน้าจอ
image_to_find = parth_image+"type.png"
select_product = parth_image+"select_all.png"
get_link = parth_image+"getlink_.png"
export_link = parth_image+"export_.png"
path_file = os.getcwd();
name_file = path_file+"\download\data_promo_list.xlsx";
space_ = parth_image+"space.png"
header_data = [
    "item_id",
    "product_name",
    "sale_price",
    "discounted_price",
    "discounted_percentage",
    "picture_url",
    "product_url",
    "maximum commission_rate",
    "Seller Id",
    "promo_link",
    "promo_short_link"
]

select = [
    "mother_baby.png",
    "beauty.png"
]
# จำนวนครั้งที่ต้องการคลิก
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

def Click_component(image,delay):
    try:
        time.sleep(delay)
        location = pyautogui.locateOnScreen(image, confidence=0.6)  # ค่า confidence ปรับได้เพื่อให้แม่นยำมากขึ้น
        if location:
            # หาใจกลางของภาพที่พบ
            x, y = pyautogui.center(location)
            # คลิกที่ตำแหน่งของภาพ
            pyautogui.click(x, y)
            print(Info("info"),f"คลิกที่ตำแหน่ง: ({x}, {y})",image)
        else:
            print(Info("warning"),"ไม่พบภาพบนหน้าจอ")
    except FileNotFoundError as e:
        print(Info("error"),e)
    except pyautogui.ImageNotFoundException as e:
        print(Info("error"),"ไม่พบภาพบนหน้าจอ")

def press_key(value,delay,time_):
    try:
        for _ in range(0,time_):
            pyautogui.press(value)
            time.sleep(delay)
            
            print(Info("info"),"Press "+value," time ",(_+1));
        print(Info("info"),value+" Finish!");
    except Exception as e:
        print(Info("error"),e)

def Mouse_scroll(time_,value,delay):
    for _ in range(0,time_):
        pyautogui.scroll(-value)
        time.sleep(delay)
        print(Info("info"),"Scroll -",value," time ",(_+1));
    print(Info("info"),"Scroll Finish!");

def Get_chrome():
    time.sleep(3)
    pyperclip.copy(url);
    pyautogui.hotkey('ctrl', 't')
    time.sleep(3)
    pyautogui.hotkey('ctrl','v')
    press_key('enter',1,3)
    print(Info("info"),"Get_Chrome Finish")

def time_start():
    for _ in range(0,3):
        print(Info("info"),_+1)
        time.sleep(1)
    print(Info("info"),"Start!")
def send_API(value):
    pass

def Read_Excel():
    try:
        time.sleep(5)
        read_excel = pd.read_excel(name_file);
        num_rows, num_columns = read_excel.shape
        print(num_rows)
        for i in range(num_rows):
            price = 0;
            data_send = {
                "item_id":None, #String
                "product_name":None,#String
                "sale_price":None, #Float
                "discounted_price":None, #Float
                "discounted_percentage":None, #String
                "picture_url":None, #String
                "product_url":None, #String
                "maximum commission_rate":None, #String
                "commission":None, #Float
                "Seller Id":None, #String
                "promo_link":None, #String
                "promo_short_link":None, #String
                "place":None, #String
                "market":"Lazada" #String
            }
            for j in range(len(header_data)):
                data_input = str(read_excel[header_data[j]][i])
                data_send[header_data[j]] = data_input;
                print(Info("info"),"[",i+1,": "+header_data[j]+" ] ",data_send[header_data[j]]);
                if(j==3):
                    price = float(data_input);
                if(j==7):
                    percentage_value = float(data_input.replace("%", ""))
                    data_send["commission"] = percentage_value/100*price;
                    print(Info("info"),"[",i+1,": commission ] ",data_send["commission"]);
        print(Info("info"),"Remove ",name_file)
        os.remove(name_file)
    except FileNotFoundError as e:
        print(Info("info"),"Remove ",name_file)
        os.remove(name_file)
        print(Info("error"),e)

def api_check(value):
    url = "http://api.openchinaapi.com/v1/lazada/products/"+value+"?nation=th"
    payload={}
    headers = {
        'Authorization':'Token ca7dfebc52c73cbbc88645bad1db57eafb68ef8f'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    data = json.loads(response.text);
    print(Info("info")+"Check Data");
    return data['data']


def run_App():
    time_start()
    Get_chrome()
    Click_component(image_to_find,5);
    Click_component(parth_image+select[0],2);
    Click_component(space_,2);
    Mouse_scroll(25,700,5);
    Click_component(select_product,2);
    press_key('tab',1,1)
    press_key('enter',1,1)
    Click_component(get_link,2);
    Click_component(export_link,2);
    press_key('tab',1,8)
    press_key('enter',1,1)
    Read_Excel()

# run_App();
