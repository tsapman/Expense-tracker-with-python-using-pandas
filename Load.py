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


