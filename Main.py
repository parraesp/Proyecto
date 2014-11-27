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
    print '1. Dar de alta a socio'
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
        print 'Dar de alta a socio: '
        DNI =raw_input('DNI: ')
        nombre = raw_input('Nombre: ')
        apellidos = raw_input('Apellidos: ')
        movil = raw_input('Movil: ')
        correo = raw_input('Correo electronico: ')
        club.alta_socio(DNI,nombre,apellidos,movil,correo)
    if(seleccion==3):
        DNI = raw_input('Introduzca el DNI del usuario a eleminar: ')
        socio = club.obtener_socio(DNI)
        print socio

    if(seleccion==4):
        DNI = raw_input('Editar datos del socio: ')
        socio = club.obtener_socio(DNI)
        print socio

    if (seleccion==5):
        DNI = raw_input('DNI del socio que desea reservar: ')
        fecha = raw_input('Fecha y hora para la reserva (dd/mm/aa HH): ')
        instalacionID = raw_input('Pista que desea reservar: ')
        club.crear_reserva(DNI,fecha, instalacionID)
