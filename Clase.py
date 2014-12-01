__author__ = 'alberto'
from Reserva import Reserva
class Clase():
    def __init__(self,profesor, reserva):
        self.__profesor = profesor
        self.__reserva = reserva

    def get_profesor(self):
        return self.__profesor

    def get_reserva(self):
        return self.__reserva

    def set_profesor(self,profesor):
        self.__profesor = profesor

    def set_reservaI(self,reserva):
        self.__reserva = reserva

    def __str__(self):
        return self.__profesor.__str__()+self.__reserva.__str__()