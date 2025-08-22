import numpy as np
# creando una matris 2*2 = 
matriz = np.array([[1, 2], [3, 4]])# la creamos
print(matriz)# esta es la forma de mostrarla

# creamos la matriz para llenar las de ceros 
matriz1=np.zeros((3,2))
#                 f,c
# f= 3 filas y c = 2 columnas
print("\033[31m",matriz1)

# otra forma de imprimir en colores
from rich import print
# productos de matrices
matriz2 = np.array([[5, 6], [7, 8]])
matriz3= np.array([[9, 10], [11, 12]])
# el producto de una  dos matrices debe cumplir unas condiciones
#https://www.matesfacil.com/matrices/resueltos-matrices-producto.html
print("[blue]el producto de la matriz[/blue]")
producto=matriz2.dot(matriz3)
print("[blue] el resultado es[/blue]",producto)
# transpuesta de una matriz, significa que cambia el orden 
transpuesta = matriz2.T
print("[purple] la transpuesta de la matriz es[/purple]", transpuesta)
#suma de matrieces
suma = matriz2 + matriz3
print("[orange] la suma de la matriz es[/orange]", suma)
# resta de matrices
resta = matriz2 - matriz3
print("[red] la resta de la matriz es[/red]", resta)
#multiplicar por un valor escarlar de una matris 3 * 6
matriz4 = np.array([[1,2,8,9,3,7], [3,4,5,6,7,8],[6,4,3,2,1,0]])
escalar=2
producto_escalar = matriz4 * escalar
print("[yellow] la matriz antes del escalar es[/yellow]", matriz4)
print("[green] el producto escalar de la matriz es[/green]", producto_escalar)
# otra forma de hacerlo
producto_escalar2 = np.multiply(matriz4, escalar)
print("[green] el producto escalar de la matriz es[/green]", producto_escalar2)

"""otra forma de realizarla pero con ciclo for, recorriendo filas y columnas
pero antes vamos a imprimir la matriz4 usando el ciclo
"""
# shape nos da la forma de la matriz
# str nos da la forma de imprimir otra cosa es que convierte en texto
print("[yellow] el es calar es [/yellow]",)
for j in range(matriz4.shape[1]):
    columna = ""
    for i in range(matriz4.shape[0]):
        columna += str(matriz4[i, j] * escalar) + " "
    print(f"Columna {j+1}: {columna}")
# diagolal superior en matrices

n=8# tamaño filas y columnas

diagonalSuperior=np.triu(np.ones((n,n)))
# vamos a imprimir la diagonal superior de color naranja
print("[orange] esta es la diagonal[/orange]",diagonalSuperior)
matriz5=np.zeros((n,n))
print("[violet]matriz 5[/violet]", matriz5)
# esta matriz5 es la que vamos a trabajar con ciclos 
for f in range(n):
    for c in range(n):
        if c>=f:
            matriz5[f,c]=1
print("[purple]el resultado es [/purple]",matriz5)
        

