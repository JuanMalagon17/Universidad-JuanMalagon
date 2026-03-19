class Cliente:
    def __init__(self, nombre: str, correo: str):
        self.nombre = nombre
        self.correo = correo

    def solicitar_catalogo(self):
        print(f"Catálogo enviado a {self.correo}")