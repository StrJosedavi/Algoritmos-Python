  
import pandas as pd

def CountUsers(data):
    df = pd.DataFrame(data)
    NumbersUsers = df.shape[0]
    return "Total de Registros " + str(NumbersUsers)
