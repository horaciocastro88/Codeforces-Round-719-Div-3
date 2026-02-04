
# Aceptado en Codeforces

def resolver():
	
	resultado = 'YES'
	dias = int(input())
	tareas = input()
	ultimaLetra = ''
	vector = [0] * 26
	
	i = 0
	while ( i < len(tareas) and resultado == 'YES'):
		
		if( ultimaLetra != tareas[i] ):
			vector[ord(tareas[i]) - 65] += 1
		
		ultimaLetra = tareas[i]
		
		if ( vector[ord(tareas[i]) - 65] > 1):
			resultado = 'NO'	
			
		i += 1
		
	return resultado

def main():	

	t = int(input())
	if not t: return

	for i in range(t):
		print(resolver())

# Entrada del programa

if __name__ == "__main__":
	main()
