import pandas as pd
import matplotlib

df = pd.read_csv("dados.csv")



def truncar(bairro):
    return bairro[:3]

print(df["bairro"].apply(lambda x: x[:3]))

df["preco"].plot.hist()