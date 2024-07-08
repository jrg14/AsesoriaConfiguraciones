
import pytest
from django.db import IntegrityError, transaction
from django.contrib.auth.models import User
from core.models import Contact, Estadisticas, ConfiguracionPC, Almacenamiento, CPU, RAM, GPU, PlacaBase, Chasis, FuenteAlimentacion
from core.models import bd_manager
from django.utils import timezone

# Métodos relacionados con Contact
@pytest.mark.django_db
def test_crear_contactar():
    contact = bd_manager.crear_contactar(
        first_name="Jane",
        last_name="Smith",
        email="jane.smith@example.com",
        country="CA",
        phone_number="987654321",
        message="Hi!",
        agree_to_policies=True
    )
    assert Contact.objects.count() == 1
    assert contact.first_name == "Jane"

@pytest.mark.django_db
def test_obtener_incidencias():
    bd_manager.crear_contactar(
        first_name="Jane",
        last_name="Smith",
        email="jane.smith@example.com",
        country="CA",
        phone_number="987654321",
        message="Hi!",
        agree_to_policies=True
    )
    incidencias = bd_manager.obtener_incidencias()
    assert len(incidencias) == 1

@pytest.mark.django_db
def test_eliminar_incidencias():
    contact = bd_manager.crear_contactar(
        first_name="Jane",
        last_name="Smith",
        email="jane.smith@example.com",
        country="CA",
        phone_number="987654321",
        message="Hi!",
        agree_to_policies=True
    )
    assert bd_manager.eliminar_incidencias(contact.id)
    assert Contact.objects.count() == 0

@pytest.mark.django_db
def test_obtener_num_incidencias():
    bd_manager.crear_contactar(
        first_name="Jane",
        last_name="Smith",
        email="jane.smith@example.com",
        country="CA",
        phone_number="987654321",
        message="Hi!",
        agree_to_policies=True
    )
    assert bd_manager.obtener_num_incidencias() == 1

# Métodos relacionados con Estadisticas
@pytest.mark.django_db
def test_obtener_estadisticas():
    estadisticas = bd_manager.obtener_estadisticas()
    assert estadisticas["visitas"] == 0

@pytest.mark.django_db
def test_actualizar_visitas():
    bd_manager.actualizar_visitas()
    estadisticas = bd_manager.obtener_estadisticas()
    assert estadisticas["visitas"] == 1

@pytest.mark.django_db
def test_actualizar_peticiones():
    bd_manager.actualizar_peticiones()
    estadisticas = bd_manager.obtener_estadisticas()
    assert estadisticas["peticiones"] == 1

@pytest.mark.django_db
def test_actualizar_guardadas():
    bd_manager.actualizar_guardadas(5)
    estadisticas = bd_manager.obtener_estadisticas()
    assert estadisticas["guardadas"] == 5

@pytest.mark.django_db
def test_actualizar_facturas():
    bd_manager.actualizar_facturas()
    estadisticas = bd_manager.obtener_estadisticas()
    assert estadisticas["facturas"] == 1

@pytest.mark.django_db
def test_actualizar_categoria_gama():
    bd_manager.actualizar_categoria_gama("gaming_gama_alta")
    estadisticas = bd_manager.obtener_estadisticas()
    assert estadisticas["gaming"] == 1
    assert estadisticas["gama_alta"] == 1

@pytest.mark.django_db
def test_obtener_numero_usuarios():
    User.objects.create_user(username="testuser", password="password")
    assert bd_manager.obtener_numero_usuarios() == 1

# Métodos relacionados con ConfiguracionPC
@pytest.mark.django_db
def test_crear_configuracion():
    user = User.objects.create_user(username="testuser", password="password")
    configuracion = bd_manager.crear_configuracion(
        usuario=user,
        filtro="gaming",
        precio=1000,
        chasis=1,
        placa_base=1,
        cpu=1,
        ram=1,
        almacenamiento=1,
        fuente_alimentacion=1,
        gpu=1,
        validez=True
    )
    assert ConfiguracionPC.objects.count() == 1

