from werkzeug.security import generate_password_hash, check_password_hash

def hash_password(password):
    return generate_password_hash(password)

def verify_password(hashed_password, plain_password):
    return check_password_hash(hashed_password, plain_password)

def validar_datos(datos):
    usuario = datos.get("usuario")
    contraseña = datos.get("contraseña")
    if not usuario or not contraseña:
        return False
    return True
