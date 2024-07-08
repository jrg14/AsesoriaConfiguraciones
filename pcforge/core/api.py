from ninja import NinjaAPI
from core.models import bd_manager
from ninja import Schema
from ninja.security import django_auth_superuser
from core.webScraping.web_scrapping import webSraping
from core.webScraping.insercion_datos import obtener_productos
from core.ensamblado.preensamblados import prensamblados
from django.http import HttpResponse
from django.http import JsonResponse
import json
from django.core.serializers import serialize
from typing import List, Dict, Any
from django.forms.models import model_to_dict
import random
from django.core.serializers.json import DjangoJSONEncoder
import os, requests
import environ
from ninja.errors import HttpError
from django.contrib.auth.models import User



api = NinjaAPI(csrf=True)
bd = bd_manager()

@api.delete("/deleteBD/", auth=django_auth_superuser, tags=['BD'])
def Delete_BD(request):
    try:
        bd.borrar_cpus()
        bd.borrar_rams()
        bd.borrar_gpus()
        bd.borrar_almacenamientos()
        bd.borrar_placas()
        bd.borrar_chasis()
        bd.borrar_fuentes()       

        return HttpResponse(status=200)
    except KeyError as e:
        return HttpResponse(status=500, content='Error en los datos recibidos: ' + str(e))
    except Exception as e:
        return HttpResponse(status=500, content='Error desconocido: ' + str(e))


@api.delete("/deleteConfiguraciones/", auth=django_auth_superuser, tags=['BD'])
def Delete_configuraciones(request):
    try:
        bd.borrar_configuraciones()      

        return HttpResponse(status=200)
    except KeyError as e:
        return HttpResponse(status=500, content='Error en los datos recibidos: ' + str(e))
    except Exception as e:
        return HttpResponse(status=500, content='Error desconocido: ' + str(e))

@api.get("/webscraping", tags=['BD'])
def web_scraping(request):
    try:
        webSraping()
        
        return HttpResponse(status=200)
    except KeyError as e:
        return HttpResponse(status=500, content='Error al realizar web scraping: ' + str(e))
    except Exception as e:
        return HttpResponse(status=500, content='Error desconocido: ' + str(e))