@pytest.mark.django_db
def test_obtener_todas_configuraciones():
    user = User.objects.create_user(username="testuser", password="password")
    bd_manager.crear_configuracion(
        usuario=user,
        filtro="gaming",
        precio=1000,
        chasis=1,
        placa_base=1,
        cpu=1,
        ram=1,
        almacenamiento=1,
        fuente_alimentacion=1,
        gpu=1,
        validez=True
    )
    configuraciones = bd_manager.obtener_todas_configuraciones()
    assert len(configuraciones) == 1

@pytest.mark.django_db
def test_borrar_configuraciones():
    user = User.objects.create_user(username="testuser", password="password")
    bd_manager.crear_configuracion(
        usuario=user,
        filtro="gaming",
        precio=1000,
        chasis=1,
        placa_base=1,
        cpu=1,
        ram=1,
        almacenamiento=1,
        fuente_alimentacion=1,
        gpu=1,
        validez=True
    )
    bd_manager.borrar_configuraciones()
    assert ConfiguracionPC.objects.count() == 0

@pytest.mark.django_db
def test_obtener_configuraciones_por_filtro_y_precio():
    user = User.objects.create_user(username="testuser", password="password")
    bd_manager.crear_configuracion(
        usuario=user,
        filtro="gaming",
        precio=1000,
        chasis=1,
        placa_base=1,
        cpu=1,
        ram=1,
        almacenamiento=1,
        fuente_alimentacion=1,
        gpu=1,
        validez=True
    )
    configuraciones = bd_manager.obtener_configuraciones_por_filtro_y_precio("gaming", 1000, 2000)
    assert len(configuraciones) == 1

@pytest.mark.django_db
def test_obtener_configuracion_por_id():
    user = User.objects.create_user(username="testuser", password="password")
    config = bd_manager.crear_configuracion(
        usuario=user,
        filtro="gaming",
        precio=1000,
        chasis=1,
        placa_base=1,
        cpu=1,
        ram=1,
        almacenamiento=1,
        fuente_alimentacion=1,
        gpu=1,
        validez=True
    )
    configuracion = bd_manager.obtener_configuracion_por_id(config.id)
    assert configuracion is not None

@pytest.mark.django_db
def test_obtener_configuraciones_por_usuario():
    user = User.objects.create_user(username="testuser", password="password")
    config = bd_manager.crear_configuracion(
        usuario=user,
        filtro="gaming",
        precio=1000,
        chasis=1,
        placa_base=1,
        cpu=1,
        ram=1,
        almacenamiento=1,
        fuente_alimentacion=1,
        gpu=1,
        validez=True
    )
    bd_manager.añadir_usuario_configuracion(user, config.id)
    configuraciones = bd_manager.obtener_configuraciones_por_usuario(user)
    assert len(configuraciones) == 1

@pytest.mark.django_db
def test_añadir_usuario_configuracion():
    user1 = User.objects.create_user(username="testuser1", password="password")
    user2 = User.objects.create_user(username="testuser2", password="password")
    config = bd_manager.crear_configuracion(
        usuario=user1,
        filtro="gaming",
        precio=1000,
        chasis=1,
        placa_base=1,
        cpu=1,
        ram=1,
        almacenamiento=1,
        fuente_alimentacion=1,
        gpu=1,
        validez=True
    )
    bd_manager.añadir_usuario_configuracion(user2, config.id)
    configuracion = bd_manager.obtener_configuracion_por_id(config.id)
    assert user2 in configuracion.Usuario.all()

