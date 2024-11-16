import pyautogui
import pyperclip
import time
from Info import Info as log
from Data import Data
class Click:

    def Click_component(image,delay):
        try:
            time.sleep(delay)
            location = pyautogui.locateOnScreen(image, confidence=0.6)  # ค่า confidence ปรับได้เพื่อให้แม่นยำมากขึ้น
            if location:
                # หาใจกลางของภาพที่พบ
                x, y = pyautogui.center(location)
                # คลิกที่ตำแหน่งของภาพ
                pyautogui.click(x, y)
                return True
                print(log.Info("info"),f"คลิกที่ตำแหน่ง: ({x}, {y})",image)
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
                
                print(log.Info("info"),"Press "+value," time ",(_+1));
            print(log.Info("info"),value+" Finish!");
        except Exception as e:
            print(log.Info("error"),e)

    def Mouse_scroll(time_,value,delay):
        for _ in range(0,time_):
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
    
    def time_start():
        for _ in range(0,3):
            if not Data.is_run:
                print(log.Info("info") + "Process stopped by user.")
                return
            print(log.Info("info"),_+1)
            time.sleep(1)
        print(log.Info("info"),"Start!")