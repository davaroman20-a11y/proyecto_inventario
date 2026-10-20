import asyncio
import aiofiles
import json

async def monitorear_sistema():
    while True:
        print("Monitor: Sistema funcionando OK...")
        await asyncio.sleep(2)

async def hacer_backup():
    print("Iniciando backup...")

    async with aiofiles.open("inventario.json", mode="r", encoding="utf-8") as archivo:
        texto_json = await archivo.read()
        datos = json.loads(texto_json)

    async with aiofiles.open("backup.json", mode="w", encoding="utf-8") as archivo:
        texto_backup = json.dumps(datos, indent=4)
        await archivo.write(texto_backup)

    print("Backup realizado correctamente.")

async def main():
    tarea_monitor = asyncio.create_task(monitorear_sistema())

    try:
        await asyncio.wait_for(hacer_backup(), timeout=1)
    except asyncio.TimeoutError:
        print("Alerta: El backup falló por lentitud del disco")
    except json.JSONDecodeError:
        print("Error: El archivo JSON tiene una estructura rota.")
    except FileNotFoundError:
        print("Error: No se encontró el archivo inventario.json.")

    tarea_monitor.cancel()

asyncio.run(main())