@pytest.mark.django_db
def test_eliminar_usuario_configuracion():
    user1 = User.objects.create_user(username="testuser1", password="password")
    user2 = User.objects.create_user(username="testuser2", password="password")
    config = bd_manager.crear_configuracion(
        usuario=user1,
        filtro="gaming",
        precio=1000,
        chasis=1,
        placa_base=1,
        cpu=1,
        ram=1,
        almacenamiento=1,
        fuente_alimentacion=1,
        gpu=1,
        validez=True
    )
    bd_manager.añadir_usuario_configuracion(user2, config.id)
    bd_manager.eliminar_usuario_configuracion(user2, config.id)
    configuracion = bd_manager.obtener_configuracion_por_id(config.id)
    assert user2 not in configuracion.Usuario.all()

# Métodos relacionados con Almacenamiento
@pytest.mark.django_db
def test_crear_almacenamiento():
    almacenamiento = bd_manager.crear_almacenamiento(
        marca="Marca1",
        modelo="Modelo1",
        precio=100,
        vendedor="Vendedor1",
        capacidad="1TB",
        velocidad="7200rpm",
        forma="3.5",
        tipo_interfaz="SATA"
    )
    assert Almacenamiento.objects.count() == 1

@pytest.mark.django_db
def test_obtener_todos_almacenamientos():
    bd_manager.crear_almacenamiento(
        marca="Marca1",
        modelo="Modelo1",
        precio=100,
        vendedor="Vendedor1",
        capacidad="1TB",
        velocidad="7200rpm",
        forma="3.5",
        tipo_interfaz="SATA"
    )
    almacenamientos = bd_manager.obtener_todos_almacenamientos()
    assert len(almacenamientos) == 1

@pytest.mark.django_db
def test_obtener_almacenamiento_por_id():
    almacenamiento = bd_manager.crear_almacenamiento(
        marca="Marca1",
        modelo="Modelo1",
        precio=100,
        vendedor="Vendedor1",
        capacidad="1TB",
        velocidad="7200rpm",
        forma="3.5",
        tipo_interfaz="SATA"
    )
    almacenamiento_obtenido = bd_manager.obtener_almacenamiento_por_id(almacenamiento.id)
    assert almacenamiento_obtenido is not None

@pytest.mark.django_db
def test_eliminar_almacenamiento():
    almacenamiento = bd_manager.crear_almacenamiento(
        marca="Marca1",
        modelo="Modelo1",
        precio=100,
        vendedor="Vendedor1",
        capacidad="1TB",
        velocidad="7200rpm",
        forma="3.5",
        tipo_interfaz="SATA"
    )
    bd_manager.borrar_almacenamientos()
    assert Almacenamiento.objects.count() == 0

# Métodos relacionados con CPU
@pytest.mark.django_db
def test_crear_cpu():
    cpu = bd_manager.crear_cpu(
        marca="Marca1",
        modelo="Modelo1",
        precio=200,
        vendedor="Vendedor1",
        velocidad_reloj = "",
        num_nucleos = 1,
        cache = "",
        graficos_integrados = "",
        socket = ""
    )
    assert CPU.objects.count() == 1

@pytest.mark.django_db
def test_obtener_todas_cpus():
    bd_manager.crear_cpu(
        marca="Marca1",
        modelo="Modelo1",
        precio=200,
        vendedor="Vendedor1",
        velocidad_reloj = "",
        num_nucleos = 1,
        cache = "",
        graficos_integrados = "",
        socket = ""
    )
    cpus = bd_manager.obtener_todas_cpus()
    assert len(cpus) == 1

@pytest.mark.django_db
def test_obtener_cpu_por_id():
    cpu = bd_manager.crear_cpu(
        marca="Marca1",
        modelo="Modelo1",
        precio=200,
        vendedor="Vendedor1",
        velocidad_reloj = "",
        num_nucleos = 1,
        cache = "",
        graficos_integrados = "",
        socket = ""
    )
    cpu_obtenido = bd_manager.obtener_cpu_por_id(cpu.id)
    assert cpu_obtenido is not None

