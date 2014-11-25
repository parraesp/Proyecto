__author__ = 'Ricardo'

class Instalacion():
    def get_descripcion(self):
        return self.__descripcion

    def get_precio(self):
        return self.__descripcion

    def get_id(self):
        return self.__descripcion

    id = property(get_id)
    descripcion = property(get_descripcion)
    precio = property(get_precio)

    def __init__(self,id, precio, descripcion):
        self.__id = id
        self.__precio = precio
        self.__descripcion = descripcion
