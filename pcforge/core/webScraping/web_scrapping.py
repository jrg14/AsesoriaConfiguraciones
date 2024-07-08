from bs4 import BeautifulSoup
import cloudscraper  
import json
import os


# Esta función realiza una solicitud HTTP a una URL especificada, obtiene el contenido HTML 
# de la página y busca dentro de él los enlaces dentro de un div con un id específico utilizando
# BeautifulSoup. Luego, devuelve una lista de enlaces sin duplicados.
def obtencion_links_neobyte(url):
    scraper = cloudscraper.create_scraper()  
    response = scraper.get(url, headers={'User-Agent': 'Mozilla/5.0'})

    if response.status_code != 200:
        print("Error al obtener la página:", response.status_code)
        exit()

    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    product_list = soup.find(id='js-product-list')
    if product_list is not None:
        products = soup.find(class_='products')
        links = products.find_all('a')
        enlaces_sin_duplicados = list(set(links))

        if len(links) == 0:
            print("No se encontraron enlaces dentro del div.")
        else:
            print("Enlaces encontrados dentro del div con id=js-product-list:")
            
    return enlaces_sin_duplicados


# Esta función realiza una solicitud HTTP a una URL especificada y devuelve un objeto 
# BeautifulSoup creado a partir del contenido HTML de la página enlazada.
def peticion_paginas(link_url):
    scraper = cloudscraper.create_scraper()  
    linked_page_response = scraper.get(link_url)

    if linked_page_response.status_code != 200:
        print(f"Error al obtener la página {link_url}: {linked_page_response.status_code}")

    linked_page_html = linked_page_response.text
    linked_page_soup = BeautifulSoup(linked_page_html, 'html.parser')

    return linked_page_soup


# Esta función toma un diccionario como argumento y lo guarda como un archivo JSON
# en el directorio especificado.
def crear_json(diccionario_principal, nombre):
    directorio = os.path.dirname(os.path.abspath(__file__))
    nombre_Archivo = nombre

    path = os.path.join(directorio, nombre_Archivo)
    with open(path, 'w') as archivo:
        json.dump(diccionario_principal, archivo)


# Esta función realiza scraping en el sitio web de neobyte.es para extraer información sobre componentes.
# Itera sobre los enlaces de la página de componentes y para cada enlace, realiza scraping de dicha página 
# para obtener información sobre el producto. La información extraída se almacena en un diccionario, donde cada 
# entrada tiene un identificador numérico como clave y la información del producto como valor.
def scrapping_neobyte():
    diccionario_principal = {}
    id_principal = 1

    # URL de la página web a scrapear
    urls = ["https://www.neobyte.es/procesadores-107",
            "https://www.neobyte.es/placas-base-106",
            "https://www.neobyte.es/memorias-ram-108",
            "https://www.neobyte.es/tarjetas-graficas-111",
            "https://www.neobyte.es/fuentes-de-alimentacion-113",
            "https://www.neobyte.es/cajas-de-ordenador-112",
            "https://www.neobyte.es/ventilacion-109",
            "https://www.neobyte.es/discos-duros-110"
            ]
    
    for url in urls:
        diccionario = {}  
        id_numerico = 1
        links = obtencion_links_neobyte(url)
        for link in links:
            link_url = link.get('href')
            if link_url != '#':
                print(link_url)
                linked_page_soup = peticion_paginas(link_url)
                
                print("Título de la página enlazada:", linked_page_soup.title.text)

                contenido = str(linked_page_soup.title.text) + ' '
                precio_actual = linked_page_soup.find(class_='current-price')
                precio = precio_actual.find('span', class_='product-price')
                contenido += precio.text.strip() + ' '

                section_content = linked_page_soup.find(class_='section-content')
                if section_content is not None:
                    product_descriptions = section_content.find_all(class_='product-description')

                    if product_descriptions is not None:
                        product_description = product_descriptions[1]
                        rte_content_div = product_description.find(class_='rte-content')

                        if rte_content_div is not None:
                            ul_elements = rte_content_div.find_all('ul')
                            
                            for ul_element in ul_elements:
                                li_elements = ul_element.find_all('li')
                                for li in li_elements:
                                    contenido += li.text.strip() + ' '

                            diccionario[id_numerico] = contenido
                            id_numerico += 1    
    
        diccionario_principal[id_principal] = diccionario
        id_principal += 1
    
    crear_json(diccionario_principal, "neobyte1.json")  
    print("WEB SCRAPING TERMINADO")


#Función para normalizar caracteres especiales del archivo scrapeado
def normalizar_neobyte():
    directorio = os.path.dirname(os.path.abspath(__file__))
    nombre_Archivo = 'neobyte1.json'
    nombre_Archivo2 = 'neobyte_normalizado1.json'

    path = os.path.join(directorio, nombre_Archivo)
    with open(path, 'r', encoding='utf-8') as f:
        json_data = f.read()

    json_data = json_data.replace('\u202f', ' ')
    data = json.loads(json_data)

    normalized_data = json.dumps(data, ensure_ascii=False)

    path2 = os.path.join(directorio, nombre_Archivo2 )
    with open(path2, 'w', encoding='utf-8') as f:
        f.write(normalized_data)

def webSraping():
    scrapping_neobyte()
    normalizar_neobyte()    

def main():
    scrapping_neobyte()
    normalizar_neobyte()


if __name__ == "__main__":
    main()

