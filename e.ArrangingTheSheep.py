
# E.ArrangingTheSheep
# Resuelto con una complejidad O(n)

# Aprobado por Codeforces

import sys

input = sys.stdin.readline

def resolver(n,a):

    costo = 0

    if n == 2:
        return costo

    vector_posiciones = [] 

    for i in range(len(a)):
        if a[i] == "*":
            vector_posiciones.append(i)

    if len(vector_posiciones) <= 1:
        return costo
    
    for i in range (len(vector_posiciones)):
        vector_posiciones[i] = vector_posiciones[i] - i

    pos_mediana = int(len(vector_posiciones) / 2)
    mediana = vector_posiciones[pos_mediana]

    for i in range(len(vector_posiciones)):
            costo = costo + (abs(vector_posiciones[i] - mediana))       # Quitamos el signo a la distancia

    #print(vector_posiciones)
    #print(mediana)    

    #input()          Para frenar la ejecucion
    
    return costo

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