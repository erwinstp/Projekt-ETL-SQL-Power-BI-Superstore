import pandas as pd

# Wczytywanie danych
zamowienia = pd.read_csv("superstore_clean.csv")

# Plik z kolumnami: ID_Regionu, Kraj, Miasto, Stan, Region pobrany z serwera potrzebny do przypisania ID_Regionu do tabeli
regiony = pd.read_csv("plik.csv")  

# Zmiana nazwy kolumn, aby pasowały
regiony.rename(columns={
    "Kraj": "Country",
    "Miasto": "City",
    "Stan": "State",
    "Region": "Region"
}, inplace=True)

# Dopasowanie po 4 kolumnach: Country, City, State, Region
merged = zamowienia.merge(regiony[["ID_Regionu", "Country", "City", "State", "Region"]],
                          on=["Country", "City", "State", "Region"],
                          how="left")

# Sprawdzanie niedopasowanych wierszy
niedopasowane = merged[merged["ID_Regionu"].isna()]
print(f"Liczba niedopasowanych wierszy: {len(niedopasowane)}")

# Zapisanie wyniku
merged.to_csv("superstore_clean.csv", index=False)