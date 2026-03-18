
# E.ArrangingTheSheep

import sys

input = sys.stdin.readline

def resolver(n,a):

    print("Esta es una prueba del 18 de marzo")
    print(a)
    print(len(a))

    if (len(a) != n):
        print("Cuidado!")
    else:
        print("Todo ok")

    vector_posiciones = [] 

    for i in range(len(a)):
        if a[i] == "*":
            vector_posiciones.append(i)
    
    print(vector_posiciones)    

    input()         # Para frenar la ejecucion
    
    return 0

def main():
    t_str = input()
    if not t_str: return # Protección por si el input está vacío
    t = int(t_str)
    
    for i in range(t):
        n = int(input())
        a = input().strip()         #eliminamos espacios o saltos de linea al ppio o al final, por ej el \n
        print(resolver(n, a))

if __name__ == "__main__":
    main()