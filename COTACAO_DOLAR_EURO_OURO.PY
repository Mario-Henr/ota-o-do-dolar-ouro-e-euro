from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys

# cotação dolar

navegador = webdriver.Chrome("chromedriver.exe")
navegador.get("https://www.google.com")
navegador.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys("Cotação Dolar")
navegador.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys(Keys.ENTER)
cotacao_dolar = navegador.find_element(By.XPATH,'//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute("data-value")
print(cotacao_dolar)

# cotação Euro
navegador.get("https://www.google.com")
navegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("Cotação Euro")
navegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
cotacao_euro = navegador.find_element(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute("data-value")
print(cotacao_euro)

# cotação do ouro 
navegador.get("https://www.melhorcambio.com/ouro-hoje")
cotacao_ouro = navegador.find_element(By.XPATH, '//*[@id="comercial"]').get_attribute("value")
# transforma a vírgula em ponto
cotacao_ouro = cotacao_ouro.replace(",",".")
print(cotacao_ouro)

# fechar o navegador
navegador.quit()

 
#importar a base de dados 

import pandas as pd 

tabela = pd.read_excel("Produtos.xlsx")
display(tabela)

# 3º PASSO: Calcular os novos preçõs e salvar/exportar a base de dados

tabela.loc[tabela["Moeda"]== "Dólar", "Cotação"] = float(cotacao_dolar)
tabela.loc[tabela["Moeda"]== "Euro", "Cotação"] = float(cotacao_euro)
tabela.loc[tabela["Moeda"]== "Ouro", "Cotação"] = float(cotacao_ouro)
display(tabela)

tabela["Preço de Compra"] = tabela["Preço Original"] * tabela["Cotação"]

tabela["Preço de Venda"] = tabela ["Preço de Compra"] * tabela["Margem"]
display(tabela)