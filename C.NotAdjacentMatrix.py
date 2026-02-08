
# C.NotAdjacentMatrix

def resolver():
    
    n_str = input()
    n = int(n_str)

    cant_elem = n * n
    elem = 1

    # [1,2,3][4,5,6][7,8,9]

    # por ej el primer elem no puede ser adjacente del que tiene al lado
    # y tampoco del primero de la lista siguiente

    # el quinto elemento no puede ser adjacente de los dos de su lista
    # y tampoco de de arriba,  que es el 2, y el de abajo, que es el 8.
    # en matrices mas grandes, el caso gral, es no adyacencia entre un elem
    # y otros cuatro, dos de su misma lista, uno de la anterior y otro de la posterior.

    matriz = []

    for i in range (n):
        fila = []
        for j in range (n):
            fila.append(elem)
            elem += 1
        matriz.append(fila)

    for fila in matriz:
        print(fila)
    
    input()         # Para frenar y ver la matriz

    resultado = -1

    return resultado

def main():

    t_str = input()
    if not t_str:
        return
    t = int(t_str)

    for i in range (t):
        print(resolver())

if __name__ == "__main__":
    main()    