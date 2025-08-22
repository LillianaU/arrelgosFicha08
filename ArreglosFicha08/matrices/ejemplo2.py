"""_summary_
Identificadores : constanes y variables

*tipos de datos primitivos:
    booleanos, numericos, tipo textos
*tipo de datos 
 arreglos: matrices y vectores
 
*las estructura de datos es un tipo de indentificador dinamico,  tenemos los que son  de tipo 
numerocos, booleanos, textos...

listas
diccionarios
conjuntos
tuplas
pilas
colas
------------ temas avanzados --------------
arboles
nodos

"""
# creacion de una lista
lista=[1,2,3,4,5,6,7]
#      0,1,2,3,4,5,6
print(f"esta la lista origina{lista}")
listacopia=lista
print(f"lista copiada {listacopia}")
lista.append(6)
print("lista con un elemento nuevo",lista)
print(f"ver la posicion 4 es  {lista[4]}")
print(f"mostrar la ultima posicion {lista[-1]}")
# agregar un elemento en la 10 en la posicion 4 alado coloca el 10
lista.insert(4,10)
print("la nueva lista es ",lista)
## diferentes formas de eliminar valores en las lisatas el 4 de la lista
# si no lo encuetra sale error

lista.remove(4)
print("la nueva lista es ",lista)
# este elimina el ultimo elemento de la lista
lista.pop()
print("la nueva lista es ",lista)
# eliminar por indice en este caso 0
print("elimino el indoce 0",lista.pop(0))
print("la nueva lista es ",lista)
# modificar un valor de una posicion
lista[5]=123
print("la nueva lista es ",lista)
# cantidad elemento de lista
print("cantidad elementos de la lista",len(lista))
print("valor maximo de la lista",max(lista))
print("valor minimo de la lista",min(lista))
print("suma de los elementos de la lista",sum(lista))
lista3=[5.42,69,2,3,0,78,9]
lista3.sort()
lista4=lista3
print("ordenar lista",lista3)
#ordenar de mayor a menor
lista3.sort(reverse=True)
print("lista ordenada",lista3)
print("lista ordenada ",lista4)
lista4.reverse()
print(lista4)
lista4.clear()
print("lista limpia", lista4)
# tuplas no son mutables , es decir no  se puede modificar despues de creadas
tuplas=(0,4,6,0,1,4,0)
# buscar un elemento
print("el valor encontrado esta en la posicion ",tuplas.index(1))
print("CUANTAS VECES ENCUENTRA EL 0", tuplas.count(0))
lista5=list(tuplas)
lista5.append(69)
print(lista5)