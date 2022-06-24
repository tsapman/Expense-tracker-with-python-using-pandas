import sys
import os
from date import Daytoday
import pandas as pd
from Load import create
from choose import choice
from expense_info import info_reason
from expense_info import info_amount
from expense_info import info_dataframe


def main():
    create()
    x=choice()
    x=int(x)

    if(x==1):
        day=Daytoday()
        reason=info_reason()
        amount=info_amount()
        amount=float(amount)
        # print(day, "\n",reason, "\t", amount)
        info_dataframe(day,reason,amount)
    elif(x==2):
        print("Enter the exact day which you have done the expenses:\n")
        Day=input("Day= ")
        month=input("Month= ")
        year=input("Year= ")

        day=Day + "/" + month + "/" + year


    elif(x==3):
        pass
    else:
        sys.exit("\n\t\tGoodbye")

    os.system("pause")

main()