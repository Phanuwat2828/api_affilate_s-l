# version 0.0.4
from Api import Api as api
from Click import Click as click
from Data import Data as data
from Info import Info as log
from Read_file import Read_file as read_file
from Show_log import ConsoleRedirector as show_log

import tkinter as tk
from Data import Data as data

import threading
import sys
from tkinter import ttk



# Gui 
root = tk.Tk()
root.title("Affiliate Lazada")
label_api_conf  = tk.Label(root, text="จำนวณสินค้าที่ส่งไปแล้ว api confirm : "+str(data.api_conf),font=(14))
label_Excel= tk.Label(root, text="จำนวณสินค้าที่เลือกตอนนี้ : "+str(data.count_product),font=(14))
label_api_conf.place(x=20,y=144)
label_Excel.place(x=20,y=164)
label_Now = tk.Label(root, text="จำนวณสินค้าทั้งหมดตอนนี้ : "+str(data.product_total),font=(14))
label_Now.place(x=20,y=184)
label_max = tk.Label(root, text="จำนวณสินค้าที่ต้องการ : "+str(data.is_product),font=(14))
label_max.place(x=20,y=204)
entry_var = tk.StringVar(value="200")

text_output = tk.Text(root, wrap="word", width=60, height=38, font=("Arial", 12))
text_output.place(x=10,y=300)
sys.stdout = show_log(text_output)
sys.stderr = show_log(text_output)

def update_labels():
    label_api_conf.config(text="จำนวณสินค้าที่ส่งไปแล้ว api confirm : " + str(data.api_conf))
    label_Excel.config(text="จำนวณสินค้าที่เลือกตอนนี้ : " + str(data.count_product))
    label_Now.config(text="จำนวณสินค้าทั้งหมดตอนนี้ : " + str(data.product_total))
    label_max.config(text="จำนวณสินค้าที่ต้องการ : " + str(data.is_product))

def run_App():
    click.time_start()
    if not data.is_run:
        print(log.Info("info") + "Process stopped by user.")
        return
    click.Click_component(data.space_,2);
    if not data.is_run:
        print(log.Info("info") + "Process stopped by user.")
        return
    while(data.product_total<data.is_product):
        first = False;
        while(data.count_product<200):
            if not data.is_run:
                print(log.Info("info") + "Process stopped by user.")
                return
            if(first):
                click.Mouse_scroll(1,550,5);
            else:
                click.Mouse_scroll(1,250,5);
                first = True;
            for i in range(4):
                status_click = click.Click_component(data.product_image,1)
                if(status_click):
                    data.count_product+=1;
                    data.product_total+=1;
                    update_labels();
                if(data.count_product>=200 and data.product_total>=data.is_product):
                    break;
            print(log.Info("info")+"Excel Max[200]: Now ",data.count_product);
            print(log.Info("info")+"Product_Total Max[",data.is_product,"]:",data.product_total);
            if(data.product_total>=data.is_product):
                break;
        click.Click_component(data.get_link,2);
        if not data.is_run:
                print(log.Info("info") + "Process stopped by user.")
                return
        click.Click_component(data.export_link,2);
        if not data.is_run:
                print(log.Info("info") + "Process stopped by user.")
                return
        click.press_key('tab',1,8)
        if not data.is_run:
                print(log.Info("info") + "Process stopped by user.")
                return
        click.press_key('enter',1,1)
        if not data.is_run:
                print(log.Info("info") + "Process stopped by user.")
                return
        read_file.Read_Excel()

def on_submit():
    try:
        update_labels();
        data.is_product = int(entry.get())  
        entry.delete(0, tk.END)  
    except Exception as e:
        pass

def toggle():
    label_Now.config(text="จำนวณสินค้าทั้งหมดตอนนี้ : "+str(data.product_total))
    if data.is_run:
        data.count_product = 0;
        data.product_total = 0;
        data.is_product = 0;
        data.api_conf = 0;
        data.is_run = False
        update_labels()
        start_stop_button.config(text="Start", bg="green", fg="white")
    else:
        data.is_run = True
        start_stop_button.config(text="Stop", bg="red", fg="white") 
        on_submit();
        update_labels()
        thread = threading.Thread(target=run_App)
        thread.daemon = True  # ให้เธรดหยุดเมื่อปิดโปรแกรม
        thread.start()
    
def on_select(event):
    data.selected_option = combo.get()
    print(log.Info('info'),"Selected "+data.selected_option)
   
combo = ttk.Combobox(root, values=data.options, state="readonly")
combo.place(x=270, y=64, width=200)
combo.set("เลือกตัวเลือก")
combo.bind("<<ComboboxSelected>>", on_select) #add even

start_stop_button = tk.Button(root, text="Start", command=toggle,width=10, height=2, bg="green", fg="white",font=("Helvetica", 16, "bold"))
start_stop_button.place(x=20, y=20)

label_entry = tk.Label(root, text="ป้อนจำนวณสินค้า :",font=("Helvetica", 13))
label_entry.place(x=180, y=20)
label_entry = tk.Label(root, text="เลือกกลุ่ม :",font=("Helvetica", 13))
label_entry.place(x=180, y=60)
entry = tk.Entry(root, width=20,textvariable=entry_var)
entry.place(x=318,y=24)

root.geometry("570x1000-0+0")
root.mainloop()