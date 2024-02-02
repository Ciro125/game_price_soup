from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#import pandas as pd
import time

# Inicializando a instancia do Chrome
service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

# Entrando num determinado site
url = "https://gg.deals/deals/"
driver.get(url)

# Encontrando elementos do HTML
titulos_elemento = driver.find_elements(By.CLASS_NAME, 'full-link')

titulos_href = []
for i in range(48):
    href = titulos_elemento[i].get_attribute('href')
    titulos_href.append(href)

# Clicando nos titulos
for titulo in titulos_href:
    driver.get(titulo)



# Fecha o Chrome
driver.quit()