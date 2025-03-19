print("Hola Mundo!!")
print("Hola mundo al final")

# ------- Tipos de Comentarios--------

# sirve para hacer un comentario sobre el código aclarando algún punto ambiguo
print("Hola Mundo") # Este comentario es para aclarar algo del código inmediatamente anterior

#print("Hola mundo")

# --------------------------------------
# Sección donde se hará x cosa
# --------------------------------------


def mi_funcion():
    """
    Esta función va a hacer algo específico y acá lo estoy aclarando
    """
    pass
# --------------- FIN --------------


# ---------------- SINTAXIS DE PYTHON ----------------

# Se refiere a las reglas que se deben seguir al escribir el código para que sea válido y puede ser interpretado correctamente

# La identación es el "espacio en blanco" llamado tabulación o sangría al comienzo de una línea de código
# El scope/ alcance de una estructura no se delimitará por llaves como otros lenguajes sino a través de la indentación

#---------------------
# for i in range(5):
#     print(i)
#---------------------
#print(i)


# --------------- VARIABLES ------------
# Contenedores que almacenan datos que pueden cambiar durante la ejecución de un programa.
# Cada variable tiene un nombre único y un valor asociado
# Para poder asignarle ese valor se utiliza el operador =

x = 5
nombre = "Juan"
y = str(x) #casteo (cambiar de tipo de formato)

print(x)
print(nombre)
print(y)
        
# Nombres que estan permitidos y no
# VALIDO: Si comienza con una letra y sin carateres especiales
mivariable = "Texto"

# VALIDO: Si comienza con una letra y con guiones bajos intermedios
mi_variable = "Texto"

# VALIDO: Podemos comenzar con _
_mi_variable = "Texto"

# VALIDO: camelCase que es utilizar mayúsculas al comenzar cada palabra salvo la primera
miVariable = "Texto"

# VALIDO: Puede comenzar y ser todo mayúscula
MIVARIABLE = "Texto"

# VALIDO: Podemos utilizar números pero no al comienzo
mivariable2 = "Texto"

# NO VALIDO: Comenzar con números
# 2mivariable = "Texto"

# # NO VALIDO: Usar guión medio 
# mi-varible = "Texto"

# # NO VALIDO: Usar espacios
# mi variable = "Texto"

# # NO VALIDO: Usar símbolo $
# $mivariable = "Texto"

#------------- FIN VARIABLES ---------

# ------------ TIPOS DE DATOS ---------
#-----------
# TEXTO:
#-----------

# - str (cadena de caracteres)
texto = "Cadena de caracteres"

#------------
#NUMERICOS
#------------

# - int(entero)
numero_entero = 10

# - float(flotante)
numero_flotante = 3.14

# complex(complejo)
numero_complejo = 2 + 3j

#------------
#SECUENCIA
#------------

# - list(lista) [colección ordenada y mutable]
lista = [1,2,3,4]

# - tuple(tupla) [colección ordenada e inmutable]
tupla = (1,2,3)

# - range(rango) [secuencia inmutable de números]
rango = range(0,10)

#------------
# MAPPING TYPE (MAPEO)
#------------

# - dict(diccionario) [colección no ordenada de pares clave-valor]
diccionario = {  
    "nombre": "Jose",
    "edad": 19
    }

#------------
#SET TYPE (CONJUNTO)
#------------

# - set(conjunto) [colección no ordenada y mutable de elementos UNICOS (no permite repetir)]
conjunto = {1,2,3,4}

# - frozenset(conjunto inmutable) [conjunto inmutable]
conjunto_inmutable = frozenset({1,2,3,4})

#------------
#BOOLEAN TYPES (BOOLEANO)
#------------

# - boolean [puede ser verdadero o falso]
booleano = True
booleano2 = False

#------------
#BINARY TYPES (BINARIO)
#------------

# - bytes [representa una secuencia inmutable de bytes]
bytes_data = b"datos"

# - bytearray(array de bytes) [una secuencia mutable de bytes]
bytearray_data = bytearray(b"datos")

# - memoryview(vista de memoria) [permite acceder a la memoria de objetos de bytes sin hacer una copia]
memoria = memoryview(b"datos")

#------------
#NONE/NULL (NULO)
#------------

# NoneType(nulo) [representa la ausencia de valor o la no definición]
nulo = None

# ---------- FIN TIPOS DE DATOS ---------



# -------- CASTEO --------
# Texto (str)
variable1 = "Texto"
variable2 = "123456"
variable3 = "Texto123"

# Numerico (int, float, complex)

