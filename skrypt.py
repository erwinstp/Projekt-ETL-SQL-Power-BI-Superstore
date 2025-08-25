import pandas as pd
import os

# Wczytanie danych
df = pd.read_csv("train.csv")

df['Order Date'] = pd.to_datetime(df['Order Date'], format="%d/%m/%Y")
df['Ship Date'] = pd.to_datetime(df['Ship Date'], format="%d/%m/%Y")

# Obliczanie czasu dostawy
df['Delivery Days'] = (df['Ship Date'] - df['Order Date']).dt.days

# Usunięcie kolumny 'Postal Code'
df.drop(columns=["Postal Code"], inplace=True, errors='ignore')

# Sprawdzanie braków w danych
braki = df.isnull().sum()
print("Braki w danych:\n", braki[braki > 0])


# Dodanie kategorii sprzedaży poprzez ilość sprzedanych produktów
df['Sales Category'] = pd.cut(
    df['Sales'],
    bins=[0, 100, 500, 1000, df['Sales'].max()],
    labels=['Niska', 'Średnia', 'Wysoka', 'Bardzo Wysoka']
    )

# Agregacje
sprzedaz_w_regionie = df.groupby('Region')['Sales'].sum().reset_index()
czas_oczekiwania_w_stanie = df.groupby('State')['Delivery Days'].mean().reset_index()

# Obliczenie całkowitej sprzedaży oraz średniej sprzedaży, a następnie wypisanie uzyskanych wyników.
całkowita_sprzedaż = df['Sales'].sum()
srednia_sprzedaz = df['Sales'].mean()
print("\n Całkowita sprzedaż: $", round(całkowita_sprzedaż, 2))
print("\n Średnia wartość zamówienia: $", round(srednia_sprzedaz, 2))

# Wypisanie najlepszych klientow wg sprzedaży
najlepsi_klienci = df.groupby('Customer Name')['Sales'] \
                  .sum().sort_values(ascending=False).head(5)
print("\n👤 Top 5 klientów wg sprzedaży:")
print(najlepsi_klienci)

# Średni czas dostawy według regionu
sredni_czas = df.groupby('Region')['Delivery Days'].mean()
print("\n Średni czas dostawy wg regionu:")
print(round(sredni_czas, 2))

# Eksport plików do nowego folderu
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# Zapisanie zmodernizowanego głównego datasetu 
df.to_csv(f"{output_dir}/superstore_clean.csv", index=False)

# Zapisanie plików .csv z agregacjami
sprzedaz_w_regionie.to_csv(f"{output_dir}/sprzedaz_w_regionie.csv", index=False)
czas_oczekiwania_w_stanie.to_csv(f"{output_dir}/czas_oczekiwania_w_stanie.csv", index=False)