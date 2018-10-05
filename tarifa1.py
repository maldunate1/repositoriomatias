import sys
import random

def tarifa(X,N,P):
	aux = 0
	for x in range(0,N):
		aux += X
		#print(P)
		if(aux < P[x]):
			aux = 0
		else:
			aux -= P[x]
		##print(aux)
		pass
	print(aux + X)


if __name__ == '__main__':
    
    
    X = int(sys.stdin.readline().strip())
    while X < 1 or X > 100:
    	print("haz ingresado un numero invalido para X (el plan), intenta denuevo con otro entre 1 y 100")
    	X = int(sys.stdin.readline().strip())
    	pass

    N = int(sys.stdin.readline().strip())
    while N < 1 or N > 100:
    	print("haz ingresado un numero invalido para N (el tiempo que dura el plan), intenta denuevo con otro entre 1 y 100")
    	N = int(sys.stdin.readline().strip())
    	pass    


    P = []
    for i in range(0,N):
        P.append(int(sys.stdin.readline().strip()))
        pass


    tarifa(X,N,P)
    #AQUI SE DEBEN PROCESAR X y N para calcular el saldo final
    
    # OJO QUE, DADO UN N, DEBEN LEER LAS LINEAS RESTANTES DEL ARCHIVO

    # LUEGO, SE SUGIERE CREAR UNA FUNCION QUE TOME LOS DATOS DEL PROBLEMA, y entregue el saldo final

	# FINALMENTE, SE DEBE IMPRIMIR DICHO SALDO
