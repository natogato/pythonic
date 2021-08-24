import pandas as pd
df = pd.read_csv('prices.csv')
# df.head()
df.to_parquet('prices.parquet')
