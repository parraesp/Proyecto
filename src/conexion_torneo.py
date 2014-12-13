from src.Torneo import Torneo
import csv
import os
__author__ = 'alberto'


class ConexionTorneo():
    """
    Modelo de la clase torneo
    """
    def __init__(self, socios):
        """
        Constructor del modelo

        :param socios: modelo de socios
        """
        self.socios = socios
        self.__torneos = self.__listar_torneos()

    def guardar_torneo(self, torneo):
        """
        Guarda un torneo en fichero y en el club

        :param torneo: torneo a guardar
        """
        f = open(os.path.dirname(__file__)+'/files/torneos.csv', 'a+')
        self.guardar_torneo_fichero(torneo, f)
        f.close()
        self.__torneos.append(torneo)

    @staticmethod
    def guardar_torneo_fichero(torneo, f):
        """
        Guarda un torneo en el fichero

        :param torneo: torneo a guardar
        :param f: fichero
        """
        texto = ''
        texto += torneo.get_nombre()+'\t'
        for s in torneo.get_socios():
            texto += s.get_dni()+'\t'
        for r in torneo.get_resultados():
            texto += r+'\t'
            texto += str(torneo.get_resultados()[r])+'\t'
        texto += '\n'
        f.write(texto)

    def sacar_torneo(self, nombre):
        """
        Obtiene los datos de un torneo

        :param nombre: nombre del torneo
        :return: torneo
        """
        valor = -1
        cont = 0
        encontrado = False
        while cont < len(self.__torneos) and not encontrado:
            if self.__torneos[cont].get_nombre() == nombre:
                encontrado = True
                valor = self.__torneos[cont]
            else:
                cont += 1
        return valor

    def poner_resultado(self, torneo, partido, resultado):
        """
        Guarda un resultado de forma permanente

        :param torneo: torneo
        :param partido: partido del torneo
        :param resultado: resultado del partido
        """
        torneo.set_resultado(partido, resultado)
        f = open(os.path.dirname(__file__)+'/files/torneos.csv', "w")
        for t in self.__torneos:
            self.guardar_torneo_fichero(t, f)
        f.close()

    def borrar_torneo(self, torneo):
        """
        Borra un torneo de forma permanente

        :param torneo: nombre del torneo
        """
        self.__torneos.remove(torneo)
        f = open(os.path.dirname(__file__)+'/files/torneos.csv', "r")
        torneos = f.readlines()
        f.close()

        f = open(os.path.dirname(__file__)+'/files/torneos.csv', "w")
        for t in torneos:
            t_aux = t.split("\t")
            if t_aux[0] != torneo.get_nombre():
                f.write(t)
        f.close()

    def __listar_torneos(self):
        """
        Obtiene todos los torneos existentes del fichero

        :return: lista de torneos
        :rtype: list
        """
        torneos = []
        with open(os.path.dirname(__file__)+'/files/torneos.csv') as f:
            content = csv.reader(f, delimiter='\t')
            for row in content:
                if row:
                    socios = []
                    for i in range(1, 9, 1):
                        socios.append(self.socios.sacar_socio(row[i]))
                    torneo = Torneo(row[0], socios)
                    for i in range(9, 23, 2):
                        torneo.set_resultado(row[i], row[i+1])
                    torneos.append(torneo)
        f.close()
        return torneos
