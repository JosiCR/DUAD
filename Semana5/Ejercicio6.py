mi_diccionario_hotel = {
    'nombre' : 'Marriott',
    'numero_estrellas' : 5,
    'Habitaciones' : [{
        'Numero' : 101,
        'piso' : 4,
        'precio_por_noche' : '$257'
    },
    {
        'Numero' : 76,
        'piso' : 3,
        'precio_por_noche' : '$176'

    },
    {
        'Numero' : 280,
        'piso' : 7,
        'precio_por_noche' : '$489'

    }
    ]
    }
for hotel, habitaciones in mi_diccionario_hotel.items():
    print(f'{hotel} : {habitaciones}')