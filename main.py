import sys
import os
from date import Daytoday
import pandas as pd
from Load import create
from choose import choice
from expense_info import info_reason
from expense_info import info_amount
from expense_info import info_date
from Load import info_dataframe
from Load import User
from Load import total_expenses
from Load import create_profile


def main():
    #name=input("User= ")
    #print("Hello ", name)
    w=input("Are you a NEW user? yes/no---->  ")
    if w=="yes":
        print("Creating new account:\n")
        name=input("username= ")
        name=name.lower()
        password=input("password= ")
        user=User()
        user.name=name
        user.password=password
        print("\nWelcome to the Expenses tracker : ",user.name,)
        create_profile(user.name,user.password)
    elif w=="no":
        name = input("username= ")
        name = name.lower()
        password = input("password= ")
        user = User()
        user.name = name
        user.password = password
        print("\nWelcome to the Expenses tracker : ", user.name, )
    while 1:
        x = choice()
        x = int(x)
        profile =  user.user_name()+ ".csv"

        if x == 1:
            day = Daytoday()
            reason = info_reason()
            amount = info_amount()
            amount = float(amount)
            # print(day, "\n",reason, "\t", amount)
            info_dataframe(day, reason, amount, profile)
        elif (x == 2):
            day= info_date()
            reason= info_reason()
            amount=info_amount()
            amount= float(amount)
            info_dataframe(day,reason,amount,profile)
        elif (x == 3):
            total_expenses(profile)
            os.system("pause")
        else:
            print("\n\t\tGoodbye ",name)
            sys.exit("\n\t\t")





#os.system("pause")

main()