__author__ = 'alberto'
from Club import Club
from Instalacion import Instalacion
def pedir_reserva():
    DNI = raw_input('DNI del socio que desea reservar: ')
    fecha = raw_input('Fecha y hora para la reserva (dd/mm/aa HH): ')
    instalacionID = raw_input('Pista que desea reservar: ')
    return club.crear_reserva(DNI,fecha, instalacionID)

def consultar_reserva():
    fecha = raw_input('Fecha y hora de la reserva (dd/mm/aa HH): ')
    reserva = club.consultar_reserva(fecha)
    return reserva

seleccion = -1
print 'Bienvenido al sistema de gestion de clubes de padel'
print '==================================================='
print "Cargando el club..."
club = Club()
print "Club cargado"
while(seleccion!='0'):
    print '1. Socios'
    print '2. Reservas'
    print '3. Alquileres'
    print '4. Profesores'
    print '5. Clases'
    print '6. Torneos'
    print '0. Salir'
    seleccion = raw_input('Haga su seleccion: ')

    if(seleccion=='1'):
        print 'Haga su seleccion: '
        print '1. Crear socio'
        print '2. Editar socio'
        print '3. Dar socio de baja'
        print '4. Consultar socio'
        seleccion = raw_input('Haga su seleccion: ')
        if(seleccion=='1'):
            DNI =raw_input('DNI: ')
            nombre = raw_input('Nombre: ')
            apellidos = raw_input('Apellidos: ')
            movil = raw_input('Movil: ')
            correo = raw_input('Correo electronico: ')
            club.alta_socio(DNI,nombre,apellidos,movil,correo)
        if(seleccion=='2'):
            DNI = raw_input('Editar datos del socio: ')
            socio = club.obtener_socio(DNI)
            print 'Introduzca nuevos valores: '
            print socio
            nombre = raw_input('Nombre: '+str(socio.nombre))
            apellidos = raw_input('Apellidos: '+str(socio.apellidos))
            movil = raw_input('Movil: '+str(socio.movil))
            correo = raw_input('Correo electronico: '+str(socio.correo))
            club.editar_socio(DNI,nombre,apellidos,movil,correo)
        if(seleccion=='3'):
            DNI = raw_input('Introduzca el DNI del usuario a dar de baja: ')
            club.dar_baja_socio(DNI)
        if(seleccion=='4'):
            DNI = raw_input('Introduzca el DNI del usuario a consultar: ')
            socio = club.obtener_socio(DNI)
            print socio

    if (seleccion=='2'):
        print 'Haga su seleccion: '
        print '1. Crear reserva'
        print '2. Cancelar reserva'
        print '3. Consultar reservas'
        seleccion = raw_input('Haga su seleccion: ')
        if (seleccion=='1'):
            pedir_reserva()
        if(seleccion=='2'):
            fecha = raw_input('Fecha y hora de la reserva (dd/mm/aa HH): ')
            if(club.cancelar_reserva(fecha)):
                print "La reserva ha sido cancelada"
            else:
                print "No existia ninguna reserva para esa fecha"
        if (seleccion=='3'):
            reserva = consultar_reserva()
            if (reserva != -1):
                print reserva
            else:
                print "No existe una reserva para esa fecha"


    if (seleccion=='3'):
        print 'Haga su seleccion: '
        print '1. Crear alquiler'
        print '2. Devolver alquiler'
        print '3. Consultar alquiler'
        seleccion = raw_input('Haga su seleccion: ')
        if (seleccion=='1'):
            reserva = consultar_reserva()
            if (reserva != -1):
                inst = '-1'
                ids = []
                while(inst!= '0'):
                    if (inst != '-1'):
                        ids.append(inst)
                    print 'Introduzca el id de la instalacion a alquilar o 0 para salir.'
                    inst = raw_input('Instalacion: ')
                club.crear_alquiler(reserva,ids)
            else:
                print "No existe una reserva para esa fecha"
        if (seleccion=='2'):
            reserva = consultar_reserva()
            if (reserva != -1):
                club.devolver_alquiler(reserva)
        if (seleccion=='3'):
            reserva = consultar_reserva()
            alquiler = club.consultar_alquiler(reserva)
            if (alquiler != -1):
                print alquiler
            else:
                print "No existe una alquiler para esa fecha"


    if(seleccion=='4'):
        print 'Haga su seleccion: '
        print '1. Crear profesor'
        print '2. Editar profesor'
        print '3. Dar profesor de baja'
        print '4. Consultar profesor'
        seleccion = raw_input('Haga su seleccion: ')
        if(seleccion=='1'):
            DNI =raw_input('DNI: ')
            nombre = raw_input('Nombre: ')
            apellidos = raw_input('Apellidos: ')
            movil = raw_input('Movil: ')
            correo = raw_input('Correo electronico: ')
            salario = raw_input('Salario en euros: ')
            jornada = raw_input('Tipo de jornada: ')
            club.alta_profesor(DNI,nombre,apellidos,movil,correo,salario,jornada)
        if(seleccion=='2'):
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
        if(seleccion=='3'):
            DNI = raw_input('Introduzca el DNI del profesor a dar de baja: ')
            club.dar_baja_profesor(DNI)
        if(seleccion=='4'):
            DNI = raw_input('I.ntroduzca el DNI del profesor a consultar: ')
            profesor = club.obtener_profesor(DNI)
            print profesor

    if(int(seleccion)==5):
        print 'Haga su seleccion: '
        print '1. Registrar Clase'
        print '2. Editar informacion clase'
        print '3. Cancelar clase'
        print '4. Consultar informacion clase'
        seleccion = raw_input('Haga su seleccion: ')
        if(int(seleccion)==1):
            reserva = pedir_reserva()
            dni_profesor = raw_input('Introduzca DNI profesor: ')
            profesor = club.obtener_profesor(dni_profesor)
            club.registrar_clase(profesor, reserva)
        if(int(seleccion)==2):
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
        if(int(seleccion)==3):
            DNI = raw_input('Introduzca el DNI del profesor a dar de baja: ')
            club.dar_baja_profesor(DNI)
        if(int(seleccion)==4):
            DNI = raw_input('Introduzca el DNI del profesor que da la clase: ')
            fecha = raw_input('Introduzca la fecha de la clase: ')
            clase = club.obtener_clase(DNI,fecha)
            print clase
