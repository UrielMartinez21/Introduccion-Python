import numpy as np
import pandas as pd

data ={
    'ciudades':['caracas','guadalajara','la habana', 'cancun', 'guasdalito'],
    'poblacion': [100000,200000,340000,210000,300000],
    'infectados': [600,400,35000,43000,3002]
}

df=pd.DataFrame(data)
print(df)