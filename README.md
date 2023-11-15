# Mercado Livre Scraper

Este é um projeto de automação Selenium em Python para extrair informações de produtos no Mercado Livre.

## Descrição

O script solicita ao usuário um produto para pesquisa, usa Selenium para acessar o Mercado Livre, coleta links e extrai informações detalhadas de cada produto, como título e preço. As informações são então armazenadas em um arquivo Excel.

## Uso
1. Clone o Repositório.
```
git clone https://github.com/RxbPythonDev/Mercado_Livre_Scrapper.git
```
2. Entre na pasta do projeto.
```
cd .\Mercado_Livre_Scrapper\
```
3. Instale as Dependências.
```
pip install -r requirements.txt
```
4. Execute o Script.
```
python ML_Scrapper.py
```
5. Insira o Produto Desejado.
6. Aguarde a Execução.

O resultado será salvo em um arquivo Excel chamado "Mercado Livre Scrapper.xlsx".

## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

## Importante
1. O programa foi testado no dia 15/11/2023 e caso o site do Mercado Livre mude sua estrutura pode acontecer de o programa não mais funcionar.
2. O script utiliza o navegador Microsoft Edge, caso você não o tenha instalado em seu computador o script não irá funcionar. Você pode mudar o navegador utilizado na linha do código na qual o driver recebe o webdriver.Edge().
