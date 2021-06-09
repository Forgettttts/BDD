import cx_Oracle

# Nos conectamos como el usuario todo con password "123" al localhost y puerto 1521.
connection = cx_Oracle.connect("TODO", "123", "localhost:1521")
print("Database version:", connection.version)
cursor = connection.cursor()

try:
    cursor.execute(
        """
    CREATE TABLE  CASOS_POR_COMUNA (
        CodigoRegion NUMBER NOT NULL,
        NombreComuna VARCHAR2(50) NOT NULL,
        CodigoComuna NUMBER NOT NULL,
        Poblacion NUMBER NOT NULL,
        CasosConfirmados NUMBER NOT NULL,

        PRIMARY KEY(CodigoComuna)
    )
    """
    )
except cx_Oracle.DatabaseError:
    print("Tabla CASOS_POR_COMUNA ya fue creada")

try:
    cursor.execute(
        """
    CREATE TABLE CASOS_POR_REGION(
        CodigoRegion NUMBER NOT NULL,
        NombreRegion VARCHAR2(50) NOT NULL,
        Poblacion NUMBER NOT NULL,
        CasosConfirmados NUMBER NOT NULL,

        PRIMARY KEY(CodigoRegion)
    )
    """
    )
except cx_Oracle.DatabaseError:
    print("Tabla CASOS_POR_REGION ya fue creada")

except cx_Oracle.DatabaseError:
    print("Tabla CASOS_POR_COMUNA ya fue creada")

try:
    cursor.execute(
        """
    CREATE TABLE COMUNAS_EN_REGION(
        CodigoRegion NUMBER NOT NULL,
        CodigoComuna NUMBER NOT NULL,

        PRIMARY KEY(CodigoRegion, CodigoComuna)
    )
    """
    )
except cx_Oracle.DatabaseError:
    print("Tabla COMUNAS_EN_REGION ya fue creada")

regiones_archivo = open("RegionesComunas.csv", "r")
comunas_archivo = open("CasosConfirmadosPorComuna.csv", "r")

for linea_leida, otra_linea in regiones_archivo, comunas_archivo:
    NombreRegion, CodigoRegion, CodigoComuna = linea_leida.strip("\n").split(",")

for linea_leida in comunas_archivo:
    NombreComuna, CodigoComuna, Poblacion, CasosConfirmados = linea_leida.strip("\n").split(",")

regiones_archivo.close()
comunas_archivo.close()

connection.close()



