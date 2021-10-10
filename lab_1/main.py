import math
import numpy as np


def cylinder_area(r: float, h: float):
    """Obliczenie pola powierzchni walca. 
    Szczegółowy opis w zadaniu 1.
    
    Parameters:
    r (float): promień podstawy walca 
    h (float): wysokosć walca
    
    Returns:
    float: pole powierzchni walca 
    """
    if r < 0 or h < 0:
        return np.NaN
    else:
        return 2 * math.pi * r**2 + 2 * math.pi * r * h


def fib(n: int):
    """Obliczenie pierwszych n wyrazów ciągu Fibonnaciego. 
    Szczegółowy opis w zadaniu 3.
    
    Parameters:
    n (int): liczba określająca ilość wyrazów ciągu do obliczenia 
    
    Returns:
    np.ndarray: wektor n pierwszych wyrazów ciągu Fibonnaciego.
    """
    if n < 1 or not isinstance(n, int):
        return None
    if n == 1:
        return np.array([1])

    fib_array = np.array([[1], [1]])
    if n == 2:
        return fib_array

    for i in range(2, n):
        fib_array = np.append(fib_array, fib_array[i - 2] + fib_array[i - 1])
    fib_nd_array = np.reshape(fib_array, (1, n))

    return fib_nd_array


def matrix_calculations(a: float):
    """Funkcja zwraca wartości obliczeń na macierzy stworzonej 
    na podstawie parametru a.  
    Szczegółowy opis w zadaniu 4.
    
    Parameters:
    a (float): wartość liczbowa 
    
    Returns:
    touple: krotka zawierająca wyniki obliczeń 
    (Minv, Mt, Mdet) - opis parametrów w zadaniu 4.
    """
    matrix = np.array([[a, 1, -a], [0, 1, 1], [-a, a, 1]])

    mt = matrix.transpose()
    mdet = np.linalg.det(matrix)
    if mdet == 0:
        minv = np.NaN
    else:
        minv = np.linalg.inv(matrix)

    return minv, mt, mdet


def custom_matrix(m: int, n: int):
    """Funkcja zwraca macierz o wymiarze mxn zgodnie 
    z opisem zadania 6.
    
    Parameters:
    m (int): ilość wierszy macierzy
    n (int): ilość kolumn macierzy  
    
    Returns:
    np.ndarray: macierz zgodna z opisem z zadania 7.
    """
    if (m < 1 or n < 1) or not isinstance(m, int) or not isinstance(n, int):
        return None

    matrix = np.zeros((m, n))
    for i in range(m):
        for j in range(n):
            if i > j:
                matrix[i][j] = i
            else:
                matrix[i][j] = j

    return matrix
