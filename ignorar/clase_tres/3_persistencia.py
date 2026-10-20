import asyncio
import aiofiles
import json

# un diccionario en py es el equivalente a objecto en js

inventario = [
    {"codigo": "PEP01", "nombre": "llanta rin17", "stock": 10},
    {"codigo": "PEP02", "nombre": "Aceite motul 7100", "stock": 5}
]

async def guardar_inventario(datos, archivo):
    print("Guardando datos de forma asincrona.....")
    async with aiofiles.open(archivo, mode="w", encoding='utf-8') as f:
        texto_json = json.dumps(datos, indent=4) #traducir de python a json
        await f.write(texto_json)
    print("inventario guardado en el dico.")

async def cargar_inventario(archivo):
    print("cargando los datos del json...")
    try:
        async with aiofiles.open(archivo, mode="r", encoding="utf-8") as archivo_json:
         texto_json = await archivo_json.read()
         datos = json.loads(texto_json) #traducir de json a python
         return datos
    except FileNotFoundError:
        print("el archivo no existe. iniciando con inventario vacio.")
        return []

async def main ():
    # 1. guardar
    await guardar_inventario(inventario, 'inventario.json')
    # 2. leer
    
    datos_recuperados = await cargar_inventario('inventario.json')
    print("datos recuperados:", datos_recuperados)

asyncio.run(main())