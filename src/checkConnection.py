from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests

USER = "seu_usuario"
PASSWORD = "sua_senha"

def verificar_site_selenium(url):
    driver = webdriver.Chrome()  # Ou Edge, Firefox...

    try:

        driver.get(url)
        time.sleep(4)
    
        if "Aba_navegador" in driver.title:
            print(f"✅ {url} Login efetuado com sucesso, site esta OK!")
        else:
            print(f"⚠️ {url} pode estar com problemas.")
            driver.quit()
            return

        campo_user = driver.find_element(By.ID, "username")
        campo_password = driver.find_element(By.ID, "password")
        botao_login = driver.find_element(By.ID, "kc-login")

        campo_user.send_keys(USER)
        campo_password.send_keys(PASSWORD)

        botao_login.click()
        time.sleep(5)

        if "" in driver.current_url:
            print("✅ Login realizado com sucesso!")
        else:
            print("❌ Falha no login. Verifique suas credenciais.")
    
    except Exception as e:
        print(f"⚠️ Erro: {e}")
    
    try:
        resposta = requests.get(url, timeout=5)
        if resposta.status_code == 200:
            print(f"✅ {url} está ONLINE!")
        else:
            print(f"⚠️ {url} está com problema! Código: {resposta.status_code}")
    except requests.exceptions.RequestException:
        print(f"❌ {url} está OFFLINE!")

    finally:
        driver.quit()

# Testando
verificar_site_selenium("seu_site")
