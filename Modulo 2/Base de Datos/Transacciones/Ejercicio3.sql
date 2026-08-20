
DO $$
DECLARE
    factura_id INTEGER := 1;
    producto RECORD;
BEGIN

    -- 1. Verificar que la factura exista y no haya sido retornada
    IF NOT EXISTS (
        SELECT 1
        FROM Bills
        WHERE ID = factura_id
        AND State <> 'Returned'
    )THEN
        RAISE EXCEPTION
            'La factura % no existe o ya fue retornada.',
            factura_id;
    END IF;


    -- 2. Aumentar el stock de los productos
    --    según las cantidades de la factura

    FOR producto IN
        SELECT ProductID, Quantity
        FROM BillProducts
        WHERE BillID = factura_id
    LOOP

        UPDATE Products
        SET Stock = Stock + producto.Quantity
        WHERE ID = producto.ProductID;

    END LOOP;


    -- 3. Marcar la factura como retornada

    UPDATE Bills
    SET State = 'Returned'
    WHERE ID = factura_id;


    -- Confirmación
    RAISE NOTICE
        'La factura % fue retornada correctamente.',
        factura_id;



END $$;