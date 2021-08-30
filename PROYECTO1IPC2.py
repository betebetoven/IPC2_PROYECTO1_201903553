
import os
import graphviz
from xml.etree import ElementTree
from LinkedList import LinkedList
dom = ElementTree.parse("C:/Users/Alberto/Desktop/borar/Entrada.xml")
j = dom.findall('terreno')
d = graphviz.Digraph(filename='matriz')
miista = LinkedList()
#minuevalista = LinkedList()
milistaposicionx = LinkedList()
milistaposiciony = LinkedList()
#mpxaux = LinkedList()
#mpyaux = LinkedList()
pruebavalor = LinkedList()
pruebax = LinkedList()
pruebay = LinkedList()
def carga():
 print("OBTENIENDO INFORMACION DEL XML...")
 for n in j:
     miista.agrega(n.attrib['nombre'])
     milistaposicionx.agrega(n.attrib['nombre'])        
     milistaposiciony.agrega(n.attrib['nombre'])
     f = n.findall('posicion')
     for x in f:
         miista.agrega(x.text)
         milistaposicionx.agrega(x.attrib['x'])
         milistaposiciony.agrega(x.attrib['y'])



def verif(nombre):
        print("PROCESANDO TERRENO ESPECIFICO...")
        ahora = miista.First
        ahorax = milistaposicionx.First
        ahoray = milistaposiciony.First
        minuevalista = LinkedList()
        mpxaux = LinkedList()
        mpyaux = LinkedList()
        #minuevalista.limpia()
        #mpxaux.limpia()
        #mpyaux.limpia()
        while ahora != None:
            if str(ahora) == nombre:
                ahora = ahora.Next
                ahorax = ahorax.Next
                ahoray = ahoray.Next
                while ahora != None and -1 == str(ahora).find("terreno") :
                  minuevalista.agrega(ahora)
                  mpxaux.agrega(ahorax)
                  mpyaux.agrega(ahoray)
                  ahora = ahora.Next
                  ahorax = ahorax.Next
                  ahoray = ahoray.Next
            elif ahora!= None:
             ahora = ahora.Next
             ahorax = ahorax.Next
             ahoray = ahoray.Next
        global pruebavalor
        global pruebax
        global pruebay
        pruebavalor = minuevalista
        pruebax = mpxaux
        pruebay = mpyaux
def tamaño():
    ahorax = pruebax.First
    ahoray = pruebay.First
    while ahorax.Next != None:
        ahorax = ahorax.Next
        ahoray = ahoray.Next 
    j = [int(str(ahorax)),int(str(ahoray))]
    return(j)
    
def matrs():
    dato1 = pruebavalor.First
    x = tamaño()[0]
    y = tamaño()[1]
    print("El tamaño de la matriz es "+str(x)+" X "+str(y))
    matrix = [[0]*x for i in range(y)]
    for n in range(x):
        for m in range(y):
            matrix[m][n] = str(dato1)
            dato1 = dato1.Next
    return(matrix)
def matrsp():
    contt = 0
    x = tamaño()[0]
    y = tamaño()[1]
    matrix = [[0]*x for i in range(y)]
    for n in range(y):
        for m in range(x):
            matrix[n][m] = contt
            contt+=1
    
    return(matrix)

cont = 0 
def declararNodos(listaFila):#Aca se definen las filas al mismo nivel
    global d 
    global cont   
    
    with d.subgraph() as s:
        s.attr(rank='same')        
        for i in listaFila:
            s.node(str(cont),str(i))
            cont+=1



def apuntarNodosHorizontales(lista):#Aca se apuntan los nodos de cada fila
    global d
    contador = 0
    for i in lista:
        if contador <= len(lista) and contador >= 1:
            d.edge(str(lista[contador - 1]), str(lista[contador]),dir = 'none')
        contador += 1    

def apuntarNodosVerticales(matriz):#Aca se apuntan los nodos de cada columna
    contador1 = 0
    for i in matriz:
        contador2 = 0
        for j in i:
            if (contador2 < len(i) and contador2 >= 1 ):
                if(contador2 == 1) and contador1 < len(matriz) - 1:
                    d.edge(str(i[contador2-1]), str(matriz[contador1 + 1][contador2-1]),dir = 'none')
                if contador1 < len(matriz) - 1:
                    d.edge(str(i[contador2]), str(matriz[contador1 + 1][contador2]),dir = 'none')
            contador2 += 1
        contador1 += 1
def graficaremergencia(matriz,matrizp):
    print("PROCESANDO GRAFICA POR MEDIO DE GRAPHVIZ...")
    for i in matriz:
        declararNodos(i)

    for i in matrizp:
        apuntarNodosHorizontales(i)

    apuntarNodosVerticales(matrizp)

    d.view()



while True:
    print("Menú principal:")
    print("1.cargar archivo")
    print("2.procesar archivo")
    print("3.escribir archivo de salida")
    print("4.Mostrar datos del estudiante")
    print("5.Generar gráfica")
    print("6.salir")
    t = input()
    if t =="1":
        carga()
    elif t == "2":
        verif(input())
        tamaño()
    elif t == "3":
        print()

    elif t == "4":
        print("ALBERTO JOSÚE HERNÁNDEZ ARMAS" +"\n201903553 ")
    
    elif t == "5":
        print("")
        matriz = matrs()
        matrizp = matrsp()
    
        graficaremergencia(matriz,matrizp)
        cont = 0
        d.clear()
        for n in matriz:
            print(n)
    
    elif t == "6":
        break
        


    
    
    
    
#print(matriz.index(4))


     

