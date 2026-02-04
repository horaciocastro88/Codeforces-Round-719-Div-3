
# Algoritmo de tiempo constante, O(1)
# Aceptado

def resolver():
	
    n_str = input()
    n_int = int(n_str)
    cifras = len(n_str)

    resultado = 9 * (cifras - 1) 
    
    primer_digito  = int(n_str[0]) 
    
    ord_actual = int(str(primer_digito) * cifras)
    
    resultado += (primer_digito - 1) 
    
    if (n_int >= ord_actual):
        resultado += 1

    return resultado
 				  
   
def main():
	
    t_int = int(input())
    if not t_int: return # Protección por si el input está vacío
    
    for i in range(t_int):
        print(resolver())

if __name__ == "__main__":
    main()
