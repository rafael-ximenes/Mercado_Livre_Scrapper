#Importação das bibliotecas necessárias
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from openpyxl import Workbook

#Listas utilizadas para percorrer os produtos pesquisados
links = []
produtos = []

#Solicitação de produto ao usuário
produto = input('Digite o que deseja pesquisar: ').strip()

#Tratamento de texto para a pesquisa do produto
produto_tratado = produto.replace(' ', '-')

#Usando o WebDriver para aquisição dos produtos pesquisados
driver = webdriver.Edge()
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
    if preco.__contains__('com'):
        preco = preco.replace(' reais com ', ',')
        preco = preco.replace(' centavos', '')
    else:  
        preco = preco.replace(' reais', ',00')
    produtos.append({'título': titulo, 'preço': preco})

#Usando Openpyxl para criar o arquivo xlsx(Excel)
arquivo = Workbook()
pagina = arquivo.active
pagina.title = f'Mercado Livre - {produto} results'
pagina['A1'] = 'Produto'
pagina['B1'] = 'Preço'
for indice, produto in enumerate(produtos):
    pagina[f'A{indice + 2}'] = produto['título']
    pagina[f'B{indice + 2}'] = produto['preço']
arquivo.save('Mercado Livre Scrapper.xlsx')
