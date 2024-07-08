import requests
from itertools import product
import json
import os


#Función para obtener todos los productos de mi BD
def obtener_productos_api():
    url_api = f"http://localhost:8000/api/productos"
    try:
        response = requests.get(url_api)
        if response.status_code == 200:
            productos = response.json()
            return productos
        else:
            print(
                f"Error al obtener la CPU desde la API. Código de estado: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error al obtener la CPU desde la API: {e}")
        return None

#Función para escribir en un json
def escribir_en_json(resultados):
    directorio = r"C:\Users\Jorge\Desktop\PCForgeNuevo\scrapping_service"
    nombre = "pruebas2.json"
    path = os.path.join(directorio, nombre)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(resultados, f)

# Función para realizar comparaciones entre una lista y un elemento
def buscar_elemento(lista, objetivo):
    for elemento in lista:
        if elemento == objetivo:
            return True
    return False

# Función para conseguir todas las combinaciones de todos los productos 
def combinar(productos):
    combinaciones = list(product(*productos.values()))

    num_combinaciones = 0
    for combo in combinaciones:
        num_combinaciones += 1

    print(num_combinaciones)

    return combinaciones

#Diferenciar las placas según la gama para eliminar iteraciones en las combinaciones
def obtener_placas_por_gama(productos, gama):
    gama_baja = [
        "A300", "A320", "B350", "X370", "B450", "X470",  # AMD
        "B360", "H310", "B365", "H470", "B460"  # INTEL
    ]

    gama_media = [
        "A520", "B550", "X570", "A620", "B650",  # AMD
        "Z490", "Z590", "H570", "B560", "H670", "B660"  # INTEL
    ]

    gama_alta = [
        "B650E", "X670", "X670E", "X399", "TRX40", "WRX80",  # AMD
        "Z690",  "X299", "Z790", "X99"  # INTEL
    ]

    placas = []
    
    if gama == 'baja':
        for producto in productos:
            if buscar_elemento(gama_baja, producto['gama']):
                placas.append(producto)
    elif gama == 'media':
        for producto in productos:
            if buscar_elemento(gama_media, producto['gama']):
                placas.append(producto)
    elif gama == 'alta':
        for producto in productos:
            if buscar_elemento(gama_alta, producto['gama']):
                placas.append(producto)
    return placas

#Diferencia las rams según el tipo
def obtener_rams_tipo(productos, tipo):
    ram = []

    for producto in productos:
        if producto['tipo'] == tipo:
            ram.append(producto)

    return ram

#Diferencia las rams según el tipo
def obtener_rams_capacidad(productos, capacidad):
    ram = []

    if capacidad == '8':
        for producto in productos:
            if producto['capacidad'] == "8GB":
                ram.append(producto)
    elif capacidad == '16':
        for producto in productos:
            if producto['capacidad'] == "16GB":
                ram.append(producto)
    elif capacidad == '32':
        for producto in productos:
            if producto['capacidad'] == "32GB":
                ram.append(producto)
    elif capacidad == '64':
        for producto in productos:
            if producto['capacidad'] == "64GB":
                ram.append(producto)

    return ram


def obtener_cpus_graficos(productos, graficos):
    cpu= []
   
    if graficos:
        for producto in productos:
            if producto['graficos_integrados'] == "Si":
                cpu.append(producto)
    else:
        for producto in productos:
            if producto['graficos_integrados'] == "Si":
                cpu.append(producto)

    return cpu


def obtener_cpus_marca(productos, marca):
    cpu= []
   
    for producto in productos:
        if producto['marca'] == marca:
            cpu.append(producto)

    return cpu


