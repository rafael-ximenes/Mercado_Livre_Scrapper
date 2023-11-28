# Importação das bibliotecas necessárias
from selenium import webdriver
from selenium.webdriver.common.by import By
from msedge.selenium_tools import Edge, EdgeOptions
from time import sleep
import pandas as pd

# Listas utilizadas para percorrer os produtos pesquisados
links = []
produtos = []

# Solicitação de produto ao usuário
produto = input('Digite o que deseja pesquisar: ').strip()

# Tratamento de texto para a pesquisa do produto
produto_tratado = produto.replace(' ', '-')

# Usando o WebDriver para aquisição dos produtos pesquisados
# Tenho problemas usando Selenium no meu PC, então preciso especificar o caminho.
path = r"C:/Users/deimo/Desktop/Global_Weather/msedgedriver.exe"
#EdgeOptions é para ficar mais fácil customizar, aqui estou usando Chromium e abrindo o navegador sem ele aparecer, tem como abrir em privado também, é para customizar apenas
options = EdgeOptions()
options.use_chromium = True
options.add_argument("--headless")
driver = Edge(executable_path=path, options=options)

driver.get(f'https://lista.mercadolivre.com.br/{produto_tratado}')

sleep(2)
elementos = driver.find_elements(By.XPATH, '//*/div[2]/div[1]/div/a')
for elemento in elementos:
    links.append(elemento.get_attribute('href'))
if len(links) == 0:
    elementos = driver.find_elements(By.XPATH, '//*[@id="root-app"]/div/div[2]/section/ol/li/div/div/div[2]/div[1]/a[1]')
    for elemento in elementos:
        links.append(elemento.get_attribute('href'))
for link in links:
    driver.get(link)
    sleep(1)
    titulo = driver.find_element(By.TAG_NAME, 'h1').text
    preco = driver.find_element(By.CSS_SELECTOR, 'div.ui-pdp-price__second-line > span > span:nth-child(1)').text
    # \n bugando a visualização no excel, tentando eliminar o problema
    preco = preco.replace('\n', '')
    # Valor vindo repetido "749,55R$749,55" usando o if preco "#if preco.__contains__('com'):"
    preco = "R$" + preco.split("R$")[1].strip()  # Mantendo apenas o valor depois do primeiro "R$"
    #if preco.__contains__('com'):
    #    preco = preco.replace(' reais com ', ',')
    #    preco = preco.replace(' centavos', '')
    #else:  
    #    preco = preco.replace(' reais', ',00')

    produtos.append({'título': titulo, 'preço': preco})

# Tive problemas ao visualizar a planilha criada pelo openpyxl, valores repetidos e prompt to excel tentando recuperar alguns valores
# Usando pandas para criar o arquivo xlsx(Excel)
df = pd.DataFrame(produtos)
df.to_excel('Mercado Livre Scrapper.xlsx', index=False)