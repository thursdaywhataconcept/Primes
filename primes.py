# Lista los divisores de un numero
def Divisores(num):
	lista = []
	for i in range(1,num+1):
		if num%i == 0:
			lista.append(i)
		else:
			continue
	return lista

# Determina si un numero es primo
def PI(n):
	out = True
	div = Divisores(n)
	if len(div) != 2:
		out = False
	return out 

# -----------------------------------------------
while True:
	try: 
		entry = int(input("\nWrite an integer number: "))
		if entry < 0:
			entry *= -1
			print("\nThe number was changed to", entry)
		if entry == 0:
			print("\nZero is not a prime number.\n")
			break
		if entry == 1:
			print("\nOne is not a prime number.\n")
			break
		print("\n --> Is {} prime?".format(entry), PI(entry))
		print(" --> Positive divisors:", Divisores(entry))
		print()
		break
	except:
		print("\nSomething's wrong. Try again.")
		
