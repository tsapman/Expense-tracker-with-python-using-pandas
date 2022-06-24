import sys
import os
from date import Daytoday
import pandas as pd
from Load import create
from choose import choice


def main():
    create()
    x=choice()
    x=int(x)

    if(x==1):
        day=Daytoday()

    elif(x==2):
        print("Enter the exact day which you have done the expenses:\n")
        Day=input("Day= ")
        month=input("Month= ")
        year=input("Year= ")

        day=Day + "/" + month + "/" + year
        print (day)

    elif(x==3):
        pass
    else:
        sys.exit("\n\t\tGoodbye")

    os.system("pause")

main()