@api.put("/rellenarBD", tags=['BD'])
def Rellenar_BD(request):
    try:
        productos = obtener_productos()
        
        hay_cpus = bd.obtener_todas_cpus()
        hay_rams = bd.obtener_todas_rams()
        hay_gpus = bd.obtener_todas_gpus()
        hay_almacenamientos = bd.obtener_todos_almacenamientos()
        hay_placas = bd.obtener_todas_placas()
        hay_cajas = bd.obtener_todos_chasis()
        hay_fuentes = bd.obtener_todas_fuentes()

        if hay_cpus:
            bd.resetear_precio_todos_cpu()
        if hay_rams:
            bd.resetear_precio_todos_ram()
        if hay_gpus:
            bd.resetear_precio_todos_gpu()
        if hay_almacenamientos:
            bd.resetear_precio_todos_almacenamientos()
        if hay_placas:
            bd.resetear_precio_todos_placa()
        if hay_cajas:
            bd.resetear_precio_todos_chasis()
        if hay_fuentes:
            bd.resetear_precio_todos_fuente()
        
        for cpu in productos['cpus']:
            
            bd.crear_cpu(
                marca=cpu['marca'],
                modelo=cpu['modelo'],
                precio=cpu['precio'],
                vendedor=cpu['vendedor'],
                velocidad_reloj=cpu['velocidad_reloj'],
                num_nucleos=int(cpu['num_nucleos']),
                cache=cpu['cache'],
                graficos_integrados=cpu['graficos_integrados'],
                socket=cpu['socket']
            )
        for ram in productos['rams']:
            
            bd.crear_ram(
                marca=ram['marca'],
                modelo=ram['modelo'],
                precio=ram['precio'],
                vendedor=ram['vendedor'],
                tipo=ram['tipo'],
                capacidad=ram['capacidad'],
                velocidad=ram['velocidad'],
                canales=int(ram['canales']),
                compatibilidad=ram['compatibilidad']
            )
        for gpu in productos['gpus']:
            bd.crear_gpu(
                marca=gpu['marca'],
                modelo=gpu['modelo'],
                precio=gpu['precio'],
                vendedor=gpu['vendedor'],
                tarjeta=gpu['tarjeta'],
                resolucion = gpu['resolucion'],
                memoria = gpu['memoria'],
                frecuencia = gpu['frecuencia'],
                hdmi = int(gpu['hdmi']),
                displayport = int(gpu['displayport']),
                ranura_expansion = int(gpu['ranura_expansion']),
                conectores = gpu['conectores'],
                consumo = gpu['consumo'],
                tamaño = gpu['tamaño']                
            )
        for alm in productos['almacenamientos']:
            bd.crear_almacenamiento(
                marca=alm['marca'],
                modelo=alm['modelo'],
                precio=alm['precio'],
                vendedor=alm['vendedor'],
                capacidad=alm['capacidad'],
                velocidad=alm['velocidad'],
                forma=alm['forma'],
                tipo_interfaz=alm['tipo_interfaz']
            )
        for placa in productos['placas']:
            bd.crear_placa(
                marca=placa['marca'],
                modelo=placa['modelo'],
                precio=placa['precio'],
                vendedor=placa['vendedor'],
                formato=placa['formato'],
                gama=placa['gama'],
                socket=placa['socket'],
                ram_compatible=placa['ram_compatible'],
                ram=int(placa['ram']),
                sata=placa['sata'],
                m2=placa['m2'],
                usb=int(placa['usb']),
                hdmi=int(placa['hdmi']),
                controlador_red=placa['controlador_red'],
                controlador_sonido=placa['controlador_sonido'],
                PCIex1=placa['PCIex1'],
                PCIex2=placa['PCIex2'],
                PCIex4=placa['PCIex4'],
                PCIex8=placa['PCIex8'],
                PCIex16=placa['PCIex16']
            )

        for chasis in productos['cajas']:
            bd.crear_chasis(
                marca = chasis['marca'],
                modelo = chasis['modelo'],
                precio = chasis['precio'],
                vendedor = chasis['vendedor'],
                placas = chasis['placas'],
                tamaño_gpu = chasis['tamaño_gpu'],
                bahia525 = int(chasis['bahia525']),
                bahias35 = int(chasis['bahias35']),
                bahias25 = int(chasis['bahias25']),
                ventiladores = chasis['ventiladores'],
                usb = chasis['usb'],
                audio = chasis['audio'],
                fuente_alimentacion = chasis['fuente_alimentacion'],
                tam_fuente = chasis['tam_fuente'],            
            )

        for fuente_alimentacion in productos['fuentes']:
            bd.crear_fuente(
                marca=fuente_alimentacion['marca'],
                modelo=fuente_alimentacion['modelo'],
                precio=fuente_alimentacion['precio'],
                vendedor=fuente_alimentacion['vendedor'],
                potencia=fuente_alimentacion['potencia'],
                forma=fuente_alimentacion['forma'],
                eficiencia=fuente_alimentacion['eficiencia'],
                tamaño=fuente_alimentacion['tamaño'],
                peso=fuente_alimentacion['peso'],
                atx24=int(fuente_alimentacion['atx24']),
                eps12v=int(fuente_alimentacion['eps12v']),
                pcie16=int(fuente_alimentacion['pcie16']),
                pcie8=int(fuente_alimentacion['pcie8'])
            )
        
        return HttpResponse(status=200)
    except KeyError as e:
        return HttpResponse(status=500, content='Error en los datos recibidos: ' + str(e))
    except Exception as e:
        return HttpResponse(status=500, content='Error desconocido: ' + str(e))   


@api.get("/stats", response=Dict[str, int], tags=['Obtener datos'])
def get_stats(request):
    try:
        estadisticas = bd.obtener_estadisticas()
        data = {
            "visitas": estadisticas["visitas"],
            "usuarios": bd.obtener_numero_usuarios(),
            "pcs": bd.obtener_num_configuraciones(),
            "peticiones": estadisticas["peticiones"],
            "guardadas": estadisticas["guardadas"],
            "incidencias": bd.obtener_num_incidencias(),
            "ofimatica": estadisticas["ofimatica"],
            "gaming": estadisticas["gaming"],
            "ia": estadisticas["ia"],
            "edicion": estadisticas["edicion"],
            "gama_baja": estadisticas["gama_baja"],
            "gama_media": estadisticas["gama_media"],
            "gama_alta": estadisticas["gama_alta"]
        }
        return data
    except KeyError as e:
        return HttpResponse(status=500, content='Error en las estadisticas recibidos: ' + str(e))
    except Exception as e:
        return HttpResponse(status=500, content='Error desconocido: ' + str(e))   


