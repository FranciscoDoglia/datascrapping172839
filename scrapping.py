import requests
import pandas as pd
import re
from bs4 import BeautifulSoup
import openpyxl


def scrape_mercadolibre(palabra, num_items=300):
    lista_prod = []

    # Calculate the number of pages needed to scrape the desired number of items
    num_pages = (num_items - 1) // 50 + 1  # MercadoLibre displays 50 items per page

    for page in range(1, num_pages + 1):
        # Construct the URL for the current page
        url = f'https://listado.mercadolibre.com.ar/{palabra}_Desde_{(page - 1) * 50 + 1}_NoIndex_True'
        html = requests.get(url).text
        soup = BeautifulSoup(html, 'html.parser')
        articulos = soup.find_all('li', class_='ui-search-layout__item shops__layout-item')

        for articulo in articulos:
            precio = articulo.find('span', class_='andes-money-amount__fraction').text
            nombre = articulo.find('h2', class_="ui-search-item__title shops__item-title").text
            link = \
            articulo.find('a', class_="ui-search-item__group__element shops__items-group-details ui-search-link")[
                'href']
            data = {
                'Nombre': nombre,
                'Precio': float(precio.replace('.', '').replace(',', '')),
                'Link': link
            }
            lista_prod.append(data)

            # Stop if we have collected enough items
            if len(lista_prod) >= num_items:
                break

        # Stop scraping if we have collected enough items
        if len(lista_prod) >= num_items:
            break

    df = pd.DataFrame(lista_prod)
    df = df.sort_values(['Precio'], ascending=True)
    df.to_excel(f'{palabra} Data Scrapping.xlsx', index=False, engine='openpyxl')

    return df


# data_scrapped = scrape_mercadolibre("Funda Iphone 13 gris", num_items=300)

#
# def data_scrapping():
#     global df
#     palabra = "Funda Iphone 13 gris"
#     palabras = palabra.split()
#     frase_unida1 = "-".join(palabras)
#     frase_unida2 = "%20".join(palabras)
#     lista_prod = []
#     url = f'https://listado.mercadolibre.com.ar/{frase_unida1}#D[A:{frase_unida2}]'
#     html = requests.get(url).text
#     soup = BeautifulSoup(html, 'html.parser')
#     articulos = soup.find_all('li', class_='ui-search-layout__item shops__layout-item')
#     for articulo in articulos[:300]:
#         precio = articulo.find('span', class_='andes-money-amount__fraction').text
#         nombre = articulo.find('h2', class_="ui-search-item__title shops__item-title").text
#         link = articulo.find('a', class_="ui-search-item__group__element shops__items-group-details ui-search-link")[
#             'href']
#         data = {
#             'Nombre': nombre,
#             'Precio': float(precio.replace('.', '').replace(',', '')),
#             'Link': link
#         }
#         lista_prod.append(data)
#     df = pd.DataFrame(lista_prod)
#     df = df.sort_values(['Precio'], ascending=True)
#     df.to_excel(f'{palabra} Data Scrapping.xlsx', index=False, engine='openpyxl')
#     return df
#
#
# data_scrapping()
#
# #podria agregar cada valor a una lista y hacer una base de datos
# #tambien deberia poner el link, maybe consumiendo apis