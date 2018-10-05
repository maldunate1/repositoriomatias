#codigo base para problema de Kattis "babelfish"
#https://open.kattis.com/problems/babelfish
import sys


def solve(word_pairs, words):
    '''
    Esta funcion toma 2 parametros:
        - lista de "pares". Cada par contiene dos strings, el primero
        es una palabra en ingles, el segundo es una palabra en idioma
        extranjero
        - una lista de palabras para traducir
    
    La funcion "solve" debe retornar una lista, con las
    palabras traducidas
    '''
    lista_palabras_traducidas = ['']*len(words)    
    for word in range(0,len(words)):
        lista_palabras_traducidas[word] = "eh"
        for diccionario in range(0, len(word_pairs)):
                if (word_pairs[diccionario][1] == words[word]):
                        lista_palabras_traducidas[word] = word_pairs[diccionario][0]
                pass
        #print(lista_palabras_traducidas[word])
        pass
    return lista_palabras_traducidas


if __name__ == "__main__":
    
    #print("Escribe los pares de palabras y para terminar apreta enter")
    line = sys.stdin.readline().strip()

    word_pairs = []
    while line != "":
        word_pairs.append(line.split())
        line = sys.stdin.readline().strip()

    #print("Escribe las palabras que quieras encontrar")
    words = []
    line = sys.stdin.readline().strip()

    while line != "":
        words.append(line.strip())
        line = sys.stdin.readline().strip()

    translated = solve(word_pairs, words)

    for w in translated:
        print(w)