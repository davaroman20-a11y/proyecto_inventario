import asyncio

from database import reiniciar_inventario, tareas_alerta, vender_producto


async def procesar_venta(codigo, cantidad):
    try:
        resultado = await vender_producto(codigo, cantidad)
        print(resultado)
    except KeyError as error:
        print(f"Error en venta de {codigo}: {error.args[0]}")
    except ValueError as error:
        print(f"Error en venta de {codigo}: {error}")


async def main():
    reiniciar_inventario()

    await asyncio.gather(
        procesar_venta("P001", 2),
        procesar_venta("P002", 3),
        procesar_venta("P003", 10),
        procesar_venta("P999", 1),
    )

    print("Ventas procesadas. Esperando alertas en segundo plano...")
    await asyncio.gather(*tareas_alerta)


asyncio.run(main())