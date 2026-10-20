import asyncio
import time

#funcion simcronica
def procesar_reporte_medico():
    print("iniciando procesamiento de reporte (Bloqueo de isitema) ...")
    time.sleep(3) #tiempo que estra bloqueado 
    print("Reporte general")
    return"reporte.pdf"

async def atender_cliente(cedula):
    print(f"atendiendo al cliente{cedula}rapidamente...")
    await asyncio.sleep(1)
    print(f"paciente{cedula}se ha ido de lata.")

async def main ():
    #trabajamos el reporteen un hilo secundario
    tarea_pesada = asyncio.to_thread(procesar_reporte_medico)
    tarea_clientes = [atender_cliente(i) for i in range(1, 4)]
    await asyncio.gather(tarea_pesada, *tarea_clientes)

asyncio.run(main())
