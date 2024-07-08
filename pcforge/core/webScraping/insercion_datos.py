import json
import os
import re

directorio =  os.path.dirname(os.path.abspath(__file__))
nombre_archivo1 = 'neobyte_normalizado.json'

productos = {
        'cpus': [],
        'placas': [],
        'rams': [],
        'gpus': [],
        'fuentes': [],
        'cajas': [],
        'ventilaciones':[],
        'almacenamientos':[]
    }


#Función que devuelve los productos
def obtener_productos():
    obtener_datos_neobyte()
    return productos


# Reemplaza las comas por puntos en un texto y convierte el resultado a un número de punto flotante.
def coma_por_punto(texto):
    numero_limpio = re.sub(r'\.', '', texto)
    numero_limpio = re.sub(r',', '.', numero_limpio)
    numero_float = float(numero_limpio)
    
    return numero_float


# Abre un archivo JSON y devuelve su contenido como una cadena de texto.
def abrir_json(nombre):
    print(directorio)
    path = os.path.join(directorio, nombre)
    with open(path, 'r', encoding='utf-8') as f:
        json_data = f.read()
    return json_data


# Extrae datos relevantes que caracterizan a un procesador a partir de una cadena de texto mediante regex .
def extraer_datos_cpu_neobyte(valor_interno):
    graficos_integrados = "Si" if re.search(r'Gráficos|Graphics', valor_interno, re.IGNORECASE) else "No"
    velocidad_reloj = re.findall(r'[0-9]+[,|.][0-9]+.?.Hz', valor_interno, re.IGNORECASE)
    precio = re.search(r'\d?\.?\d+,\d+(?=.€)', valor_interno).group()
    
    cpu = {
        'marca': re.search(r'Intel|AMD', valor_interno, re.IGNORECASE).group(),
        'modelo': re.search(r'(Intel.Core.i[0-9].[0-9]+[a-zA-Z]{0,2})|(AMD.Ryzen.[0-9].[0-9]+[a-zA-Z]{0,2})|(Intel.Celeron.[a-zA-Z][0-9]+)', valor_interno, re.IGNORECASE).group(),
        'precio': coma_por_punto(precio),
        'vendedor': 'Neobyte',
        'velocidad_reloj':  velocidad_reloj[0],
        'num_nucleos': re.search(r'((?<=núcleos: )\d+)|(\d+(?= núcleos))|((?<=Núcleos CPU: )\d+)', valor_interno, re.IGNORECASE).group(),
        'cache': re.search(r'((?<=Caché:.)[0-9]+.B)|((?<=Caché\sL[0-9]\s.total.:\s)[0-9]+\wB)|((?<=Caché\sL[0-9]\stotal:\s)[0-9]+\wB)|((?<=Caché\sL[0-9]\s\+\sL[0-9]\s.total.:\s)[0-9]+\wB)', valor_interno, re.IGNORECASE).group(),
        'graficos_integrados': graficos_integrados,
        'socket': re.search(r'LGA.?1200|LGA.?1700|AM4|AM5|LGA.?115|AMD.?sTRX4|AMD.?sTR4|TRX40|LGA.?2066|LGA.?3647', valor_interno, re.IGNORECASE).group()
    }
    return cpu


