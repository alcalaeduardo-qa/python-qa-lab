# 🧪 Python QA Lab — Selenium WebDriver Exercises

![Python](https://img.shields.io/badge/Python-3.7+-blue?logo=python&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-WebDriver-green?logo=selenium&logoColor=white)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![Focus](https://img.shields.io/badge/Focus-QA%20Automation-orange)

---

## 🇬🇧 English

A hands-on collection of browser automation exercises built with **Python and Selenium WebDriver**, developed as part of a QA Engineer training program. Each script demonstrates a specific testing technique — from basic navigation to complete CRUD validation flows.

> 👨‍💻 Built by **Eduardo Alcalá** | Industrial Engineer transitioning into QA Automation  
> 🔗 [LinkedIn](https://www.linkedin.com/in/TU_PERFIL) · [Portfolio](https://github.com/alcalaeduardo-qa)

---

### 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.7+ | Core language |
| Selenium WebDriver | Browser automation |
| ChromeDriver | Chrome browser control |
| PyCharm | IDE |

---

### 📂 Exercise Overview

#### 🔰 Basic Exercises

| File | Technique | Description |
|------|-----------|-------------|
| `open_and_close_page.py` | Driver setup | Navigate to a URL and close the browser |
| `connect_selenium_in_pycharm.py` | Configuration | Verify Selenium installation |
| `find_element_exercise_1.py` | `By.CSS_SELECTOR` | Locate element by CSS class and read its text |
| `find_element_exercise_2.py` | `By.XPATH` + `find_elements()` | Find multiple elements and assert count |
| `find_element_exercise_3.py` | `By.ID` + `get_attribute()` | Validate placeholder attributes on form fields |

#### ⚙️ Interaction Exercises

| File | Technique | Description |
|------|-----------|-------------|
| `click_on_an_element.py` | `click()` + `By.XPATH` | Find and click a button |
| `filling_in_the_input_field.py` | `send_keys()` + `WebDriverWait` | Fill login form with explicit wait |
| `get_text.py` | `.text` + visibility wait | Login and validate button text |
| `go_to_element.py` | `execute_script()` + `scrollIntoView` | Scroll to footer and validate |

#### 🚀 Advanced Practice Exercises

| File | Technique | Description |
|------|-----------|-------------|
| `practice_exercise_1.py` | Attribute wait + CSS validation | Login, update profile photo, verify change |
| `practice_exercise_2.py` | Random data + CRUD + state restore | Add a post with random name and delete it |
| `practice_exercise_3.py` | CSS selector + scroll | Scroll first feed card into view |

---

### ✅ QA Best Practices Applied

- **Explicit waits** with `WebDriverWait` + `expected_conditions` — no hardcoded `sleep()`
- **Assertions** with descriptive messages for clear failure reporting
- **`driver.quit()`** in every script to ensure proper browser cleanup
- **Robust selectors** — CSS, XPath, and ID chosen by reliability per context
- **State restoration** — tests leave the app in its original state (practice_exercise_2)
- **Separation of concerns** — each file tests one specific behavior

---

### 🧠 Selenium Techniques Covered

```
Element Location:    By.ID · By.CLASS_NAME · By.CSS_SELECTOR · By.XPATH · By.TAG_NAME
Actions:             click() · send_keys() · execute_script()
Assertions:          assert · len() · in operator · get_attribute()
Waits:               implicitly_wait() · WebDriverWait · expected_conditions
Scroll:              scrollIntoView() via JavaScript
```

---

### ▶️ How to Run

```bash
# Install dependencies
pip install selenium

# Run any exercise
python find_element_exercise_1.py
```

> ⚠️ Requires Chrome browser and a compatible ChromeDriver version installed.

---

---

## 🇲🇽 Español

Colección de ejercicios de automatización de navegador con **Python y Selenium WebDriver**, desarrollados como parte de un programa de formación como QA Engineer. Cada script demuestra una técnica específica de testing, desde navegación básica hasta flujos de validación CRUD completos.

> 👨‍💻 Desarrollado por **Eduardo Alcalá** | Ingeniero Industrial en transición a QA Automation  
> 🔗 [LinkedIn](https://www.linkedin.com/in/TU_PERFIL) · [Portafolio](https://github.com/alcalaeduardo-qa)

---

### 📂 Descripción de Ejercicios

#### 🔰 Ejercicios Básicos

| Archivo | Técnica | Descripción |
|---------|---------|-------------|
| `open_and_close_page.py` | Configuración del driver | Navegar a URL y cerrar el navegador |
| `connect_selenium_in_pycharm.py` | Configuración | Verificar instalación de Selenium |
| `find_element_exercise_1.py` | `By.CSS_SELECTOR` | Localizar elemento por clase CSS y leer su texto |
| `find_element_exercise_2.py` | `By.XPATH` + `find_elements()` | Encontrar múltiples elementos y validar cantidad |
| `find_element_exercise_3.py` | `By.ID` + `get_attribute()` | Validar atributos placeholder en campos de formulario |

#### ⚙️ Ejercicios de Interacción

| Archivo | Técnica | Descripción |
|---------|---------|-------------|
| `click_on_an_element.py` | `click()` + `By.XPATH` | Encontrar y hacer clic en un botón |
| `filling_in_the_input_field.py` | `send_keys()` + `WebDriverWait` | Llenar formulario de login con espera explícita |
| `get_text.py` | `.text` + espera de visibilidad | Login y validación de texto de botón |
| `go_to_element.py` | `execute_script()` + `scrollIntoView` | Desplazarse al footer y validar |

#### 🚀 Ejercicios Prácticos Avanzados

| Archivo | Técnica | Descripción |
|---------|---------|-------------|
| `practice_exercise_1.py` | Espera de atributos + validación CSS | Login, cambio de foto de perfil y verificación |
| `practice_exercise_2.py` | Datos aleatorios + CRUD + restauración | Agregar publicación con nombre aleatorio y eliminarla |
| `practice_exercise_3.py` | Selector CSS + scroll | Desplazar primera tarjeta del feed a la vista |

---

### ✅ Buenas Prácticas de QA Implementadas

- **Esperas explícitas** con `WebDriverWait` — sin `sleep()` hardcodeado
- **Aserciones** con mensajes descriptivos para reportes de fallo claros
- **`driver.quit()`** en cada script para cierre correcto del navegador
- **Selectores robustos** — CSS, XPath e ID elegidos por fiabilidad según contexto
- **Restauración de estado** — los tests dejan la app en su estado original
- **Separación de responsabilidades** — cada archivo prueba un comportamiento específico

---

### ▶️ Cómo Ejecutar

```bash
# Instalar dependencias
pip install selenium

# Ejecutar cualquier ejercicio
python find_element_exercise_1.py
```

> ⚠️ Requiere Chrome instalado y una versión compatible de ChromeDriver.

---

## 📁 Estructura del Proyecto

```
python-qa-lab/
├── README.md
├── open_and_close_page.py
├── connect_selenium_in_pycharm.py
├── find_element_exercise_1.py
├── find_element_exercise_2.py
├── find_element_exercise_3.py
├── click_on_an_element.py
├── filling_in_the_input_field.py
├── get_text.py
├── go_to_element.py
├── practice_exercise_1.py
├── practice_exercise_2.py
└── practice_exercise_3.py
```
