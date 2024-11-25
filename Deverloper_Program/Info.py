import time
from datetime import datetime
class Info:
    def Timer_():
        current_time = datetime.now()
        formatted_time = current_time.strftime("[%H:%M:%S]")
        return formatted_time

    def Info(type):
        valueinfo = Info.Timer_()
        if(type=="info"):
            valueinfo+=" [INFO] :"
        elif(type=="warning"):
            valueinfo+=" [WARNING] :"
        elif(type=="error"):
            valueinfo+=" [ERROR] :"
        return valueinfo