variable4 = 10
variable5 = 2.5
variable6 = 1j

# casteo de str a int
variableCasteada = int(variable2)

# casteo de int a str
variableCasteada2 = str(variable4)

print(type(variable1)) #<class 'str'>
print(type(variableCasteada)) #<class 'str'>
print(type(variable3)) #<class 'str'>
print(type(variableCasteada2)) #<class 'int'>
print(type(variable5)) #<class 'float'>
print(type(variable6)) #<class 'complex'>

# ¿Comó se castea? (Camnbiar de tipo de dato) tipoDeDato("el dato original")
# con type podemos saber que tipo de dato es el que estamos manejando

lista = ["manzana", "pera", "naranja"]
x = list(("manzana", "pera", "naranja"))

print(type(x))

tupla = ("manzana", "pera", "naranja")
list = list(tupla)

print(type(list))

#-------- TIPOS DE DATOS NUMERICOS --------
# x = 1 # int
# y = 2.8 # float
# z = 2j # complex

# print(type(x))
# print(type(y))
# print(type(z))

# Casteo entre entero y flotante
x = 5

y = float(x)

print(y)
print(type(y))

# Casteo de flotante a entero
x2 = 5.5

y = int(x)

print(y)
print(type(y))

# ----numero random. No se incluye el num 10---
# import random

# x = random.randrange(1,10)
# print(x)

#--numero random entre 0 y 1 tipo float--
# import random

# x2 = random.random()

# print(x2)

#--numero random enteros y se incluye el num 10--
from pickle import FALSE
import random


x3 = random.randint(1,10)

print(x3)

#-------- FIN TIPOS DE DATOS NUMERICOS --------

#-------- CADENA DE CARACTERES --------
string_comillas_simples = 'Hola Mundo!'
string_comillas_dobles = "Hola, Mundo!"
string_comillas_triples = '''Este texto puede ser 
multilinea'''
string_comillas_triples2 = """También se pueden 
utilizar multiples lineas"""

# Slicing ponemos desde un índice hasta un índice NO íncluido
txt = "Seguimos trabajando con Strings"
print(txt[-11:-1])

txt = "CUANDO ESCRIBO EN MAYUSCULA TODOS PIENSAN QUE ESTOY GRITANDO"
minusculas = txt.lower()
print(minusculas)

txt2 = "este texto es tan importante que si lo pongo en minusculas nadie le presta atención"
mayusculas = txt2.upper()
print(mayusculas)

txt3 = "          Uy! Me dejé algunos espacios antes y después de este texto!           "
textoimportante = "clave "

txt3corregido = txt3.strip()
txtcorregido2 = textoimportante.strip()

print(txt3corregido)
print(txtcorregido2)

a = "Hola"
b = "Mundo"
c = a + " " + b
print(c)

horas = 10
texto1 = "El contenido de este curso va a durar: {} horas"

print(texto1.format(horas))

horas2 = 10
clases = 60
texto2 = "El contenido de este curso va a durar {} horas y tendrá {} clases"

print(texto2.format(horas, clases))

horas3 = 10
clases2 = 60
texto3 = "El contenido de este curso va a durar {1} horas y tendrá {0} clases"

print(texto3.format(clases, horas))

# con la barra \ invertida podremos hacer "escaoe de caracteres"

text = "La mejor película que vi en mi vida es \"Corazones de Hierro(Fury)\""
print(text)

text2 = "La mejor película que vi en mi vida es: \nCorazones de Hierro(Fury)"
print(text2)

textito = "este texto esta todo en minuscula. La manzana es mi fruta favorita ¿Tienes alguna manzana? Sí, manzana"
word = "centrado"
numeros = "123456789"
print(textito.islower())
# print(textito.capitalize())
# print(textito.title())
# print(textito.count("manzana"))
# print(textito.endswith("manzana"))
# print(textito.find("manzana"))
# print(word.center(20))
# print(numeros.isdigit())
# print(numeros.isdecimal())


#---------OPERADORES--------
# Son símbolos o conjuntos de símbolos que realizan una operación específica en uno o más operandos.

#---------- TIPOS DE OPERADORES -------
# Aritmeticos
# De comparación
# Lógicos
# De asignación
# De pertenencia
# De identidad

# OPERADORES ARITMETICOS
# + para sumar
# - para rstar
# * para multiplicar
# / para dividir
# // para dividir enteros (floor division)
# % resto o módulo (modulus)
# ** exponenciación

# a = 5
# b = 4
# c = a // b
# d = a % b

