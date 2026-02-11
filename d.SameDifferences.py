
# D.SameDifferences

# aprobado por Codeforces
# complejidad O(n) lineal

import sys
from collections import defaultdict

input = sys.stdin.readline

def resolver(n, vector):
    
    frecuencias = defaultdict(int)

    # aca va el calculo

    for i in range(n):
        res_resta = vector[i] - i       # optimizamos evitando un vector de ai - i
        frecuencias[res_resta] += 1
    
    pares = 0
    for f in frecuencias.values():
        pares += f * (f - 1) // 2       # usamos // 2 para mantener la vble en int
        
    return pares

def main():

    t_str = input()
    if not t_str: return

    t = int(t_str)
    
    for i in range(t):
        # carga de datos
        n = int(input())
        a = input()
        vector = list(map(int, a.split()))
            
        print(resolver(n, vector))
        #input()          frenar la ejecucion si lo necesitamos

if __name__ == "__main__":
    main()