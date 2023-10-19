import math

def area_cuadrado(L):
    
    area=L**2
    return  print('el area del cuadrado es: ', area)


def area_circulo(R):
    
    area=math.pi*R**2
    return print('el area del circulo es %.3f ' % area)

def area_triangulo(b,h):

    area=b*h/2
    return print('El area del triángulo es: ', area)