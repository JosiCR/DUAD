
SELECT *
FROM Products;


SELECT *
FROM Products
WHERE Price > 50000;


SELECT *
FROM InvoiceItems
WHERE Code = 'P001';


SELECT
    Code,
    SUM(Quantity) AS TotalPurchased
FROM InvoiceItems
GROUP BY Code;


SELECT *
FROM Invoices
WHERE BuyerEmail = 'juan@gmail.com';


SELECT *
FROM Invoices
ORDER BY TotalAmount DESC;

SELECT *
FROM Invoices
WHERE InvoiceNumber = 'INV001';