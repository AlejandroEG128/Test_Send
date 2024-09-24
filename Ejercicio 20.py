#Ejercicio 20 Suma de los pares, impares del 1 al 100

def serie():
    try:
        #Al usar contadores es necesario declarar variables e inicializarlas a 0
        par = 0
        impar = 0
        
        #Se va a repetir 100 veces la informacion correspondiente
        for numero_del_ciclo in range(1,101):
            #1. suma de pares e impares
            if numero_del_ciclo%2==0:
                #Cuando el numero sea par
                #Operador de asignacion: +=
                par+=numero_del_ciclo
            else:
                #Cuando el numero sea impar
                impar += numero_del_ciclo
        print("La suma de los pares es: ",par)
        print("La suma de los impares es:", impar)
    except SystemError:
        print("Error en el sistema")
#Termina funcion

#Llamar funcion
serie()
