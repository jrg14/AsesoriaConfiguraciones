from django.db import models, transaction
from django.contrib.auth.models import User
from django.utils import timezone

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    country = models.CharField(max_length=2, choices=[('US', 'US'), ('CA', 'CA'), ('EU', 'EU')])
    phone_number = models.CharField(max_length=15)
    message = models.TextField()
    agree_to_policies = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


class Estadisticas(models.Model):
    visitas = models.PositiveIntegerField(default=0)
    peticiones = models.PositiveIntegerField(default=0)
    guardadas = models.PositiveIntegerField(default=0)
    facturas = models.PositiveIntegerField(default=0)
    
    ofimatica = models.PositiveIntegerField(default=0)
    gaming = models.PositiveIntegerField(default=0)
    ia = models.PositiveIntegerField(default=0)
    edicion = models.PositiveIntegerField(default=0)
    gama_baja = models.PositiveIntegerField(default=0)
    gama_media = models.PositiveIntegerField(default=0)
    gama_alta = models.PositiveIntegerField(default=0)
    
    
    

# Define un modelo de Djanfo llamado ConfiguracionPC encargada de guardar las 
# configuraciones de los usuarios haciendo referencia a los ids de los componentes
class ConfiguracionPC(models.Model):
    Usuario = models.ManyToManyField(User, related_name='configuraciones')
    filtro = models.CharField(max_length=100)
    precio = models.FloatField(null=True)
    chasis = models.IntegerField()
    placa_base = models.IntegerField()
    cpu = models.IntegerField()
    ram = models.IntegerField()
    almacenamiento = models.IntegerField()
    fuente_alimentacion = models.IntegerField()
    gpu = models.IntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    validez = models.BooleanField(default=True)


# Define un modelo de Django llamado CPU para representar información sobre un procesador. 
class CPU(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=200)
    precio = models.FloatField()
    vendedor = models.CharField(max_length=50)
    velocidad_reloj = models.CharField(max_length=20)
    num_nucleos = models.IntegerField()
    cache = models.CharField(max_length=20)
    graficos_integrados = models.CharField(max_length=10, choices=[('Sí', 'Sí'), ('No', 'No')])
    socket = models.CharField(max_length=20)


# Define un modelo de Django llamado RAM para representar información sobre las memorias RAM.
class RAM(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=200)
    precio = models.FloatField()
    vendedor = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20)
    capacidad = models.CharField(max_length=20)
    velocidad = models.CharField(max_length=20)
    canales = models.IntegerField()
    compatibilidad = models.CharField(max_length=150)


# Define un modelo de Django llamado GPU para representar información sobre las tarjetas gráficas.
class GPU(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=200)
    precio = models.FloatField()
    vendedor = models.CharField(max_length=100)
    tarjeta = models.CharField(max_length=100)
    resolucion = models.CharField(max_length=50)
    memoria = models.CharField(max_length=50)
    frecuencia = models.CharField(max_length=20)
    hdmi = models.IntegerField()
    displayport = models.IntegerField()
    ranura_expansion = models.IntegerField()
    conectores = models.CharField(max_length=50)
    consumo = models.IntegerField()
    tamaño = models.CharField(max_length=50)

    
# Define un modelo de Django llamado Chasis para representar información sobre las torres o chasis. 
class Chasis(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=200)
    precio = models.FloatField()
    vendedor = models.CharField(max_length=100)
    placas = models.CharField(max_length=100)
    tamaño_gpu = models.CharField(max_length=50)
    bahia525 = models.IntegerField(default=0)
    bahias35 = models.IntegerField(default=0)
    bahias25 = models.IntegerField(default=0)   
    ventiladores = models.CharField(max_length=3, choices=[('Sí', 'Sí'), ('No', 'No')])
    usb = models.CharField(max_length=10)
    audio = models.CharField(max_length=3, choices=[('Sí', 'Sí'), ('No', 'No')])
    fuente_alimentacion = models.CharField(max_length=3, choices=[('Sí', 'Sí'), ('No', 'No')])
    tam_fuente = models.CharField(max_length=50)


