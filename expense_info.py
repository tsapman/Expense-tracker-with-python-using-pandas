import sys
import pandas as pd


def info_reason():
    print("Import Information about the expense you have made:\n")
    reason=input("Reason/Concept= ")

    return reason

def info_amount():
    s = input("Amount= ")
    s = float(s)

    return s


def info_date():
    print("Enter the exact day which you have done the expenses:\n")
    Day = input("Day= ")
    month = input("Month= ")
    year = input("Year= ")
    d=Day+"/"+month+"/"+year

    return d

