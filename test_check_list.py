import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

EMAIL = "davi5555amaral@gmail.com"
SENHA = "Davi:4424"
URL_LOGIN = "https://trello.com/login"

@pytest.fixture
def navegador():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def login(navegador, wait):
    navegador.get(URL_LOGIN)
    wait.until(EC.element_to_be_clickable((By.ID, "username"))).send_keys(EMAIL)
    navegador.find_element(By.CLASS_NAME, "css-178ag6o").click()
    wait.until(EC.element_to_be_clickable((By.ID, "password"))).send_keys(SENHA)
    navegador.find_element(By.CLASS_NAME, "css-178ag6o").click()
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "kpv7OitsgQTIxo")))

def abrir_quadro_e_cartao(navegador, wait):
    time.sleep(1)
    btn_quadros = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div/div[2]/div/div/div/div/nav/div[3]/div/ul/li/ul/li[1]/a/span[2]')))
    btn_quadros.click()
    time.sleep(1)

    quadro = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div/div[2]/div/div/div/div/div/div/div/div[2]/div[2]/div[2]/ul/li[1]/a/div/div[1]/div')))
    quadro.click()
    time.sleep(1)

    cartao = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="board"]/li[1]/div/ol/li/div/div[1]/div[1]/span[2]/a')))
    cartao.click()
    time.sleep(1)

def checklist_existe(navegador, nome_checklist):
    try:
        xpath = f"//h3[@data-testid='checklist-title' and normalize-space(text())='{nome_checklist}']"
        WebDriverWait(navegador, 5).until(EC.presence_of_element_located((By.XPATH, xpath)))
        print(f"Checklist '{nome_checklist}' encontrada no DOM.")
        return True
    except:
        print(f"Checklist '{nome_checklist}' NÃO encontrada no DOM.")
        return False

def criar_checklist(navegador, wait, nome_checklist):
    try:
        btn_checklist = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@data-testid="card-back-checklist-button"]')))
        btn_checklist.click()
        time.sleep(1)

        campo_nome = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="id-checklist"]')))
        campo_nome.clear()
        campo_nome.send_keys(nome_checklist)
        time.sleep(1)

        botao_adicionar = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="checklist-add-button"]')))
        botao_adicionar.click()
        time.sleep(1)

        return True
    except Exception as e:
        print(f"Erro ao criar checklist '{nome_checklist}': {e}")
        return False

def test_criar_checklists(navegador):
    wait = WebDriverWait(navegador, 15)
    login(navegador, wait)
    abrir_quadro_e_cartao(navegador, wait)

    checklists = ["teste 1", "teste 2"]

    todas_existem = True
    todas_criadas = True

    for checklist in checklists:
        if not checklist_existe(navegador, checklist):
            todas_existem = False
            criado = criar_checklist(navegador, wait, checklist)
            if not criado:
                todas_criadas = False
            print(f"Checklist '{checklist}' criada? {criado}")
        else:
            print(f"Checklist '{checklist}' já existe")

    if todas_existem:
        print("Checklists já existem")
    elif todas_criadas:
        print("Checklists criadas com sucesso")
