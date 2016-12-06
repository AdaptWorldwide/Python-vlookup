import pandas as pd
import glob
import os
import numpy as np
import re
import pandas.io.sql as pd_sql
import sqlite3 as sql
import datetime
import requests


file = r'book1.csv'
classification = r'book2.csv'

# Combine all the CSV's together Note: Must be in the same format

df = pd.read_csv(file, sep='\s*,\s*', na_filter=False, index_col=False, delimiter=',', encoding = 'latin1', error_bad_lines = False)
df1 = pd.read_csv(classification, sep='\s*,\s*', na_filter=False, index_col=False, delimiter=',', encoding = 'latin1', error_bad_lines = False)
#df10.drop_duplicates(['Path'], keep='first')

df.rename(columns = lambda x: x.replace(' ', '_'), inplace=True)
df.rename(columns = lambda x: x.replace('ï»¿', ''), inplace=True)
print(df[:10])

# Classification against the index classification file

df2 = df.merge(df1, on='Value', how='left')

print(df2[:10])

df2.to_csv(r'Combined.csv', sep=',', encoding='utf-8')