usuarios = {"admin": "1234", "usuario1": "hola"}

def login():
    usuario = input("Usuario: ")
    contrasena = input("Contraseña: ")

    # Validación de credenciales
    if usuario in usuarios and usuarios[usuario] == contrasena:
        print("¡Inicio de sesión exitoso!")
    else:
        print("Usuario o contraseña incorrectos.")

login()