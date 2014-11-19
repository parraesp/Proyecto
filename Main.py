__author__ = 'alberto'
import Socio
import Club

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
      DNI = raw_input('DNI: ')
      nombre = raw_input('Nombre: ')
      apellidos = int(raw_input('Apellidos: '))
      movil = raw_input('Movil: ')
      correo = raw_input('Correo electronico: ')
      socio = Socio(DNI,nombre,apellidos,movil,correo)
      club.alta_socio(socio)