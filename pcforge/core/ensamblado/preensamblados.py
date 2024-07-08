from core.ensamblado.funcionesPreensamblados import *
from core.ensamblado.compatibilidad import *


def ofimatica_gama_baja(productos):
    tipo = obtener_rams_tipo(productos['ram'], 'DDR4')
    ram = obtener_rams_capacidad(tipo, '8')
    gra = obtener_cpus_graficos(productos['cpu'], True)
    cpu = obtener_cpu_por_gama(gra, 'baja')
    filtro = [{'filtro':'ofimatica_gama_baja'}]

    resultados = {
        'almacenamiento': obtener_almacenamiento_tipo(productos['almacenamiento'], 'sata'),
        'chasis': obtener_chasis_precio(productos['chasis'], 0, 100),
        'cpu': cpu,
        'fuente': obtener_fuente_alimentacion(productos['fuente'], 0, 650),
        'gpu': obtener_gpu(productos, False, 'baja'),
        'placa': obtener_placas_por_gama(productos['placa'], 'baja'),
        'ram': ram,
        'filtro': filtro
    }

    return resultados


def ofimatica_gama_media(productos):
    tipo = obtener_rams_tipo(productos['ram'], 'DDR4')
    ram = obtener_rams_capacidad(tipo, '16')
    gra = obtener_cpus_graficos(productos['cpu'], True)
    cpu = obtener_cpu_por_gama(gra, 'baja')    
    filtro = [{'filtro':'ofimatica_gama_media'}]

    resultados = {
        'almacenamiento': obtener_almacenamiento_tipo(productos['almacenamiento'], 'ssd'),
        'chasis': obtener_chasis_precio(productos['chasis'], 100, 150),
        'cpu': cpu,
        'fuente': obtener_fuente_alimentacion(productos['fuente'], 0, 650),
        'gpu': obtener_gpu(productos, False, 'baja'),
        'placa': obtener_placas_por_gama(productos['placa'], 'baja'),
        'ram': ram,
        'filtro': filtro
    }

    return resultados


def ofimatica_gama_alta(productos):
    tipo = obtener_rams_tipo(productos['ram'], 'DDR4')
    ram = obtener_rams_capacidad(tipo, '32')
    gra = obtener_cpus_graficos(productos['cpu'], True)
    cpu = obtener_cpu_por_gama(gra, 'media')    
    filtro = [{'filtro':'ofimatica_gama_alta'}]

    resultados = {
        'almacenamiento': obtener_almacenamiento_tipo(productos['almacenamiento'], 'ssd'),
        'chasis': obtener_chasis_precio(productos['chasis'], 150, 200),
        'cpu': cpu,
        'fuente': obtener_fuente_alimentacion(productos['fuente'], 0, 650),
        'gpu': obtener_gpu(productos, False, 'baja'),
        'placa': obtener_placas_por_gama(productos['placa'], 'media'),
        'ram': ram,
        'filtro': filtro
    }

    return resultados
 

def gaming_gama_baja(productos):
    tipo = obtener_rams_tipo(productos['ram'], 'DDR4')
    ram = obtener_rams_capacidad(tipo, '16')
    gra = obtener_cpus_graficos(productos['cpu'], False)
    cpu = obtener_cpu_por_gama(gra, 'media')
    filtro = [{'filtro':'gaming_gama_baja'}]

    resultados = {
        'almacenamiento': obtener_almacenamiento_tipo(productos['almacenamiento'], 'ssd'),
        'chasis': obtener_chasis_precio(productos['chasis'], 0, 100),
        'cpu': cpu,
        'fuente': obtener_fuente_alimentacion(productos['fuente'], 0, 750),
        'gpu': obtener_gpu(productos['gpu'], True, 'baja'),
        'placa': obtener_placas_por_gama(productos['placa'], 'baja'),
        'ram': ram,
        'filtro': filtro
    }

    return resultados


def gaming_gama_media(productos):
    tipo = obtener_rams_tipo(productos['ram'], 'DDR5')
    ram = obtener_rams_capacidad(tipo, '16')
    gra = obtener_cpus_graficos(productos['cpu'], False)
    cpu = obtener_cpu_por_gama(gra, 'media')        
    filtro = [{'filtro':'gaming_gama_media'}]


    resultados = {
        'almacenamiento': obtener_almacenamiento_tipo(productos['almacenamiento'], 'ssd'),
        'chasis': obtener_chasis_precio(productos['chasis'], 100, 150),
        'cpu': cpu,
        'fuente': obtener_fuente_alimentacion(productos['fuente'], 750, 850),
        'gpu': obtener_gpu(productos['gpu'], True, 'media'),
        'placa': obtener_placas_por_gama(productos['placa'], 'media'),
        'ram': ram,
        'filtro': filtro
    }

    return resultados


