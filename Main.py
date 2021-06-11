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
    if(NombreRegion == "Region"):
        continue
    update_cpr = """
        INSERT INTO CASOS_POR_REGION(
            CodigoRegion,
            NombreRegion,
            Poblacion,
            CasosConfirmados,
        )
        VALUES({},'{}', 0, 0)
        """.format(CodigoRegion, NombreRegion)
    cursor.execute(update_cpr)
print("Tabla Region creada con éxito. \n")

for linea_leida in comunas_archivo:
    NombreComuna, CodigoComuna, Poblacion, CasosConfirmados = linea_leida.strip("\n").split(",")
    if(NombreComuna == "Comuna"):
        continue
    if (len(CodigoComuna) == 4):
        CodReg = CodigoComuna[0:2]
    elif(len(CodigoComuna) == 5):
        CodReg=CodigoComuna[0:1]
    update_cpr="""
        INSERT INTO CASOS_POR_COMUNA(
            CodigoRegion,
            NombreComuna,
            CodigoComuna,
            Poblacion,
            CasosConfirmados
        )
        VALUES({},'{}',{},{},{})
        """.format(CodReg,NombreComuna,CodigoComuna, Poblacion, CasosConfirmados)
    cursor.execute(update_cpr)
print("Tabla Comunas creada con éxito. \n")

regiones_archivo.close()
comunas_archivo.close()
connection.commit()
connection.close()
