import pandas as pd

df = pd.read_csv('superstore_clean.csv')

kolumny_1 = ['Product ID', 'Product Name', 'Category', 'Sub-Category']

t_produkty = df[kolumny_1]

bez_duplikatow = t_produkty.drop_duplicates(subset=['Product ID'])

bez_duplikatow.to_csv('unikalne_produkty.csv', index=False)

duplikaty = bez_duplikatow.duplicated(subset=['Product ID'])

print("Duplikaty", duplikaty.sum())