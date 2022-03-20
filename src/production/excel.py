import os
import sys
import pandas as pd


wb = pd.ExcelFile("sample.xlsx")
wss = wb.sheet_names



for ws in wss:
    print(ws)