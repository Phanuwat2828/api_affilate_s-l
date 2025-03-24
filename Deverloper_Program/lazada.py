
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
import time
import pandas as pd
import os
import json
from datetime import datetime
import requests
import pyautogui
import pyperclip


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
                status_click = click.Click_component(data.product_image_lazada,1,0.4)

                if(not status_click):
                    status_click = click.Click_component(data.product_image1_lazada,1,0.4)
                
                if(status_click):
                    data.count_product+=1;
                    data.product_total+=1;
                if(data.count_product>=200 or data.product_total>=data.is_product):
                    break;
            print(log.Info("info")+"Excel Max[200]: Now ",data.count_product);
            print(log.Info("info")+"Product_Total Max[",data.is_product,"]:",data.product_total);
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
        
        data_ = read_file.ReadExcelLazada();
        api.SendInformationAPI(data=data_);
        data.is_run = False
    data.count_product = 0;
    data.product_total = 0;
    data.is_product = 0;
    data.is_run = False

data.is_product = 1000;
data.is_run = True;
run_App_lazada();
