def convertir_base(numero,base): 
    conversion = "6789"  

    if numero < base:              
        return conversion[numero]  
    
    else:                                                                     
        return convertir_base(numero//base, base) + conversion[numero % base] 

numero = int(input("ingrese numero base 10:  "))
base = int(input("ingrese base que desea calcular del numero en base 10: "))
resultado = convertir_base(numero,base)
print("el resultado de la base deseado es: ",resultado)      

def binario_a_decimal(numero_binario):
	numero_decimal = 0 

	for posicion, digito_string in enumerate(numero_binario[::-1]):
		numero_decimal += int(digito_string) * 2 ** posicion

	return numero_decimal

print("el numero a binario es: ", binario_a_decimal(convertir_base(numero,base)))


