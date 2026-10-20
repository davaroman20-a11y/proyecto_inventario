#you, 2 minutes ago | author(you)
from fastapi import FastAPI, HTTPException
from database import leer_base_datos, obtener_producto

#inicializar la aplicacion
apiRest = FastAPI(
    title="API de Inventarios SENA",
    description="mi primer api",
    version="1.0.0",
)

#nuestro primer endpoint
@apiRest.get("/") #decorador -> funcion que recibe como parametro otra funcion
async def ruta_principal():
    return {"mensaje": "Bienvenido a mi primera API Rest!"}
#you 3 days ago * primer commit terminado 

@apiRest.get("/estado")
async def estado_servidor():
    return {"status": "en linea", "servicios": "operativos sin ningun inconveniente "}

@apiRest.get("/suma")
async def sumar_numeros():
    numero1 = 10
    numero2 = 20
    total = numero1 + numero2

    return { "las suma de numero1 y numero2 es": total,
        "numero1": numero1,
        "numero2": numero2,
        "total": total
    }

@apiRest.get("/productos")
async def lista_productos():
    datos = await leer_base_datos()
    return {"cantidad": len(datos),"productos": datos}

@apiRest.get("/productos/{codigo_producto}")
async def buscar_un_producto(codigo_producto: str):
    try:
        producto = await obtener_producto(codigo_producto)
        return producto
    except KeyError:
        raise HTTPException(status_code=404, detail="El producto solicitado no existe en la BD")


   