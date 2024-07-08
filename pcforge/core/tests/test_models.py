# core/tests/test_models.py

import pytest
from django.contrib.auth.models import User
from core.models import Contact, Estadisticas, ConfiguracionPC, CPU, RAM, GPU, Chasis, PlacaBase, FuenteAlimentacion, Almacenamiento

@pytest.mark.django_db
def test_create_contact():
    contact = Contact.objects.create(
        first_name='John',
        last_name='Doe',
        email='john.doe@example.com',
        country='US',
        phone_number='1234567890',
        message='This is a test message',
        agree_to_policies=True
    )
    assert contact.first_name == 'John'
    assert contact.last_name == 'Doe'
    assert contact.email == 'john.doe@example.com'
    assert contact.country == 'US'
    assert contact.phone_number == '1234567890'
    assert contact.message == 'This is a test message'
    assert contact.agree_to_policies is True

@pytest.mark.django_db
def test_create_estadisticas():
    estadisticas = Estadisticas.objects.create(
        visitas=100,
        peticiones=50,
        guardadas=25,
        facturas=10,
        ofimatica=5,
        gaming=10,
        ia=2,
        edicion=3,
        gama_baja=4,
        gama_media=5,
        gama_alta=6
    )
    assert estadisticas.visitas == 100
    assert estadisticas.peticiones == 50
    assert estadisticas.guardadas == 25
    assert estadisticas.facturas == 10
    assert estadisticas.ofimatica == 5
    assert estadisticas.gaming == 10
    assert estadisticas.ia == 2
    assert estadisticas.edicion == 3
    assert estadisticas.gama_baja == 4
    assert estadisticas.gama_media == 5
    assert estadisticas.gama_alta == 6

@pytest.mark.django_db
def test_create_configuracion_pc():
    user = User.objects.create_user(username='testuser', password='12345')
    configuracion_pc = ConfiguracionPC.objects.create(
        filtro='gaming',
        precio=1500.00,
        chasis=1,
        placa_base=1,
        cpu=1,
        ram=1,
        almacenamiento=1,
        fuente_alimentacion=1,
        gpu=1
    )
    configuracion_pc.Usuario.add(user)
    assert configuracion_pc.filtro == 'gaming'
    assert configuracion_pc.precio == 1500.00
    assert configuracion_pc.chasis == 1
    assert configuracion_pc.placa_base == 1
    assert configuracion_pc.cpu == 1
    assert configuracion_pc.ram == 1
    assert configuracion_pc.almacenamiento == 1
    assert configuracion_pc.fuente_alimentacion == 1
    assert configuracion_pc.gpu == 1
    assert user in configuracion_pc.Usuario.all()

@pytest.mark.django_db
def test_create_cpu():
    cpu = CPU.objects.create(
        marca='Intel',
        modelo='Core i7',
        precio=300.00,
        vendedor='Vendedor1',
        velocidad_reloj='3.6 GHz',
        num_nucleos=8,
        cache='12 MB',
        graficos_integrados='Sí',
        socket='LGA1151'
    )
    assert cpu.marca == 'Intel'
    assert cpu.modelo == 'Core i7'
    assert cpu.precio == 300.00
    assert cpu.vendedor == 'Vendedor1'
    assert cpu.velocidad_reloj == '3.6 GHz'
    assert cpu.num_nucleos == 8
    assert cpu.cache == '12 MB'
    assert cpu.graficos_integrados == 'Sí'
    assert cpu.socket == 'LGA1151'

@pytest.mark.django_db
def test_create_ram():
    ram = RAM.objects.create(
        marca='Corsair',
        modelo='Vengeance',
        precio=150.00,
        vendedor='Vendedor2',
        tipo='DDR4',
        capacidad='16 GB',
        velocidad='3200 MHz',
        canales=2,
        compatibilidad='Intel, AMD'
    )
    assert ram.marca == 'Corsair'
    assert ram.modelo == 'Vengeance'
    assert ram.precio == 150.00
    assert ram.vendedor == 'Vendedor2'
    assert ram.tipo == 'DDR4'
    assert ram.capacidad == '16 GB'
    assert ram.velocidad == '3200 MHz'
    assert ram.canales == 2
    assert ram.compatibilidad == 'Intel, AMD'

@pytest.mark.django_db
def test_create_gpu():
    gpu = GPU.objects.create(
        marca='NVIDIA',
        modelo='RTX 3080',
        precio=700.00,
        vendedor='Vendedor3',
        tarjeta='PCIe',
        resolucion='4K',
        memoria='10 GB',
        frecuencia='1.8 GHz',
        hdmi=2,
        displayport=3,
        ranura_expansion=2,
        conectores='8-pin',
        consumo=320,
        tamaño='280 mm'
    )
    assert gpu.marca == 'NVIDIA'
    assert gpu.modelo == 'RTX 3080'
    assert gpu.precio == 700.00
    assert gpu.vendedor == 'Vendedor3'
    assert gpu.tarjeta == 'PCIe'
    assert gpu.resolucion == '4K'
    assert gpu.memoria == '10 GB'
    assert gpu.frecuencia == '1.8 GHz'
    assert gpu.hdmi == 2
    assert gpu.displayport == 3
    assert gpu.ranura_expansion == 2
    assert gpu.conectores == '8-pin'
    assert gpu.consumo == 320
    assert gpu.tamaño == '280 mm'

