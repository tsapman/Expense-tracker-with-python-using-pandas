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


def info_dataframe(d,r,a):
    d=pd.DataFrame({"Day":[d],
                    "Reason/Concept":[r],
                    "Amount":[a]
    })

    d.to_csv("expenses.csv",mode="a",index=False,header=False)

