# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 16:48:12 2020

@author: Leonardo
"""


import time
import pandas as pd

from bs4 import BeautifulSoup


# Código necessário para trabalhar com a api selenium

from selenium import webdriver

from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe')

driver = webdriver.Firefox(firefox_binary=binary, executable_path=r'C:\geckodriver-v0.28.0-win64 (1)\\geckodriver.exe')

# trabalhando com o selenium

url = "https://globoesporte.globo.com/futebol/brasileirao-serie-a/"

driver.get(url)   # Comando para abrir o mozila e imputar a url definida

time.sleep(10)

# capturando o conteúdo HTML da tabela da página 

driver.find_element_by_xpath("//*[@id='classificacao__wrapper']//article//section[1]//div//table[2]").click  # Segue o caminho do conteúdo (caminho retirado do HTML do site) e faz um click

element = driver.find_element_by_xpath("//*[@id='classificacao__wrapper']//article//section[1]//div//table[2]")  # captura o elemento tabela 

html_content = element.get_attribute('outerHTML') # captura o cógico HTML do elemento


# Parsear o conteúdo HTML - Beautifulsoup
soup = BeautifulSoup(html_content,'html.parser') # Analisa o código html do html_content e parseia
table = soup.find(name='table') # transforma o html em um dado estruturado

# Estruturar o conteúdo em um Dataframe - Pandas
df_full = pd.read_html(str(table))[0] # O método lê string portanto a tabela foi convertida em string - com str(table), volta um array (volta na posição 0) - com [0] e limita os dados a 10 registros com head(10) 

driver.quit() # comando para fechar o mozila

print(df_full)

df_full.to_excel('webscrapbras.xlsx')