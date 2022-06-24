import sys
import os
from date import Daytoday
import pandas as pd
from Load import create
from choose import choice
from expense_info import info_reason
from expense_info import info_amount
from Load import info_dataframe


def main():
    name=input("User= ")
    print("Hello ", name)
    while 1:
        x = choice()
        x = int(x)
        profile = name + ".csv"

        if x == 1:
            day = Daytoday()
            reason = info_reason()
            amount = info_amount()
            amount = float(amount)
            # print(day, "\n",reason, "\t", amount)
            info_dataframe(day, reason, amount, profile)
        elif (x == 2):
            print("Enter the exact day which you have done the expenses:\n")
            Day = input("Day= ")
            month = input("Month= ")
            year = input("Year= ")

            day = Day + "/" + month + "/" + year


        elif (x == 3):
            pass
        else:
            print("\n\t\tGoodbye ",name)
            sys.exit("\n\t\t")





#os.system("pause")

main()