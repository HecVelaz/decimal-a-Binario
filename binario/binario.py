#numero decimal al sistema binario

num=int(input("Ingrese numero decimal:"))
#funcion que convierte decimal a binario
def binario(decim):
    binario=" "#string vacio
    while decim//2!=0 : #division entera redondeando al sgte nro entero mas pequeño
        binario= str(decim % 2)+binario #binario va tomando valores para cada ciclo , inicialmente binario=vacio
        decim=decim//2 #decim toma el siguiente valor de decim divido 2 (divsion entera)
    return str(decim)+binario#retorna el ultimo numero de la division entera y la serie de numeros 1 y 0 de los restos de la division entera
print(binario(num)) 
        
