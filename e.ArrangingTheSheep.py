
# E.ArrangingTheSheep

import sys

input = sys.stdin.readline

def resolver(n,a):
    pass

def main():
    t_str = input()
    if not t_str: return # Protección por si el input está vacío
    t = int(t_str)
    
    for i in range(t):
        n = int(input())
        a = input().strip()         #eliminamos espacios o saltos de linea al ppio o al final
        print(resolver(n, a))

if __name__ == "__main__":
    main()