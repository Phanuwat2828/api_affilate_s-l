# version 0.0.1

import pyautogui
import time
from datetime import datetime
import pyautogui

parth_image = "./image/"
url = "https://adsense.lazada.co.th/index.htm#!/offer/product_offer"
# ชื่อไฟล์ภาพที่ต้องการค้นหาบนหน้าจอ
image_to_find = parth_image+"type.png"
select_product = parth_image+"select_all.png"
get_link = parth_image+"getlink_.png"
export_link = parth_image+"export_.png"
name_file = "data_promo_list.xls";
space_ = parth_image+"space.png"

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

    



Click_component(image_to_find,5);
Click_component(parth_image+select[0],2);
Click_component(space_,2);
Mouse_scroll(20,700,5);
Click_component(select_product,2);
press_key('tab',1,1)
press_key('enter',1,1)
Click_component(get_link,2);
Click_component(export_link,2);
press_key('tab',1,8)

