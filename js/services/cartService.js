/* ==========================================
Get Cart
========================================== */

function getCart() {

    try {

        const cart = JSON.parse(localStorage.getItem("cart")) || [];

        return {
            success: true,
            cart: cart
        };

    }
    catch (error) {

        return {
            success: false,
            error: "No fue posible obtener el carrito."
        };

    }

}


/* ==========================================
Save Cart
========================================== */

function saveCart(cart) {

    localStorage.setItem("cart", JSON.stringify(cart));

}


/* ==========================================
Add Product to Cart
========================================== */

function addToCart(product) {

    try {

        const cart = JSON.parse(localStorage.getItem("cart")) || [];

        const existingProduct = cart.find(function (item) {

            return item.id === product.id;

        });


        if (existingProduct) {

            if (existingProduct.quantity >= product.data.stock) {

                return {
                    success: false,
                    error: "No hay más unidades disponibles de este producto."
                };

            }

            existingProduct.quantity++;

        }
        else {

            if (product.data.stock <= 0) {

                return {
                    success: false,
                    error: "Este producto no tiene unidades disponibles."
                };

            }

            cart.push({
                id: product.id,
                name: product.name,
                data: product.data,
                quantity: 1
            });

        }


        saveCart(cart);


        return {
            success: true,
            message: "Producto agregado al carrito."
        };

    }
    catch (error) {

        return {
            success: false,
            error: "No fue posible agregar el producto al carrito."
        };

    }

}


/* ==========================================
Increase Product Quantity
========================================== */

function increaseCartQuantity(productId) {

    try {

        const cart = JSON.parse(localStorage.getItem("cart")) || [];

        const product = cart.find(function (item) {

            return item.id === productId;

        });


        if (!product) {

            return {
                success: false,
                error: "El producto no existe en el carrito."
            };

        }


        if (product.quantity >= product.data.stock) {

            return {
                success: false,
                error: "No hay más unidades disponibles de este producto."
            };

        }


        product.quantity++;

        saveCart(cart);


        return {
            success: true
        };

    }
    catch (error) {

        return {
            success: false,
            error: "No fue posible aumentar la cantidad."
        };

    }

}


/* ==========================================
Decrease Product Quantity
========================================== */

function decreaseCartQuantity(productId) {

    try {

        const cart = JSON.parse(localStorage.getItem("cart")) || [];

        const product = cart.find(function (item) {

            return item.id === productId;

        });


        if (!product) {

            return {
                success: false,
                error: "El producto no existe en el carrito."
            };

        }


        if (product.quantity <= 1) {

            return {
                success: false,
                error: "La cantidad mínima es una unidad."
            };

        }


        product.quantity--;

        saveCart(cart);


        return {
            success: true
        };

    }
    catch (error) {

        return {
            success: false,
            error: "No fue posible disminuir la cantidad."
        };

    }

}


/* ==========================================
Remove Product from Cart
========================================== */

function removeFromCart(productId) {

    try {

        const cart = JSON.parse(localStorage.getItem("cart")) || [];

        const updatedCart = cart.filter(function (item) {

            return item.id !== productId;

        });


        saveCart(updatedCart);


        return {
            success: true,
            message: "Producto eliminado del carrito."
        };

    }
    catch (error) {

        return {
            success: false,
            error: "No fue posible eliminar el producto."
        };

    }

}