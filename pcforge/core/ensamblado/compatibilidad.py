import re
from core.webScraping.insercion_datos import coma_por_punto


#Comprueba la compatibilidad de la placa con la CPU
def placa_cpu(placa, cpu):
    return (placa['socket'] == cpu['socket'])

#Comprueba la compatibilidad de la placa con la RAM
def placa_ram(placa, ram):
    return ((placa['ram_compatible'] == ram['tipo']) and (placa['ram'] >= ram['canales']))  

#Comprueba la compatibilidad de la placa con el chasis
def placa_chasis(placa, chasis):
    placa_formato = placa['formato']
    chasis_formato = chasis['placas']
    if chasis_formato == "E-ATX" and (placa_formato == "E-ATX" or placa_formato == "ATX" or placa_formato == "Micro-ATX") :
        return True
    elif chasis_formato == "ATX" and (placa == "ATX" or placa == "Micro-ATX"):
        return True
    elif chasis_formato == "Micro-ATX" and (placa == "Micro-ATX"):
        return True
    elif chasis_formato == "Mini ITX" and (placa == "Mini ITX"):
        return True
    else:
        return False

#Comprueba la compatibilidad de la placa con el almacenamiento
def placa_alma(placa, almacenamiento):
    if almacenamiento['tipo_interfaz'] == "SATA" and placa['sata'] >= 1:
        return True
    elif almacenamiento['tipo_interfaz'] == "PCIe" and placa['m2'] == "Si":
        return True
    else:
        return False

#Comprueba la compatibilidad de la fuente con la GPU
def fuente_gpu(fuente, gpu):
    if gpu['conectores'] == "1 x 16 pin" and fuente['pcie16'] >= 1:
        if fuente['potencia'] >= gpu['consumo']:
            return True
        else:
            return False
    elif (gpu['conectores'] == "1 x 8 pin" or gpu['conectores'] == "1 x 12VHPWR")  and fuente['pcie8'] >= 1:
        if fuente['potencia'] >= gpu['consumo']:
            return True
        else:
            return False
    else:
        return False

#Comprueba la compatibilidad de la fuente con el chasis
def fuente_chasis(fuente, chasis):
    
    if chasis['fuente_alimentacion'] == "No" and chasis['tam_fuente'] != "No":
        tam_chasis = float(re.search(r'\d+(?=\s)|\d+(?=mm)|\d+(?=x)', fuente['tamaño']).group(0))
        
        tam_fuente = float(coma_por_punto(re.search(r'\d+', chasis['tam_fuente']).group()))
        if tam_fuente < 70:
            tam_fuente *=10
        
        if tam_chasis <= tam_fuente:
            return True
        else:
            return False
    else:
        return False

#Comprueba la compatibilidad del chasis con la GPU
def chasis_gpu(chasis, gpu):
    tam_gpu = float(re.search(r'^\d+', gpu['tamaño']).group())
    tam_chasis = float(re.search(r'\d+', chasis['tamaño_gpu']).group()) 
    if tam_chasis < 70:
        tam_chasis *= 10

    if tam_gpu <= tam_chasis:
        return True
    else:
        return False


#Función que comprueba si todas las compatibilidades son correctas
def comatibilidad_con_gpu(chasis, placa, cpu, gpu, ram, almacenamiento, fuente):
    comp_placa_cpu = placa_cpu(placa, cpu)
    comp_placa_ram = placa_ram(placa, ram)
    comp_placa_chasis = placa_chasis(placa, chasis)
    comp_placa_alm = placa_alma(placa, almacenamiento)
    comp_fuente_gpu = fuente_gpu(fuente, gpu)
    comp_fuente_chasis = fuente_chasis(fuente, chasis)
    comp_chasis_gpu = chasis_gpu(chasis, gpu)
    
    es_compatible = (comp_placa_cpu and comp_placa_ram and comp_placa_chasis and comp_placa_alm and comp_fuente_gpu and comp_fuente_chasis and comp_chasis_gpu)
    
    return es_compatible


#Función que comprueba si todas las compatibilidades son correctas
def comatibilidad_sin_gpu(chasis, placa, cpu, ram, almacenamiento, fuente):
    comp_placa_cpu = placa_cpu(placa, cpu)
    comp_placa_ram = placa_ram(placa, ram)
    comp_placa_chasis = placa_chasis(placa, chasis)
    comp_placa_alm = placa_alma(placa, almacenamiento)
    comp_fuente_chasis = fuente_chasis(fuente, chasis)

    
    es_compatible = (comp_placa_cpu and comp_placa_ram and comp_placa_chasis and comp_placa_alm and comp_fuente_chasis)
    
    return es_compatible