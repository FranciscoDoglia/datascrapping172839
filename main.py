from scrapping import scrape_mercadolibre
from graphic import create_graphic
from alt import scrape_goog

palabra = "Funda personalizada Samsung Galaxy A24 "
df = scrape_mercadolibre(palabra, num_items=250)
create_graphic(df)
scrape_goog(palabra)

print('Automatización finalizada.')