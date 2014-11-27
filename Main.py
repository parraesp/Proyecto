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
    print '2. Editar datos de socio'
    print '3. Dar de baja socio'
    print '4. Consultar datos de socio'
    print '5. Crear nueva reserva'
    print '6. Crear nuevo alquiler'
    print '7. Cancelar reserva'
    print '8. Devolver alquiler'
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
            print 'Datos del socio seleccionado: '
            print socio
            DNI =raw_input('DNI['.str(socio[0]))
            nombre = raw_input('Nombre: '.str(socio[1]))
            apellidos = raw_input('Apellidos: '.str(socio[2]))
            movil = raw_input('Movil: '.str(socio[3]))
            correo = raw_input('Correo electronico: '.str(socio[4]))
        if(seleccion==3):
            DNI = raw_input('Introduzca el DNI del usuario a dar de baja: ')
            socio = club.dar_baja_socio(DNI)
            print socio
        if(seleccion==4):
            DNI = raw_input('Introduzca el DNI del usuario a consultar: ')
            socio = club.obtener_socio(DNI)
            print socio



    if (seleccion==5):
        DNI = raw_input('DNI del socio que desea reservar: ')
        fecha = raw_input('Fecha para la reserva (dd/mm/aa): ')
        instalacionID = raw_input('Pista que desea reservar: ')
        instalacion = Instalacion(instalacionID,20,'prueba')
        club.crear_reserva(DNI,fecha, instalacion)
