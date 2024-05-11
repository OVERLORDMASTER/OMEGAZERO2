n1 = 0
n2 = 0
resultado = 0
operation = 0

n1 = int (input("\n ingrese el  primer numero :"))
n2 = int (input("\n ingrese el  segundo numero :"))
          
while True:

    operation = int (input("\n por favor seleccione una opcion del menu \n\t"+
                    
              " (1)  sumar \n\t"+
            
              " (2)  restar \n\t"+

              " (3)  multiplicar\n\t"+

              " (4) dividir \n\t"+

              " (5) ingrese nuevos numero \n\t"+

              " (6) salir del programa \n\t"+

              " ----> " ))
    
    if operation == 1:
        resultado = n1 + n2
        print ("\n la suma del :",n1," + ",n2," = ",resultado,"\n")

    elif operation == 2:
        resultado = n1 - n2
        print ("\n la resta del :",n1," - ",n2," = ",resultado,"\n")

    elif operation == 3:
        resultado = n1 * n2
        print ("\n la multiplicacion del :",n1," x ",n2," = ",resultado,"\n")

    elif operation == 4:
        resultado = n1 / n2
        print ("\n la division del :",n1," / ",n2," = ",resultado,"\n")

    elif operation == 5:
        n1 = int (input("\n ingrese el  primer numero :"))
        n2 = int (input("\n ingrese el  segundo numero :"))

    elif operation == 6:

        break

    else:
        print("\n\t !POR FAVOR INGRESE UNA OPCION VALIDA \n")

        