@api.get("/productos", tags=['Obtener datos'])
def listar_productos(request):
    try:
        almacenamiento = bd.obtener_todos_almacenamientos()
        chasis = bd.obtener_todos_chasis()
        cpu = bd.obtener_todas_cpus()
        fuente = bd.obtener_todas_fuentes()
        gpu = bd.obtener_todas_gpus()
        placa = bd.obtener_todas_placas()
        ram = bd.obtener_todas_rams()

        productos = {
            'almacenamiento': list(almacenamiento.values()),  
            'chasis': list(chasis.values()),  
            'cpu': list(cpu.values()),  
            'fuente': list(fuente.values()),  
            'gpu': list(gpu.values()),  
            'placa': list(placa.values()),  
            'ram': list(ram.values())  
        }

        return JsonResponse(productos, status=200)
    except KeyError as e:
        return HttpResponse(status=500, content='Error en los datos recibidos: ' + str(e))
    except Exception as e:
        return HttpResponse(status=500, content='Error desconocido: ' + str(e))
    

@api.put("/crearPCs/", tags=['BD'])
def Crear_PCs(request):
    try:
        pcs = prensamblados()
        
        for index, pc in enumerate(pcs):
            almacenamiento = pc[0]['id'] if isinstance(pc[0], dict) else None
            chasis = pc[1]['id'] if isinstance(pc[1], dict) else None
            cpu = pc[2]['id'] if isinstance(pc[2], dict) else None
            placa_base = pc[5]['id'] if isinstance(pc[3], dict) else None
            gpu = pc[4]['id'] if isinstance(pc[4], dict) else None
            ram = pc[6]['id'] if isinstance(pc[5], dict) else None
            fuente_alimentacion = pc[3]['id'] if isinstance(pc[6], dict) else None
            filtro = pc[7]['filtro'] if isinstance(pc[7], dict) else None
            
            precios = [
                pc[0].get('precio'),
                pc[1].get('precio'),
                pc[2].get('precio'),
                pc[3].get('precio'),
                pc[4].get('precio'),
                pc[5].get('precio'),
                pc[6].get('precio')
            ]
            
            # Check if any price is None
            if any(precio is None for precio in precios):
                validez = False
                precio = 0.0
            else:
                validez = True
                precio = sum(precios)
                precio = round(precio, 2)
                
            bd.crear_configuracion(
                usuario=1,
                filtro=filtro,
                precio=precio,
                chasis=chasis,
                placa_base=placa_base,
                cpu=cpu,
                ram=ram,
                almacenamiento=almacenamiento,
                fuente_alimentacion=fuente_alimentacion,
                gpu=gpu, 
                validez = validez             
            )
               
        return HttpResponse(status=200)
    except KeyError as e:
        return HttpResponse(status=500, content='Error en los datos recibidos: ' + str(e))
    except Exception as e:
        return HttpResponse(status=500, content='Error desconocido: ' + str(e))      
   

@api.get('/filtrar', tags=['Configuraciones'])
def obtener_configuraciones_por_filtro_y_precio(request, filtro: str, precio_min: int, precio_max: int):
    try:
        bd.actualizar_categoria_gama(filtro)
        precio_min = int(request.GET.get('precio_min', 0))
        precio_max = int(request.GET.get('precio_max', 5000))     
                    
        configuraciones = bd.obtener_configuraciones_por_filtro_y_precio(filtro, precio_min, precio_max)
        listaConfiguraciones = list(configuraciones)
        listaConfiguraciones.sort(key=lambda x: x.precio)
        configuracionesBaratas = configuraciones[:50]
        random.shuffle(configuracionesBaratas)
        configuracionesBaratas = configuracionesBaratas[:6]
        configuracionesBaratas.sort(key=lambda x: x.precio)
  
        configuraciones_serializadas = serialize('json', configuracionesBaratas, cls=DjangoJSONEncoder)

        configuraciones_json = json.loads(configuraciones_serializadas)

        return JsonResponse(configuraciones_json, status=200, safe=False)
    except KeyError as e:
        return HttpResponse(status=500, content='Error en los datos recibidos: ' + str(e))
    except Exception as e:
        return HttpResponse(status=500, content='Error desconocido: ' + str(e))



class IdsSchema(Schema):
    ids: List[int]

