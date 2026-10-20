import asyncio

async def cobrar_tarjeta(monto):
    print("conectando con mercadopago.....")
    await asyncio.sleep(2)
    return "pago aprobado"

async def procesar_compra():
    try:
        # se le va a dar el maximo de tres segundos
        resultado = await asyncio.wait_for(cobrar_tarjeta (150000), timeout=3.0)
        print(f"Exito: {resultado} ")
    except asyncio.TimeoutError:
        print("error: MercadoPago tardo demasiado. transaccion cancelada.")

asyncio.run(procesar_compra())