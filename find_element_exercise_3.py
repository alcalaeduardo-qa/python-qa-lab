import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=es")
time.sleep(5)

# Buscar elementos por ID
email = driver.find_element(By.ID, "email")
password = driver.find_element(By.ID, "password")

# Probar el atributo placeholder para cada elemento
assert email.get_attribute('placeholder') == "Correo electrónico", f"Placeholder de email incorrecto: {email.get_attribute('placeholder')}"
assert password.get_attribute('placeholder') == "Contraseña", f"Placeholder de password incorrecto: {password.get_attribute('placeholder')}"

print("Todos los placeholders son correctos")

# Cerrar el navegador
driver.quit()
