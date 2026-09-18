# Ejercicios de Normalización

## Ejercicio Orders

### Tabla original
Order ID   Customer Name   Customer Phone   Address          Item ID   Item Name      Price   Quantity   Special Request   Delivery Time
--------   --------------  ---------------  ---------------  --------  -------------  ------  ---------  ----------------  -------------
001        Alice           123-456-7890     123 Main St      101       Cheeseburger   $8      2          No onions         6:00 PM
001        Alice           123-456-7890     123 Main St      102       Fries          $3      1          Extra ketchup     6:00 PM
002        Bob             987-654-3210     456 Elm St       103       Pizza          $12     1          Extra cheese      7:30 PM
002        Bob             987-654-3210     4th Avenue       102       Fries          $3      2          None              7:30 PM
003        Claire          555-123-4567     789 Oak St       105       Salad          $6      1          No croutons       12:00 PM
004        Claire          555-123-4567     464 Georgia St   106       Water          $1      1          None              5:00 PM


---

## Primera Forma Normal (1FN)

### Justificación

La Primera Forma Normal busca que cada registro tenga una llave primaria única y que todos los atributos sean atómicos. Además, cuando una tabla mezcla varias entidades o presenta una relación de muchos a muchos, estas deben separarse en tablas relacionadas. En este caso, una orden puede contener varios productos y un producto puede aparecer en varias órdenes, por lo que se crea una tabla intermedia para representar esa relación. 

### Orders
OrderID    CustomerName    CustomerPhone    Address          DeliveryTime
-------    ------------    -------------    ---------------  ------------
001        Alice           123-456-7890     123 Main St      6:00 PM
002        Bob             987-654-3210     456 Elm St       7:30 PM
003        Claire          555-123-4567     789 Oak St       12:00 PM
004        Claire          555-123-4567     464 Georgia St   5:00 PM


### OrderItems
OrderID    ItemID    ItemName       Price    Quantity    SpecialRequest
-------    ------    -------------  -----    --------    ----------------
001        101       Cheeseburger   8        2           No onions
001        102       Fries          3        1           Extra ketchup
002        103       Pizza          12       1           Extra cheese
002        102       Fries          3        2           None
003        105       Salad          6        1           No croutons
004        106       Water          1        1           None


## Segunda Forma Normal (2FN)
Justificación

Se creó la tabla Products porque el nombre y el precio del producto dependen únicamente 
del ItemID. Si esos datos permanecieran en OrderItems, se repetirían cada vez que un 
producto apareciera en una orden diferente.

### Products
ItemID     ItemName       Price
------     -------------  -----
101        Cheeseburger   8
102        Fries          3
103        Pizza          12
105        Salad          6
106        Water          1


### Orders
OrderID    CustomerName    CustomerPhone    Address          DeliveryTime
-------    ------------    -------------    ---------------  ------------
001        Alice           123-456-7890     123 Main St      6:00 PM
002        Bob             987-654-3210     456 Elm St       7:30 PM
003        Claire          555-123-4567     789 Oak St       12:00 PM
004        Claire          555-123-4567     464 Georgia St   5:00 PM


### OrderItems
OrderID    ItemID    Quantity    SpecialRequest
-------    ------    --------    ----------------
001        101       2           No onions
001        102       1           Extra ketchup
002        103       1           Extra cheese
002        102       2           None
003        105       1           No croutons
004        106       1           None


## Tercera Forma Normal (3FN)

Justificación

Se creó la tabla Customers porque el nombre y el teléfono pertenecen 
al cliente y no a la orden. De esta forma, si un cliente realiza varias compras, 
su información personal se almacena una sola vez y únicamente se relaciona mediante CustomerID.


### Customers
CustomerID    CustomerName    CustomerPhone
----------    ------------    ----------------
1             Alice           123-456-7890
2             Bob             987-654-3210
3             Claire          555-123-4567


### Orders
OrderID    CustomerID    Address          DeliveryTime
-------    ----------    ---------------  ------------
001        1             123 Main St      6:00 PM
002        2             456 Elm St       7:30 PM
003        3             789 Oak St       12:00 PM
004        3             464 Georgia St   5:00 PM


### Products
ItemID     ItemName       Price
------     -------------  -----
101        Cheeseburger   8
102        Fries          3
103        Pizza          12
105        Salad          6
106        Water          1


### OrderItems
OrderID    ItemID    Quantity    SpecialRequest
-------    ------    --------    ----------------
001        101       2           No onions
001        102       1           Extra ketchup
002        103       1           Extra cheese
002        102       2           None
003        105       1           No croutons
004        106       1           None

## Resultado Final


### Customers
CustomerID    CustomerName    CustomerPhone
----------    ------------    ----------------
1             Alice           123-456-7890
2             Bob             987-654-3210
3             Claire          555-123-4567


### Orders
OrderID    CustomerID    Address          DeliveryTime
-------    ----------    ---------------  ------------
001        1             123 Main St      6:00 PM
002        2             456 Elm St       7:30 PM
003        3             789 Oak St       12:00 PM
004        3             464 Georgia St   5:00 PM
### Products
ItemID     ItemName       Price
------     -------------  -----
101        Cheeseburger   8
102        Fries          3
103        Pizza          12
105        Salad          6
106        Water          1


### OrderItems
OrderID    ItemID    Quantity    SpecialRequest
-------    ------    --------    ----------------
001        101       2           No onions
001        102       1           Extra ketchup
002        103       1           Extra cheese
002        102       2           None
003        105       1           No croutons
004        106       1           None

