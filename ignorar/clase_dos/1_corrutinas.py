import asyncio 

def verificar_repuestos_motos_sync(repuesto):
    return f"Repuesto {repuesto} verificado (Sync)"

async def verificar_repuestos_motos_async(repuesto):
    return f"Repuesto {repuesto} verificado (Async)"

resultado_sync = verificar_repuestos_motos_sync("pastillas de freno gixxer")
print("resultado normal:", resultado_sync)

print("USANDO UN EVENT LOOP")
resultado_async = asyncio.run(verificar_repuestos_motos_async("Filtro de aceite"))
print("Resultado real async", resultado_async)