from src.Club import Club
__author__ = 'alberto'


def pedir_reserva():
    """
    Pide los datos para crear un reserva

    :return: reserva creada
    """
    dni_res = raw_input('dni del socio que desea reservar: ')
    while not Club.validar_dni(dni_res):
                print '\033[91m'+'El dni no tiene un formato correcto.'+'\033[0m'
                dni_res = raw_input('dni: ')
    fecha_res = raw_input('Fecha y hora para la reserva (dd/mm/aa HH): ')
    while not club.validar_fecha(fecha_res):
                print '\033[91m'+'La fecha no tiene un formato correcto.'+'\033[0m'
                fecha_res = raw_input('Fecha y hora para la reserva (dd/mm/aa HH): ')
    instalacion_id = raw_input('Pista que desea reservar: ')
    while not club.validar_instalacion(instalacion_id):
                print '\033[91m'+'La instalacion no existe.'+'\033[0m'
                instalacion_id = raw_input('Pista que desea reservar: ')
    return club.crear_reserva(dni_res, fecha_res, instalacion_id)


def consultar_reserva():
    """
    Pide los datos para consultar una reserva

    :return: reserva consultada
    """
    dni_res = raw_input('dni del socio que ha reservado: ')
    while not Club.validar_dni(dni_res):
                print '\033[91m'+'El dni no tiene un formato correcto.'+'\033[0m'
                dni_res = raw_input('dni: ')
    fecha_res = raw_input('Fecha y hora para la reserva (dd/mm/aa HH): ')
    while not club.validar_fecha(fecha_res):
                print '\033[91m'+'La fecha no tiene un formato correcto.'+'\033[0m'
                fecha_res = raw_input('Fecha y hora para la reserva (dd/mm/aa HH): ')
    reserva_res = club.consultar_reserva(dni_res, fecha_res)
    return reserva_res


def pedir_datos_persona():
    """
    Pide los datos necesarios para crear un socio o un profesor.

    :return: lista de datos
    :rtype: list
    """
    dni_res = raw_input('dni: ')
    while not Club.validar_dni(dni_res) and club.obtener_socio(dni_res) == -1 and club.obtener_profesor(dni_res) == -1:
        print '\033[91m'+'El dni no tiene un formato correcto o ya existe.'+'\033[0m'
        dni_res = raw_input('dni: ')
    nombre_per = raw_input('Nombre: ')
    apellidos_per = raw_input('Apellidos: ')
    movil_per = raw_input('Movil: ')
    while not club.validar_telefono(movil_per):
        print '\033[91m'+'El telefono no tiene un formato correcto. Deben ser 9 digitos'+'\033[0m'
        movil_per = raw_input('Movil: ')
    correo_per = raw_input('Correo electronico: ')
    while not club.validar_email(correo_per):
        print '\033[91m'+'El email no es correcto.'+'\033[0m'
        correo_per = raw_input('Correo electronico: ')
    datos_per = [dni_res, nombre_per, apellidos_per, movil_per, correo_per]
    return datos_per


