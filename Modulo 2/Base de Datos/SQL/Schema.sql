
CREATE TABLE Products (
    Code VARCHAR(15) PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Price DECIMAL(10,2) NOT NULL,
    EntryDate DATE NOT NULL,
    Brand VARCHAR(50) NOT NULL,
    StockAvailable INTEGER NOT NULL
);


CREATE TABLE Invoices (
    InvoiceNumber VARCHAR(20) PRIMARY KEY,
    PurchaseDate DATE NOT NULL,
    BuyerEmail VARCHAR(255) NOT NULL,
    TotalAmount DECIMAL(10,2) NOT NULL
);


CREATE TABLE InvoiceItems (
    InvoiceNumber VARCHAR(20) NOT NULL,
    Code VARCHAR(15) NOT NULL,
    Quantity INTEGER NOT NULL,
    TotalAmount DECIMAL(10,2) NOT NULL,

    PRIMARY KEY (InvoiceNumber, Code),

    FOREIGN KEY (InvoiceNumber)
        REFERENCES Invoices(InvoiceNumber),

    FOREIGN KEY (Code)
        REFERENCES Products(Code)
);


CREATE TABLE ShoppingCart (
    CartID INTEGER PRIMARY KEY AUTOINCREMENT,
    BuyerEmail VARCHAR(255) NOT NULL
);


CREATE TABLE CartItems (
    CartID INTEGER NOT NULL,
    Code VARCHAR(15) NOT NULL,

    PRIMARY KEY (CartID, Code),

    FOREIGN KEY (CartID)
        REFERENCES ShoppingCart(CartID),

    FOREIGN KEY (Code)
        REFERENCES Products(Code)
);

ALTER TABLE Invoices
ADD COLUMN PhoneNumber VARCHAR(20);

ALTER TABLE Invoices
ADD COLUMN EmployeeID VARCHAR(20);