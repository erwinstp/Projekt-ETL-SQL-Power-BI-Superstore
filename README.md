\# 📊 Projekt ETL + SQL + Power BI – Superstore  

\## Opis projektu  

Celem projektu jest zbudowanie procesu \*\*ETL\*\* dla danych sprzedażowych „Superstore” oraz przygotowanie modelu analitycznego w \*\*SQL Server\*\* i \*\*Power BI\*\*.  

Projekt obejmuje:  

1\. \*\*ETL w Pythonie\*\* – czyszczenie danych źródłowych, usunięcie zbędnych kolumn, dodanie kolumn, tworzenie tabel, konwersja typów oraz przygotowanie plików CSV do importu.  

2\. \*\*SQL Server (SSMS)\*\* – stworzenie tabel w relacyjnej bazie danych, załadowanie oczyszczonych danych i wstawienie ich do stworzonych tabel oraz zbudowanie relacji między tabelami:  

- `Zamowienia`  
- `Produkty`  
- `Klienci`  
- `Regiony`  

3\. \*\*Power BI\*\* – stworzenie raportów i dashboardów:  

- import danych z SQL Server 
- tabela dat z kolumnami Rok, Kwartał, Miesiąc, Dzień,  
- wizualizacje pokazujące sprzedaż według regionów, dat i produktów.  

Główne cele analizy  

- Analiza sprzedaży w czasie (rok, kwartał, miesiąc, dzień).
- Analiza po regionach.   
- Przedstawienie najlepszych 5 klientów w wybranym okresie i regionie.
- Przedstawienie sprzedaży poszczególnych kategorii i podkategorii produktów.   

Struktura projektu  

- skrypty Pythona do obróbki danych.  
- skrypty SQL do tworzenia tabel i importu danych.  
- plik raportu PBIX z raportem.  
- `README.md` – opis projektu i instrukcja uruchomienia.  

Technologia  

- \*\*Python (pandas)\*\* – ETL.  
- \*\*SQL Server (T-SQL, SSMS)\*\* – baza danych.  
- \*\*Power BI (Power Query, DAX, raportowanie)\*\* – dashboardy i analizy.  