# print(c) ## división de enteros
# print(d) ## el resto

# e = 3
# f = 2
# g = e ** f

# print(g)

#------OPERADORES DE ASIGNACION------
# = asignación

# x = 10
# sumatorio = 3

# x += sumatorio
# x += sumatorio
# x += sumatorio
# x += sumatorio

# y = 10
# aRestar = 2

# y -= aRestar
# y -= aRestar
# y -= aRestar
# y -= aRestar

# z = 10
# aMultiplicar = 2

# z *= aMultiplicar
# z *= aMultiplicar
# z *= aMultiplicar
# z *= aMultiplicar

# q = 800
# aDividir = 2

# q /= aDividir
# q /= aDividir
# q /= aDividir
# q /= aDividir

# f = 2
# aExponer = 2

# f **= aExponer
# f **= aExponer
# f **= aExponer
# f **= aExponer

# print(x)
# print(y)
# print(z)
# print(q)
# print(f)

#----OPERADORES DE COMPARACION-----
# No es lo mismo usar el = para asignar que dos ==
# == nos va a servir para comparar igualdad
# ! es la negación (ampliaremos)
# != nos sirve para comparar diferencia
# > mayor
# < menor
# >= mayor o igual
# <= menor o igual
# x = 5
# y = 5

# print(x == y)

#--------OPERADORES LOGICOS--------
# and nos va a devolver verdadero si y solo si ambas afirmaciones son verdaderas
# or nos va a devolver verdadero si alguna de las dos afirmaciones es verdaderas
# not nos devolvera el lo opuesto al valor que siga

# x = 0
# y = 5

# a = x < y #true
# b = y > x #true

# booleano = not (a and b)

# print(booleano)

#-----OPERADORES DE IDENTIDAD------
# is
# is not

# a = 5
# b = 5

# booleano2 = a is b

# print(booleano2)

# c = "Esto es un texto"
# d = "Esto es un texto"

# booleano3 = c == d
# print(booleano3)

# e = 10
# f = 12

# booleano4 = e is not f
# print(booleano4)

#----OPERADORES DE PERTENENCIA----
# in
# not in

# tTexto = "En este texto pondremos algunas tecnologias: Python, R, Django y TensorFLow"

# print("Django" in tTexto)
# print("JavaScript" not in tTexto)


#----ESTRUCTURAS DE CONTROL----
# if, elif, else

x = 10

if x < 0:
    print("X es un número positivo")
elif x < 0:
    print("X es un número negativo")
else:
    print("X es igual a 0")

# Quisieramos viajar internacionalmente

visa = False
pasaporte = False

if visa and pasaporte:
    print("Puedes ingresar al pais de destino")
elif pasaporte and not visa:
    print("Puedes ingresar sólo a los paises que no requieran visa")
else:
    print("Debes consuguir la documentación antes de viajar")

#

edad = 60

if edad < 18 or edad > 60:
    if edad < 18:
        print("No tienes edad suficiente para entrar al boliche")
    else:
        print("Por una cuestión de seguridad no se permite el ingreso de personas de más de 60 años")
elif edad >= 18 and edad <= 60:
    print("Puedes ingresar al boliche")


#-----ESTRUCTURAS DE CONTROL: BUCLES
# While(mientras...se cumpla una condición)

# contador = 0
# limite = 5
# sumatoria = 0

# while contador <= limite:
#     sumatoria += contador
#     contador += 1

# print("La suma de los números hasta: ", limite, "es:", sumatoria)


#----ESTRUCTURA DE CONTROL: FOR

for i in range(100):
    if i == 2:
        print("Paso por el número 50")

for j in range(1,10):
    print(j)


#----ESTRUCTURA DE CONTROL: Manejo de errores
# try, except, finally

# Manejo de la división por cero

a = 10
b = 5
resultado = 0
try: #Intenta hacer algo
    resultado = a/b
    print(resultado)
except ZeroDivisionError: # Si tiene un error lo maneja
    print("No se puede dividir por cero")
finally: # Se ejecuta siempre
    resultado = 0

print(resultado)

# Palabras claves dentro de la estructuras de control

# BREAK:

# contador1 = 0

# while contador1 < 5:
#     print(contador1)
#     contador1 += 1
#     if contador1 == 3:
#          continue
#     print("Imprimir por cada vuelta")

# # print(contador1)

# PASS:

edad1 = 18

if edad > 18:
    print("Puedes ingresar a esta institución")
elif edad == 18:
    pass
else:
    print("No tienes la edad suficiente para entrar aqui")