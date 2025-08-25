# input_file = 'Regiony.csv'
# output_file = 'regiony_.csv'

# with open(input_file, 'r', encoding='utf-8') as f_in, open(output_file, 'w', encoding='utf-8') as f_out:
#     for line in f_in:
#         new_line = line.replace(';', ',')
#         f_out.write(new_line)

# print(f"Zamiana średników na przecinki zakończona. Plik zapisano jako {output_file}")


import pandas as pd

# 1. Wczytaj dane
zamowienia = pd.read_csv("superstore_clean.csv")
regiony = pd.read_csv("plik.csv")  # <- plik z kolumnami: ID_Regionu, Kraj, Miasto, Stan, Region

# 2. Zmień nazwy kolumn, aby pasowały
regiony.rename(columns={
    "Kraj": "Country",
    "Miasto": "City",
    "Stan": "State",
    "Region": "Region"
}, inplace=True)

# 3. Dopasuj po 4 kolumnach: Country, City, State, Region
merged = zamowienia.merge(regiony[["ID_Regionu", "Country", "City", "State", "Region"]],
                          on=["Country", "City", "State", "Region"],
                          how="left")

# 4. Sprawdź niedopasowane wiersze (opcjonalne)
niedopasowane = merged[merged["ID_Regionu"].isna()]
print(f"Liczba niedopasowanych wierszy: {len(niedopasowane)}")

# 5. Zapisz wynik
merged.to_csv("superstore_with_region_id.csv", index=False)