# Extrae datos relevantes que caracterizan a una placa base a partir de una cadena de texto mediante regex .
def extraer_datos_placa_base_neobyte(valor_interno):
    precio = re.search(r'\d?\.?\d+,\d+(?=.€)', valor_interno).group()
    socket_regex =  re.search(r'LGA.?1200|LGA.?1700|AM4|AM5|LGA.?115|AMD.?sTRX4|AMD.?sTR4|TRX40|LGA.?2066|LGA.?3647', valor_interno, re.IGNORECASE)
    if not socket_regex:
        sock = re.search(r'(5000)|(3000)|(7000)|(9000)', valor_interno, re.IGNORECASE).group()
        if ((sock == "5000") or (sock == "3000")):
            socket = "AM4"
        else:
            socket= "AM5"
    else:
        socket = socket_regex.group()
    
    modelo =  re.search(r'\s*(.*?)((?=\s*Placa)|(?=\s*-)|(?=\smás\sbarata))', valor_interno, re.IGNORECASE).group()
    modelo = re.sub(r'^Comprar\s*', '', modelo)
    gama = re.search(r'\w\d{3}\w?', valor_interno, re.IGNORECASE).group()
    
    m2_regex = re.search(r'(m2)|(m.2)', valor_interno, re.IGNORECASE)
    m2 = "Si" if m2_regex else "No"
    
    wifi_regex = re.search(r'(Wi-Fi)|(wifi)|(LAN)|(Ethernet)', valor_interno, re.IGNORECASE)
    wifi = "Si" if wifi_regex else "No"
 
    sonido_regex = re.search(r'(audio|sound)', valor_interno, re.IGNORECASE)
    sonido = "Si" if sonido_regex else "No" 
    
    PCIex1_regex = re.search(r'(PCIe\s\d.?\d?\sx\s?1\s)|(PCI Express\sx\s?1\s)|(PCI-E\sx\s?1\s)', valor_interno, re.IGNORECASE)
    PCIex1 = "Si" if PCIex1_regex else "No" 
    PCIex2_regex =  re.search(r'(PCIe\s\d.?\d?\sx\s?2\s)|(PCI Express\sx\s?2\s)|(PCI-E\sx\s?2\s)', valor_interno, re.IGNORECASE)
    PCIex2 = "Si" if PCIex2_regex else "No"  
    PCIex4_regex =  re.search(r'(PCIe\s\d.?\d?\sx\s?4\s)|(PCI Express\sx\s?4\s)|(PCI-E\sx\s?4\s)', valor_interno, re.IGNORECASE)
    PCIex4 = "Si" if PCIex4_regex else "No"  
    PCIex8_regex =  re.search(r'(PCIe\s\d.?\d?\sx\s?8\s)|(PCI Express\sx\s?8\s)|(PCI-E\sx\s?8\s)', valor_interno, re.IGNORECASE)
    PCIex8 = "Si" if PCIex8_regex else "No"  
    PCIex16_regex =  re.search(r'(PCIe\s\d.?\d?\sx\s?16\s)|(PCI Express\sx\s?16\s)|(PCI-E\sx\s?16\s)', valor_interno, re.IGNORECASE)
    PCIex16 = "Si" if PCIex16_regex else "No"      
    
    placa = {
        'marca': re.search(r'(Asrock)|(Asus)|(Gigabyte)|(MSI)|(sharkoon)', valor_interno, re.IGNORECASE).group(), 
        'modelo': modelo,
        'precio': coma_por_punto(precio),
        'vendedor': 'Neobyte',
        'formato': re.search(r'(Micro.?ATX)|(Mini-ITX)|(Extended ATX)|(e-ATX)|(Flex-ATX)|(Mini-STX)|(ATX)', valor_interno, re.IGNORECASE).group(),
        'gama': gama,
        'socket': socket,
        'ram_compatible': re.search(r'DDR1|DDR2|DDR3|DDR4|DDR5', valor_interno, re.IGNORECASE).group(),
        'ram': re.search(r'(\d(?=.\sDDR))|(\d(?=\sx\sDDR))|(\d(?=\sx\sDIMM))|(\d(?=\sx\s\w+\sslots))|(\d(?=\smódulos)) |(\d(?=\sx\s\w+\,\s\w+.\s\d+\w+.\sDDR))', valor_interno, re.IGNORECASE).group(),
        'sata': re.search(r'(\d(?=\sx\sSATA))|(\d(?=x\sSATA))|(\d(?=\s\w+\sSATA))|(\d(?=\sx\s\w+\sSATA))', valor_interno, re.IGNORECASE).group(),
        'm2': m2,
        'usb':re.search(r'(\d+(?=\s*x\s*USB))|(\d(?=\sx\s\w+\sUSB))', valor_interno).group(),
        'hdmi': re.search(r'(\d+(?=\s*x\s*HDMI))|(\d(?=\sx\s\w+\sHDMI))', valor_interno).group(),
        'controlador_red': wifi,
        'controlador_sonido': sonido,
        'PCIex1':  PCIex1,
        'PCIex2':  PCIex2,
        'PCIex4': PCIex4,
        'PCIex8':  PCIex8,
        'PCIex16':  PCIex16,
    }
    return placa