@pytest.mark.django_db
def test_create_chasis():
    chasis = Chasis.objects.create(
        marca='Cooler Master',
        modelo='MasterBox Q300L',
        precio=50.00,
        vendedor='Vendedor4',
        placas='ATX, Micro-ATX',
        tamaño_gpu='360 mm',
        bahia525=0,
        bahias35=2,
        bahias25=2,
        ventiladores='Sí',
        usb='USB 3.0',
        audio='Sí',
        fuente_alimentacion='Sí',
        tam_fuente='ATX'
    )
    assert chasis.marca == 'Cooler Master'
    assert chasis.modelo == 'MasterBox Q300L'
    assert chasis.precio == 50.00
    assert chasis.vendedor == 'Vendedor4'
    assert chasis.placas == 'ATX, Micro-ATX'
    assert chasis.tamaño_gpu == '360 mm'
    assert chasis.bahia525 == 0
    assert chasis.bahias35 == 2
    assert chasis.bahias25 == 2
    assert chasis.ventiladores == 'Sí'
    assert chasis.usb == 'USB 3.0'
    assert chasis.audio == 'Sí'
    assert chasis.fuente_alimentacion == 'Sí'
    assert chasis.tam_fuente == 'ATX'

@pytest.mark.django_db
def test_create_placabase():
    placabase = PlacaBase.objects.create(
        marca='ASUS',
        modelo='ROG STRIX B550-F',
        precio=200.00,
        vendedor='Vendedor5',
        formato='ATX',
        gama='Media',
        socket='AM4',
        ram_compatible='DDR4',
        ram=4,
        sata=6,
        m2='Sí',
        usb=10,
        hdmi=1,
        controlador_red='Sí',
        controlador_sonido='Sí',
        PCIex1='Sí',
        PCIex2='No',
        PCIex4='No',
        PCIex8='No',
        PCIex16='Sí'
    )
    assert placabase.marca == 'ASUS'
    assert placabase.modelo == 'ROG STRIX B550-F'
    assert placabase.precio == 200.00
    assert placabase.vendedor == 'Vendedor5'
    assert placabase.formato == 'ATX'
    assert placabase.gama == 'Media'
    assert placabase.socket == 'AM4'
    assert placabase.ram_compatible == 'DDR4'
    assert placabase.ram == 4
    assert placabase.sata == 6
    assert placabase.m2 == 'Sí'
    assert placabase.usb == 10
    assert placabase.hdmi == 1
    assert placabase.controlador_red == 'Sí'
    assert placabase.controlador_sonido == 'Sí'
    assert placabase.PCIex1 == 'Sí'
    assert placabase.PCIex2 == 'No'
    assert placabase.PCIex4 == 'No'
    assert placabase.PCIex8 == 'No'
    assert placabase.PCIex16 == 'Sí'

@pytest.mark.django_db
def test_create_fuente_alimentacion():
    fuente_alimentacion = FuenteAlimentacion.objects.create(
        marca='Corsair',
        modelo='RM850x',
        precio=150.00,
        vendedor='Vendedor6',
        potencia=850,
        forma='ATX',
        eficiencia='80 Plus Gold',
        tamaño='160 mm',
        peso='1.7 kg',
        atx24=1,
        eps12v=1,
        pcie16=2,
        pcie8=2
    )
    assert fuente_alimentacion.marca == 'Corsair'
    assert fuente_alimentacion.modelo == 'RM850x'
    assert fuente_alimentacion.precio == 150.00
    assert fuente_alimentacion.vendedor == 'Vendedor6'
    assert fuente_alimentacion.potencia == 850
    assert fuente_alimentacion.forma == 'ATX'
    assert fuente_alimentacion.eficiencia == '80 Plus Gold'
    assert fuente_alimentacion.tamaño == '160 mm'
    assert fuente_alimentacion.peso == '1.7 kg'
    assert fuente_alimentacion.atx24 == 1
    assert fuente_alimentacion.eps12v == 1
    assert fuente_alimentacion.pcie16 == 2
    assert fuente_alimentacion.pcie8 == 2

@pytest.mark.django_db
def test_create_almacenamiento():
    almacenamiento = Almacenamiento.objects.create(
        marca='Samsung',
        modelo='970 EVO Plus',
        precio=120.00,
        vendedor='Vendedor7',
        capacidad='1 TB',
        velocidad='3500 MB/s',
        forma='M.2',
        tipo_interfaz='NVMe'
    )
    assert almacenamiento.marca == 'Samsung'
    assert almacenamiento.modelo == '970 EVO Plus'
    assert almacenamiento.precio == 120.00
    assert almacenamiento.vendedor == 'Vendedor7'
    assert almacenamiento.capacidad == '1 TB'
    assert almacenamiento.velocidad == '3500 MB/s'
    assert almacenamiento.forma == 'M.2'
    assert almacenamiento.tipo_interfaz == 'NVMe'
