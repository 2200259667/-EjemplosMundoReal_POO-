# biblioteca.py

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.prestado = False

    def prestar(self):
        if not self.prestado:
            self.prestado = True
            return f"El libro '{self.titulo}' ha sido prestado."
        else:
            return f"El libro '{self.titulo}' ya está prestado."

    def devolver(self):
        if self.prestado:
            self.prestado = False
            return f"El libro '{self.titulo}' ha sido devuelto."
        else:
            return f"El libro '{self.titulo}' no estaba prestado."


class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)
        return f"El libro '{libro.titulo}' ha sido agregado a la biblioteca."

    def buscar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                return libro
        return None


# Ejemplo de uso
if __name__ == "__main__":
    libro1 = Libro("Python for Beginners", "John Smith")
    libro2 = Libro("Data Science Handbook", "Jane Doe")

    biblioteca = Biblioteca()
    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)

    libro_prestar = biblioteca.buscar_libro("Python for Beginners")
    if libro_prestar:
        print(libro_prestar.prestar())
    else:
        print("Libro no encontrado.")

    libro_devolver = biblioteca.buscar_libro("Data Science Handbook")
    if libro_devolver:
        print(libro_devolver.devolver())
    else:
        print("Libro no encontrado.")
