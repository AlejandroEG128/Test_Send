#Ejercicio 14 - Mayor de 3 numeros

#Funcion
def mayor_dos_numeros():
    try:
        #Declaramos variables
        #Solicitamos el ingreso de informacion
        #Y convertimos
        numero1= int(input("Ingresa el primer numero: "))
        numero2=int(input("Ingresa el segundo numero: "))
        numero3=int(input("Ingresa el tercer numero: "))
        
        #Validar que los numeros sean iguales
        if numero1 == numero2 == numero3:
            return "Los numeros son iguales"
        #Validar que uno de los numeros es igual 0
        # And V and V = V
        # Or V or V = V
        # Or V of F = V
        elif numero1 == 0 or numero2 == 0 or numero3 ==0 :
            return "Alguno(s) de los numeros es 0"
        #Mayor o menor 
        else:
            #Validar el mayor de dos numeros
            if numero1 > numero2 and numero1 > numero3:
                return "El numero 1 es mayor: ", numero1
            elif numero2 > numero1 and numero2 > numero3:
                return "El numero 2 es mayor: ", numero2
            else:
                return "El numero 3 es mayor: ", numero3
    except ValueError:
        return "Error: No puedes ingresar cadena de texto"    
#Termina funcion

#Llamada a la funcion
resul=mayor_dos_numeros()
#Imprimimos resultado por return
print(resul)
