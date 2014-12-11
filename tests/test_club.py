from unittest import TestCase
from src.Club import Club
from mockito import mock

__author__ = 'Ricardo'


class TestClub(TestCase):
    def test_validarDNI(self):
        club = Club()
        self.assertTrue(club.validarDNI('12345678A'))
        self.assertTrue(club.validarDNI('12345678a'))
        self.assertFalse(club.validarDNI('olakase'))
        self.assertFalse(club.validarDNI('123456789'))
        self.assertFalse(club.validarDNI(''))
        self.assertFalse(club.validarDNI('12345678-a'))
        self.assertFalse(club.validarDNI('1234567a8'))



