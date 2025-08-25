-- Wype�nienie tabeli Klienci
INSERT INTO dbo.Klienci (ID_Klienta, Nazwa_Klienta, Segment)
SELECT DISTINCT Customer_ID, Customer_Name, Segment
FROM dbo.superstore_clean
GROUP BY Customer_ID, Customer_Name, Segment;

--Wype�nienie tabeli Regiony
INSERT INTO dbo.Regiony (Kraj, Miasto, Stan, Region)
SELECT DISTINCT Country, City, "State", Region
FROM dbo.superstore_clean;

--Wypełnianie tabeli Produkty
INSERT INTO dbo.Produkty (ID_Produktu, Nazwa_Produktu, Kategoria, Podkategoria)
SELECT DISTINCT Product_ID, Product_Name, Category, Sub_Category
FROM dbo.unikalne_produkty
GROUP BY Product_ID, Product_Name, Category, Sub_Category;

--Wypełnianie tabeli Zamówienia
INSERT INTO dbo.Zamowienia (ID, ID_Zam�wienia, Data_Zam�wienia, Data_Dostarczenia, Spos�b_Dostawy, ID_Klienta, ID_Produktu, Sprzedaz, Czas_Dostawy, ID_Regionu)
SELECT
	[Row_ID],
	[Order_ID],
	CAST([Order_Date] AS DATE),
	CAST([Ship_Date] AS DATE),
	[Ship_Mode],
	[Customer_ID],
	[Product_ID],
	Sales,
	DATEDIFF(DAY, [Order_Date], [Ship_Date]),
	ID_Regionu
FROM dbo.superstore_clean