# Extrae datos relevantes que caracterizan a una RAM a partir de una cadena de texto mediante regex .
def extraer_datos_ram_neobyte(valor_interno):
    canales_regex = re.search(r'((?<=Módulos:\s)[1-4])|([1-4](?=.módulos))|([1-4](?=.modulo))', valor_interno, re.IGNORECASE)                
    canales = "1" if not canales_regex else canales_regex.group()
    compatibilidad_regex = re.search(r"(?:(Compatibilidad|Compatible):)(.*?)(?=(Dimensiones:|Formato:|$))", valor_interno, re.IGNORECASE)
    compatibilidad = "Todas" if not compatibilidad_regex else compatibilidad_regex.group()
    precio = re.search(r'\d?\.?\d+,\d+(?=.€)', valor_interno).group()
                
    ram = {
        'marca': re.search(r'Kingston|Corsair|G.Skill|Crucial', valor_interno, re.IGNORECASE).group(),
        'modelo': re.search(r'\s*(.*?)((?=\s*Memoria)|(?=\s*Kit)|(?=\s*Comprar)|(?=\s*-))', valor_interno, re.IGNORECASE).group(),
        'precio': coma_por_punto(precio),
        'vendedor': "Neobyte",
        'tipo': re.search(r'DDR1|DDR2|DDR3|DDR4|DDR5', valor_interno, re.IGNORECASE).group(),
        'capacidad': re.search(r'[0-9]+.B', valor_interno, re.IGNORECASE).group(),
        'velocidad': re.search(r'[0-9]+.?.?Hz', valor_interno, re.IGNORECASE).group(),
        'canales': canales,
        'compatibilidad': compatibilidad,
    }
    
    return ram


