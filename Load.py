import sys
import pandas as pd
import os.path

def create():
    file_exists=os.path.exists("expenses.csv")
    if(file_exists):
        pass
    else:
        with open("expenses.csv","w") as file:
            pass

create()



