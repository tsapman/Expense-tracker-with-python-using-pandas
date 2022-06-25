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
    else:
        print("Total= 0")