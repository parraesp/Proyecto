from unittest import TestCase
from src.Club import Club
from src.Reserva import Reserva
from random import randrange
from datetime import *
from src.Socio import Socio
from src.Profesor import Profesor
__author__ = 'Ricardo'


class TestClub(TestCase):
    def crear_fecha_random(self):
        delta = datetime.strptime('1/1/00 15', '%d/%m/%y %H')
        random_second = randrange(999999999)
        return (delta + timedelta(seconds=random_second)).strftime('%d/%m/%y %H')

    def test_validarDNI(self):
        club = Club()
        self.assertTrue(club.validarDNI('12345678A'))
        self.assertTrue(club.validarDNI('12345678a'))
        self.assertFalse(club.validarDNI('olakase'))
        self.assertFalse(club.validarDNI('123456789'))
        self.assertFalse(club.validarDNI(''))
        self.assertFalse(club.validarDNI('12345678-a'))
        self.assertFalse(club.validarDNI('1234567a8'))

    def test_validarInstalacion(self):
        club = Club()
        self.assertTrue(club.validarInstalacion('inst01'))
        self.assertTrue(club.validarInstalacion('luz'))
        self.assertTrue(club.validarInstalacion('pala3'))
        self.assertFalse(club.validarInstalacion('1234134'))
        self.assertFalse(club.validarInstalacion('inst1'))

    def test_validarEmail(self):
        club = Club()
        self.assertTrue(club.validarEmail('olakase@hotmail.com'))
        self.assertFalse(club.validarEmail('noesunemail'))

    def test_validarTelefono(self):
        club = Club()
        self.assertTrue(club.validarTelefono('123456789'))
        self.assertFalse(club.validarTelefono('1234589'))
        self.assertFalse(club.validarTelefono('abcdefghi'))

    def test_validarFecha(self):
        club = Club()
        self.assertTrue(club.validarFecha('12/12/14 17'))
        self.assertFalse(club.validarFecha('12-12-14 17'))
        self.assertFalse(club.validarFecha('32/22/14 17'))
        self.assertFalse(club.validarFecha('12/20/14 17'))
        self.assertFalse(club.validarFecha('12/12/14 17:00'))

    def test_crear_reserva(self):
        fecha = self.crear_fecha_random()
        club = Club()
        self.assertIsInstance(club.crear_reserva('12345678A', fecha, 'inst01'), Reserva)
        res1 = club.crear_reserva('11111111A', '01/01/01 15', 'inst01')
        self.assertEqual(-1, res1)
        res2 = club.crear_reserva('12345678A', fecha, 'inst01')
        self.assertEqual(-1, res2)

    def test_consultar_reserva(self):
        club = Club()
        fecha = self.crear_fecha_random()
        self.assertIsInstance(club.consultar_reserva('12345678A', '27/04/01 22'), Reserva)
        self.assertEqual(-1, club.consultar_reserva('12345678A', fecha))
        self.assertEqual(-1, club.consultar_reserva('12223334A', fecha))
        self.assertEqual(-1, club.consultar_reserva('12223334A', '27/04/01 22'))

    def test_cancelar_reserva(self):
        fecha = self.crear_fecha_random()
        club = Club()
        club.crear_reserva('12345678A', fecha, 'inst02')
        self.assertIsInstance(club.cancelar_reserva('12345678A', fecha), Reserva)
        self.assertEqual(-1, club.cancelar_reserva('12345678A', fecha))
        self.assertEqual(-1, club.cancelar_reserva('12345555A',fecha))

"""
    def test_obtener_socio(self):
        club = Club()
        self.assertIsInstance(club.obtener_socio("49116999K"), Socio)
        self.assertEqual(club.obtener_socio("socioNoExistente"), -1)

    def test_editar_socio(self):
        club = Club()
        club.editar_socio("49116999K","Juan Jose", "Perez","666209821","email_nuevo@example.org")
        socio = club.obtener_socio("49116999K")
        self.assertEqual(socio.nombre,"Juan Jose")
        self.assertEqual(socio.apellidos,"Perez")
        self.assertEqual(socio.movil,"666209821")
        self.assertEqual(socio.correo,"email_nuevo@example.org")

    def test_dar_baja_socio(self):
        club = Club()
        club.dar_baja_socio("49116999K")
        socio = club.obtener_socio("49116999K")
        self.assertFalse(socio.estado)

    def alta_socio(self):
        club = Club()
        club.alta_socio("49116999J","Ernesto", "de la Serna","633456564","rotesherztz@mail.de")
        socio = club.obtener_socio("49116999J")
        self.assertEqual(socio.nombre,"Ernesto")
        self.assertEqual(socio.apellidos,"de la Serna")
        self.assertEqual(socio.movil,"633456564")
        self.assertEqual(socio.correo,"rotesherztz@mail.de")

    def test_obtener_profesor(self):
        club = Club()
        self.assertIsInstance(club.obtener_profesor("25335374T"), Profesor)
        self.assertEqual(club.obtener_profesor("profesorNoExistente"), -1)

    def test_editar_profesor(self):
        club = Club()
        club.editar_profesor("25335374T","Don Juan", "Tenorio","666209821","email_nuevo@example.org",2500,"Completa")
        profesor = club.obtener_profesor("25335374T")
        self.assertEqual(profesor.nombre,"Don Juan")
        self.assertEqual(profesor.apellidos,"Tenorio")
        self.assertEqual(profesor.movil,"666209821")
        self.assertEqual(profesor.correo,"email_nuevo@example.org")
        self.assertEqual(profesor.get_salario(),2500)
        self.assertEqual(profesor.get_jornada(),"Completa")

    def test_dar_baja_profesor(self):
        club = Club()
        club.dar_baja_profesor("25335374T")
        profesor = club.obtener_profesor("25335374T")
        self.assertFalse(profesor.estado)

    def alta_profesor(self):
        club = Club()
        club.alta_profesor("49116999A","Eva", "Castro","733456564","eslebt@derkom.in",3000,"Completa")
        profesor = club.obtener_profesor("49116999A")
        self.assertEqual(profesor.nombre,"Eva")
        self.assertEqual(profesor.apellidos,"Castro")
        self.assertEqual(profesor.movil,"733456564")
        self.assertEqual(profesor.correo,"eslebt@derkom.in")
        self.assertEqual(profesor.get_salario(),3000)
        self.assertEqual(profesor.get_jornada(),"Completa")
"""