#Diferenciar las placas según la gama para eliminar iteraciones en las combinaciones
def obtener_cpu_por_gama(productos, gama):
    gama_baja = [
        "AMD Ryzen 5 5500", "AMD Ryzen 5 5500GT",  # AMD
        "Intel Core i3-10100", "Intel Celeron G5905", "Intel Core i3-10105", "Intel Core i5-10400"  # INTEL
    ]

    gama_media = [
        "AMD Ryzen 7 7700", "AMD Ryzen 5 8600G", "AMD Ryzen 7 5700X", "AMD Ryzen 5 5600G", "AMD Ryzen 5 8500G", " AMD Ryzen 5 5600" # AMD
        "Intel Core i5-11400F", "Intel Core i5-14400F", "Intel Core i5-13600KF", "Intel Core i5-11400", "Intel Core i5-14600K", "Intel Core i5-10400F"  # INTEL
    ]

    gama_alta = [
        "AMD Ryzen 9 7900X", "AMD Ryzen 7 5800X", "AMD Ryzen 9 7950X", "AMD Ryzen 7 7700X", # AMD
        "Intel Core i7-14700K",  "Intel Core i7-14700KF", "Intel Core i9-11900KF", "Intel Core i9-13900KF", "Intel Core i9-14900KF", "Intel Core i9-14900K"  # INTEL
    ]

    cpu = []
    
    if gama == 'baja':
        for producto in productos:
            if buscar_elemento(gama_baja, producto['modelo']):
                cpu.append(producto)
    elif gama == 'media':
        for producto in productos:
            if buscar_elemento(gama_media, producto['modelo']):
                cpu.append(producto)
    elif gama == 'alta':
        for producto in productos:
            if buscar_elemento(gama_alta, producto['modelo']):
                cpu.append(producto)
    return cpu

#Obtener almacenamientos según el tipo
def obtener_almacenamiento_tipo(productos, tipo):
    alm = []

    if tipo == 'sata':
        for producto in productos:
            if producto['tipo_interfaz'] == "SATA":
                alm.append(producto)
    elif tipo == 'ssd':
        for producto in productos:
            if producto['tipo_interfaz'] == "PCIe":
                alm.append(producto)

    return alm

def obtener_gpu(productos, necesita_gpu, gama):
    gama_baja = [
        "3060 TI", "3060", "3070 TI", "3070", "3050", "4060 TI", "4060", # NVIDIA
        "7600 XT", "7600", "6800 XT", "6800", "6750 XT", "6750 GRE", "6700 XT", "6700", "6650 XT", "6600 XT", "6600"  # AMD
    ]

    gama_media = [
        "4070 TI", "4070 TI SUPER", "4070 SUPER", "4070", "3080 TI", "3080", # NVIDIA
        "6950 XT", "6900 XT", "7900 GRE", "7800 XT", "7700 XT",  # AMD
    ]

    gama_alta = [
        "4090", "4080", "4080 SUPER", "3090 TI", "3090", # NVIDIA
        "7900 XTX", "7900 XT" # AMD
    ]

    gpu = []

    if necesita_gpu:
        
        if gama == 'baja':
            for producto in productos:
                if buscar_elemento(gama_baja, producto['tarjeta']):
                    gpu.append(producto)
        elif gama == 'media':
            for producto in productos:
                if buscar_elemento(gama_media, producto['tarjeta']):
                    gpu.append(producto)
        elif gama == 'alta':
            for producto in productos:
                if buscar_elemento(gama_alta, producto['tarjeta']):
                    gpu.append(producto)
        return gpu
        
    else:
        gpu_nula = [{ 'id': '0', 'marca': 'No', 'modelo': 'No', 'precio': 0.0,
            'vendedor': 'N/A', 'tarjeta': 'N/A', 'resolucion': 'N/A', 'memoria': 'N/A',
            'frecuencia': 'N/A', 'hdmi': 0, 'displayport': 0, 'ranura_expansion': 0,
            'conectores': 'N/A', 'consumo': 0, 'tamaño': 'N/A'
        }]

        return gpu_nula
    
def obtener_marca_gpu(productos, marca):
    gpu = []

    for producto in productos:
        if producto['marca'] == marca:
            gpu.append(producto)
    
    return gpu
    

#Obtiene la fuente de alimentacion según su potencia
def obtener_fuente_alimentacion(productos, alime_min, alime_max):
    fuentes = []
    for producto in productos:
        if producto['potencia'] <= alime_max and producto['potencia'] > alime_min:
            fuentes.append(producto)
    
    return fuentes      

#Obtiene el chasis según su precio
def obtener_chasis_precio(productos, precio_min, precio_max):
    chasis = []
    for producto in productos:
        if producto['precio'] <= precio_max and producto['precio'] > precio_min:
            chasis.append(producto)
    
    return chasis    


def main():
    productos = obtener_productos_api()
    print(obtener_placas_por_gama(1, productos['placa']))
    
if __name__ == "__main__":
    main()