@pytest.mark.django_db
def test_eliminar_cpu():
    cpu = bd_manager.crear_cpu(
        marca="Marca1",
        modelo="Modelo1",
        precio=200,
        vendedor="Vendedor1",
        velocidad_reloj = "",
        num_nucleos = 1,
        cache = "",
        graficos_integrados = "",
        socket = ""
    )
    bd_manager.borrar_cpus()
    assert CPU.objects.count() == 0

# Métodos relacionados con RAM
@pytest.mark.django_db
def test_crear_ram():
    ram = bd_manager.crear_ram(
        marca="Marca1",
        modelo="Modelo1",
        precio=100,
        vendedor="Vendedor1",
        tipo = "",
        capacidad = "",
        velocidad = "",
        canales = 1,
        compatibilidad = "",
    )
    assert RAM.objects.count() == 1

@pytest.mark.django_db
def test_obtener_todas_rams():
    bd_manager.crear_ram(
        marca="Marca1",
        modelo="Modelo1",
        precio=100,
        vendedor="Vendedor1",
        tipo = "",
        capacidad = "",
        velocidad = "",
        canales = 1,
        compatibilidad = "",
    )
    rams = bd_manager.obtener_todas_rams()
    assert len(rams) == 1

@pytest.mark.django_db
def test_obtener_ram_por_id():
    ram = bd_manager.crear_ram(
        marca="Marca1",
        modelo="Modelo1",
        precio=100,
        vendedor="Vendedor1",
        tipo = "",
        capacidad = "",
        velocidad = "",
        canales = 1,
        compatibilidad = "",
    )
    ram_obtenida = bd_manager.obtener_ram_por_id(ram.id)
    assert ram_obtenida is not None

@pytest.mark.django_db
def test_eliminar_ram():
    ram = bd_manager.crear_ram(
        marca="Marca1",
        modelo="Modelo1",
        precio=100,
        vendedor="Vendedor1",
        tipo = "",
        capacidad = "",
        velocidad = "",
        canales = 1,
        compatibilidad = "",
    )
    bd_manager.borrar_rams()
    assert RAM.objects.count() == 0

# Métodos relacionados con GPU
@pytest.mark.django_db
def test_crear_gpu():
    gpu = bd_manager.crear_gpu(
        marca="Marca1",
        modelo="Modelo1",
        precio=300,
        vendedor="Vendedor1",
        tarjeta = "",
        resolucion = "",
        memoria = "",
        frecuencia = "",
        hdmi = 1,
        displayport = 1,
        ranura_expansion = 1,
        conectores = "",
        consumo = 1,
        tamaño = ""
    )
    assert GPU.objects.count() == 1

@pytest.mark.django_db
def test_obtener_todas_gpus():
    bd_manager.crear_gpu(
        marca="Marca1",
        modelo="Modelo1",
        precio=300,
        vendedor="Vendedor1",
        tarjeta = "",
        resolucion = "",
        memoria = "",
        frecuencia = "",
        hdmi = 1,
        displayport = 1,
        ranura_expansion = 1,
        conectores = "",
        consumo = 1,
        tamaño = ""
    )
    gpus = bd_manager.obtener_todas_gpus()
    assert len(gpus) == 1

@pytest.mark.django_db
def test_obtener_gpu_por_id():
    gpu = bd_manager.crear_gpu(
        marca="Marca1",
        modelo="Modelo1",
        precio=300,
        vendedor="Vendedor1",
        tarjeta = "",
        resolucion = "",
        memoria = "",
        frecuencia = "",
        hdmi = 1,
        displayport = 1,
        ranura_expansion = 1,
        conectores = "",
        consumo = 1,
        tamaño = ""
    )
    gpu_obtenida = bd_manager.obtener_gpu_por_id(gpu.id)
    assert gpu_obtenida is not None

