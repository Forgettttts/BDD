import cx_Oracle

# Nos conectamos como el usuario todo con password "123" al localhost y puerto 1521.
connection = cx_Oracle.connect("TODO", "123", "localhost:1521")
print("Database version:", connection.version)
cursor = connection.cursor()

try:
    cursor.execute(
        """
        CREATE TABLE CASOS_POR_REGION(
        CodigoRegion NUMBER NOT NULL,
        NombreRegion VARCHAR2(50) NOT NULL,
        Poblacion NUMBER NOT NULL,
        CasosConfirmados NUMBER NOT NULL,
        CONSTRAINT PK_REGION PRIMARY KEY(CodigoRegion)
    )
    """
    )
except cx_Oracle.DatabaseError:
    print("Tabla CASOS_POR_REGION ya fue creada")
try:
    cursor.execute(
        """
        CREATE TABLE  CASOS_POR_COMUNA (
        CodigoRegion NUMBER NOT NULL,
        NombreComuna VARCHAR2(50) NOT NULL,
        CodigoComuna NUMBER NOT NULL,
        Poblacion NUMBER NOT NULL,
        CasosConfirmados NUMBER NOT NULL,
        CONSTRAINT FK_COMUNA FOREIGN KEY(CodigoRegion) REFERENCES CASOS_POR_REGION(CodigoRegion),
        CONSTRAINT PK_COMUNA PRIMARY KEY(CodigoComuna)
    )
    """
    )
except cx_Oracle.DatabaseError:
    print("Tabla CASOS_POR_COMUNA ya fue creada")
regiones_archivo = open("RegionesComunas.csv", "r")
comunas_archivo = open("CasosConfirmadosPorComuna.csv", "r")

for linea_leida in regiones_archivo:
    NombreRegion, CodigoRegion, CodigoComuna = linea_leida.strip("\n").split(",")

for linea_leida in comunas_archivo:
    NombreComuna, CodigoComuna, Poblacion, CasosConfirmados = linea_leida.strip("\n").split(",")

regiones_archivo.close()
comunas_archivo.close()
connection.commit()
connection.close()



