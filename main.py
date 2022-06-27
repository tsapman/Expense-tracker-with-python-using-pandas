import sys
import os
from date import Daytoday
from choose import choice
from expense_info import info_reason
from expense_info import info_amount
from expense_info import info_date
from Load import info_dataframe
from Load import User
from Load import total_expenses
from Load import create_profile
from Load import check_user



def Log():
    name = input("username= ")
    name = name.lower()
    password=input("password= ")
    password=str(password)
    user = User()
    user.name = name
    user.password = password


    return user.name,user.password


def main():
    print("\t\t\t\t\t\t\t\t***** Welcome to the Expense tracker!!!*****\n")
    w=input("Are you a NEW user? yes/no---->  ")
    if w=="yes":
        print("Creating new account:\nThe password must contain at least 1 number and 1 char\n")
        name, password = Log()
        x = check_user(name, password)
        while x==1:
            print("the username and the password are used from another user try another combination:\n")
            name, password = Log()
            x = check_user(name, password)
        create_profile(name,password)
        print("\nWelcome to the Expenses tracker : ", name)

    elif w=="no":
        x=0
        i=1
        name, password = Log()
        while x!=1 and i<4:
            x=check_user(name,password)
            i=i+1
            if(x!=1):
                print("wrong username/password- try againg  \t\t\t\t\t\t\t\t\tremaining attempts = ", 4-i,"\n")
                name, password = Log()
            if(x==1):
                print("Logging\n\nWelcome to the Expenses tracker : ", name)
                break

        if(x==0):
            sys.exit("\n\t\tAnable to authenticate try later!!!")
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