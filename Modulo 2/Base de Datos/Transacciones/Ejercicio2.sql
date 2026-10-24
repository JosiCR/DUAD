
DO $$
DECLARE
    usuario_id INTEGER := 1;
    factura_id INTEGER;
    producto RECORD;
    stock_actual INTEGER;
BEGIN

    -- 1. Verificar que el usuario exista
    IF NOT EXISTS (
        SELECT 1
        FROM Users
        WHERE ID = usuario_id
    ) THEN
        RAISE EXCEPTION 'El usuario % no existe.', usuario_id;
    END IF;


    -- 2. Verificar que haya stock suficiente
    --    para TODOS los productos de la compra

    FOR producto IN
        SELECT *
        FROM (
            VALUES
                (1, 2),
                (2, 3),
                (5, 1)
        ) AS compras(ProductID, Quantity)
    LOOP

        SELECT Stock
        INTO stock_actual
        FROM Products
        WHERE ID = producto.ProductID
        FOR UPDATE;

        IF stock_actual IS NULL THEN
            RAISE EXCEPTION
                'El producto % no existe.',
                producto.ProductID;
        END IF;

        IF stock_actual < producto.Quantity THEN
            RAISE EXCEPTION
                'Stock insuficiente para el producto %. Stock disponible: %, cantidad solicitada: %.',
                producto.ProductID,
                stock_actual,
                producto.Quantity;
        END IF;

    END LOOP;


    -- 3. Crear la factura
    INSERT INTO Bills (UserID, State)
    VALUES (usuario_id, 'Active')
    RETURNING ID INTO factura_id;


    -- 4. Registrar los productos de la factura
    -- 5. Reducir el stock

    FOR producto IN
        SELECT *
        FROM (
            VALUES
                (1, 2),
                (2, 3),
                (5, 1)
        ) AS compras(ProductID, Quantity)
    LOOP

        INSERT INTO BillProducts
            (BillID, ProductID, Quantity, Price)
        SELECT
            factura_id,
            ID,
            producto.Quantity,
            Price
        FROM Products
        WHERE ID = producto.ProductID;


        UPDATE Products
        SET Stock = Stock - producto.Quantity
        WHERE ID = producto.ProductID;

    END LOOP;


    -- Confirmación
    RAISE NOTICE
        'Compra realizada correctamente. Factura: %',
        factura_id;

END $$;