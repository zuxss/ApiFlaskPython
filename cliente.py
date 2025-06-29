import requests

def mostrar_menu():
    print("\n1. Registrarse")
    print("2. Iniciar sesión")
    print("3. Ver bienvenida de tareas")
    print("4. Salir")

while True:
    mostrar_menu()
    opcion = input("Elige una opción: ")

    if opcion == "1":
        usuario = input("Usuario: ")
        contraseña = input("Contraseña: ")
        res = requests.post("http://127.0.0.1:5000/registro", json={"usuario": usuario, "contraseña": contraseña})
        print(res.json())

    elif opcion == "2":
        usuario = input("Usuario: ")
        contraseña = input("Contraseña: ")
        res = requests.post("http://127.0.0.1:5000/login", json={"usuario": usuario, "contraseña": contraseña})
        print(res.json())

    elif opcion == "3":
        res = requests.get("http://127.0.0.1:5000/tareas")
        print(res.text)

    elif opcion == "4":
        print("Adiós.")
        break
