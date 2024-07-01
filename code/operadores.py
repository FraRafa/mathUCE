"""Operadores Python
Operadores aritméticas"""
a = 9
b = 3
suma = a + b
resta = a - b
dividir = a / b
multiplicar = a * b
division_ent = a // b
modulo = a % b
exponente = a ** b
mod_par = a % 2

if mod_par==1:
    print("El número",a,"es impar")
else : print("El número",a,"es par")

print("La suma de",a,"más",b,"es:",suma)
print("La resta de",a,"menos",b,"es:",resta)
print("La división de",a,"para",b,"es:",dividir)
print("La multiplicación de",a,"por",b,"es:",multiplicar)
print("La división entera de",a,"entre",b,"es:",division_ent)
print("El residuo de la división entre",a,"y",b,"es:",modulo)
print("La potenciación de",a,"elevado a",b,"es:",exponente)

## Operadores relacionales

a = 6
b = 7
c = 2
d = 1

print(a,"es mayor que",b,"?",a>b)
print(a,"es menor que",b,"?",a<b)
print(c,"es mayor o igual que",d,"?",c>=d)
print(c,"es menor o igual que",b,"?",c<=b)
print(a,"es diferente de",d,"?",a!=d)
print(c,"es igual a",a,"?",c==a)

"""Operdores Lógicos"""
p=5>2
q=2<1
p or q #esto significa o
p and q #esto significa y
print("P es 5>2")
print("Q es 2<1")
print("La proposicion P o Q es:", p or q)
print("La proposicion P y Q es:",p and q)
print("La proposicion de P entonces Q es:", not p or q)

#Tipos de divisiones:
#Entero:
div_ent2=27//14
print(div_ent2)
#Decimal:
div_dec2=27/14
print(div_dec2)
#Modulo:
div_modl2=27%14
print(div_modl2)

#Conversiones de expresiones
a=1
b=5
c=6
x1 =(-b) +(b**2-4*a*c)**0.5/2*a
x2 =(-b) -(b**2-4*a*c)**0.5/2*av
a=(x**(2-n))/((y*x+z)/z**(2+x))












































