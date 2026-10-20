import asyncio
import time

async def enviar_correro_bienvenida (usuario):
    print(f"[{time.strftime('%X')}] PREPARANDO CORREO PARA {usuario}....")
    await asyncio.sleep(4)
    print(f"[{time.strftime('%X')}] Correo Enviado exitosamente a {usuario}....")

async def registrar_usuario(usuario):
     print(f"[{time.strftime('%X')}] Guardando a {usuario} en la BD")
     await asyncio.sleep(1)
     print(f"[{time.strftime('%X')}]{usuario} Guardado en la BD....")
     tarea_correo = asyncio.create_task (enviar_correro_bienvenida )
     
