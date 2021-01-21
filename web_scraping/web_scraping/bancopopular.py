import os
import sys
from bs4 import BeautifulSoup
import urllib.request

def scraping(environ, start_response):
    
    start_response('200 OK', [('Content-Type', 'text/html')])

    URL = 'https://www.bancopopular.com.co/wps/portal/bancopopular/inicio/informacion-interes/tasas'
    pagina = urllib.request.urlopen(URL)
    
    soup = BeautifulSoup(pagina, 'html.parser')
    
    # Buscamos el contenedor de la tabla
    conteneder_tabla = tabla = soup.find('div', {'class': 'table-wrap'})
    
    str_tabla = str(conteneder_tabla)
    # nos quedamos ocn el "outputHTML" de la tabla
    str_tabla = str_tabla[str_tabla.index('<table') : (str_tabla.rindex('</table>') + 1)]
    
    soup = BeautifulSoup(str_tabla, 'html.parser')
    
    tabla = soup.find('table', attrs={'class':'simple-table'})
    
    return [tabla.encode()]
    
