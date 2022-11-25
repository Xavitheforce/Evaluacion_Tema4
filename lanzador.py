from ejercicio_Huffman import *
from ejercicio_pokemon import *
from codigo_base.arboles import *
from codigo_base.grafos import *
from random import choice, randint
from codigo_base.cola import Cola, arribo, atencion, cola_vacia
from introducir import solicitar_introducir_numero_extremo, solicitar_introducir_cadena
import csv

def ejecutar():
    #ej1
    ej = solicitar_introducir_numero_extremo("Elige que ejercicio quieres ejecutar", 1, 3)
    if ej == 1:
        tabla = [['A', 0.2], ['F', 0.17], ['1', 0.13], ['3', 0.21], ['0', 0.05], ['M', 0.09], ['T', 0.15]]
        dic_codificacion = {'A':'00', '3':'01', '1':'100', 'T':'110', 'F':'111', '0':'1010', 'M':'1011'}

        tabla = ordenar_tabla_por_probabilidad(tabla)
        bosque = []
        for elemento in tabla:
            nodo = ArbolHuffman(elemento[0], elemento[1])
            bosque.append(nodo)
        #probar a ver la tabla ordenada
        print("")
        print("Tabla ordenada:")
        print("")
        for elemento in bosque:
            print(elemento.info, elemento.valor)
        while(len(bosque) > 1):
            elemento1 = bosque.pop(0)
            elemento2 = bosque.pop(0)
            nodo = ArbolHuffman('', elemento1.valor+elemento2.valor)
            nodo.izq = elemento1
            nodo.der = elemento2
            bosque.append(nodo)
            bosque = ordenar_nodo_por_probabilidad(bosque)
        print("")
        print("Tabla para decodificar:")
        print("")
        generar_Huffman(bosque[0])
        print("")
        print("A continuación se muestra un ejemplo con el funcionamiento del árbol de Huffman:")
        cadena = "MT1AT003FAT0113MATF3010"
        print("Cadena original: ", cadena)
        codificado = codificar(cadena, dic_codificacion)
        print("Cadena codificada: ", codificado)
        print("Decodificando...")
        print("Cadena decodificada: ", decodificar(codificado, bosque[0]))
        print("Ahora, ¿quieres probar a decodificar una cadena que no sea la original?")
        print("Introduce la cadena que quieras decodificar:")
        cadena = str(input())
        for element in cadena.split():
            if element != '0' and element != '1':
                print("La cadena no es válida, debe ser binaria")
                break
        print("Decodificando...")
        print("Cadena decodificada: ", decodificar(cadena, bosque[0]))
    #ej2   
    elif ej == 2:
        '''with open("Pokemon.csv", 'r') as f:
            reader = csv.reader(f)
            nombres = [row[1] for row in reader]
        nombre = [choice(nombres) for i in range(20)]
        tipo = ['agua', 'fuego', 'tierra', 'electrico', 'acero', 'hada', 'fantasma', 'volador', 'dragon', 'veneno', 'bicho', 'planta', 'roca', 'normal', 'lucha', 'psiquico', 'siniestro', 'hielo']
        pokemondebil = ['Jolteon', 'Lycanroc', 'Tyrantum']+[choice(nombre) for i in range(5)]
        debil = ['agua', 'fuego', 'tierra', 'electrico', 'acero', 'hada', 'fantasma', 'volador', 'dragon', 'veneno', 'bicho', 'planta', 'roca', 'normal', 'lucha', 'psiquico', 'siniestro', 'hielo']+pokemondebil'''
        tipo = ['agua', 'fuego', 'tierra', 'electrico']
        debil = ['agua', 'fuego', 'tierra', 'electrico', 'Jolteon', 'Lycanroc', 'Tyrantum']
        nombre = ['Bulbasaur', 'Charmander', 'Pikachu', 'Ivysaur', 'Charmeleon', 'Charizard', 'Squirtle', 'wartortle', 'Venusaur']
        arbol_nombres = None
        arbol_tipo = None
        arbol_numero = None
        #apartado a
        for i in range (0, len(nombre)):
            pokemon = Pokemon(nombre[i], randint(1, 100), choice(tipo), choice(debil))
            arbol_nombres = insertar_nodo_pokemon(arbol_nombres, [pokemon, pokemon.nombre])
            arbol_tipo = insertar_nodo_pokemon(arbol_tipo, [pokemon, pokemon.tipo])
            arbol_numero = insertar_nodo_pokemon(arbol_numero, [pokemon, pokemon.numero])

        #apartado b
        print('Listado en orden de los pokemon por número:')
        print('')
        inorden_numero(arbol_numero)
        print('')
        nombre_pokemonabuscar = solicitar_introducir_cadena('Ingrese el nombre parcial o total del pokemon que quieres buscar')
        print('')
        print('Todos los pokemon con ese string son: ')
        print('')
        busqueda_proximidad_pokemon(arbol_nombres, nombre_pokemonabuscar)

        #apartado c
        tipo_pokemon = solicitar_introducir_cadena('Ingrese el tipo de los pokemon a buscar')
        print('')
        print('Todos los pokemon del tipo especificado son: ')
        print('')
        busqueda_proximidad_pokemon_tipo(arbol_tipo, tipo_pokemon.lower())

        #apartado d
        print('')
        print('Listado en orden creciente numérico de pokemon:')
        print('')
        inorden_numero2(arbol_numero)
        print('')
        print('Listado en orden creciente alfabético de pokemon:')
        print('')
        inorden_nombre(arbol_nombres)
        print('')
        print('Listado en orden por nivel de pokemon:')
        print('')
        por_nivel_nombre(arbol_nombres)
        print('')

        #apartado e
        print('Los pokemon debiles contra Jolteon son: ')
        busqueda_proximidad_pokemon_debilesa(arbol_nombres, 'Jolteon')
        print('')
        print('Los pokemon debiles contra Lycanroc son: ')
        busqueda_proximidad_pokemon_debilesa(arbol_nombres, 'Lycanroc')
        print('')
        print('Los pokemon debiles contra Tyrantrum son: ')
        busqueda_proximidad_pokemon_debilesa(arbol_nombres, 'Tyrantrum')
        print('')

        #apartado f
        contador = 0
        print('Listado de pokemon y su tipo:')
        print('')
        contador = inorden_tipo(arbol_nombres, contador)
        print('')
        print('Cantidad del tipo fuego:',contador)

    elif ej == 3:
        g = Grafo(dirigido=False)
        # las maravillas naturales
        g.insertar_vertice('T', datos={'tipo': 'a', 'pais': 'egipto'})
        g.insertar_vertice('Z', datos={'tipo': 'a', 'pais': 'francia'})
        g.insertar_vertice('F', datos={'tipo': 'a', 'pais': 'china'})
        g.insertar_vertice('X', datos={'tipo': 'a', 'pais': 'india'})
        g.insertar_vertice('R', datos={'tipo': 'a', 'pais': 'eeuu'})
        g.insertar_vertice('K', datos={'tipo': 'a', 'pais': 'brasil'})
        # las maravillas arquitectonicas
        g.insertar_vertice('L', datos={'tipo': 'n', 'pais': 'argentina-brasil-paragauy'})
        g.insertar_vertice('J', datos={'tipo': 'n', 'pais': 'indonesia'})
        g.insertar_vertice('I', datos={'tipo': 'n', 'pais': 'sudafrica'})
        g.insertar_vertice('M', datos={'tipo': 'n', 'pais': 'india'})
        g.insertar_vertice('S', datos={'tipo': 'n', 'pais': 'china'})
        g.insertar_vertice('Y', datos={'tipo': 'n', 'pais': 'brasil'})

        g.insertar_arista('L', 'J', 6)
        g.insertar_arista('L', 'I', 3)
        g.insertar_arista('I', 'M', 8)
        g.insertar_arista('M', 'S', 2)
        g.insertar_arista('M', 'Y', 2)
        g.insertar_arista('Y', 'I', 9)
        g.insertar_arista('T', 'X', 6)
        g.insertar_arista('T', 'F', 3)
        g.insertar_arista('T', 'R', 8)
        g.insertar_arista('F', 'X', 2)
        g.insertar_arista('F', 'R', 2)
        g.insertar_arista('X', 'Z', 9)
        g.insertar_arista('R', 'Z', 4)
        g.insertar_arista('K', 'Z', 3)
        g.insertar_arista('R', 'X', 5)


        paises = g.contar_maravillas()
        print('Los paises con una maravilla y su tipo son los siguientes:')
        print('')
        for pais in paises:
            print(pais, paises[pais])

        arbol_min = g.kruskal()
        arbol_min = arbol_min[0].split('-')
        peso_total = 0
        print('')
        print('El arbol minimo es el siguiente:')
        print('')
        for nodo in arbol_min:
            nodo = nodo.split(';')
            peso_total += int(nodo[2])
            print(f'{nodo[0]}-{nodo[1]}-{nodo[2]}')
        print('')
        print(f"El peso total del recorrido es {peso_total}")
        print('')
        print('Vamos a probar a encontrar un camino de T a Z.')
        print('')
        if g.existe_paso('T', 'Z'):
            resultados1 = g.dijkstra('T')
            camino = g.camino(resultados1, 'T', 'Z')
            print(camino)
        else:
            print('no se puede llega de T a Z')
            g.eliminar_arista('A', 'C')
            g.eliminar_vertice('C')