def gaming_gama_alta(productos):
    tipo = obtener_rams_tipo(productos['ram'], 'DDR5')
    ram = obtener_rams_capacidad(tipo, '32')
    gra = obtener_cpus_graficos(productos['cpu'], False)
    cpu = obtener_cpu_por_gama(gra, 'alta')    
    filtro = [{'filtro':'gaming_gama_alta'}]
    
    resultados = {
        'almacenamiento': obtener_almacenamiento_tipo(productos['almacenamiento'], 'ssd'),
        'chasis': obtener_chasis_precio(productos['chasis'], 150, 200),
        'cpu': cpu,
        'fuente': obtener_fuente_alimentacion(productos['fuente'], 850, 1000),
        'gpu': obtener_gpu(productos['gpu'], True, 'alta'),
        'placa': obtener_placas_por_gama(productos['placa'], 'alta'),
        'ram': ram,
        'filtro': filtro
    }

    return resultados


def edicion_gama_baja(productos):
    tipo = obtener_rams_tipo(productos['ram'], 'DDR5')
    ram = obtener_rams_capacidad(tipo, '16')
    gama = obtener_gpu(productos['gpu'], True, 'media')
    gpu = obtener_marca_gpu(gama, 'NVIDIA' )
    gama = obtener_cpu_por_gama(productos['cpu'], 'alta')
    cpu = obtener_cpus_marca(gama, 'Intel')    
    filtro = [{'filtro':'edicion_gama_baja'}]

    resultados = {
        'almacenamiento': obtener_almacenamiento_tipo(productos['almacenamiento'], 'ssd'),
        'chasis': obtener_chasis_precio(productos['chasis'], 0, 100),
        'cpu': cpu,
        'fuente': obtener_fuente_alimentacion(productos['fuente'], 0, 750),
        'gpu': gpu,
        'placa': obtener_placas_por_gama(productos['placa'], 'alta'),
        'ram': ram,
        'filtro': filtro
    }
    
    return resultados


def edicion_gama_media(productos):
    tipo = obtener_rams_tipo(productos['ram'], 'DDR5')
    ram = obtener_rams_capacidad(tipo, '32')   
    gama = obtener_gpu(productos['gpu'], True, 'media')
    gpu = obtener_marca_gpu(gama, 'NVIDIA' )
    gra = obtener_cpus_graficos(productos['cpu'], False)
    gama = obtener_cpu_por_gama(gra, 'media')
    cpu = obtener_cpus_marca(gama, 'Intel')      
    filtro = [{'filtro':'edicion_gama_media'}]


    resultados = {
        'almacenamiento': obtener_almacenamiento_tipo(productos['almacenamiento'], 'ssd'),
        'chasis': obtener_chasis_precio(productos['chasis'], 100, 150),
        'cpu': cpu,
        'fuente': obtener_fuente_alimentacion(productos['fuente'], 750, 850),
        'gpu': gpu,
        'placa': obtener_placas_por_gama(productos['placa'], 'alta'),
        'ram': ram,
        'filtro': filtro
    }

    return resultados


def edicion_gama_alta(productos):
    tipo = obtener_rams_tipo(productos['ram'], 'DDR5')
    ram = obtener_rams_capacidad(tipo, '64')
    gama = obtener_gpu(productos['gpu'], True, 'alta')
    gpu = obtener_marca_gpu(gama, 'NVIDIA' )
    gra = obtener_cpus_graficos(productos['cpu'], False)
    gama = obtener_cpu_por_gama(gra, 'alta')
    cpu = obtener_cpus_marca(gama, 'Intel')        
    filtro = [{'filtro':'edicion_gama_alta'}]
    
    resultados = {
        'almacenamiento': obtener_almacenamiento_tipo(productos['almacenamiento'], 'ssd'),
        'chasis': obtener_chasis_precio(productos['chasis'], 150, 200),
        'cpu': cpu,
        'fuente': obtener_fuente_alimentacion(productos['fuente'], 850, 1000),
        'gpu': gpu,
        'placa': obtener_placas_por_gama(productos['placa'], 'alta'),
        'ram': ram,
        'filtro': filtro
    }

    return resultados


