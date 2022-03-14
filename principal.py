import math
def area_cuadrado(lado):
	area=lado**2
	print(f"El area es {area}")

def rhombusArea(d1,d2): 
    area = (d1*d2)/2
    return area
	
area_cuadrado(6) 


def area_esfera(radio):
    area=4*3.1415*(radio*radio)
    return print(f"el area de la esfera es {area}")

radio=int(input("ingrese el radio:" ))
area= area_esfera(radio)