# Extrae datos relevantes que caracterizan a un procesador a partir de una cadena de texto mediante regex .
def extraer_datos_gpu_neobyte(valor_interno):
    if re.search(r'Radeon|RX', valor_interno, re.IGNORECASE):
        marca = "AMD"
    if re.search(r'RTX|GeForce', valor_interno, re.IGNORECASE):
        marca = "NVIDIA"
    if re.search(r'Iris Xe', valor_interno, re.IGNORECASE):
        marca  = "Intel"
    
    modelo = re.search(r'\s*(.*?)(?=\s*Tarjeta|\s*-|\s*Comprar)', valor_interno, re.IGNORECASE).group()
    tarjeta_regex = re.search(r'\d{4}(\sTi|\sTi\sSUPER|\sSUPER|\sXT|\sXTX|\sGRE)?', modelo, re.IGNORECASE)
    tarjeta = "Desconocida" if not tarjeta_regex else tarjeta_regex.group().upper()
    displayport_regex = re.search(r'(\d+)\s*x\s*DisplayPort', valor_interno)                
    displayport = "0" if not displayport_regex else displayport_regex.group(1)
    precio = re.search(r'\d?\.?\d+,\d+(?=.€)', valor_interno).group()
    conectores_regex = re.search(r'((?<=Conector:\s)\d\sx\s\d+.\w+)|((?<=Conectores:\s)\d\sx\s\d+.\w+)', valor_interno, re.IGNORECASE)
    conectores = "Desconocido" if not conectores_regex else conectores_regex.group()    
    resolucion_regex =  re.search(r'((?<=digital:\s)\d+\s?x\s?\d+)|((?<=máxima:\s)\d+\s?x\s?\d+)', valor_interno, re.IGNORECASE)
    resolucion = "Desconocido" if not resolucion_regex else resolucion_regex.group()
    frecuencia_regex =  re.findall(r'[0-9]+.?.Hz', valor_interno, re.IGNORECASE)
    frecuencia = "Desconocido" if not frecuencia_regex else frecuencia_regex[0]
    
    gpu = {
        'marca': marca,
        'modelo': modelo,
        'precio': coma_por_punto(precio),
        'vendedor': "Neobyte",
        'tarjeta': tarjeta,
        'resolucion':resolucion,
        'memoria': re.search(r'((?<=Memoria:\s)\d+\w+\s\w+\d)|((?<=Memoria de vídeo:\s)\d+\w+\s\w+\d)|((?<=Memoria de video:\s)\d+\w+\s\w+\d)', valor_interno, re.IGNORECASE).group(),
        'frecuencia': frecuencia,
        'hdmi': re.search(r'(\d+)\s*x\s*HDMI', valor_interno).group(1),
        'displayport': displayport,
        'ranura_expansion': re.search(r'(PCI Express\s|PCIe\s|PCI Express Gen\s)([1-5])', valor_interno, re.IGNORECASE).group(2),
        'conectores': conectores,
        'consumo': re.search(r'(\d{3,4}(?=W))|(\d{3,4}(?=\sW))', valor_interno, re.IGNORECASE).group(),
        'tamaño': re.search(r'(?<=Dimensiones:\s).?[0-9]+((.|,)[0-9]+)?.?x.?[0-9]+((.|,)[0-9]+)?.?x.?[0-9]+((.|,)[0-9]+)?',valor_interno, re.IGNORECASE).group()
    }
    
    return gpu


# Extrae datos relevantes que caracterizan a una fuente de alimentación a partir de una cadena de texto mediante regex .
def extraer_datos_fuente_neobyte(valor_interno):
    precio = re.search(r'\d?\.?\d+,\d+(?=.€)', valor_interno).group()
    peso_regex = re.search(r'(\d+(\.\d+)?)(?=\s*Kg)', valor_interno, re.IGNORECASE)
    peso = "0" if not peso_regex else peso_regex.group()
    
    atx24_regex = re.search(r'\d\s?x\s\w+\s?(24|20\+4|\S24|\S20\+4|\S+\s20\+4|\S+\s-\s24|.\w+\s.20\+4)', valor_interno, re.IGNORECASE)
    atx24 = "0" if not atx24_regex else atx24_regex.group()
    atx24_1 = re.search(r'(\d(?=x))|(\d(?=\sx))|(0)', atx24, re.IGNORECASE).group()
    
    pci8_regex = re.search(r'\d\s?x\s\S+\s?\S+\s(6\+2|8|-\s8|.6\+2)', valor_interno, re.IGNORECASE)
    pci8 = "0" if not pci8_regex else pci8_regex.group()
    pci8_1 = re.search(r'(\d(?=x))|(\d(?=\sx))|(0)', pci8, re.IGNORECASE).group()

    pci16_regex = re.search(r'\d\sx\s\S+\s(16|\S+\s.16|\S+\s-\s16|\S+\s\S+\s\S+\s.\s16|\S+\s\S+\s\S+\s\S+\s16)', valor_interno, re.IGNORECASE)
    pci16 = "0" if not pci16_regex else pci16_regex.group()
    pci16_1 = re.search(r'(\d(?=x))|(\d(?=\sx))|(0)', pci16, re.IGNORECASE).group()

    eps_regex = re.search(r'\d\s?x\s\S+\s(.?4\+4|\+12V\s4\+4|\S+\s.\s\S+\s.\s8|.?8|EPS12V)', valor_interno, re.IGNORECASE)
    eps = "0" if not eps_regex else eps_regex.group()
    eps_1 = re.search(r'(\d(?=x))|(\d(?=\sx))|(0)', eps, re.IGNORECASE).group()    
    
    
    fuente = {
        'marca': re.search(r'(?:Aerocool|Antec|Asus|Bequiet|Coolbox|Cooler Master|Corsair|DeepCool|EVGA|FSP|Gigabyte|Lian Li|Mars Gaming|MSI|Nfortec|Nox|NZXT|Seasonic|Sharkoon|Streacom|Thermaltake)', valor_interno, re.IGNORECASE).group(),
        'modelo': re.search(r'\s*(.*?)(?=\s*Caja|\s*-|\s*Comprar|\d+\,\d+\s€)', valor_interno, re.IGNORECASE).group(),
        'precio': coma_por_punto(precio),
        'vendedor': 'Neobyte',
        'potencia':  re.search(r'(\d{3,4}(?=W))|(\d{3,4}(?=\sW))', valor_interno, re.IGNORECASE).group(),
        'forma': re.search(r'ATX|MicroATX|Mini-ITX|Extended ATX|Flex-ATX|Mini-STX', valor_interno, re.IGNORECASE).group(),
        'eficiencia': re.search(r'(?i)80\s*(?:Plus|\+|PLUS.)\s*(?:Bronze|Silver|Gold|Platinum|Titanium|White)', valor_interno, re.IGNORECASE).group(),
        'tamaño': re.search(r'(?<=Dimensiones.)\s?\d+\D*\s?x\s?\d+\D*\s?x\s?\d+',valor_interno, re.IGNORECASE).group(),
        'peso': peso,
        'atx24': atx24_1,
        'eps12v': eps_1,
        'pcie16': pci16_1,
        'pcie8': pci8_1 
    }
    
    return fuente


