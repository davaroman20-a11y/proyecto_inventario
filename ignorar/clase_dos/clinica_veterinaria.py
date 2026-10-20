import asyncio
import time

async def calcular_hidratacion (nombre, peso,constante_hidratacion, tiempo):
    print(f"calculando hidratacio para{nombre }......")
    await asyncio.sleep(1)
    
    try:
        resultado = (peso * constante_hidratacion) / tiempo

        if resultado > 500:
            raise ValueError("La dosis es demasiado alta")

        print(f"{nombre}: {resultado} ml/hora")

    except ZeroDivisionError:
        print(f"{nombre}: Emergencia, el tiempo no puede ser cero")

    except ValueError as e:
        print(f"{nombre}: Error, {e}")
      
async def main():
    inicio = time.time()

    await asyncio.gather(
        calcular_hidratacion(" gato1", 60, 20, 2),
        calcular_hidratacion(" gato2", 4, 10, 1),
        calcular_hidratacion(" perro1", 3, 20, 4),
        calcular_hidratacion(" perro2", 4, 30, 6),
    )

    fin = time.time()

    print(f" Tiempo total: {fin - inicio:.2f} segundos")

asyncio.run(main())