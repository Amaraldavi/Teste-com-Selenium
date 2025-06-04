import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

@pytest.fixture
def navegador():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://trello.com/login")
    wait = WebDriverWait(driver, 15)

    campo_email = wait.until(EC.element_to_be_clickable((By.ID, "username")))
    campo_email.send_keys("davi5555amaral@gmail.com")
    driver.find_element(By.ID, "login-submit").click()

    campo_senha = wait.until(EC.element_to_be_clickable((By.ID, "password")))
    campo_senha.send_keys("Davi:4424")
    driver.find_element(By.ID, "login-submit").click()

    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "kpv7OitsgQTIxo")))

    yield driver
    driver.quit()

def abrir_criacao_area(driver):
    wait = WebDriverWait(driver, 15)
    driver.get("https://trello.com")

    botao_menu = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "kpv7OitsgQTIxo")))
    botao_menu.click()

    botao_criar = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "kgXqyT2weJmrQm")))
    botao_criar.click()

@pytest.mark.parametrize("nome, duplicado, esperado", [
    ("Projeto Inédito Selenium", False, "criado"),     # CT05
    ("", False, "erro_nome"),                          # CT06
    ("Projeto Inédito Selenium", True, "duplicado")    # CT07
])
def test_criacao_area_trabalho(navegador, nome, duplicado, esperado):
    wait = WebDriverWait(navegador, 15)
    abrir_criacao_area(navegador)

    campo_nome = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "t3HWXDBRL8_M30")))
    campo_nome.clear()
    campo_nome.send_keys(nome)

    # Escolher tipo de trabalho
    tipo_trabalho = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "css-1c8bys3-singleValue")))
    tipo_trabalho.click()
    time.sleep(2)

    # Usa ActionChains corretamente
    actions = ActionChains(navegador)
    actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()

    botao_continuar = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layer-manager-overlay"]/div/div/div/div/div[1]/form/footer/button')))
    botao_continuar.click()

    if esperado == "criado":
        assert "boards" in navegador.current_url or "workspace" in navegador.current_url
    elif esperado == "erro_nome":
        erro = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "t3HWXDBRL8_M30")))
        assert erro.get_attribute("aria-invalid") == "true"
    elif esperado == "duplicado":
        assert "workspace" in navegador.current_url or "duplicado" in navegador.page_source.lower()

    input("Teste finalizado. Aperte ENTER para continuar...")  # Pausa para ação manual

def test_redirecionamento_apos_criacao(navegador):
    wait = WebDriverWait(navegador, 15)
    abrir_criacao_area(navegador)

    campo_nome = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "t3HWXDBRL8_M30")))
    campo_nome.clear()
    campo_nome.send_keys("Redirecionamento Teste")

    botao_continuar = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layer-manager-overlay"]/div/div/div/div/div[1]/form/footer/button')))
    botao_continuar.click()
    botao_farei_mais_tarde = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "oKVIor6Kmg9SX3")))
    time.sleep(2)
    botao_farei_mais_tarde.click()
    time.sleep(3)
    assert "workspace" in navegador.current_url

    input("Teste finalizado. Aperte ENTER para continuar...")  # Pausa para ação manual
