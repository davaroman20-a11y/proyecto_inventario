inventario_tienda = [
    {"nombre": "Llanta Trasera Voge 300 DS", "categoria": "Repuestos", "precio": 280000, "stock": 4},
    {"nombre": "Kit Arrastre Suzuki Gixxer 150", "categoria": "Repuestos", "precio": 120000, "stock": 15},
    {"nombre": "Exploradoras LED Dominar 400", "categoria": "accesorios", "precio": 150000, "stock": 8},
    {"nombre": "Pastillas Freno Gixxer 150", "categoria": "Repuestos", "precio": 45000, "stock": 0},
    {"nombre": "Soporte Celular Aluminio", "categoria": "accesorios", "precio": 60000, "stock": 3}
]


def procesar_inventario (productos):
    for producto in productos:
        if producto ["stock"] <= 5:
            print(f"alerta stock critico para: {producto['nombre']}")
        elif producto ["categoria"] == "accesorios":
            descuento = producto["precio"] * 0.10
            print(f"descuento aplicado a  {producto['nombre']}: {descuento}")
        elif producto ["stock"] == 0:
            print(f"producto agotado {producto['nombre']}")
            
            
lista_productos = inventario_tienda
procesar_inventario(inventario_tienda)

            