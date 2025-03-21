class GestorArchivo:
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo
        self.archivo = None  

    def __enter__(self):
        self.archivo = open(self.nombre_archivo, "a", encoding="utf-8")
        return self.archivo  

    def __exit__(self, exc_type, exc_value, traceback):
        self.archivo.close() 

mensaje = input("📝 Escribe tu mensaje para guardar en el archivo: ")


with GestorArchivo("mi_archivo.txt") as archivo:
    archivo.write(mensaje + "\n") 

 
print("✅ Mensaje guardado en 'mi_archivo.txt'")