@pytest.mark.django_db
def test_eliminar_gpu():
    gpu = bd_manager.crear_gpu(
        marca="Marca1",
        modelo="Modelo1",
        precio=300,
        vendedor="Vendedor1",
        tarjeta = "",
        resolucion = "",
        memoria = "",
        frecuencia = "",
        hdmi = 1,
        displayport = 1,
        ranura_expansion = 1,
        conectores = "",
        consumo = 1,
        tamaño = ""
    )
    bd_manager.borrar_gpus()
    assert GPU.objects.count() == 0

# Métodos relacionados con PlacaBase
@pytest.mark.django_db
def test_crear_placa_base():
    placa_base = bd_manager.crear_placa(
        marca="Marca1",
        modelo="Modelo1",
        precio=150,
        vendedor="Vendedor1",
        formato = "",
        gama = "",
        socket = "",
        ram_compatible = "",
        ram = 1,
        sata = 1,
        m2 = "",
        usb = 1,
        hdmi = 1,
        controlador_red = "",
        controlador_sonido = "",
        PCIex1 = "",
        PCIex2 = "",
        PCIex4 = "",
        PCIex8 = "",
        PCIex16 = ""
    )
    assert PlacaBase.objects.count() == 1

@pytest.mark.django_db
def test_obtener_todas_placas_base():
    bd_manager.crear_placa(
        marca="Marca1",
        modelo="Modelo1",
        precio=150,
        vendedor="Vendedor1",
        formato = "",
        gama = "",
        socket = "",
        ram_compatible = "",
        ram = 1,
        sata = 1,
        m2 = "",
        usb = 1,
        hdmi = 1,
        controlador_red = "",
        controlador_sonido = "",
        PCIex1 = "",
        PCIex2 = "",
        PCIex4 = "",
        PCIex8 = "",
        PCIex16 = ""
    )
    placas_base = bd_manager.obtener_todas_placas()
    assert len(placas_base) == 1

@pytest.mark.django_db
def test_obtener_placa_base_por_id():
    placa_base = bd_manager.crear_placa(
        marca="Marca1",
        modelo="Modelo1",
        precio=150,
        vendedor="Vendedor1",
        formato = "",
        gama = "",
        socket = "",
        ram_compatible = "",
        ram = 1,
        sata = 1,
        m2 = "",
        usb = 1,
        hdmi = 1,
        controlador_red = "",
        controlador_sonido = "",
        PCIex1 = "",
        PCIex2 = "",
        PCIex4 = "",
        PCIex8 = "",
        PCIex16 = ""
    )
    placa_base_obtenida = bd_manager.obtener_placa_por_id(placa_base.id)
    assert placa_base_obtenida is not None

@pytest.mark.django_db
def test_eliminar_placa_base():
    placa_base = bd_manager.crear_placa(
        marca="Marca1",
        modelo="Modelo1",
        precio=150,
        vendedor="Vendedor1",
        formato = "",
        gama = "",
        socket = "",
        ram_compatible = "",
        ram = 1,
        sata = 1,
        m2 = "",
        usb = 1,
        hdmi = 1,
        controlador_red = "",
        controlador_sonido = "",
        PCIex1 = "",
        PCIex2 = "",
        PCIex4 = "",
        PCIex8 = "",
        PCIex16 = ""
    )
    bd_manager.borrar_placas()
    assert PlacaBase.objects.count() == 0

# Métodos relacionados con Chasis
@pytest.mark.django_db
def test_crear_chasis():
    chasis = bd_manager.crear_chasis(
        marca="Marca1",
        modelo="Modelo1",
        precio=50,
        vendedor="Vendedor1",
        placas = "",
        tamaño_gpu = "",
        bahia525 = 1,
        bahias35 = 1,
        bahias25 = 1,  
        ventiladores = "",
        usb = "",
        audio = "",
        fuente_alimentacion = "",
        tam_fuente = ""
    )
    assert Chasis.objects.count() == 1

