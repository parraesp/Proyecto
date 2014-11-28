__author__ = 'alberto'
from Club import Club
from Instalacion import Instalacion

seleccion = -1
print 'Bienvenido al sistema de gestion de clubes de padel'
print '==================================================='
print "Cargando el club..."
club = Club()
print "Club cargado"
while(seleccion!=0):
    print '1. Socios'
    print '2. Reservas'
    print '3. Alquileres'
    print '4. Profesores'
    print '5. Clases'
    print '6. Torneos'
    print '0. Salir'
    seleccion = int(raw_input('Haga su seleccion: '))

    if(seleccion==1):
        print 'Haga su seleccion: '
        print '1. Crear socio'
        print '2. Editar socio'
        print '3. Dar socio de baja'
        print '4. Consultar socio'
        seleccion = int(raw_input('Haga su seleccion: '))
        if(seleccion==1):
            DNI =raw_input('DNI: ')
            nombre = raw_input('Nombre: ')
            apellidos = raw_input('Apellidos: ')
            movil = raw_input('Movil: ')
            correo = raw_input('Correo electronico: ')
            club.alta_socio(DNI,nombre,apellidos,movil,correo)
        if(seleccion==2):
            DNI = raw_input('Editar datos del socio: ')
            socio = club.obtener_socio(DNI)
            print 'Introduzca nuevos valores: '
            print socio
            nombre = raw_input('Nombre: '+str(socio.nombre))
            apellidos = raw_input('Apellidos: '+str(socio.apellidos))
            movil = raw_input('Movil: '+str(socio.movil))
            correo = raw_input('Correo electronico: '+str(socio.correo))
            club.editar_socio(DNI,nombre,apellidos,movil,correo)
        if(seleccion==3):
            DNI = raw_input('Introduzca el DNI del usuario a dar de baja: ')
            club.dar_baja_socio(DNI)
        if(seleccion==4):
            DNI = raw_input('Introduzca el DNI del usuario a consultar: ')
            socio = club.obtener_socio(DNI)
            print socio

    if(seleccion==4):
        print 'Haga su seleccion: '
        print '1. Crear profesor'
        print '2. Editar profesor'
        print '3. Dar profesor de baja'
        print '4. Consultar profesor'
        seleccion = int(raw_input('Haga su seleccion: '))
        if(seleccion==1):
            DNI =raw_input('DNI: ')
            nombre = raw_input('Nombre: ')
            apellidos = raw_input('Apellidos: ')
            movil = raw_input('Movil: ')
            correo = raw_input('Correo electronico: ')
            salario = raw_input('Salario en euros: ')
            jornada = raw_input('Tipo de jornada: ')
            club.alta_profesor(DNI,nombre,apellidos,movil,correo,salario,jornada)
        if(seleccion==2):
            DNI = raw_input('Editar datos del profesor: ')
            profesor = club.obtener_profesor(DNI)
            print 'Introduzca nuevos valores: '
            print profesor
            nombre = raw_input('Nombre: ')
            apellidos = raw_input('Apellidos: ')
            movil = raw_input('Movil: ')
            correo = raw_input('Correo electronico: ')
            sueldo = raw_input('Sueldo: ')
            jornada = raw_input('Jornada: ')
            club.editar_profesor(DNI,nombre,apellidos,movil,correo, sueldo, jornada)
        if(seleccion==3):
            DNI = raw_input('Introduzca el DNI del profesor a dar de baja: ')
            club.dar_baja_profesor(DNI)
        if(seleccion==4):
            DNI = raw_input('I.ntroduzca el DNI del profesor a consultar: ')
            profesor = club.obtener_profesor(DNI)
            print profesor

    if (seleccion==5):
        DNI = raw_input('DNI del socio que desea reservar: ')
        fecha = raw_input('Fecha y hora para la reserva (dd/mm/aa HH): ')
        instalacionID = raw_input('Pista que desea reservar: ')
        club.crear_reserva(DNI,fecha, instalacionID)
