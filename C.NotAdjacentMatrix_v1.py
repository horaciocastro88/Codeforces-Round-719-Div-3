
# C.NotAdjacentMatrix_v1

def resolver():
    
    n_str = input()
    n = int(n_str)

    if ( n == 1):
        return [[1]]

    if ( n == 2):
        return [[-1]]

    cant_elem = n * n

    pares = list(range(2, cant_elem + 1, 2))

    impares = list(range(1, cant_elem + 1, 2))

    todos = impares + pares

    resultado = []

    k = 0
    for i in range(n):
        fila = []
        for j in range(n):
            fila.append(todos[k])
            k += 1
        resultado.append(fila)

    return resultado

def formato_matriz(matriz):
        
        for fila in matriz:
            print(*fila)


def main():

    t_str = input()
    if not t_str:
        return
    t = int(t_str)

    for i in range (t):
        formato_matriz(resolver())
        #input()         para frenar la ejecucion, en caso de ser necesario

if __name__ == "__main__":
    main()    