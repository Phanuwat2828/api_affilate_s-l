# version 0.0.1
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




def run_app():
    data.is_product = 200;

    click.time_start()
    status_ = click.Click_component(data.space_shopee,1,0.7);
    click.Mouse_scroll(2,700,5);
    while(data.product_total<data.is_product):
        data.count_product=0;
        while(data.count_product<100):
            status_ = click.Click_component(data.select_product_shopee,1,0.6);
            if(status_):
                data.count_product+=20;
                data.product_total+=20;
            click.Click_component(data.change_page_shopee,1,0.8);
            print(log.Info("info")+"Excel Max[100]: Now ",data.count_product);
            print(log.Info("info")+"Product_Total Max[",data.is_product,"]:",data.product_total);
        
        click.Click_component(data.get_link_shopee,1,0.7);
        click.Click_component(data.take_link_shopee,2,0.8);
        read_file.Read_csv();
        click.Click_component(data.cant_shopee,1,0.8);
        click.Click_component(data.cant2_shopee,2,0.9);



run_app()