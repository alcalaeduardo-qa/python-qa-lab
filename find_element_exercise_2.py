import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=es")
time.sleep(5)
# Encontrar todos los elementos <img> usando XPath
elements = driver.find_elements(By.XPATH, ".//img")

# Comprobar que el número de elementos encontrados es mayor que 1 usando len()
assert len(elements) > 1, f"Se esperaban más de 1 elemento img, pero se encontraron {len(elements)}"
print(f"Se encontraron {len(elements)} elementos <img>")

# Cerrar el navegador
driver.quit()
