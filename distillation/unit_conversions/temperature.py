def Rankine_to_Kelvin(T):
    """

    :param T: temperature in Rankine
    :return: temperature in Kelvin
    """
    return T / 1.8


def Kelvin_to_Rankine(T):
    """

    :param T: temperature in Kelvin
    :return: temperature in Rankine
    """
    return T * 1.8

def Kelvin_to_Celsius(T):
    """

    :param T: temperature in Kelvin
    :return: temperature in Celsius
    """
    return T - 273.15

def Celcius_to_Kelvin(T):
    """

    :param T: temperature in Celsius
    :return: temperature in Kelvin
    """
    return T + 273.15