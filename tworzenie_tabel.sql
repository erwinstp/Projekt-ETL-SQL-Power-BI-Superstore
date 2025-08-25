-- Tworzenie tabel w bazie danych

CREATE TABLE Klienci (
	ID_Klienta VARCHAR(20) PRIMARY KEY,
	Nazwa_Klienta VARCHAR(100),
	Segment VARCHAR(50)
);

CREATE TABLE Regiony (
	ID_Regionu INT IDENTITY(1,1) PRIMARY KEY,
	Kraj VARCHAR(50),
	Miasto VARCHAR(100),
	Stan VARCHAR(100),
	Region VARCHAR(50)
);

CREATE TABLE Produkty (
    ID_Produktu VARCHAR(20) PRIMARY KEY,
    Nazwa_Produktu VARCHAR(200),
    Kategoria VARCHAR(50),
    Podkategoria VARCHAR(50)
);

CREATE TABLE Zamowienia (
    ID INT PRIMARY KEY,
    ID_Zam�wienia VARCHAR(20),
    Data_Zam�wienia DATE,
    Data_Dostarczenia DATE,
    Spos�b_Dostawy VARCHAR(50),
    ID_Klienta VARCHAR(20) FOREIGN KEY REFERENCES Klienci(ID_Klienta),
    ID_Produktu VARCHAR(20) FOREIGN KEY REFERENCES Produkty(ID_Produktu),
	Sprzedaz FLOAT,
    Czas_dostawy INT,
	ID_Regionu INT FOREIGN KEY REFERENCES Regiony(ID_Regionu)
);