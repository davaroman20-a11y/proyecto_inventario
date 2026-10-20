import asyncio
import time

async def verificar_inventario(item):
    print(f"Buscando {item} en la bodega ...")
    await asyncio.sleep(1)
    print(f"{item} encontrado.")
    return 50000

async def procesar_pago (monto):
    print(f"procesando pago de {monto} con bre_b . ...")
    await asyncio.sleep(2)
    print("pago aprobado.")
    return "ABC_091"

async def generar_factura (item, transaccion):
    print(f"generando factura {item} (REF: {transaccion})")
    await asyncio.sleep(1)
    print("factura electronica enviada.")

async def atender_cliente(cliente):
    print(f"INICIO ATENCION AL CLIENTE {cliente}")
    item = "aceite sintetico"

    precio = await verificar_inventario(item)
    transaccion = await procesar_pago(precio)
    await generar_factura(item, transaccion)
    print(f"fin atencion a cliente {cliente}")

async def main():
    print(f"inicio de la colsulta")
    inicio = time.time()
    tareas = [
        atender_cliente(1),
        atender_cliente(2),
        atender_cliente(3),
    ]
    await asyncio.gather(*tareas)

    fin = time.time()
    print(f"fin del programa")
    print(f"timepo total. {fin - inicio:.1f} segundos")      

asyncio.run(main())