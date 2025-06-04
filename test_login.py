import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

URL_TRELLO = "https://trello.com/login"

@pytest.fixture
def navegador():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(URL_TRELLO)
    yield driver
    driver.quit()

def realizar_login(navegador, email, senha=None):
    wait = WebDriverWait(navegador, 10)
    
    campo_email = wait.until(EC.element_to_be_clickable((By.ID, "username")))
    campo_email.send_keys(email)
    
    botao_continuar = navegador.find_element(By.ID, "login-submit")
    botao_continuar.click()
    
    if senha:
        try:
            campo_senha = wait.until(EC.element_to_be_clickable((By.ID, "password")))
            campo_senha.send_keys(senha)
            navegador.find_element(By.ID, "login-submit").click()
        except:
            pass  # Campo de senha não apareceu — email inválido

@pytest.mark.parametrize("email, senha, esperado", [
    ("davi5555amaral@gmail.com", "Davi:4424", "acesso"),                  # CT01
    ("davi5555amaral@gmail.com", "senha_incorreta", False),               # CT02
    ("emailinexistente@teste.com", "email_nao_encontrado", False)         # CT03
])
def test_login(navegador, email, senha, esperado):
    realizar_login(navegador, email, senha)
    wait = WebDriverWait(navegador, 10)
    
    if esperado == "acesso":
        assert "boards" in navegador.current_url or "trello.com" in navegador.current_url
    elif esperado == "senha_incorreta":
        erro = wait.until(EC.visibility_of_element_located((By.ID, "password")))
        assert "senha" in erro.text.lower()
    elif esperado == "email_nao_encontrado":
        erro = wait.until(EC.visibility_of_element_located((By.ID, "")))
        assert "não" in erro.text.lower()
