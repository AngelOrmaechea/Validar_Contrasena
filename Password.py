"""
Escribe una funcion llamada contrasena_valida(contrasena) que devuelva true en caso de superar las siguientes
validaciones sobre la contraseña producida por el usuario:
1- longitud entre 6 y 20 caracteres
2- debe contener al menos 1 numero
3- debe contener al menos 1 mayusculas
4- debe contener al menos 1 caracter especial
5- no puede contener espacios
caracteres especiales [$&+;:,=?@#|<>.^*()%!-]
"""
import re

usuario = input("Ingrese el nombre de usuario: ")
password = input("Ingrese una contraseña: ")


caract_esp = "[$&+;:,=?@#|<>.^*()%!-]"


def contra_valida(contra):
    if not (6 <= len(contra) <= 20):
        return False

    if not re.findall("[0-9]", contra):
        return False

    if not re.search("[A-Z]", contra):
        return False

    if not re.search(caract_esp, contra):
        return False

    if re.search(" ", contra):
        return False

    return True


print(contra_valida(password))
