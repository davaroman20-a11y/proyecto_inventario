import asyncio
import json

ARCHIVO = "inventario.json"

INVENTARIO_INICIAL = {
    "P001": {"nombre": "Laptop", "stock": 10},
    "P002": {"nombre": "Mouse", "stock": 5},
    "P003": {"nombre": "Teclado", "stock": 4},
}




tareas_alerta = []


def guardar_inventario(inventario):
    with open(ARCHIVO, "w", encoding="utf-8") as archivo:
        json.dump(inventario, archivo, indent=4, ensure_ascii=False)


def cargar_inventario():
    with open(ARCHIVO, "r", encoding="utf-8") as archivo:
        return json.load(archivo)


def reiniciar_inventario():
    guardar_inventario(INVENTARIO_INICIAL)


async def alerta_stock_bajo(codigo, nombre, stock_actual):
    await asyncio.sleep(2)
    print(f"⚠️ ALERTA CRÍTICA: El producto {nombre} ({codigo}) ha bajado a {stock_actual} unidades. Solicitar restock inmediato.")


async def vender_producto(codigo, cantidad_vendida):
    inventario = cargar_inventario()

    if codigo not in inventario:
        raise KeyError("Producto no encontrado")

    producto = inventario[codigo]

    if cantidad_vendida > producto["stock"]:
        raise ValueError("Stock insuficiente")

    producto["stock"] -= cantidad_vendida
    guardar_inventario(inventario)

    if producto["stock"] < 3:
        tarea = asyncio.create_task(
            alerta_stock_bajo(codigo, producto["nombre"], producto["stock"])
        )
        tareas_alerta.append(tarea)

    return f"Venta exitosa: {cantidad_vendida} x {producto['nombre']} ({codigo}). Stock restante: {producto['stock']}"