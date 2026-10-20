import asyncio
import time

async def calcular_hidratacion(nombre, peso, constante, tiempo):
    print(f"Calculando hidratacion para {nombre}...")
    await asyncio.sleep(1)

    try:
        resultado = (peso * constante) / tiempo

        if resultado > 500:
            raise ValueError("La dosis es demasiado alta")

        print(f"{nombre}: {resultado} ml/hora")

    except ZeroDivisionError:
        print(f"{nombre}: Emergencia, el tiempo no puede ser cero")

    except ValueError as e:
        print(f"{nombre}: Error, {e}")

async def main():
    inicio = time.perf_counter()

    await asyncio.gather(
        calcular_hidratacion("Perro", 10, 20, 2),
        calcular_hidratacion("Gato", 4, 20, 1),
        calcular_hidratacion("Conejo", 5, 20, 0),
        calcular_hidratacion("Caballo", 60, 20, 2)
    )
    fin = time.perf_counter()

    print(f"\nTiempo total: {fin - inicio:.2f} segundos")

asyncio.run(main())