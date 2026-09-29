

-- Tabla de usuarios
CREATE TABLE Users (
    ID SERIAL PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Email VARCHAR(150) UNIQUE NOT NULL
);

-- Tabla de productos
CREATE TABLE Products (
    ID SERIAL PRIMARY KEY,
    Name VARCHAR(150) NOT NULL,
    Price NUMERIC(10,2) NOT NULL,
    Stock INTEGER NOT NULL
);

-- Tabla de facturas
CREATE TABLE Bills (
    ID SERIAL PRIMARY KEY,
    UserID INTEGER NOT NULL,
    Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    State VARCHAR(20) NOT NULL DEFAULT 'Active'
        CHECK (State IN ('Active', 'Returned')),
    FOREIGN KEY (UserID) REFERENCES Users(ID)
);

-- Tabla cruz: productos incluidos en cada factura
CREATE TABLE BillProducts (
    BillID INTEGER NOT NULL,
    ProductID INTEGER NOT NULL,
    Quantity INTEGER NOT NULL,
    Price NUMERIC(10,2) NOT NULL,

    PRIMARY KEY (BillID, ProductID),

    FOREIGN KEY (BillID) REFERENCES Bills(ID),
    FOREIGN KEY (ProductID) REFERENCES Products(ID)
);



-- DATOS DE PRUEBA

INSERT INTO Users (Name, Email)
VALUES
    ('John Doe', 'john@email.com'),
    ('Jane Doe', 'jane@email.com'),
    ('Luke Skywalker', 'luke@email.com');


INSERT INTO Products (Name, Price, Stock)
VALUES
    ('Laptop', 850.00, 10),
    ('Mouse', 25.00, 20),
    ('Keyboard', 45.00, 15),
    ('Monitor', 250.00, 8),
    ('Headphones', 75.00, 12);