# Define un modelo de Django llamado PlacaBase para representar información sobre las placas base.
class PlacaBase(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=200)
    precio = models.FloatField()
    vendedor = models.CharField(max_length=100)
    formato = models.CharField(max_length=20)
    gama = models.CharField(max_length=20)
    socket = models.CharField(max_length=20)
    ram_compatible = models.CharField(max_length=100)
    ram = models.IntegerField()
    sata = models.IntegerField()
    m2 = models.CharField(max_length=3, choices=[('Sí', 'Sí'), ('No', 'No')])
    usb = models.IntegerField()
    hdmi = models.IntegerField()
    controlador_red = models.CharField(max_length=3, choices=[('Sí', 'Sí'), ('No', 'No')])
    controlador_sonido = models.CharField(max_length=3, choices=[('Sí', 'Sí'), ('No', 'No')])
    PCIex1 = models.CharField(max_length=3, choices=[('Sí', 'Sí'), ('No', 'No')])
    PCIex2 = models.CharField(max_length=3, choices=[('Sí', 'Sí'), ('No', 'No')])
    PCIex4 = models.CharField(max_length=3, choices=[('Sí', 'Sí'), ('No', 'No')])
    PCIex8 = models.CharField(max_length=3, choices=[('Sí', 'Sí'), ('No', 'No')])
    PCIex16 = models.CharField(max_length=3, choices=[('Sí', 'Sí'), ('No', 'No')])

    
class FuenteAlimentacion(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=200)
    precio = models.FloatField()
    vendedor = models.CharField(max_length=100)
    potencia = models.IntegerField()
    forma = models.CharField(max_length=20)
    eficiencia = models.CharField(max_length=100)
    tamaño = models.CharField(max_length=50)
    peso = models.CharField(max_length=20)
    atx24 = models.IntegerField()
    eps12v = models.IntegerField()
    pcie16 = models.IntegerField()    
    pcie8 = models.IntegerField()    
    
  
# Define un modelo de Django llamado Almacenamiento para representar información sobre las memorias no volatiles. 
class Almacenamiento(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=200)
    precio = models.FloatField()
    vendedor = models.CharField(max_length=100)
    capacidad = models.CharField(max_length=50)
    velocidad = models.CharField(max_length=50)
    forma = models.CharField(max_length=50)
    tipo_interfaz = models.CharField(max_length=50)   

    
