class Producto:
    def __init__(self, codigo: str, descripcion: str,
                 precio: float, cantidad: int):
        self.codigo = codigo
        self.descripcion = descripcion
        self.precio = precio
        self.cantidad = cantidad