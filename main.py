import pandas as pd

print("teste")

df = pd.read_csv('mal_top2000_anime.csv')

df = df.drop('Unnamed: 0', axis=1)
print(df.head(5))
print(df.columns)
