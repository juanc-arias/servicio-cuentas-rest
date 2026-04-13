# Servicio REST de Consulta de Cuenta

Este proyecto implementa un servicio REST básico para consultar la información de una cuenta bancaria de forma simulada (**mockeada**), usando **Python** y **FastAPI**.

## Propósito

Este servicio fue construido como ejemplo académico de una funcionalidad que podría exponerse desde un sistema bancario legado mediante una arquitectura orientada a servicios, con el fin de mostrar una interfaz clara, desacoplada y fácil de consumir.

## Tecnologías utilizadas

- Python 3.13
- FastAPI
- Uvicorn

## Requisitos

Antes de ejecutar el proyecto, se recomienda tener instalado:

- Python 3.13 o superior
- Visual Studio Code (opcional)
- PowerShell o una terminal de comandos

## Instalación y ejecución

### 1. Clonar o descargar el proyecto

```powershell
git clone https://github.com/juan-arias/servicio-cuentas-rest.git
cd servicio-cuentas-rest
```

### 2. Crear el entorno virtual

```powershell
py -3.13 -m venv .venv
```

### 3. Activar el entorno virtual

Si PowerShell bloquea la activación, ejecutar primero:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Luego activar el entorno:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Instalar dependencias

```powershell
pip install -r requirements.txt
```

### 5. Ejecutar el servicio

```powershell
uvicorn main:app --reload
```

## Rutas para probar

### Ruta base

```text
http://127.0.0.1:8000/
```

### Documentación interactiva

```text
http://127.0.0.1:8000/docs
```

### Endpoint principal

**Método:** `GET`  
**Ruta:** `/api/cuentas/{numero_cuenta}`

**Ejemplo:**

```text
http://127.0.0.1:8000/api/cuentas/123456
```

## Ejemplo de respuesta exitosa

```json
{
  "cuenta": "123456",
  "titular": "Carlos Gómez",
  "saldo": 4250000,
  "estado": "activa",
  "moneda": "COP"
}
```

## Ejemplo de respuesta de error

Si la cuenta no existe, el servicio responde con código `404` y un mensaje similar a este:

```json
{
  "detail": "La cuenta 999999 no fue encontrada"
}
```

## Nota

La información devuelta por el servicio es simulada y no proviene de una base de datos ni de un core bancario real. Este proyecto tiene fines académicos y busca demostrar cómo una funcionalidad bancaria puede exponerse mediante una API REST.