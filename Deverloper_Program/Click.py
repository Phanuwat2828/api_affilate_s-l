import pyautogui
import pyperclip
import time
from Info import Info as log
from Data import Data
import os

class Click:
    def Click_component(image,delay,confidence):
        try:
            time.sleep(delay)
            location = pyautogui.locateOnScreen(image, confidence=confidence)  
            if location:
                # หาใจกลางของภาพที่พบ
                if not Data.is_run:
                    print(log.Info("info") + "Process stopped by user.")
                    return
                x, y = pyautogui.center(location)
                # คลิกที่ตำแหน่งของภาพ
                pyautogui.click(x, y)
                print(log.Info("info"),f"คลิกที่ตำแหน่ง: ({x}, {y})",image)
                return True
            else:
                print(log.Info("warning"),"ไม่พบภาพบนหน้าจอ")
                return False
        except FileNotFoundError as e:
            print(log.Info("error"),e)
        except pyautogui.ImageNotFoundException as e:
            print(log.Info("error"),"ไม่พบภาพบนหน้าจอ")
            return False
        
    def press_key(value,delay,time_):
        try:
            for _ in range(0,time_):
                pyautogui.press(value)
                time.sleep(delay)
                if not Data.is_run:
                    print(log.Info("info") + "Process stopped by user.")
                    return
                print(log.Info("info"),"Press "+value," time ",(_+1));
            print(log.Info("info"),value+" Finish!");
        except Exception as e:
            print(log.Info("error"),e)

    def Mouse_scroll(time_,value,delay):
        for _ in range(0,time_):
            if not Data.is_run:
                print(log.Info("info") + "Process stopped by user.")
                return
            pyautogui.scroll(-value)
            time.sleep(delay)
            print(log.Info("info"),"Scroll -",value," time ",(_+1));
        print(log.Info("info"),"Scroll Finish!");

    def Get_chrome():
        time.sleep(3)
        pyperclip.copy(Data.url);
        pyautogui.hotkey('ctrl', 't')
        time.sleep(3)
        pyautogui.hotkey('ctrl','v')
        Click.press_key('enter',1,3)
        print(log.Info("info"),"Get_Chrome Finish")
    
    def delete_all_files_in_folder(folder_path):
        try:
            for file_name in os.listdir(folder_path):  # วนลูปทุกไฟล์ในโฟลเดอร์
                file_path = os.path.join(folder_path, file_name)  # สร้าง path เต็มของไฟล์
                if os.path.isfile(file_path):  # ตรวจสอบว่าเป็นไฟล์
                    os.remove(file_path)  # ลบไฟล์
                    print(log.Info("info"),f"ลบไฟล์: {file_path}")
            print(log.Info("info")," ลบไฟล์ทั้งหมดเสร็จเรียบร้อย!")
        except Exception as e:
            print(log.Info("error"),f"เกิดข้อผิดพลาด: {e}")
    
    def time_start():
        for _ in range(0,3):
            if not Data.is_run:
                print(log.Info("info") + "Process stopped by user.")
                return
            print(log.Info("info"),_+1)
            time.sleep(1)
        print(log.Info("info"),"Start!")
        Click.delete_all_files_in_folder(Data.folder_down);