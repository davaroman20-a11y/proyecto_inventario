import asyncio
#importar funciones de otro archivo
from database import crear_producto, obtener_producto, actualizar_stock,eliminar_producto

async def prueba_de_estres():
    print("...iniciando prueba....")
    tareas_creacion = [
        crear_producto("M001", "llantas trasera", 10),
        crear_producto("M001", "filtros de aire", 25),
        crear_producto("M001", "bujia", 50),
    ]

    try:
        await asyncio.gather(*tareas_creacion)
        print("productos creados exitosamente")
    except Exception as e:
        print(f"error de creacion: {e}")

    print("\nactualizar y consultar..")
    try:
        resultado = await asyncio.gather(
            actualizar_stock(8,"M002"),
            obtener_producto("M002")
        )
        print("operaciones mixtas completadas")
        print(f"-update devolvio {resultado[0]}")
        print(f"-get devolvio:{resultado[1]}")
    except Exception as e:
        print("error en operaciones mixtas")

asyncio.run(prueba_de_estres())