def ia_gama_baja(productos):
    tipo = obtener_rams_tipo(productos['ram'], 'DDR4')
    ram = obtener_rams_capacidad(tipo, '32')
    gra = obtener_cpus_graficos(productos['cpu'], False)
    cpu = obtener_cpu_por_gama(gra, 'media')        
    filtro = [{'filtro':'ia_gama_baja'}]

    resultados = {
        'almacenamiento': obtener_almacenamiento_tipo(productos['almacenamiento'], 'ssd'),
        'chasis': obtener_chasis_precio(productos['chasis'], 0, 100),
        'cpu': cpu,
        'fuente': obtener_fuente_alimentacion(productos['fuente'], 0, 750),
        'gpu': obtener_gpu(productos['gpu'], True, 'media'),
        'placa': obtener_placas_por_gama(productos['placa'], 'baja'),
        'ram': ram,
        'filtro': filtro
    }

    return resultados


def ia_gama_media(productos):
    tipo = obtener_rams_tipo(productos['ram'], 'DDR5')
    ram = obtener_rams_capacidad(tipo, '32')
    gra = obtener_cpus_graficos(productos['cpu'], False)
    cpu = obtener_cpu_por_gama(gra, 'alta')            
    filtro = [{'filtro':'ia_gama_media'}]


    resultados = {
        'almacenamiento': obtener_almacenamiento_tipo(productos['almacenamiento'], 'ssd'),
        'chasis': obtener_chasis_precio(productos['chasis'], 100, 150),
        'cpu': cpu,
        'fuente': obtener_fuente_alimentacion(productos['fuente'], 750, 850),
        'gpu': obtener_gpu(productos['gpu'], True, 'alta'),
        'placa': obtener_placas_por_gama(productos['placa'], 'alta'),
        'ram': ram,
        'filtro': filtro
    }

    return resultados


def ia_gama_alta(productos):
    tipo = obtener_rams_tipo(productos['ram'], 'DDR5')
    ram = obtener_rams_capacidad(tipo, '64')
    gra = obtener_cpus_graficos(productos['cpu'], False)
    cpu = obtener_cpu_por_gama(gra, 'alta')        
    filtro = [{'filtro':'ia_gama_alta'}]
    
    resultados = {
        'almacenamiento': obtener_almacenamiento_tipo(productos['almacenamiento'], 'ssd'),
        'chasis': obtener_chasis_precio(productos['chasis'], 150, 200),
        'cpu': cpu,
        'fuente': obtener_fuente_alimentacion(productos['fuente'], 850, 1000),
        'gpu': obtener_gpu(productos['gpu'], True, 'alta'),
        'placa': obtener_placas_por_gama(productos['placa'], 'alta'),
        'ram': ram,
        'filtro': filtro
    }

    

    return resultados


def generar_pcs_ofimatica(productos):
    res = combinar(ofimatica_gama_baja(productos)) 
    res += combinar(ofimatica_gama_media(productos))
    res += combinar(ofimatica_gama_alta(productos))

    return res


def generar_pcs_gaming(productos):
    res = combinar(gaming_gama_baja(productos))
    res += combinar(gaming_gama_media(productos))
    res += combinar(gaming_gama_alta(productos))

    return res


def generar_pcs_edicion(productos):
    res = combinar(edicion_gama_baja(productos)) 
    res += combinar(edicion_gama_media(productos)) 
    res += combinar(edicion_gama_alta(productos)) 

    return res


def generar_pcs_ia(productos):
    res = combinar(ia_gama_baja(productos)) 
    res += combinar(ia_gama_media(productos)) 
    res += combinar(ia_gama_alta(productos)) 

    return res


def prensamblados():
    productos = obtener_productos_api()
    res = []
    comp = 0
        
    lista_de_listas1 =  generar_pcs_gaming(productos) + generar_pcs_edicion(productos) + generar_pcs_ia(productos)
    
    for index, lista in enumerate(lista_de_listas1): 
        almacenamiento = lista[0]
        chasis = lista[1]
        cpu = lista[2]
        fuente = lista[3]
        gpu = lista[4]
        placa = lista[5]
        ram = lista[6]

        compatible = comatibilidad_con_gpu(chasis, placa, cpu, gpu, ram, almacenamiento, fuente)
        index += 1
        if compatible:
            comp += 1
            res.append(lista)
            
            
    lista_de_listas2 = generar_pcs_ofimatica(productos)
    
    for index, lista in enumerate(lista_de_listas2): 
        almacenamiento = lista[0]
        chasis = lista[1]
        cpu = lista[2]
        fuente = lista[3]
        gpu = lista[4]
        placa = lista[5]
        ram = lista[6]

        compatible = comatibilidad_sin_gpu(chasis, placa, cpu, ram, almacenamiento, fuente)
        index += 1
        if compatible:
            comp += 1
            res.append(lista)  

    print("Numero de compatibilidades: ", comp)
    
    return res  

def main():
    prensamblados()
    
if __name__ == "__main__":
    main()