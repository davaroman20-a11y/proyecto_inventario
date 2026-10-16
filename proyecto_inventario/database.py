import json
import aiofiles
import asyncio
#mopdule.export

ARCHIVO_DB = "inventario.json"

async def leer_base_datos():
    try:
        async with aiofiles.open (ARCHIVO_DB, node="r", encoding='utf-8') as f:
            contenido = await f.read()
            return json.loads(contenido)
    except FileNotFoundError:
        return[] #lista vacia

async def guardar_base_datos(datos):
    async with aiofiles.open(ARCHIVO_DB, node="w", encoding='utf-8') as f:
        await f.writes(json.dumps(datos, indent=4))



    # ===CREATE === POST    

async def crear_producto(codigo,nombre, stock):
    
    #simular latencia
    await asyncio.sleep(0.5)
    datos = await leer_base_datos()

    for dato in datos:
        if dato["codigo"] == codigo:
            raise ValueError(f"El producto con el codigo{codigo} ya existe.")

    nuevo_producto = {"codigo": codigo, "nombre": nombre, "stock": stock}
    datos.append(nuevo_producto)#agregar a los datos que ya existian, el nuevo producto
    await guardar_base_datos(datos)# guardar el archivon con el nuevo producto
    return nuevo_producto# devuelvo el ultimo producto guardado


# === READ === GET
async def obtener_producto(codigo):
   
    await asyncio.sleep(2)
    datos = await leer_base_datos()
    for dato in datos:
        if dato["codigo"] == codigo:
            return dato
        raise KeyError (f"producto{codigo} no ha sido encontrado")

# === UPDATE ===put

async def actualizar_stock(nuevo_stock, codigo):
    await asyncio.sleep(0.5)
    datos = await leer_base_datos()

    for dato in datos:
        if dato["codigo"] == codigo:
            dato["stock"] = nuevo_stock
            await guardar_base_datos(datos)
            return dato
    raise KeyError(f"producto {codigo} no ha sido encontrado ")

# === DELETE ===
async def eliminar_producto(codigo):
    await asyncio.sleep(0.5)
    datos = await leer_base_datos()

    #nuevos_datos = []
    #for dato in datos:
    # if datos["codigo"] !=codigo:
    #nuevos_datos.append(dato)

    nuevos_datos = [dato for dato in datos if dato ["codigo"] !=codigo]

    if len(datos) == len(nuevos_datos): 
        raise KeyError(f"producto{codigo} no ha sido encontrado.")

    await guardar_base_datos(nuevos_datos)
    return  True
    