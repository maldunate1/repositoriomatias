# codigo base para https://open.kattis.com/problems/plantingtrees

import sys


def solve(times):
    '''
    Input: una lista de enteros, cada uno representando t_i (según problema)
    Esta funcion debe retornar un entero, que corresponde
    al número de días mínimo en que se puede organizar la fiesta
    '''
    times = selectionSort(times)
    print(times)
    dia_minimo = 0

    for x in range(0,len(times)):
        if(x + times[x] + 1 > dia_minimo):
            dia_minimo = x + times[x] + 1
        pass
    return dia_minimo + 1

def selectionSort(alist):
    for fillslot in range(len(alist)-1,0,-1):
        positionOfMin=0
        for location in range(1,fillslot+1):
            if alist[location]<alist[positionOfMin]:
                positionOfMin = location

        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMin]
        alist[positionOfMin] = temp
    return alist


if __name__ == "__main__":
    print("Insert the quantity of seeds and then in how much time each of the trees grows: ")
    n = int(sys.stdin.readline().strip())
    tokens = []
    for i in range(0,n):
        tokens.append(int(sys.stdin.readline().strip()))
        pass
    
    print(solve(tokens))    
    ##tokens = sys.stdin.read().strip().split()

    #n = int(tokens.pop(0))

    #times = [int(t) for t in tokens]
    #assert len(times) == n

    #print(solve(times))