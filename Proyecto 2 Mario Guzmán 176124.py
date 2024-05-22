print("BIENVENIDO AL PROGRAMA DE PRODUCCIÓN DE DOLORÍN")
print("0. Iniciar el programa")
print("8. Salir del programa")
principio=int(input("Ingrese el número de la opción deseada: "))
while not principio==0 and not principio==8:
    principio=int(input("ingrese un número válido: "))
while not principio ==8:
    print()
    #supervisor datos
    equipo = []
    equipo.append(["código ID", "Estación", "Nombre", "Apellido", "Fecha Nac.", "Contraseña"])
    Supervisor=[]
    opeario=[]
        #id supervisor 
    codigoidsupervisor= input("Ingrese su código id: ").upper()
    inicialsupervisor= codigoidsupervisor[0]
    inicialsupervisorupper= inicialsupervisor.upper()
    while not inicialsupervisorupper =="S":
        comodin= input("ingrese un id de supervisor: ").upper()
        inicialsupervisorupper= comodin.upper()[0]
        codigoidsupervisor= comodin
        #Estación supervisor
    Estacionsupervisor= input("ingrese su estación: ").upper()

    Estacionsupervisorupper= Estacionsupervisor.upper()
    while not Estacionsupervisorupper == "SUPERVISOR":
        Estacionsupervisorupper= input("Tiene que ser supervisor para entrar a este progama, intentelo de nuevo: ")
        Estacionsupervisor= Estacionsupervisorupper.upper()
        #nombre y apellido supervisor
    nombresupervisor= input("Ingrese su nombre: ")
    apellidosupervisor= input("ingrese su apellido: ")
        #Fecha de nacimiento del supervisor 
    fecha= input("Ingrese su fecha de nacimiento con el formato DD-MM-AAAA (sin separación ni guiones): ")
    a= fecha[0]
    a1= fecha[1]
    b= fecha[2]
    b2= fecha[3]
    c= fecha[4]
    c1= fecha[5]
    c2= fecha[6]
    c3= fecha[7]
    fechadenacimiento= str(a)+str(a1)+"-"+str(b)+str(b2)+"-"+str(c)+str(c1)+str(c2)+str(c3)
        #contraseña supervisor 
    contraseñasupervisor= input("ingrese su contraseña: ")
        #ingresar los datos del supervisor en un vector 
    Supervisor.append(codigoidsupervisor)
    Supervisor.append(Estacionsupervisor)
    Supervisor.append(nombresupervisor)
    Supervisor.append(apellidosupervisor)
    Supervisor.append(fechadenacimiento)
    Supervisor.append(contraseñasupervisor)
    #operarios


    def operarios (codigoidsupervisor, Estacionsupervisor, nombresupervisor, apellidosupervisor, fecha, contraseñasupervisor, opeario):
        codigoidsupervisor= input("Ingrese código id de operario: ").upper()
        inicialsupervisor= codigoidsupervisor[0]
        inicialsupervisorupper= inicialsupervisor.upper()
        while not inicialsupervisorupper =="O":
            comodin= input("ingrese un id de operario: ")
            inicialsupervisorupper= comodin.upper()[0]
            codigoidsupervisor= comodin.upper()
        #Estación supervisor
        Estacionsupervisor= input("ingrese su estación: ").upper()
        #nombre y apellido supervisor
        nombresupervisor= input("Ingrese su nombre: ")
        apellidosupervisor= input("ingrese su apellido: ")
        #Fecha de nacimiento del supervisor 
        fecha= input("Ingrese su fecha de nacimiento con el formato DD-MM-AAAA (sin separación ni guiones): ")
        a= fecha[0]
        a1= fecha[1]
        b= fecha[2]
        b2= fecha[3]
        c= fecha[4]
        c1= fecha[5]
        c2= fecha[6]
        c3= fecha[7]
        fechadenacimiento= str(a)+str(a1)+"-"+str(b)+str(b2)+"-"+str(c)+str(c1)+str(c2)+str(c3)
        #contraseña supervisor 
        contraseñasupervisor= input("ingrese su contraseña: ")
        #ingresar los datos del supervisor en un vector 
        opeario.append(codigoidsupervisor)
        opeario.append(Estacionsupervisor)
        opeario.append(nombresupervisor)
        opeario.append(apellidosupervisor)
        opeario.append(fechadenacimiento)
        opeario.append(contraseñasupervisor)
        return opeario
    idoperario1=""
    Estacion1=""
    nombre1=""
    apellido1=""
    fecha1=""
    contraseña1=""
    idoperario2=""
    Estacion2=""
    nombre2=""
    apellido2=""
    fecha2=""
    contraseña2=""
    idoperario3=""
    Estacion3=""
    nombre3=""
    apellido3=""
    fecha3=""
    contraseña3=""
    equipo.append(Supervisor)
    opeario2=[]
    opeario3=[]
    operarios(idoperario1,Estacion1,nombre1,apellido1,fecha1,contraseña1, opeario)
    equipo.append(opeario) 
    operarios(idoperario2,Estacion2,nombre2,apellido2,fecha2,contraseña2, opeario2)
    equipo.append(opeario2)
    operarios(idoperario3,Estacion3,nombre3,apellido3,fecha3,contraseña3, opeario3)
    equipo.append(opeario3)

        #se vuelve matriz
    texto=""
    for i in range (len(equipo)):
        for j in range (6):
            texto += str(equipo[i][j])+"\t"
        print(texto)
        texto = " "
    #Simulacíón e historial de producción 
    estaciones =[]
    estacion11= []
    estacion22=[]
    estacion33=[]
    estacion11.append(["Estación 1"])
    estacion22.append(["Estación 2"])
    estacion33.append(["Estación 3"])
    import random
    def i3 (estacion1):
        for e1 in range (5):
            numero = random.randint(75,120)
            estacion1.append(numero)
    i3(estacion11)
    i3(estacion22)
    i3(estacion33)
    estaciones.append(estacion11)
    estaciones.append(estacion22)
    estaciones.append(estacion33)
    tex=""
    for w in range (len(estaciones)):
        for ww in range (len(estacion11)):
            tex += str(estaciones[w][ww])+"\t"
        print(tex)
        tex = " "
    # control de calidad 
    print("1. Estación1")
    print("2. Estación2")
    print("3. Estación3")
    controlcalidad= int(input("ingresa el número de la estación en la cual desea pasar el control de calidad, (1 al 3): "))
    while controlcalidad<1 or controlcalidad>3:
        controlcalidad = int(input("error, ingrese un número del 1 al 3: "))
    def porcentaje (estacion11, porciento):
        x=1
        a1=0
        for pp in range (5):
            n=estacion11[x]
            a1=a1+n
            x=x+1
        productototal1 = a1*porciento
        productoxd= int(productototal1)
        totx2="la cantidad de producto total es: "+str(a1)
        print(totx2)
        totx1= "La cantidad de producto luego del control de calidad es: "+str(productoxd)
        print(totx1)
    porciento1= 0.9
    poecentaje2= 0.94
    porcentaje3= 0.97
    if controlcalidad== 1:
        porcentaje(estacion11, porciento1)
    elif controlcalidad== 2:
        porcentaje(estacion22, poecentaje2)
    else :
        porcentaje(estacion33, porcentaje3)
    #pago a operarios
    print("1. Estación1")
    print("2. Estación2")
    print("3. Estación3")
    numoperario=int(input("ingrese el número de la estación del operario para el calculo de su pago: "))
    while numoperario<1 or numoperario>3:
        numoperario = int(input("error, ingrese un número del 1 al 3: "))
    def pago (estacion11):
        x=1
        a1=0
        for pp in range (5):
            n=estacion11[x]
            a1=a1+n
            x=x+1
        notot= a1*5
        if a1>100:
            noseya= notot+15
            suma= ("El pago es de: ")+str(noseya)+"$"+"    (bono ya incluido)"
            print(suma)
        else:
            suamsi=("El pago es")+str(notot)+"$"
            print(suamsi)
    if numoperario==1:
        pago(estacion11)
    elif numoperario==2:
        pago(estacion22)
    else: 
        pago(estacion33)