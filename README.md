# QA Python Tasks - Selenium Exercises

Este proyecto contiene una serie de ejercicios de automatización de pruebas web utilizando Selenium WebDriver en Python. Los ejercicios están diseñados para aprender y practicar diferentes técnicas de localización de elementos, interacción con formularios y validaciones en el sitio web Around.

## Requisitos Previos

- Python 3.7+
- Selenium WebDriver
- Chrome Browser
- ChromeDriver

## Instalación

```bash
pip install selenium
```

## Descripción de Archivos

### Ejercicios Básicos

#### `open_and_close_page.py`
- **Descripción**: Ejercicio básico para abrir y cerrar una página web
- **Funcionalidad**: Inicia Chrome, navega a una URL y cierra el navegador
- **Conceptos aprendidos**: Configuración básica de Selenium, navegación web

#### `connect_selenium_in_pycharm.py`
- **Descripción**: Archivo de configuración para conectar Selenium en PyCharm
- **Funcionalidad**: Verifica la instalación y configuración de Selenium

#### `find_element_exercise_1.py`
- **Descripción**: Búsqueda de un elemento mediante selector CSS
- **Funcionalidad**: Encuentra el título "Iniciar sesión" usando la clase `.auth-form__title`
- **Técnicas**: `find_element()`, `By.CSS_SELECTOR`, obtención de texto

#### `find_element_exercise_2.py`
- **Descripción**: Búsqueda de múltiples elementos mediante XPath
- **Funcionalidad**: Encuentra todos los elementos `<img>` y verifica que haya más de uno
- **Técnicas**: `find_elements()`, `By.XPATH`, `assert`, `len()`

#### `find_element_exercise_3.py`
- **Descripción**: Validación de atributos de elementos
- **Funcionalidad**: Verifica los placeholders de los campos email y password
- **Técnicas**: `By.ID`, `get_attribute()`, validaciones con `assert`

### Ejercicios de Interacción

#### `сlick_on_an_element.py`
- **Descripción**: Ejercicio de hacer clic en elementos
- **Funcionalidad**: Busca y hace clic en el botón "Iniciar sesión" mediante XPath
- **Técnicas**: `click()`, `By.XPATH`, búsqueda por clase y ruta relativa

#### `filling_in_the_input_field.py`
- **Descripción**: Llenado de formularios y espera explícita
- **Funcionalidad**: Completa el formulario de inicio de sesión y espera a que cargue la página principal
- **Técnicas**: `send_keys()`, `WebDriverWait`, `expected_conditions`, verificación de URL

#### `get_text.py`
- **Descripción**: Obtención y validación de texto de elementos
- **Funcionalidad**: Inicia sesión y verifica que el botón "Cerrar sesión" contenga el texto correcto
- **Técnicas**: `text`, validaciones de texto, espera de visibilidad

#### `go_to_element.py`
- **Descripción**: Desplazamiento a elementos específicos
- **Funcionalidad**: Inicia sesión, busca el footer y lo desplaza a la vista
- **Técnicas**: `scrollIntoView()`, `execute_script()`, validación con operador `in`

### Ejercicios Prácticos Avanzados

#### `practice_exercise_1.py`
- **Descripción**: Cambio de foto de perfil
- **Funcionalidad**: Inicia sesión, accede al perfil, cambia la foto y verifica el cambio
- **Técnicas**: Manipulación de formularios, espera de atributos, validación de estilo CSS
- **URL de foto**: https://practicum-content.s3.us-west-1.amazonaws.com/new-markets/qa-sprint-7/avatarSelenium.png

#### `practice_exercise_2.py`
- **Descripción**: Gestión completa de contenido (CRUD)
- **Funcionalidad**: Agrega una nueva publicación con nombre aleatorio y luego la elimina
- **Técnicas**: Generación aleatoria, validación de estado, restauración del estado inicial
- **Características**: 
  - Genera nombres como "Tokio###" con números aleatorios
  - Verifica creación y eliminación
  - Mantiene el estado original del sitio

#### `practice_exercise_3.py`
- **Descripción**: Desplazamiento de elementos
- **Funcionalidad**: Inicia sesión y desplaza la primera tarjeta del feed a la vista
- **Técnicas**: `scrollIntoView()`, selectores CSS, espera de carga de contenido

## Estructura del Proyecto

```
qa_python_tasks-es/
├── README.md                           # Documentación del proyecto
├── open_and_close_page.py              # Ejercicio básico de navegación
├── connect_selenium_in_pycharm.py      # Configuración de Selenium
├── find_element_exercise_1.py          # Búsqueda por CSS
├── find_element_exercise_2.py          # Búsqueda múltiple por XPath
├── find_element_exercise_3.py          # Validación de atributos
├── сlick_on_an_element.py              # Ejercicio de clic
├── filling_in_the_input_field.py       # Llenado de formularios
├── get_text.py                         # Obtención de texto
├── go_to_element.py                    # Desplazamiento a elementos
├── practice_exercise_1.py              # Cambio de foto de perfil
├── practice_exercise_2.py              # Gestión de contenido
└── practice_exercise_3.py              # Desplazamiento de tarjetas
```

## Sitio Web de Pruebas

- **URL**: https://around-v1.nm.tripleten-services.com/signin?lng=es
- **Credenciales de prueba**:
  - Email: coqwerty1@mail.com
  - Password: 12345678

## Conceptos Aprendidos

### Localización de Elementos
- `By.ID`: Búsqueda por identificador único
- `By.CLASS_NAME`: Búsqueda por nombre de clase
- `By.CSS_SELECTOR`: Selectores CSS
- `By.XPATH`: Expresiones XPath
- `By.TAG_NAME`: Búsqueda por etiqueta HTML
- `By.NAME`: Búsqueda por atributo name

### Interacciones
- `click()`: Hacer clic en elementos
- `send_keys()`: Ingresar texto
- `text`: Obtener texto de elementos
- `get_attribute()`: Obtener atributos

### Esperas
- `implicitly_wait()`: Espera implícita
- `WebDriverWait()`: Espera explícita
- `expected_conditions`: Condiciones de espera

### Validaciones
- `assert`: Aserciones para pruebas
- `len()`: Conteo de elementos
- Operador `in`: Verificación de contenido

### Scripts Personalizados
- `execute_script()`: Ejecución de JavaScript
- `scrollIntoView()`: Desplazamiento a elementos

## Uso

Para ejecutar cualquier ejercicio:

```bash
python nombre_del_archivo.py
```

## Notas Importantes

- Todos los ejercicios incluyen tiempos de espera adecuados
- Las credenciales usadas son de prueba y pueden ser reemplazadas
- Los ejercicios están diseñados para ejecutarse secuencialmente
- Cada archivo es independiente y puede ejecutarse por separado

## Mejores Prácticas Implementadas

1. **Manejo de esperas**: Uso adecuado de esperas implícitas y explícitas
2. **Validaciones**: Verificación de resultados con `assert`
3. **Limpieza**: Cierre adecuado del navegador con `driver.quit()`
4. **Selectores robustos**: Uso de selectores específicos y confiables
5. **Manejo de errores**: Mensajes descriptivos en las validaciones
