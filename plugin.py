# Plugin: saludo
# Author: prueva
# Description: prueva para ter
"""
libraries required
"""
from typing import Dict, Callable
import os

def main_func():
    # Ejemplo: script que solicita el nombre del usuario y muestra un saludo
    print("¡Bienvenido al script!")
    
    nombre = input("Por favor, ingresa tu nombre: ").strip()
    
    if nombre:
        print(f"Hola, {nombre} 👋. ¡Es un gusto tenerte aquí!")
    else:
        print("No ingresaste ningún nombre. 😕")

    # Simulación de una tarea adicional: cálculo simple
    try:
        edad = int(input("¿Cuántos años tienes? "))
        if edad < 0:
            print("La edad no puede ser negativa.")
        elif edad < 18:
            print("Eres menor de edad.")
        else:
            print("Eres mayor de edad.")
    except ValueError:
        print("Entrada inválida: debes ingresar un número entero.")

    print("Script finalizado. ✅")


# Ejecutar la función principal si este archivo se ejecuta directamente


"""
Main function that runs when the plugin command is called
"""
def main():
    main_func()

"""
Function that runs when the plugin is loaded
"""
def install():
    print("saludo loaded successfully")

"""
Function that registers additional plugin commands
"""
def register_commands() -> Dict[str, Callable]:
    return {
        "saludo": main_func
    }
