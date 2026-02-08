
# D.SameDifferences

import sys

input = sys.stdin.readline

def resolver(n, vector):
    
    print(n)
    print(vector)

def main():

    t_str = input()
    if not t_str: return

    t = int(t_str)
    
    for i in range(t):
        # carga de datos
        n = int(input())
        vector = [0] * n
        for j in range(n):
            vector[j] = int(input())
            
        print(resolver(n, vector))
        input()         # frenar la ejecucion si lo necesitamos

if __name__ == "__main__":
    main()