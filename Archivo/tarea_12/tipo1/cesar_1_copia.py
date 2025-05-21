import random
import string

def crear_password(long=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(chars, k=long))

def crear_lista_passwords(cuantas, long=12):
    passwords = set()
    while len(passwords) < cuantas:
        nueva_pass = crear_password(long)
        if nueva_pass not in passwords:
            passwords.add(nueva_pass)
    return list(passwords)

def main():
    n = int(input("Introduce cuántas contraseñas: "))
    resultado = crear_lista_passwords(n)
    print("Contraseñas:")
    for idx, pwd in enumerate(resultado, 1):
        print(f"{idx} -> {pwd}")

if __name__ == '__main__':
    main()

