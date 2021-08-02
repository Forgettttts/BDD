from prettytable import PrettyTable
import cx_Oracle

# Nos conectamos como el usuario todo con password "123" al localhost y puerto 1521.
connection = cx_Oracle.connect("TODO", "123", "localhost:1521")
print("Database version:", connection.version)
cursor = connection.cursor()

def combinar_comuna(CodigoPrimero, CodigoSegundo, CodigoAMantener):
    if (len(CodigoPrimero) == 4):
        CodiRegi1 = CodigoPrimero[0:1]
    elif(len(CodigoPrimero) == 5):
        CodiRegi1 = CodigoPrimero[0:2]
    if (len(CodigoSegundo) == 4):
        CodiRegi2 = CodigoSegundo[0:1]
    elif(len(CodigoSegundo) == 5):
        CodiRegi2 = CodigoSegundo[0:2]
    if CodiRegi1 == CodiRegi2:  # Las comunas pertenecen a regiones distintas
        if CodigoAMantener == 1:
            cursor.execute(
                """SELECT * FROM CASOS_POR_COMUNA WHERE CodigoComuna=:1""", [str(CodigoSegundo)])
            print(cursor.fetchall())
