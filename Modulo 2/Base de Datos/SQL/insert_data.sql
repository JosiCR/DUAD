
INSERT INTO Products VALUES
('P001','Mouse Logitech',25000,'2026-07-01','Logitech',20),
('P002','Teclado Mecánico',65000,'2026-07-02','Redragon',15),
('P003','Monitor 24"',120000,'2026-07-03','Samsung',8);


INSERT INTO Invoices
(InvoiceNumber, PurchaseDate, BuyerEmail, TotalAmount, PhoneNumber, EmployeeID)
VALUES
('INV001','2026-07-10','juan@gmail.com',155000,'88881234','EMP001'),
('INV002','2026-07-12','juan@gmail.com',65000,'88881234','EMP001'),
('INV003','2026-07-13','ana@gmail.com',25000,'88776655','EMP002');


INSERT INTO InvoiceItems VALUES
('INV001','P002',1,65000),
('INV001','P003',1,90000),
('INV002','P002',1,65000),
('INV003','P001',1,25000);


INSERT INTO ShoppingCart (BuyerEmail)
VALUES
('juan@gmail.com'),
('ana@gmail.com');


INSERT INTO CartItems VALUES
(1,'P001'),
(1,'P002'),
(2,'P003');