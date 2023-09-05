import pandas as pd
import numpy as np


def CreateTableForExcel(data, NameCsv):
    df = pd.DataFrame(data)
    return df.to_excel("Files/" + NameCsv + ".xlsx", index=False)


def CreateDataFrame(data):
    return pd.DataFrame(data)