@pytest.mark.django_db
def test_obtener_todos_chasis():
    bd_manager.crear_chasis(
        marca="Marca1",
        modelo="Modelo1",
        precio=50,
        vendedor="Vendedor1",
        placas = "",
        tamaño_gpu = "",
        bahia525 = 1,
        bahias35 = 1,
        bahias25 = 1,  
        ventiladores = "",
        usb = "",
        audio = "",
        fuente_alimentacion = "",
        tam_fuente = ""
    )
    chasis = bd_manager.obtener_todos_chasis()
    assert len(chasis) == 1

@pytest.mark.django_db
def test_obtener_chasis_por_id():
    chasis = bd_manager.crear_chasis(
        marca="Marca1",
        modelo="Modelo1",
        precio=50,
        vendedor="Vendedor1",
        placas = "",
        tamaño_gpu = "",
        bahia525 = 1,
        bahias35 = 1,
        bahias25 = 1,  
        ventiladores = "",
        usb = "",
        audio = "",
        fuente_alimentacion = "",
        tam_fuente = ""
    )
    chasis_obtenido = bd_manager.obtener_chasis_por_id(chasis.id)
    assert chasis_obtenido is not None

@pytest.mark.django_db
def test_eliminar_chasis():
    chasis = bd_manager.crear_chasis(
        marca="Marca1",
        modelo="Modelo1",
        precio=50,
        vendedor="Vendedor1",
        placas = "",
        tamaño_gpu = "",
        bahia525 = 1,
        bahias35 = 1,
        bahias25 = 1,  
        ventiladores = "",
        usb = "",
        audio = "",
        fuente_alimentacion = "",
        tam_fuente = ""
    )
    bd_manager.borrar_chasis()
    assert Chasis.objects.count() == 0

# Métodos relacionados con FuenteAlimentacion
@pytest.mark.django_db
def test_crear_fuente_alimentacion():
    bd_manager.crear_fuente(
        marca="Marca1",
        modelo="Modelo1",
        precio=70,
        vendedor="Vendedor1",
        potencia=500,
        forma="sad",
        eficiencia="80+ Bronze",
        tamaño="20s0",
        peso="213",
        atx24=1,
        eps12v=1,
        pcie16=1,
        pcie8=1
    )
    assert FuenteAlimentacion.objects.count() == 1

@pytest.mark.django_db
def test_obtener_todas_fuentes_alimentacion():
    bd_manager.crear_fuente(
        marca="Marca1",
        modelo="Modelo1",
        precio=70,
        vendedor="Vendedor1",
        potencia=500,
        forma="sad",
        eficiencia="80+ Bronze",
        tamaño="20s0",
        peso="213",
        atx24=1,
        eps12v=1,
        pcie16=1,
        pcie8=1
    )
    fuentes_alimentacion = bd_manager.obtener_todas_fuentes()
    assert len(fuentes_alimentacion) == 1

@pytest.mark.django_db
def test_obtener_fuente_alimentacion_por_id():
    fuente_alimentacion = bd_manager.crear_fuente(
        marca="Marca1",
        modelo="Modelo1",
        precio=70,
        vendedor="Vendedor1",
        potencia=500,
        forma="sad",
        eficiencia="80+ Bronze",
        tamaño="20s0",
        peso="213",
        atx24=1,
        eps12v=1,
        pcie16=1,
        pcie8=1
    )
    fuente_alimentacion_obtenida = bd_manager.obtener_fuente_por_id(fuente_alimentacion.id)
    assert fuente_alimentacion_obtenida is not None

@pytest.mark.django_db
def test_eliminar_fuentes_alimentacion():
    bd_manager.crear_fuente(
        marca="Marca1",
        modelo="Modelo1",
        precio=70,
        vendedor="Vendedor1",
        potencia=500,
        forma="sad",
        eficiencia="80+ Bronze",
        tamaño="20s0",
        peso="213",
        atx24=1,
        eps12v=1,
        pcie16=1,
        pcie8=1
    )
    bd_manager.borrar_fuentes()
    assert FuenteAlimentacion.objects.count() == 0
