# Funciones basicas

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x ,y):
    if y == 0:
        raise ValueError('No se puede dividir por cero!')
    return x / y