seleccion = -1
print 'Bienvenido al sistema de gestion de clubes de padel'
print '==================================================='
print "Cargando el club..."
club = Club()
print "Club cargado"
while seleccion != '0':
    print '1. Socios'
    print '2. Reservas'
    print '3. Alquileres'
    print '4. Profesores'
    print '5. Clases'
    print '6. Torneos'
    print '0. Salir'
    seleccion = raw_input('Haga su seleccion: ')

    if seleccion == '1':
        print 'Haga su seleccion: '
        print '1. Crear socio'
        print '2. Editar socio'
        print '3. Dar socio de baja'
        print '4. Consultar socio'
        seleccion = raw_input('Haga su seleccion: ')

        if seleccion == '1':
            datos = pedir_datos_persona()
            club.alta_socio(datos[0], datos[1], datos[2], datos[3], datos[4])
            seleccion = '-1'
        if seleccion == '2':
            dni = raw_input('Editar datos del socio: ')
            while not Club.validar_dni(dni):
                print '\033[91m'+'El dni no tiene un formato correcto.'+'\033[0m'
                dni = raw_input('dni: ')
            socio = club.obtener_socio(dni)
            if socio != -1:
                print 'Introduzca nuevos valores: '
                print socio
                nombre = raw_input('Nombre: '+str(socio.nombre))
                apellidos = raw_input('Apellidos: '+str(socio.apellidos))
                movil = raw_input('Movil: '+str(socio.movil))
                while not club.validar_telefono(movil):
                    print '\033[91m'+'El telefono no tiene un formato correcto. Deben ser 9 digitos'+'\033[0m'
                    movil = raw_input('Movil: '+str(socio.movil))
                correo = raw_input('Correo electronico: '+str(socio.correo))
                while not club.validar_email(correo):
                    print '\033[91m'+'El email no es correcto.'+'\033[0m'
                    correo = raw_input('Correo electronico: '+str(socio.correo))
                club.editar_socio(dni, nombre, apellidos, movil, correo)
            else:
                print '\033[91m'+'No existe ningun socio con ese dni.'+'\033[0m'
            seleccion = '-1'
        if seleccion == '3':
            dni = raw_input('Introduzca el dni del usuario a dar de baja: ')
            while not Club.validar_dni(dni):
                print '\033[91m'+'El dni no tiene un formato correcto.'+'\033[0m'
            socio = club.dar_baja_socio(dni)
            if socio == -1:
                print '\033[91m'+'No existe ningun socio con ese dni.'+'\033[0m'
            seleccion = '-1'
        if seleccion == '4':
            dni = raw_input('Introduzca el dni del usuario a consultar: ')
            while not Club.validar_dni(dni):
                print '\033[91m'+'El dni no tiene un formato correcto.'+'\033[0m'
                dni = raw_input('Introduzca el dni del usuario a consultar: ')
            socio = club.obtener_socio(dni)
            if socio != -1:
                print socio
            else:
                print '\033[91m'+'No existe ningun socio con ese dni.'+'\033[0m'
            seleccion = '-1'

    if seleccion == '2':
        print 'Haga su seleccion: '
        print '1. Crear reserva'
        print '2. Cancelar reserva'
        print '3. Consultar reservas'
        seleccion = raw_input('Haga su seleccion: ')
        if seleccion == '1':
            reserva = pedir_reserva()
            seleccion = "-1"
        if seleccion == '2':
            dni = raw_input('dni del socio que desea reservar: ')
            while not Club.validar_dni(dni):
                print '\033[91m'+'El dni no tiene un formato correcto.'+'\033[0m'
                dni = raw_input('dni: ')
            fecha = raw_input('Fecha y hora para la reserva (dd/mm/aa HH): ')
            while not club.validar_fecha(fecha):
                print '\033[91m'+'La fecha no tiene un formato correcto.'+'\033[0m'
                fecha = raw_input('Fecha y hora para la reserva (dd/mm/aa HH): ')
            if club.cancelar_reserva(dni, fecha):
                print "La reserva ha sido cancelada"
            else:
                print "No existia ninguna reserva para esa fecha"
            seleccion = "-1"
        if seleccion == '3':
            reserva = consultar_reserva()
            if reserva != -1:
                print reserva
            else:
                print "No existe una reserva para esa fecha"
            seleccion = "-1"

    if seleccion == '3':
        print 'Haga su seleccion: '
        print '1. Crear alquiler'
        print '2. Devolver alquiler'
        print '3. Consultar alquiler'
        seleccion = raw_input('Haga su seleccion: ')
        if seleccion == '1':
            reserva = consultar_reserva()
            if reserva != -1:
                inst = '-1'
                ids = []
                while inst != '0':
                    if inst != '-1':
                        ids.append(inst)
                    print 'Introduzca el id de la instalacion a alquilar o 0 para salir.'
                    inst = raw_input('Instalacion: ')
                    while not club.validar_instalacion(inst) and inst != '0':
                        print '\033[91m'+'La instalacion no existe.'+'\033[0m'
                        inst = raw_input('Introduzca el id de la instalacion a alquilar o 0 para salir: ')
                club.crear_alquiler(reserva, ids)
            else:
                print "No existe una reserva para esa fecha"
        if seleccion == '2':
            reserva = consultar_reserva()
            if reserva != -1:
                club.devolver_alquiler(reserva)
        if seleccion == '3':
            reserva = consultar_reserva()
            alquiler = club.consultar_alquiler(reserva)
            if alquiler != -1:
                print alquiler
            else:
                print "No existe una alquiler para esa fecha"

    if seleccion == '4':
        print 'Haga su seleccion: '
        print '1. Crear profesor'
        print '2. Editar profesor'
        print '3. Dar profesor de baja'
        print '4. Consultar profesor'
        seleccion = raw_input('Haga su seleccion: ')
        if seleccion == '1':
            datos = pedir_datos_persona()
            salario = raw_input('Salario en euros: ')
            jornada = raw_input('Tipo de jornada: ')
            club.alta_profesor(datos[0], datos[1], datos[2], datos[3], datos[4], salario, jornada)
        if seleccion == '2':
            dni = raw_input('dni del profesor: ')
            while not Club.validar_dni(dni):
                print '\033[91m'+'El dni no tiene un formato correcto.'+'\033[0m'
                dni = raw_input('dni: ')
            profesor = club.obtener_profesor(dni)
            if profesor != -1:
                print 'Introduzca nuevos valores: '
                nombre = raw_input('Nombre: ')
                apellidos = raw_input('Apellidos: ')
                movil = raw_input('Movil: ')
                while not club.validar_telefono(movil):
                    print '\033[91m'+'El telefono no tiene un formato correcto. Deben ser 9 digitos'+'\033[0m'
                    movil = raw_input('Movil: ')
                correo = raw_input('Correo electronico: ')
                while not club.validar_email(correo):
                    print '\033[91m'+'El email no es correcto.'+'\033[0m'
                    correo = raw_input('Correo electronico: ')
                sueldo = raw_input('Sueldo: ')
                jornada = raw_input('Jornada: ')
                club.editar_profesor(dni, nombre, apellidos, movil, correo, sueldo, jornada)
            else:
                print '\033[91m'+'No existe ningun profesor con ese dni'+'\033[0m'
            seleccion = '-1'
        if seleccion == '3':
            dni = raw_input('Introduzca el dni del profesor a dar de baja: ')
            while not Club.validar_dni(dni):
                print '\033[91m'+'El dni no tiene un formato correcto.'+'\033[0m'
                dni = raw_input('dni: ')
            club.dar_baja_profesor(dni)
        if seleccion == '4':
            dni = raw_input('Introduzca el dni del profesor a consultar: ')
            while not Club.validar_dni(dni):
                print '\033[91m'+'El dni no tiene un formato correcto.'+'\033[0m'
                dni = raw_input('dni: ')
            profesor = club.obtener_profesor(dni)
            if profesor != -1:
                print profesor
            else:
                print 'No existe dicho profesor.'

    if seleccion == '5':
        print 'Haga su seleccion: '
        print '1. Registrar Clase'
        print '2. Cancelar clase'
        print '3. Consultar informacion clase'
        seleccion = raw_input('Haga su seleccion: ')
        if seleccion == '1':
            reserva = pedir_reserva()
            if reserva != -1:
                dni_profesor = raw_input('Introduzca dni profesor: ')
                while not Club.validar_dni(dni_profesor):
                    print '\033[91m'+'El dni no tiene un formato correcto.'+'\033[0m'
                    dni_profesor = raw_input('Introduzca dni profesor: ')
                profesor = club.obtener_profesor(dni_profesor)
                club.registrar_clase(profesor, reserva)
            else:
                print 'Ya existe una reserva para esa fecha'
        if seleccion == '2':
            dni = raw_input('Introduzca el dni del profesor que da la clase:')
            while not Club.validar_dni(dni):
                print '\033[91m'+'El dni no tiene un formato correcto.'+'\033[0m'
                dni = raw_input('dni: ')
            dni2 = raw_input('Introduzca el dni del socio:')
            while not Club.validar_dni(dni2):
                print '\033[91m'+'El dni no tiene un formato correcto.'+'\033[0m'
                dni2 = raw_input('dni: ')
            fecha = raw_input('Fecha y hora para la clase (dd/mm/aa HH): ')
            while not club.validar_fecha(fecha):
                print '\033[91m'+'La fecha no tiene un formato correcto.'+'\033[0m'
                fecha = raw_input('Fecha y hora para la clase (dd/mm/aa HH): ')
            club.cancelar_clase(dni, dni2, fecha)
        if seleccion == '3':
            dni = raw_input('Introduzca el dni del profesor que da la clase:')
            while not Club.validar_dni(dni):
                print '\033[91m'+'El dni no tiene un formato correcto.'+'\033[0m'
                dni = raw_input('dni: ')
            dni2 = raw_input('Introduzca el dni del socio:')
            while not Club.validar_dni(dni2):
                print '\033[91m'+'El dni no tiene un formato correcto.'+'\033[0m'
                dni2 = raw_input('dni: ')
            fecha = raw_input('Fecha y hora para la clase (dd/mm/aa HH): ')
            while not club.validar_fecha(fecha):
                print '\033[91m'+'La fecha no tiene un formato correcto.'+'\033[0m'
                fecha = raw_input('Fecha y hora para la clase (dd/mm/aa HH): ')
            clase = club.obtener_clase(dni, dni2, fecha)
            if clase != -1:
                print clase
            else:
                print 'No existe clase dicha clase.'

    if seleccion == '6':
        print 'Haga su seleccion: '
        print '1. Crear Torneo.'
        print '2. Introducir resultado.'
        print '3. Borrar torneo.'
        print '4. Consultar torneo.'
        seleccion = raw_input('Haga su seleccion: ')
        if seleccion == '1':
            nombre = raw_input('Introduzca el nombre del torneo: ')
            i = 0
            socios = []
            while i < 8:
                dni = raw_input('Introduzca el dni del participante: ')
                while not Club.validar_dni(dni):
                    print '\033[91m'+'El dni no tiene un formato correcto.'+'\033[0m'
                    dni = raw_input('dni: ')
                socio = club.obtener_socio(dni)
                if socio != -1:
                    socios.append(socio)
                    i += 1
                else:
                    print 'No existe socio para ese dni.'
            fecha = raw_input('Introduzca una fecha para empezar el torneo: ')
            while not club.validar_fecha(fecha):
                print '\033[91m'+'La fecha no tiene un formato correcto.'+'\033[0m'
                fecha = raw_input('Fecha y hora para la clase (dd/mm/aa HH): ')
            club.crear_torneo(nombre, socios, fecha)

        if seleccion == '2':
            nombre = raw_input('Introduzca el nombre del torneo: ')
            partido = raw_input('Introduzca el partido del torneo: ')
            resultado = raw_input('Introduzca el resultado del partido: ')
            club.introducir_resultado(nombre, partido, resultado)

        if seleccion == '3':
            nombre = raw_input('Introduzca el nombre del torneo: ')
            torneo = club.borrar_torneo(nombre)
            if torneo == -1:
                print 'No existe un toreno con ese nombre.'

        if seleccion == '4':
            nombre = raw_input('Introduzca el nombre del torneo: ')
            torneo = club.consultar_torneo(nombre)
            if torneo != -1:
                print torneo
            else:
                print 'No existe un toreno con ese nombre.'
