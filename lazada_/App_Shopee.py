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
    click.time_start()
    click.Mouse_scroll(2,700,5);
    for j in range(1):
        for i in range(1):
            click.Click_component(data.select_product_shopee,1,0.6);

            click.Click_component(data.get_link_shopee,1,0.7);
            click.Click_component(data.take_link_shopee,2,0.8);

            click.Click_component(data.change_page_shopee,1,0.8);

            click.Click_component(data.cant_shopee,1,0.8);
            click.Click_component(data.cant2_shopee,2,0.9);



run_app()