@api.post("/componentes/", tags=['Obtener datos'], response=Dict[str, Any])
def obtener_detalles_componentes(request, data: IdsSchema):
    ids = data.ids
    componentes = {
        "chasis": [model_to_dict(bd.obtener_chasis_por_id(id)) for id in ids if bd.obtener_chasis_por_id(id)],
        "placa_base": [model_to_dict(bd.obtener_placa_por_id(id)) for id in ids if bd.obtener_placa_por_id(id)],
        "cpu": [model_to_dict(bd.obtener_cpu_por_id(id)) for id in ids if bd.obtener_cpu_por_id(id)],
        "ram": [model_to_dict(bd.obtener_ram_por_id(id)) for id in ids if bd.obtener_ram_por_id(id)],
        "almacenamiento": [model_to_dict(bd.obtener_almacenamiento_por_id(id)) for id in ids if bd.obtener_almacenamiento_por_id(id)],
        "fuente_alimentacion": [model_to_dict(bd.obtener_fuente_por_id(id)) for id in ids if bd.obtener_fuente_por_id(id)],
        "gpu": [model_to_dict(bd.obtener_gpu_por_id(id)) for id in ids if bd.obtener_gpu_por_id(id)],
    }
    return componentes


class ChatGPTRequest(Schema):
    prompt: str

# @api.post("/chatgpt", tags=['Asistencia'])
# def chatgpt(request, data: ChatGPTRequest):
#     return JsonResponse({"message": "Este PC cuenta con un chasis elegante y espacioso que favorece una excelente circulación de aire. La placa base Gigabyte Z790 AORUS Elite AX brinda un soporte confiable para los componentes. El procesador Intel Core i9-14900KF ofrece un rendimiento de alto nivel para tareas exigentes. Con 32GB de RAM Kingston Fury Beast DDR5 5200MHz, este PC garantiza una gran capacidad de multitarea. El almacenamiento de 2TB en el Western Digital Black SN850X y la GPU MSI RTX 4080 Super Ventus 3X OC 16GB GDDR6X proporcionan una potencia y velocidad impresionantes para juegos y aplicaciones intensivas."}) 

@api.post("/chatgpt", tags=['Asistencia'])
def chatgpt(request, data: ChatGPTRequest):
    bd.actualizar_peticiones()
    env = environ.Env()
    environ.Env.read_env()
    OPENAI_API_KEY = os.environ.get('CHATGPT_KEY')

    try:
        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENAI_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "gpt-3.5-turbo",
                "messages": [{"role": "user", "content": data.prompt}],
                "max_tokens": 200 
            }
        )
        response.raise_for_status()
       
        response_data = response.json()
        message = response_data.get("choices", [{}])[0].get("message", {}).get("content", "").strip()
        return JsonResponse({"message": message})
    except requests.exceptions.RequestException as e:
        return JsonResponse({"error": str(e)}, status=500)



class SaveConfigSchema(Schema):
    config_id: int

@api.post("/save_configuration", tags=['Configuraciones'])
def save_configuration(request, payload: SaveConfigSchema):
    try:
        bd.actualizar_guardadas(1)
        bd.añadir_usuario_configuracion(request.user, configuracion_id=payload.config_id)
        return {"message": "Configuración guardada con éxito"}
    except KeyError as e:
        raise HttpError(404, "Configuración no encontrada")    


@api.post("/delete_configuration", tags=['Configuraciones'])
def delete_configuration(request, payload: SaveConfigSchema):
    try:
        bd.actualizar_guardadas(-1)
        bd.eliminar_usuario_configuracion(request.user, configuracion_id=payload.config_id)
        return {"message": "Configuración guardada con éxito"}
    except KeyError as e:
        raise HttpError(404, "Configuración no encontrada")    
    
    
@api.get("/configuraciones_usuario", tags=['Configuraciones'])
def obtener_configuraciones_usuario(request):
    try:
        configuraciones = bd.obtener_configuraciones_por_usuario(request.user)
        
        configuraciones_serializadas = serialize('json', configuraciones, cls=DjangoJSONEncoder)
        
        configuraciones_json = json.loads(configuraciones_serializadas)

        return JsonResponse(configuraciones_json, status=200, safe=False)
    except User.DoesNotExist:
        return {"error": "Usuario no encontrado"}    
    

@api.delete("/eliminar_incidencia/{id}")
def eliminar_incidencia(request, id: int):
    try:
        bd.eliminar_incidencias(id)
        return HttpResponse(status=200)
    except KeyError as e:
        return HttpResponse(status=500, content='Error en los datos recibidos: ' + str(e))
    except Exception as e:
        return HttpResponse(status=500, content='Error desconocido: ' + str(e))
