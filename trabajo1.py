
# Binario a octal
b1 = input ('Ingrese un número binario:')
c1=(int(b1,10))
print ('La conversión de binario a octal es:', c1)
 # Convertir octal a binario
b2 = input ('Introduzca un número octal:')
c2=bin(int(b2,8))
print ('La conversión de octal a binario es:', c2)
 # Binario a hexadecimal
b3 = input ('Ingrese un número binario:')
c3=hex(int(b3,2))
print ('La conversión de binario a hexadecimal es:', c3)
 # Convertir hexadecimal a binario
b4 = input ('Ingrese un número hexadecimal:')
c4=bin(int(b4,16))
print ('La conversión de hexadecimal a binario es:', c4)
 # Convertir octal a hexadecimal
b5 = input ('Ingrese un número octal:')
c5=hex(int(b5,8))
print ('La conversión de octal a hexadecimal es:', c5)
 # Convertir hexadecimal a octal
b6 = input ('Ingrese un número hexadecimal:')
c6=oct(int(b6,16))
print ('La conversión de hexadecimal a octal es:', c6)