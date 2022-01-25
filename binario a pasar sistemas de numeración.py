n = int(input("para calcular un numero de base 10 a otro base precione (1) o si quieres alcular otro numero a base 10 preciones(2): "))

if n==1:
    numero=int(input("ingrese el numero que esta en base 10: "))
    base=int(input("Ingrese base que le deseas remplazar : "))
    
    def imprime_digito(digito):
        if digito < 10:
            print("{:d}".format(digito), end="")
        else:
            digito_t = chr(digito - 10 + ord('A'))
            print("{}".format(digito_t), end="")
        
    def imprime_otra_base(numero, base):
        if numero > 0:
            digito = numero % base
            numero //= base
            imprime_otra_base(numero, base)
            imprime_digito(digito)

    if base >= 2 and base <= 36:
        imprime_otra_base(numero, base)


    else:
        print("Debe ingresar una base entre 2 y 36")


elif n==2:
    numero = input("ingrese el numero para pasarlo a base 10: ")
    base = int(input("ingrese la base del numero: "))
    base10 = 0
    a = []

    tam = len(numero)

    for m in range (len(numero)):
        a.append(numero[m])

    c = tam -1

    tem = 0 

    for i in range(tam):
        tem = int(a[i]) * pow(base,c)
        c = c-1
        base10 = base10 + tem
    print("le numero a numero decimal es: {} ".format(base10))

else:
    print("porfavor ingrese alguno de la seleccion ")