# Extrae datos relevantes que caracterizan a un chasis a partir de una cadena de texto mediante regex .
def extraer_datos_cajas_neobyte(valor_interno):

    precio = re.search(r'\d?\.?\d+,\d+(?=.€)', valor_interno).group()
    tam_gpu_regex = re.findall(r'((?<=GPU.)\s?\d+mm)|((?<=gráficas hasta:)\s?\d+\s?mm)|((?<=gráfica:)\s?\d+,\d+\s?cm)|((?<=Gráfica de hasta)\s?\d+\s?mm)', valor_interno, re.IGNORECASE)
    tam_gpu = next((match for match in tam_gpu_regex if any(match)), "No")

    if tam_gpu == "No":
        pass
    else:
        tam_gpu = next(part for part in tam_gpu if part)


    tam_psu_regex = re.search(r'((?<=alimentación:)\s?\d+\,?\d?\s?.m)|((?<=PSU:)\s?\d+.m)', valor_interno, re.IGNORECASE)
    tam_psu = "No"
    if tam_psu_regex:
        tam_psu = next((match for match in tam_psu_regex.groups() if match), "No")
    
    fuente_regex = re.findall(r'(Fuente de alimentación incluida)|(Incluye fuente de alimentación)|(Potencia:)|(Fuente de alimentación: \d+W)', valor_interno, re.IGNORECASE)
    coin = next((match for match in fuente_regex if any(match)), None)
    fuente = "No" if not coin else "Si"
    
    bahias525_regex = re.search(r'((?<=Bahías 5\.25\":)\s?\d)|((?<=Bahía 5\.25\":)\s?\d)|(\d(?= x Bahías de 5\.25))', valor_interno, re.IGNORECASE)
    bahias525 = "0" if not bahias525_regex else bahias525_regex.group()

    bahias35_regex = re.search(r'((?<=Bahías 3\.5\":)\s?\d)|((?<=Bahía 3\.5\":)\s?\d)|(\d(?= x Bahías de 3\.5))', valor_interno, re.IGNORECASE)
    bahias35 = "0" if not bahias35_regex else bahias35_regex.group()
 
    bahias25_regex = re.search(r'((?<=Bahías 2\.5\":)\s?\d)|((?<=Bahía 2\.5\":)\s?\d)|(\d(?= x Bahías de 2\.5))', valor_interno, re.IGNORECASE)
    bahias25 = "0" if not bahias25_regex else bahias25_regex.group()
    
    audio_regex = re.search(r'(audio)|(sonido)', valor_interno, re.IGNORECASE)
    audio = "Si" if audio_regex else "No"
    
    usb_regex = re.search(r'(\d+(?=\s*x\s*USB))|(\d(?=\sx\s\w+\sUSB))', valor_interno)
    usb = usb_regex.group() if usb_regex else "No"
    
    # placa_regex = re.findall(r'(Micro.?ATX|Mini-ITX|Extended ATX|e-ATX|Flex-ATX|Mini-STX|ATX)', valor_interno, re.IGNORECASE)
    placa_regex = re.search(r'((e-ATX)|(ATX)|(Mini-ATX)|(Micro.?ATX)|(Mini-ITX))', valor_interno, re.IGNORECASE)
    placas_base_concatenadas = re.sub(r"e-ATX","E-ATX", placa_regex.group())
    
    caja = {
        'marca': re.search(r'(?:Aerocool|Antec|Approx|Asus|Bequiet|Bitfenix|Coolbox|Cooler\sMaster|Corsair|DeepCool|Eminent-\sewent|Fractal|FSP|Generico|Gigabyte|Hyte|Iggual|Lian\sLi|Mars\sGaming|MSI|Nfortec|Nox|NZXT|Raspberry|Seasonic|Sharkoon|Startech|Streacom|Tacens|Thermaltake|Tooq)', valor_interno, re.IGNORECASE).group(),
        'modelo': re.search(r'\s*(.*?)((?=\s*Caja)|(?=\s*Comprar)|(?=\s*-))', valor_interno, re.IGNORECASE).group(),
        'precio': coma_por_punto(precio),
        'vendedor': 'Neobyte',
        'placas': placas_base_concatenadas,
        'tamaño_gpu':tam_gpu ,
        'bahia525': bahias525,
        'bahias35': bahias35,
        'bahias25': bahias25,
        'ventiladores':'Si',
        'usb': usb ,
        'audio': audio,
        'fuente_alimentacion': fuente,
        'tam_fuente': tam_psu
    }
    return caja
    
    
