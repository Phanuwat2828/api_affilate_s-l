# version 0.1.0 lazada & shopee
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
from tkinter import messagebox
from tkinter import PhotoImage

# Gui 
root = tk.Tk()
root.title("Affiliate Lazada")
icon = PhotoImage(file=data.icon_lazada)  # ระบุชื่อไฟล์หรือเส้นทางของไฟล์ PNG
root.iconphoto(False, icon)  # เปลี่ยนไอคอนของหน้าต่าง
label_api_conf  = tk.Label(root, text="จำนวณสินค้าที่ส่งไปแล้ว api confirm : "+str(data.api_conf),font=(14),fg="green")
label_Excel= tk.Label(root, text="จำนวณสินค้าที่เลือกลง Excel สูงสุด 200 ชิ้น : "+str(data.count_product),font=(14),fg="green")
label_api_conf.place(x=20,y=144)
label_Excel.place(x=20,y=164)
label_Now = tk.Label(root, text="จำนวณสินค้าทั้งหมดตอนนี้ : "+str(data.product_total),font=(14),fg="green")
label_Now.place(x=20,y=184)
label_max = tk.Label(root, text="จำนวณสินค้าที่ต้องการ : "+str(data.is_product),font=(14),fg="red")
label_max.place(x=20,y=204)
entry_var = tk.StringVar(value="200")



text_output = tk.Text(root, wrap="word", width=60, height=38, font=("Arial", 12),bd=0,relief="flat")
text_output.place(x=10,y=270)
sys.stdout = show_log(text_output)
sys.stderr = show_log(text_output)

def update_labels():
    if(data.mode=="lazada"):
        label_api_conf.config(text="จำนวณสินค้าที่ส่งไปแล้ว api confirm : " + str(data.api_conf))
        label_Excel.config(text="จำนวณสินค้าที่เลือกลง Excel สูงสุด 200 ชิ้น : " + str(data.count_product))
        label_Now.config(text="จำนวณสินค้าทั้งหมดตอนนี้ : " + str(data.product_total))
        label_max.config(text="จำนวณสินค้าที่ต้องการ : " + str(data.is_product))
    else:
        label_api_conf.config(text="จำนวณสินค้าที่ส่งไปแล้ว api confirm : " + str(data.api_conf))
        label_Excel.config(text="จำนวณสินค้าที่เลือกลง Excel สูงสุด 100 ชิ้น : " + str(data.count_product))
        label_Now.config(text="จำนวณสินค้าทั้งหมดตอนนี้ : " + str(data.product_total))
        label_max.config(text="จำนวณสินค้าที่ต้องการ : " + str(data.is_product))

def run_App_lazada():
    click.time_start()
    if not data.is_run:
        print(log.Info("info") + "Process stopped by user.")
        return
    click.Click_component(data.space_lazada,2,0.6);
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
                if not data.is_run:
                    print(log.Info("info") + "Process stopped by user.")
                    return
                status_click = click.Click_component(data.product_image_lazada,1,0.6)

                if(not status_click):
                    status_click = click.Click_component(data.product_image1_lazada,1,0.6)
                
                if(status_click):
                    data.count_product+=1;
                    data.product_total+=1;
                    update_labels();
                if(data.count_product>=200 or data.product_total>=data.is_product):
                    break;
            print(log.Info("info")+"Excel Max[200]: Now ",data.count_product);
            print(log.Info("info")+"Product_Total Max[",data.is_product,"]:",data.product_total);
            update_labels();
            if(data.product_total>=data.is_product):
                break;
        click.Click_component(data.get_link_lazada,2,0.6);
        if not data.is_run:
                print(log.Info("info") + "Process stopped by user.")
                return
        click.Click_component(data.export_link_lazad,2,0.6);
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
        update_labels();
        data.is_run = False
    start_stop_button.config(text="Start", bg="green", fg="white")
    data.is_run = False

def run_App_shopee():
    click.time_start()
    if not data.is_run:
        print(log.Info("info") + "Process stopped by user.")
        return
    status_ = click.Click_component(data.space_shopee,1,0.7);
    if not data.is_run:
        print(log.Info("info") + "Process stopped by user.")
        return
    click.Mouse_scroll(2,700,5);
    while(data.product_total<data.is_product):
        data.count_product=0;
        while(data.count_product<100):
            if not data.is_run:
                print(log.Info("info") + "Process stopped by user.")
                return
            status_ = click.Click_component(data.select_product_shopee,1,0.6);
            if(status_):
                data.count_product+=20;
                update_labels();
            if(data.count_product>=100 or data.product_total>=data.is_product or data.count_product>=(data.is_product-data.product_total)):
                break;
            if not data.is_run:
                print(log.Info("info") + "Process stopped by user.")
                return
            click.Mouse_scroll(1,500,5);
            click.Click_component(data.change_page_shopee,1,0.8);
            print(log.Info("info")+"Excel Max[100]: Now ",data.count_product);
            print(log.Info("info")+"Product_Total Max[",data.is_product,"]:",data.product_total);

        click.Click_component(data.get_link_shopee,1,0.7);
        if not data.is_run:
            print(log.Info("info") + "Process stopped by user.")
            return
        click.Click_component(data.take_link_shopee,2,0.8);
        if not data.is_run:
            print(log.Info("info") + "Process stopped by user.")
            return
        read_file.Read_csv();
        if not data.is_run:
            print(log.Info("info") + "Process stopped by user.")
            return
        click.Click_component(data.cant_shopee,1,0.8);
        if not data.is_run:
            print(log.Info("info") + "Process stopped by user.")
            return
        click.Click_component(data.cant2_shopee,2,0.9);
        update_labels();
    start_stop_button.config(text="Start", bg="green", fg="white")
    data.is_run = False

