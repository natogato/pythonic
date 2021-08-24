import py7zr
with py7zr.SevenZipFile("prices.7z", 'r') as archive:
    archive.extractall()

import pandas as pd
df = pd.read_csv('prices.csv')
# df.head()
df.to_parquet('prices.parquet')
