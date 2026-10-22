
from fastapi import FastAPI, HTTPException
from database import leer_base_datos, obtener_producto


apiRest = FastAPI(
    title="API de Inventarios SENA",
    description="mi primer api",
    version="1.0.0",
)


@apiRest.get("/")
async def ruta_principal():
    return {"mensaje": "Bienvenido a mi primera API Rest!"}



@apiRest.get("/estado")
async def estado_servidor():
    return {
        "status": "en linea",
        "servicios": "operativos sin ningun inconveniente"
    }



@apiRest.get("/suma")
async def sumar_numeros():
    numero1 = 10
    numero2 = 20
    total = numero1 + numero2

    return {
        "la suma de numero1 y numero2 es": total,
        "numero1": numero1,
        "numero2": numero2,
        "total": total
    }



@apiRest.get("/productos")
async def lista_productos():
    datos = await leer_base_datos()

    return {
        "cantidad": len(datos),
        "productos": datos
    }



@apiRest.get("/productos/{codigo_producto}")
async def buscar_un_producto(codigo_producto: str):
    try:
        producto = await obtener_producto(codigo_producto)
        return producto

    except KeyError:
        raise HTTPException(
            status_code=404,
            detail="El producto solicitado no existe en la BD"
        )



@apiRest.get("/categorias")
async def listar_categorias():
    datos = await leer_base_datos()

    categorias = set()

    for producto in datos:
        if "categoria" in producto:
            categorias.add(producto["categoria"])

    return list(categorias)



@apiRest.get("/alertas/stock")
async def stock_critico():
    datos = await leer_base_datos()

    productos_criticos = []

    for producto in datos:
        if producto["stock"] <= 3:
            productos_criticos.append(producto)

    return productos_criticos



@apiRest.get("/productos/buscar/{palabra_clave}")
async def buscar_producto_por_nombre(palabra_clave: str):
    datos = await leer_base_datos()

    productos_encontrados = []

    for producto in datos:
        nombre = producto["nombre"]

        if palabra_clave.lower() in nombre.lower():
            productos_encontrados.append(producto)

    return productos_encontrados