def on_submit():
    try:
        update_labels();
        data.is_product = int(entry.get())  
        entry.delete(0, tk.END)  
    except Exception as e:
        pass

label_entry1 = tk.Label(root, text="ป้อนจำนวณสินค้า :",font=("Helvetica", 13),fg="#091057")
label_entry1.place(x=180, y=20)
entry = tk.Entry(root, width=20,textvariable=entry_var,font=("Helvetica", 14),bd=0,relief="flat")
entry.place(x=318,y=21)

def toggle():
    label_Now.config(text="จำนวณสินค้าทั้งหมดตอนนี้ : "+str(data.product_total))
    if data.is_run:
        if messagebox.askyesno("ยืนยัน", "คุณต้องการหยุดการทำงานหรือไม่?"):
            data.count_product = 0;
            data.product_total = 0;
            data.is_product = 0;
            data.is_run = False
            start_stop_button.config(text="Start", bg="green", fg="white")
            update_labels()
        else:
            print(log.Info("info") + "User canceled stopping the process.")
    else:
        data.is_run = True
        start_stop_button.config(text="Stop", bg="red", fg="white") 
        on_submit();
        update_labels()
        if(data.mode=="lazada"):
            thread = threading.Thread(target=run_App_lazada)
        else:
            thread = threading.Thread(target=run_App_shopee)
        thread.daemon = True  # ให้เธรดหยุดเมื่อปิดโปรแกรม
        thread.start()

start_stop_button = tk.Button(root, text="Start", command=toggle,width=10, height=2, bg="green", fg="white",font=("Helvetica", 13),bd=0,relief="flat")
start_stop_button.place(x=20, y=20)

def on_select(event):
    data.selected_option = combo.get()
    print(log.Info('info'),"Selected "+data.selected_option)

combo = ttk.Combobox(root, values=data.options_lazada, state="readonly",font=("Helvetica", 14))
combo.place(x=270, y=64, width=230)
combo.set("อุปกรณ์-อิเล็กทรอนิกส์")
combo.bind("<<ComboboxSelected>>", on_select) #add even
label_entry2 = tk.Label(root, text="เลือกกลุ่ม :",font=("Helvetica", 13),fg="#091057")
label_entry2.place(x=180, y=65)

def change_mode():
    if(data.mode == "lazada"): #shopee
        icon = PhotoImage(file=data.icon_shopee)  # ระบุชื่อไฟล์หรือเส้นทางของไฟล์ PNG
        root.iconphoto(False, icon)  # เปลี่ยนไอคอนของหน้าต่าง
        data.mode="shopee"
        mode.config(text=data.mode,bg="#FA4032")
        label_entry1.config(fg="#FA4032")
        label_entry2.config(fg="#FA4032")
        root.title("Affiliate Shopee")
        text_output.config(fg="#FA4032")
        label_Excel.config(text="จำนวณสินค้าที่เลือกลง Excel สูงสุด 100 ชิ้น : " + str(data.count_product))
    else: #lazada
        icon = PhotoImage(file=data.icon_lazada)  # ระบุชื่อไฟล์หรือเส้นทางของไฟล์ PNG
        root.iconphoto(False, icon)  # เปลี่ยนไอคอนของหน้าต่าง
        data.mode="lazada"
        mode.config(text=data.mode,bg="#091057")
        label_entry1.config(fg="#091057")
        label_entry2.config(fg="#091057")
        text_output.config(fg="#091057")
        root.title("Affiliate Lazada")
        label_Excel.config(text="จำนวณสินค้าที่เลือกลง Excel สูงสุด 200 ชิ้น : " + str(data.count_product))

mode = tk.Button(root, text="lazada", command=change_mode,width=10, height=1, bg="#091057", fg="white",font=("Helvetica", 13),bd=0,relief="flat")
mode.place(x=20, y=80)
root.geometry("570x1000-0+0")
root.mainloop()