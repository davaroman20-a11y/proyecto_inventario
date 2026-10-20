# 1. definir variables

nombre_producto = "llantas pirelli"
precio = 430000
stock = 12
activo = True

print(f"producto: {nombre_producto} precio: {precio}")

# 2. condiciones 
if stock > 0 and activo:
    print("producto disponible para la venta")
elif stock == 0:
    print("producto agotado")
else:
    print("producto inactivo")
    
categorias = ["lubricantes", "repuestos", "accesorios"]

#for categoria in categorias:
 #   print (f"revisando categoria: {categoria}")
 
 
 # unamos "def" en lugar de "function" 0 "() =>"
def calcular_descuento(precio_base, porcentaje):
    descuento = precio_base * (porcentaje/ 100)
    return precio_base - descuento 

precio_final = calcular_descuento(precio, 10)
print(F"precio con descuento: ${precio_final}")
