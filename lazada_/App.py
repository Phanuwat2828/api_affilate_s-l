# version 0.0.2
import tkinter as tk
from Api import Api as api
from Click import Click as click
from Data import Data as data
from Info import Info as log
from Read_file import Read_file as read_file


def run_App():
    click.time_start()
    click.Click_component(data.space_,2);
    while(data.product_total<data.is_product):
        first = False;
        while(data.count_product<200):
            if(first):
                click.Mouse_scroll(1,550,5);
            else:
                click.Mouse_scroll(1,250,5);
                first = True;
            for i in range(4):
                status_click = click.Click_component(data.product_image,1)
                if(status_click):
                    count_product+=1;
                    product_total+=1;
                if(data.count_product>=200 and data.product_total>=data.is_product):
                    break;
            print(log.Info("info")+"Excel Max[200]: Now ",data.count_product);
            print(log.Info("info")+"Product_Total Max[",data.is_product,"]:",data.product_total);
            if(data.product_total>=data.is_product):
                break;
        click.Click_component(data.get_link,2);
        click.Click_component(data.export_link,2);
        click.press_key('tab',1,8)
        click.press_key('enter',1,1)
        read_file.Read_Excel()

# Gui 
root = tk.Tk()
root.title("Affiliate Lazada")
def toggle():
    if data.is_run:
        print("หยุดแล้ว!")
        start_stop_button.config(text="Start", bg="green", fg="white")
    else:
        print("เริ่มต้นแล้ว!")  
        start_stop_button.config(text="Stop", bg="red", fg="white")  
    data.is_run = not data.is_run

start_stop_button = tk.Button(root, text="Start", command=toggle,width=10, height=2, bg="green", fg="white",font=("Helvetica", 16, "bold"))
start_stop_button.place(x=20, y=20)
root.geometry("570x1000-0+0")
root.mainloop()