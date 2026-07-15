/* ==========================================
Products
========================================== */

const products = [

    {
        id: 1,
        name: "Alimento Premium para Perro",
        data: {
            category: "Alimentos",
            price: 24900,
            stock: 30,
            image: "../assets/images/dog-food.png",
            description: "Alimento premium para perros adultos, elaborado con ingredientes de alta calidad que proporcionan una nutrición completa, fortalecen el sistema inmunológico y favorecen un pelaje sano y brillante."
        }
    },

    {
        id: 2,
        name: "Alimento Premium para Gato",
        data: {
            category: "Alimentos",
            price: 21900,
            stock: 25,
            image: "../assets/images/cat-food.png",
            description: "Alimento premium formulado para gatos adultos, rico en proteínas y nutrientes esenciales que contribuyen a una digestión saludable, un pelaje brillante y un sistema inmunológico fuerte."
        }
    },

    {
        id: 3,
        name: "Pelota de Goma para Perro",
        data: {
            category: "Juguetes",
            price: 5500,
            stock: 50,
            image: "../assets/images/dog-ball.png",
            description: "Pelota de goma resistente diseñada para juegos interactivos con tu perro. Ayuda a estimular la actividad física, fortalecer la mandíbula y proporcionar horas de entretenimiento."
        }
    },

    {
        id: 4,
        name: "Rascador para Gato",
        data: {
            category: "Juguetes",
            price: 28900,
            stock: 15,
            image: "../assets/images/scratching-post.png",
            description: "Rascador fabricado con materiales resistentes que permite a los gatos afilar sus uñas de forma segura, proteger los muebles y mantenerse activos mientras juegan."
        }
    },

    {
        id: 5,
        name: "Cama Ortopédica para Perro",
        data: {
            category: "Camas",
            price: 45900,
            stock: 10,
            image: "../assets/images/orthopedic-bed.png",
            description: "Cama ortopédica elaborada con espuma de alta densidad que brinda un excelente soporte para las articulaciones, proporcionando mayor comodidad y descanso a perros de todas las edades."
        }
    },

    {
        id: 6,
        name: "Correa Ajustable para Perro",
        data: {
            category: "Accesorios",
            price: 9900,
            stock: 40,
            image: "../assets/images/dog-leash.png",
            description: "Correa ajustable y resistente, ideal para paseos diarios. Su diseño ergonómico ofrece comodidad, seguridad y un mejor control durante cada recorrido."
        }
    },

    {
        id: 7,
        name: "Jaula para Aves",
        data: {
            category: "Hábitats",
            price: 49900,
            stock: 8,
            image: "../assets/images/bird-cage.png",
            description: "Jaula espaciosa fabricada con materiales de alta calidad que ofrece un ambiente seguro y cómodo para aves pequeñas y medianas, facilitando su movilidad y bienestar."
        }
    },

    {
        id: 8,
        name: "Acuario de Vidrio 40L",
        data: {
            category: "Hábitats",
            price: 69900,
            stock: 5,
            image: "../assets/images/aquarium.png",
            description: "Acuario de vidrio con capacidad de 40 litros, ideal para crear un entorno limpio y atractivo para peces de agua dulce. Su diseño moderno facilita la decoración y el mantenimiento."
        }
    },

    {
        id: 9,
        name: "Rueda para Hámster",
        data: {
            category: "Accesorios",
            price: 7900,
            stock: 20,
            image: "../assets/images/hamster-wheel.png",
            description: "Rueda de ejercicio silenciosa que promueve la actividad física diaria de los hámsteres, ayudando a mantenerlos saludables, activos y entretenidos."
        }
    },

    {
        id: 10,
        name: "Champú para Mascotas",
        data: {
            category: "Higiene",
            price: 8500,
            stock: 35,
            image: "../assets/images/pet-shampoo.png",
            description: "Champú de fórmula suave especialmente desarrollado para perros y gatos. Limpia profundamente, elimina malos olores y deja el pelaje limpio, brillante y con un agradable aroma."
        }
    }

];


/* ==========================================
Initialize Products
========================================== */

function initializeProducts() {

    const savedProducts = localStorage.getItem("products");

    if (!savedProducts) {

        localStorage.setItem("products", JSON.stringify(products));

    }

}


/* ==========================================
Reset Products
========================================== */

function resetProducts() {

    localStorage.setItem("products", JSON.stringify(products));

}


/* ==========================================
Get Products
========================================== */

async function getProducts() {

    try {

        const products = JSON.parse(localStorage.getItem("products"));

        if (!products) {

            return {
                success: false,
                error: "No existen productos registrados."
            };

        }

        return {
            success: true,
            products: products
        };

    }
    catch (error) {

        return {
            success: false,
            error: "No fue posible obtener los productos."
        };

    }

}


/* ==========================================
Get Product By ID
========================================== */

async function getProductById(id) {

    try {

        const products = JSON.parse(localStorage.getItem("products"));

        if (!products) {

            return {
                success: false,
                error: "No existen productos registrados."
            };

        }

        const product = products.find(function (product) {

            return product.id === id;

        });

        if (!product) {

            return {
                success: false,
                error: "Producto no encontrado."
            };

        }

        return {
            success: true,
            product: product
        };

    }
    catch (error) {

        return {
            success: false,
            error: "No fue posible obtener el producto."
        };

    }

}


/* ==========================================
Delete Product
========================================== */

function deleteProduct(productId) {

    try {

        const products = JSON.parse(localStorage.getItem("products")) || [];

        const productExists = products.some(function (product) {

            return product.id === productId;

        });

        if (!productExists) {

            return {
                success: false,
                error: "El producto no existe."
            };

        }

        const updatedProducts = products.filter(function (product) {

            return product.id !== productId;

        });

        localStorage.setItem("products", JSON.stringify(updatedProducts));

        return {
            success: true,
            message: "Producto eliminado correctamente."
        };

    }
    catch (error) {

        return {
            success: false,
            error: "No fue posible eliminar el producto."
        };

    }

}


/* ==========================================
Create Product
========================================== */

function createProduct(productData) {

    try {

        const products = JSON.parse(localStorage.getItem("products")) || [];

        const highestId = products.reduce(function (highestId, product) {

            if (product.id > highestId) {

                return product.id;

            }

            return highestId;

        }, 0);


        const newProduct = {

            id: highestId + 1,

            name: productData.name,

            data: {
                category: productData.category,
                price: productData.price,
                stock: productData.stock,
                image: productData.image,
                description: productData.description
            }

        };


        products.push(newProduct);

        localStorage.setItem("products", JSON.stringify(products));


        return {
            success: true,
            message: "Producto creado correctamente.",
            product: newProduct
        };

    }
    catch (error) {

        return {
            success: false,
            error: "No fue posible crear el producto."
        };

    }

}


/* ==========================================
Update Product
========================================== */

function updateProduct(productId, productData) {

    try {

        const products = JSON.parse(localStorage.getItem("products")) || [];

        const product = products.find(function (product) {

            return product.id === productId;

        });

        if (!product) {

            return {
                success: false,
                error: "El producto no existe."
            };

        }

        product.name = productData.name;

        product.data.category = productData.category;

        product.data.price = productData.price;

        product.data.stock = productData.stock;

        product.data.image = productData.image;

        product.data.description = productData.description;


        localStorage.setItem("products", JSON.stringify(products));


        return {
            success: true,
            message: "Producto actualizado correctamente."
        };

    }
    catch (error) {

        return {
            success: false,
            error: "No fue posible actualizar el producto."
        };

    }

}


/* ==========================================
Initialize Product Service
========================================== */

initializeProducts();

//resetProducts();