from abc import ABC, abstractmethod

class Interfaz_Inventario(ABC):
    @abstractmethod
    def obtener_producto(self, codigo: str):
        pass

    @abstractmethod
    def actualizar_stock(self, codigo: str, cantidad: int):
        pass