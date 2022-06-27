import sys
import pandas as pd
import os.path

def create(p):
    file_exists=os.path.exists(p)
    if(file_exists):
        pass
    else:
        with open(p,"w") as file:
            pass

def info_dataframe(d,r,a,p):
    file_exists=os.path.exists(p)
    if file_exists:
        d = pd.DataFrame({"Day": [d],
                          "Reason/Concept": [r],
                          "Amount": [a]
                          })

        d.to_csv(p, mode="a", index=False, header=False)

    else:
        create(p)
        d = pd.DataFrame({"Day": [d],
                          "Reason/Concept": [r],
                          "Amount": [a]
                          })

        d.to_csv(p, mode="a", index=False, header=True)


class User(object):
    def __int__(self,name,password):
        self.name = name
        self.password = password

    def user_name(self):
        return self.name
    def user_password(self):
        return self.password

def total_expenses(profile):
    file_exists=os.path.exists(profile)
    if file_exists:
        df=pd.read_csv(profile)
        df.at["Total" , "Amount"]=df["Amount"].sum()
        print(df)
        print("\n")
    else:
        print("Total= 0\n")


def create_profile(name,password):
    d=pd.DataFrame({"Username":[name],
                    "Password":[password]
    })

    file_exists=os.path.exists("users.csv")

    if file_exists:
        d.to_csv("users.csv",mode="a",index=False,header=False)

    else:
        create("users.csv")
        d.to_csv("users.csv",mode="a",index=False,header= True)


def check_user(name,password):
    d=pd.read_csv("users.csv")
    d_list=d.values.tolist()
    #print("\nusers",d_list, "\n")
    x1 = 0

    if [name,password] in d_list:
        x1 = 1
        #print("x1=", x1)
        return x1
    else:
        return x1