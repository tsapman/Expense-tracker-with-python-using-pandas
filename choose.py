import sys

def choice():
    print("================================================================================================================================================================\n")
    print("Menu:\n\t1.import Today 's Expenses\n\t2.import Previous day expenses\n\t3.Show amount of expenses so far\n\t4.exit\n\t")
    x=input("select---> ")
    x=int(x)
    while x<0 or x>4:
        x=input("You have chosen an invalid operation please input the number again----> ")
        x=int(x)

    return x