# Extrae datos relevantes que caracterizan a una refrigeración a partir de una cadena de texto mediante regex .    
def extraer_datos_ventilacion_neobyte(valor_interno): 
    ventilacion = {
        # 'marca': re.search(r'(?:Aerocool|Antec|Approx|Asus|Bequiet|Bitfenix|Coolbox|Cooler\sMaster|Corsair|DeepCool|Eminent-\sewent|Fractal|FSP|Generico|Gigabyte|Hyte|Iggual|Lian\sLi|Mars\sGaming|MSI|Nfortec|Nox|NZXT|Raspberry|Seasonic|Sharkoon|Startech|Streacom|Tacens|Thermaltake|Tooq)', valor_interno, re.IGNORECASE).group(),
        # 'modelo': re.search(r'\s*(.*?)((?=\s*Caja)|(?=\s*Comprar)|(?=\s*-))', valor_interno, re.IGNORECASE).group(),
        # 'precio': re.search(r'[0-9]+,[0-9]+.€', valor_interno).group(),
        # 'vendedor': 'Neobyte',        
    }   

    return ventilacion


# Extrae datos relevantes que caracterizan a un sistema de almacenamiento no volatil a partir de una cadena de texto mediante regex .    
def extraer_datos_almacenamiento_neobyte(valor_interno): 
    precio = re.search(r'\d?\.?\d+,\d+(?=.€)', valor_interno).group()
    forma_regex =  re.search(r'((?<=Formato:)\s?\d+.\d+\")|((?<=forma:)\s?\d+.\d+\")|((?<=Formato:)\s?\w+\.\d)|((?<=forma:)\s?\w+\.\d)', valor_interno, re.IGNORECASE)
    forma = "Portable" if not forma_regex else forma_regex.group()
    velocidad_regex=re.search(r'(\d+\s?MB/s)|(\d+.\d+ Gbit/s)|(\d+\sMBps)|(\d+\srpm)', valor_interno, re.IGNORECASE)
    velocidad="Desconocido" if not velocidad_regex else velocidad_regex.group()
    
    almacenamiento = {
        'marca': re.search(r'(?:Acer|Adata|Asus|Asustor|Conceptronic|Coolbox|Corsair|Crucial|Eminent\-\sewent|Generico|Gigabyte|Iggual|Kingston|Lacie|Lexar|Mobilis|MSI|OWC|Qnap|Samsung|Seagate|Sharkoon|Startech|Subblim|Synology|TeamGroup|Tooq|Toshiba|Western\sDigital|WD)', valor_interno, re.IGNORECASE).group(),
        'modelo': re.search(r'\s*(.*?)((?=\s*Disco)|(?=\s*Comprar)|(?=\s*-)|(?=\s\d+.\d+\s€))', valor_interno, re.IGNORECASE).group(),
        'precio': coma_por_punto(precio),
        'vendedor': 'Neobyte', 
        'capacidad' : re.search(r'((?<=Capacidad:)\s?\d+\s?\w{1,2}B)|((?<=Capacidad de Almacenamiento:)\s?\d+\s?\w{1,2}B)', valor_interno, re.IGNORECASE).group(),
        'velocidad' :velocidad ,
        'forma' : forma,
        'tipo_interfaz' : re.search(r'((?<=Interfaz:\s)\w+)|((?<=Conexión:\s)\w+)|((?<=Interfaz\s)\w+)', valor_interno, re.IGNORECASE).group(), 
    }   

    return almacenamiento


   
