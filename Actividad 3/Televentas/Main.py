from Modelos.Productos import Producto
from Modelos.Cliente import Cliente


def main():
    producto = Producto("001", "Celular", 1200, 10)
    cliente = Cliente("Juan", "juan@gmail.com")

    print(producto.descripcion)
    print(cliente.nombre)


if __name__ == "__main__":
    main()