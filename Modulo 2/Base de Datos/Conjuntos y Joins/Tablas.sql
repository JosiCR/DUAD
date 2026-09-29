CREATE TABLE Authors (
    ID INTEGER PRIMARY KEY,
    Name TEXT
);
INSERT INTO Authors (ID, Name)
VALUES
    (1, 'Miguel de Cervantes'),
    (2, 'Dante Alighieri'),
    (3, 'Takehiko Inoue'),
    (4, 'Akira Toriyama'),
    (5, 'Walt Disney');


CREATE TABLE Books (
    ID INTEGER PRIMARY KEY,
    Name TEXT,
    Author INTEGER,
    FOREIGN KEY (Author) REFERENCES Authors(ID)
);
INSERT INTO Books (ID, Name, Author)
VALUES
    (1, 'Don Quijote', 1),
    (2, 'La Divina Comedia', 2),
    (3, 'Vagabond 1-3', 3),
    (4, 'Dragon Ball 1', 4),
    (5, 'The Book of the 5 Rings', NULL);


CREATE TABLE Customers (
    ID INTEGER PRIMARY KEY,
    Name TEXT,
    Email TEXT
);
INSERT INTO Customers (ID, Name, Email)
VALUES
    (1, 'John Doe', 'j.doe@email.com'),
    (2, 'Jane Doe', 'jane@doe.com'),
    (3, 'Luke Skywalker', 'darth.son@email.com');


CREATE TABLE Rents (
    ID INTEGER PRIMARY KEY,
    BookID INTEGER,
    CustomerID INTEGER,
    State TEXT,
    FOREIGN KEY (BookID) REFERENCES Books(ID),
    FOREIGN KEY (CustomerID) REFERENCES Customers(ID)
);
INSERT INTO Rents (ID, BookID, CustomerID, State)
VALUES
    (1, 1, 2, 'Returned'),
    (2, 2, 2, 'Returned'),
    (3, 1, 1, 'On time'),
    (4, 3, 1, 'On time'),
    (5, 2, 2, 'Overdue');


//joins

//#1
SELECT Books.Name, Authors.Name
FROM Books
LEFT JOIN Authors
ON Books.Author = Authors.ID;


//#2
SELECT Books.Name, Authors.Name
FROM Books
LEFT JOIN Authors
ON Books.Author = Authors.ID
WHERE Authors.ID IS NULL;


//#3
SELECT Authors.Name, Books.Name
FROM Authors
LEFT JOIN Books
ON Authors.ID = Books.Author
WHERE Books.ID IS NULL;


//#4
SELECT DISTINCT Books.Name
FROM Books
INNER JOIN Rents
ON Books.ID = Rents.BookID;


//#5
SELECT Books.Name
FROM Books
LEFT JOIN Rents
ON Books.ID = Rents.BookID
WHERE Rents.BookID IS NULL;


//#6
SELECT Customers.Name
FROM Customers
LEFT JOIN Rents
ON Customers.ID = Rents.CustomerID
WHERE Rents.CustomerID IS NULL;


//#7
SELECT Books.Name, Rents.State
FROM Books
INNER JOIN Rents
ON Books.ID = Rents.BookID
WHERE Rents.State = 'Overdue';