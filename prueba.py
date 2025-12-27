
primer = input("Nombre?")

primLetra = primer[0]

print("Num prim letra:" , ord(primLetra))

edadStr = input("Edad:")

edadInt = int(edadStr)

#print("En 2 decadas tendras:", edadInt + 20)


salStr = input("Salario:")

salFlo = float(salStr)

#print("%10.1f" % salFlo)

print("Cantidad: %d Total: %10.2f" % ( edadInt, salFlo))
