# ApiFlaskPython
 Proyecto de una API REST con Flask y SQLite para gestionar usuarios y mostrar una pantalla de bienvenida a tareas



## ✔️ Funcionalidades

- Registro de usuarios con contraseña hasheada
- Inicio de sesión con verificación
- Endpoint HTML de bienvenida a tareas
- Base de datos persistente con SQLite

## 📦 Requisitos

- Python 3.10 o superior
- pip

## 🚀 Instalación y ejecución

pip install -r requirements.txt

python servidor.py

📌 Endpoints disponibles

POST /registro
Registra un nuevo usuario.

POST /login
Inicia sesión verificando las credenciales.

GET /tareas
Muestra una página HTML de bienvenida.