def obtener_datos_neobyte():

    json_data = abrir_json(nombre_archivo1)
    data = json.loads(json_data)

    for clave_externa, diccionario_interno in data.items():
        for clave_interna, valor_interno in diccionario_interno.items():
            if clave_externa == "1":
                cpu = extraer_datos_cpu_neobyte(valor_interno)
                # print(clave_interna)
                # print(cpu)
                productos['cpus'].append(cpu)
            elif clave_externa == "2":
                placa_base = extraer_datos_placa_base_neobyte(valor_interno)
                # print(clave_interna)
                # print(placa_base)
                productos['placas'].append(placa_base)
            elif clave_externa == "3":
                ram = extraer_datos_ram_neobyte(valor_interno)
                # print(clave_interna)
                # print(ram)
                productos['rams'].append(ram)
            elif clave_externa == "4":
                gpu = extraer_datos_gpu_neobyte(valor_interno)
                # print(clave_interna)
                # print(gpu)                
                productos['gpus'].append(gpu)
            elif clave_externa == "5":
                fuente = extraer_datos_fuente_neobyte(valor_interno)
                # print(clave_interna)
                # print(fuente)                
                productos['fuentes'].append(fuente)     
            elif clave_externa == "6":
                caja = extraer_datos_cajas_neobyte(valor_interno)
                # print(clave_interna)
                # print(caja)                
                productos['cajas'].append(caja)                    
            elif clave_externa == "7":
                ventilacion = extraer_datos_ventilacion_neobyte(valor_interno)
                # print(clave_interna)
                # print(ventilacion)                
                productos['ventilaciones'].append(ventilacion)   
            elif clave_externa == "8":
                almacenamiento = extraer_datos_almacenamiento_neobyte(valor_interno)
                # print(clave_interna)
                # print(almacenamiento)                
                productos['almacenamientos'].append(almacenamiento)      
                

def main():
    obtener_datos_neobyte()


if __name__ == "__main__":
    main()
