<<<<<<< HEAD
import cx_Oracle

# Nos conectamos como el usuario todo con password "123" al localhost y puerto 1521.
connection = cx_Oracle.connect("TODO", "123", "localhost:1521")
print("Database version:", connection.version)
cursor = connection.cursor()



# Una vez creada la tabla comenten esta sección de código, 
# porque si vuelven a ejecutar arrojara error ya que la base
# ya se encuentra creada.
# NOTA : esto para el ejemplo, en la tarea deben buscar como
# verificar que no ejecutan este comando si la tabla se 
# encuentra previamente creada
cursor.execute(
    """
        SELECT first_name, last_name
        FROM Persona 
    """
)


for fname, lname in cursor:
    print("Values:", fname, lname)


connection.close()
=======
lista=["24", "43", "66"]
perro, gato, zorro=lista
print(gato, zorro, perro)
gato=int(gato)
print(type(gato))
>>>>>>> f77d7d63ccfec89c65857a56b3349b8cc0c056f7
