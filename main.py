__author__ = 'alberto'

seleccion = -1
print 'Bienvenido al sistema de gestion de clubes de padel'
print '==================================================='
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
      movil = int(raw_input('Móvil: '))
      correo = int(raw_input('Correo electrónico: '))
