# coding: utf8


def fizz_buzz(value):
    # Comprobamos el tipo de la variable
    tipo_de_la_variable = type(value)  # int, float, str, dict, list, etc...

    if tipo_de_la_variable not in (int, float):
        raise TypeError

    # Comprobamos que sea divisible por 5 y por 3
    if value % 3 == 0 and value % 5 == 0:
        return 'fizz buzz'
    # Comprobamos que sea divisible por 3
    if value % 3 == 0:
        return 'fizz'
    # Comprobamos que sea divisible por 5
    if value % 5 == 0:
        return 'buzz'

    return value