# Define una clase encargada de toda la lógica y conexiones con la base de datos
class bd_manager: 

    @staticmethod
    def crear_contactar(first_name, last_name, email, country, phone_number, message, agree_to_policies):
        contact = Contact.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            country=country,
            phone_number=phone_number,
            message=message,
            agree_to_policies=agree_to_policies
        )
        return contact

    @staticmethod
    def obtener_incidencias():
        return Contact.objects.all()
    
    @staticmethod
    def eliminar_incidencias(id_incidencia):
        incidencia = Contact.objects.get(id=id_incidencia)
        incidencia.delete()
        return True
    
    @staticmethod
    def obtener_num_incidencias():
        return Contact.objects.count()
    
    @staticmethod
    def obtener_estadisticas():
        estadisticas, created = Estadisticas.objects.get_or_create(id=1)
        return {
            "visitas": estadisticas.visitas,
            "peticiones": estadisticas.peticiones,
            "guardadas": estadisticas.guardadas,
            "facturas": estadisticas.facturas,
            "ofimatica": estadisticas.ofimatica,
            "gaming": estadisticas.gaming,
            "ia": estadisticas.ia,
            "edicion": estadisticas.edicion,
            "gama_baja": estadisticas.gama_baja,
            "gama_media": estadisticas.gama_media,
            "gama_alta": estadisticas.gama_alta,            
        }
        
    @staticmethod
    @transaction.atomic
    def actualizar_visitas():
        estadisticas, created = Estadisticas.objects.get_or_create(id=1)
        estadisticas.visitas += 1
        estadisticas.save()

    @staticmethod
    @transaction.atomic
    def actualizar_peticiones():
        estadisticas, created = Estadisticas.objects.get_or_create(id=1)
        estadisticas.peticiones += 1
        estadisticas.save()

    @staticmethod
    @transaction.atomic
    def actualizar_guardadas(num):
        estadisticas, created = Estadisticas.objects.get_or_create(id=1)
        estadisticas.guardadas += num
        estadisticas.save()

    @staticmethod
    @transaction.atomic
    def actualizar_facturas():
        estadisticas, created = Estadisticas.objects.get_or_create(id=1)
        estadisticas.facturas += 1
        estadisticas.save()        
        
    @staticmethod
    @transaction.atomic
    def actualizar_categoria_gama(categoria_gama):
        categoria, gama, tipo = categoria_gama.split('_')
        if categoria in ['ofimatica', 'gaming', 'ia', 'edicion'] and tipo in ['baja', 'media', 'alta']:
            gam = gama + '_' + tipo
            estadisticas = Estadisticas.objects.get_or_create(id=1)[0]
            setattr(estadisticas, categoria, getattr(estadisticas, categoria) + 1)
            setattr(estadisticas, gam, getattr(estadisticas, gam) + 1)
            estadisticas.save()
        else:
            raise ValueError("Categoría o gama no válida.")

    @staticmethod
    def obtener_numero_usuarios():
        return User.objects.count()
    
    #Metodos para crear las configuraciones de los PCs, obtener todos los PCs y borrar todos los PCs 
    @staticmethod
    def crear_configuracion(usuario, filtro, precio, chasis, placa_base, cpu, ram, almacenamiento, fuente_alimentacion, gpu, validez):
        configuracion, created = ConfiguracionPC.objects.update_or_create(
            filtro=filtro,
            chasis=chasis,
            placa_base=placa_base,
            cpu=cpu,
            ram=ram,
            almacenamiento=almacenamiento,
            fuente_alimentacion=fuente_alimentacion,
            gpu=gpu,
            defaults={'precio': precio, 
                      'validez': validez,
                      'fecha_creacion': timezone.now()}
        )
        
        # If not created, update the fields
        if not created:
            configuracion.precio = precio
            configuracion.validez = validez
            configuracion.fecha_creacion = timezone.now()
            configuracion.save()
            
        return configuracion
        # configuracion, created = ConfiguracionPC.objects.get_or_create(
        #     #Usuario=usuario,
        #     filtro=filtro,
        #     precio=precio,
        #     chasis=chasis,
        #     placa_base=placa_base,
        #     cpu=cpu,
        #     ram=ram,
        #     almacenamiento=almacenamiento,
        #     fuente_alimentacion=fuente_alimentacion,
        #     gpu=gpu
        # )
        # if not created:
        #     #configuracion.Usuario = usuario
        #     configuracion.filtro = filtro
        #     configuracion.precio = precio
        #     configuracion.chasis = chasis
        #     configuracion.placa_base = placa_base
        #     configuracion.cpu = cpu
        #     configuracion.ram = ram
        #     configuracion.almacenamiento = almacenamiento
        #     configuracion.fuente_alimentacion = fuente_alimentacion
        #     configuracion.gpu = gpu
        #     configuracion.save()        


    @staticmethod
    def obtener_todas_configuraciones():
        return ConfiguracionPC.objects.all()

    @staticmethod
    def obtener_num_configuraciones():
        return ConfiguracionPC.objects.count()

    @staticmethod
    def borrar_configuraciones():
        ConfiguracionPC.objects.all().delete()
        
    @staticmethod
    def obtener_configuraciones_por_filtro_y_precio(filtro, precio_min, precio_max):
        return ConfiguracionPC.objects.filter(filtro=filtro, precio__gte=precio_min, precio__lte=precio_max)    
    
    @staticmethod
    def obtener_configuracion_por_id(configuracion_id):
        try:
            return ConfiguracionPC.objects.get(id=configuracion_id)
        except ConfiguracionPC.DoesNotExist:
            return None
        
    @staticmethod
    def obtener_configuraciones_por_usuario(usuario):
        try:
            return ConfiguracionPC.objects.filter(Usuario=usuario)
        except ConfiguracionPC.DoesNotExist:
            return None    
        
    @staticmethod
    def añadir_usuario_configuracion(usuario, configuracion_id):
        try:
            configuracion = ConfiguracionPC.objects.get(id=configuracion_id)
            configuracion.Usuario.set([usuario]) 
        except ConfiguracionPC.DoesNotExist:
            return None

    @staticmethod
    def eliminar_usuario_configuracion(usuario, configuracion_id):
        try:
            configuracion = ConfiguracionPC.objects.get(id=configuracion_id)
            configuracion.Usuario.remove(usuario)
        except ConfiguracionPC.DoesNotExist:
            return None

    #Metodos para crear un almacenamiento, obtener todos los almacenamientos, obtener un almacenamiento y borrar todos los almacenamientos    
    @staticmethod
    def crear_almacenamiento(marca, modelo, precio, vendedor, capacidad, velocidad, forma, tipo_interfaz):
        almacenamiento, creado = Almacenamiento.objects.update_or_create(
            marca=marca,
            modelo=modelo,
            vendedor=vendedor,
            defaults={
                'precio': precio,
                'capacidad': capacidad,
                'velocidad': velocidad,
                'forma': forma,
                'tipo_interfaz': tipo_interfaz
            }
        )
        return almacenamiento
        
    @staticmethod
    def resetear_precio_todos_almacenamientos():
        Almacenamiento.objects.all().update(precio=None)        
        
    @staticmethod
    def obtener_todos_almacenamientos():
        return Almacenamiento.objects.all()

    @staticmethod
    def borrar_almacenamientos():
        Almacenamiento.objects.all().delete()

    @staticmethod
    def obtener_almacenamiento_por_id(id):
        try:
            return Almacenamiento.objects.get(id=id)
        except Almacenamiento.DoesNotExist:
            return None

    #Metodos para crear una cpu, obtener todos las cpu, obtener una cpu y borrar todos las cpu
    @staticmethod
    def crear_cpu(marca, modelo, precio, vendedor, velocidad_reloj, num_nucleos, cache, graficos_integrados, socket):
        cpu, created = CPU.objects.update_or_create(
            marca=marca,
            modelo=modelo,
            vendedor=vendedor,
            defaults={
                'precio': precio,
                'velocidad_reloj': velocidad_reloj,
                'num_nucleos': num_nucleos,
                'cache': cache,
                'graficos_integrados': graficos_integrados,
                'socket': socket
            }
        )
        return cpu

    @staticmethod
    def resetear_precio_todos_cpu():
        CPU.objects.all().update(precio=None)        

    @staticmethod
    def obtener_todas_cpus():
        return CPU.objects.all()

    @staticmethod
    def borrar_cpus():
        CPU.objects.all().delete()

    @staticmethod
    def obtener_cpu_por_id(id):
        try:
            return CPU.objects.get(id=id)
        except CPU.DoesNotExist:
            return None
    
    #Metodos para crear una ram, obtener todos las ram, obtener una ram y borrar todos las ram    
    @staticmethod
    def crear_ram(marca, modelo, precio, vendedor, tipo, capacidad, velocidad, canales, compatibilidad):
        ram, created = RAM.objects.update_or_create(
            marca=marca,
            modelo=modelo,
            vendedor=vendedor,
            defaults={
                'precio': precio,
                'tipo': tipo,
                'capacidad': capacidad,
                'velocidad': velocidad,
                'canales': canales,
                'compatibilidad': compatibilidad
            }
        )
        return ram

    @staticmethod
    def resetear_precio_todos_ram():
        RAM.objects.all().update(precio=None)        
        
    @staticmethod
    def obtener_todas_rams():
        return RAM.objects.all()

    @staticmethod
    def borrar_rams():
        RAM.objects.all().delete()        

    @staticmethod
    def obtener_ram_por_id(id):
        try:
            return RAM.objects.get(id=id)
        except RAM.DoesNotExist:
            return None

    #Metodos para crear una gpu, obtener todos las gpu, obtener una gpu y borrar todos las gpu
    @staticmethod
    def crear_gpu(marca, modelo, precio, vendedor, tarjeta, resolucion, memoria, frecuencia, hdmi, displayport, ranura_expansion, conectores, consumo, tamaño):
        gpu, created = GPU.objects.update_or_create(
            marca=marca,
            modelo=modelo,
            vendedor=vendedor,
            defaults={
                'tarjeta': tarjeta,
                'precio': precio,
                'resolucion': resolucion,
                'memoria': memoria,
                'frecuencia': frecuencia,
                'hdmi': hdmi,
                'displayport': displayport,
                'ranura_expansion': ranura_expansion,
                'conectores': conectores,
                'consumo': consumo,
                'tamaño': tamaño
            }
        )
        return gpu

    @staticmethod
    def resetear_precio_todos_gpu():
        GPU.objects.all().update(precio=None)        

    @staticmethod
    def obtener_todas_gpus():
        return GPU.objects.all()

    @staticmethod
    def borrar_gpus():
        GPU.objects.all().delete()  

    @staticmethod
    def obtener_gpu_por_id(id):
        try:
            return GPU.objects.get(id=id)
        except GPU.DoesNotExist:
            return None

    #Metodos para crear una placa, obtener todos las placas, obtener una placa y borrar todos las placas
    @staticmethod
    def crear_placa(marca, modelo, precio, vendedor, formato, gama, socket, ram_compatible, ram, sata, m2, usb, hdmi, 
                    controlador_red, controlador_sonido, PCIex1, PCIex2, PCIex4, PCIex8, PCIex16):
        placa, created = PlacaBase.objects.update_or_create(
            marca=marca,
            modelo=modelo,
            vendedor=vendedor,
            defaults={
                'precio': precio,
                'formato': formato,
                'gama': gama,
                'socket': socket,
                'ram_compatible': ram_compatible,
                'ram': ram,
                'sata': sata,
                'm2': m2,
                'usb': usb,
                'hdmi': hdmi,
                'controlador_red': controlador_red,
                'controlador_sonido': controlador_sonido,
                'PCIex1': PCIex1,
                'PCIex2': PCIex2,
                'PCIex4': PCIex4,
                'PCIex8': PCIex8,
                'PCIex16': PCIex16
            }
        )
        return placa

    @staticmethod
    def resetear_precio_todos_placa():
        PlacaBase.objects.all().update(precio=None)        

    @staticmethod
    def obtener_todas_placas():
        return PlacaBase.objects.all()

    @staticmethod
    def borrar_placas():
        PlacaBase.objects.all().delete()  

    @staticmethod
    def obtener_placa_por_id(id):
        try:
            return PlacaBase.objects.get(id=id)
        except PlacaBase.DoesNotExist:
            return None

    #Metodos para crear un chasis, obtener todos los chasis, obtener un chasis y borrar todos los chasis        
    @staticmethod
    def crear_chasis(marca, modelo, precio, vendedor, placas, tamaño_gpu, bahia525, bahias35, bahias25, ventiladores, usb, audio, fuente_alimentacion, tam_fuente):
        chasis, created = Chasis.objects.update_or_create(
            marca=marca,
            modelo=modelo,
            vendedor=vendedor,
            defaults={
                'precio': precio,
                'placas': placas,
                'tamaño_gpu': tamaño_gpu,
                'bahia525': bahia525,
                'bahias35': bahias35,
                'bahias25': bahias25,
                'ventiladores': ventiladores,
                'usb': usb,
                'audio': audio,
                'fuente_alimentacion': fuente_alimentacion,
                'tam_fuente': tam_fuente
            }
        )
        return chasis

    @staticmethod
    def resetear_precio_todos_chasis():
        Chasis.objects.all().update(precio=None)        
        
    @staticmethod
    def obtener_todos_chasis():
        return Chasis.objects.all()

    @staticmethod
    def borrar_chasis():
        Chasis.objects.all().delete()

    @staticmethod
    def obtener_chasis_por_id(id):
        try:
            return Chasis.objects.get(id=id)
        except Chasis.DoesNotExist:
            return None
    
    #Metodos para crear una fuente, obtener todos las fuentes, obtener una fuente y borrar todos las fuentes    
    @staticmethod
    def crear_fuente(marca, modelo, precio, vendedor, potencia, forma, eficiencia, tamaño, peso, atx24, eps12v, pcie16, pcie8):
        fuente_alimentacion, created = FuenteAlimentacion.objects.update_or_create(
            marca=marca,
            modelo=modelo,
            vendedor=vendedor,
            defaults={
                'precio': precio,
                'potencia': potencia,
                'forma': forma,
                'eficiencia': eficiencia,
                'tamaño': tamaño,
                'peso': peso,
                'atx24': atx24,
                'eps12v': eps12v,
                'pcie16': pcie16,
                'pcie8': pcie8
            }
        )
        return fuente_alimentacion

    @staticmethod
    def resetear_precio_todos_fuente():
        FuenteAlimentacion.objects.all().update(precio=None)        
       
    @staticmethod
    def obtener_todas_fuentes():
        return FuenteAlimentacion.objects.all()

    @staticmethod
    def borrar_fuentes():
        FuenteAlimentacion.objects.all().delete() 
 
    @staticmethod
    def obtener_fuente_por_id(id):
        try:
            return FuenteAlimentacion.objects.get(id=id)
        except FuenteAlimentacion.DoesNotExist:
            return None
 
 