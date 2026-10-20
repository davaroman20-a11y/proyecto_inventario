import asyncio

async def consultar_inventario_fragil(repuesto):
    print(f"Buscando {repuesto}....")
    await asyncio.sleep(1)
    if repuesto == "filtro de aire":
        raise Exception("Error 500: se cayo la conexion con la bodega")
    return {"repuesto": repuesto, "stock": 15}

async def procesar_oden_segura (repuesto):
    try:
        resultado = await consultar_inventario_fragil(repuesto)
        print(f"Exito: {resultado}")
    except Exception as e:
        print(f"manejo de crisis: no se puedo consultar el {repuesto}. motivo {e}")

async def main():
    await procesar_oden_segura("pastillas de freno")
    await procesar_oden_segura("filtro de aire")

asyncio.run(main())
