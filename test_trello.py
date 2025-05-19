from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


# Abrir o navegador
navegador = webdriver.Chrome()

# Variaveis utilizadas
wait = WebDriverWait(navegador, 10)
action = ActionChains(navegador)

# Acessar o site
navegador.get("https://trello.com/")
navegador.maximize_window()
time.sleep(2)
# #Encontrar o botão de cookies e clicar
# botao_cookies = wait.until(EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler")))
# botao_cookies.click()

# Selecionar o botão de login
botao_login = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Log In")))
botao_login.click()

# Preencher o campo de login
# Preencher o campo de email
campo_email = wait.until(EC.element_to_be_clickable((By.ID, "username")))
campo_email.send_keys("davi5555amaral@gmail.com")

# Clicar no botão de continuar
botao_continuar = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "css-178ag6o")))
botao_continuar.click()

# Preencher o campo de senha
campo_senha = wait.until(EC.element_to_be_clickable((By.ID, "password")))
campo_senha.send_keys("Davi:4424")

# Clicar no botão de Entrar
botao_entrar = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "css-178ag6o")))
botao_entrar.click()

input("Pressione Enter para continuar...")
print("Continuando...")


#Criação de uma area de trabalho
# Clicar no botão de áreas de trabalho
botao_areas_de_trabalho = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "kpv7OitsgQTIxo")))
botao_areas_de_trabalho.click()

# Clicar no botão de criar uma área de trabalho
botao_criar_trabalho = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "kgXqyT2weJmrQm")))
botao_criar_trabalho.click()

# Preencher o campo de nome da área de trabalho
nome_area_trabalho = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "t3HWXDBRL8_M30")))
nome_area_trabalho.click()
nome_area_trabalho.send_keys("Teste Selenium/Pytest")

# Escolher o tipo de trabalho
tipo_trabalho = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "css-1c8bys3-singleValue")))
tipo_trabalho.click()
time.sleep(2)
action.send_keys(Keys.ARROW_DOWN).perform()
time.sleep(1)
action.send_keys(Keys.ENTER).perform()

botao_continuar = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layer-manager-overlay"]/div/div/div/div/div[1]/form/footer/button')))
botao_continuar.click()

botao_farei_mais_tarde = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "oKVIor6Kmg9SX3")))
time.sleep(2)
botao_farei_mais_tarde.click()

input("Pressione Enter para fechar o navegador...")
print("Fechando o navegador...")
navegador.quit()