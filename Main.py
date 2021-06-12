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
regiones_archivo = open("RegionesComunas.csv", "r", encoding="utf-8")
comunas_archivo = open("CasosConfirmadosPorComuna.csv", "r", encoding="utf-8")

for linea_leida in regiones_archivo:
    NombreRegion, CodigoRegion, CodigoComuna = linea_leida.strip("\n").split(",")
    if(NombreRegion == "Region"):
        continue
    try:
        cursor.execute(
            """
            INSERT INTO CASOS_POR_REGION
            VALUES(:1,:2, 0, 0)
            """,[int(CodigoRegion), NombreRegion]
            )
    except Exception:
        continue
print("Tabla Region creada con éxito. \n")

for linea_leida in comunas_archivo:
    NombreComuna, CodigoComuna, PoblacionComuna, CasosConfirmadosComuna = linea_leida.strip("\n").split(",")
    if(NombreComuna == "Comuna"):
        continue
    if (len(CodigoComuna) == 4):
        CodReg = CodigoComuna[0:1]
    elif(len(CodigoComuna) == 5):
        CodReg=CodigoComuna[0:2]
    try:
        cursor.execute(
            """
            INSERT INTO CASOS_POR_COMUNA
            VALUES(:1, :2, :3, :4, :5)
            """, [int(CodReg), NombreComuna, int(CodigoComuna), int(PoblacionComuna), int(CasosConfirmadosComuna)]
        )
    except Exception:
        continue
    cursor.execute(
        """
        UPDATE CASOS_POR_REGION
        SET CasosConfirmados=CasosConfirmados+ :1 , Poblacion=Poblacion+:2
        WHERE CodigoRegion= :3
        """,[int(CasosConfirmadosComuna), int(PoblacionComuna), int(CodReg)]
    )
print("Tabla Comunas creada con éxito. \n")
connection.commit()

def crear_comuna(NombreNuevo, CodigoNuevo):
    try:
        #? Revision de existencia previa en tabla del nombre y/o codigo
        db=""" SELECT * FROM CASOS_POR_COMUNA """
        cursor.execute(db)
        fila=cursor.fetchall()
        for datos in fila:
            NomCom= fila[1]
            CodCom= fila[2]
            if NombreNuevo == NomCom:
                print("Nombre de comuna ya en uso, por favor, intente con otro.\n")
                if CodigoNuevo == CodCom:
                    print("También el código de comuna ya en uso, por favor, intente con otro.\n")
                return
            if CodigoNuevo == CodCom:
                print("Codigo de comuna ya en uso, por favor, intente con otro.\n")
                return
    except Exception:
        print("Error en revisar la existencia previa del nombre o del codigo de comuna.\n")
    try:
        #? Revision de existencia de la region
        db = """ SELECT * FROM CASOS_POR_REGION """
        cursor.execute(db)
        fila = cursor.fetchall()
        if (len(CodigoNuevo) == 4):
            CodiRegi = CodigoComuna[0:1]
        elif(len(CodigoNuevo) == 5):
            CodiRegi = CodigoComuna[0:2]
        RegionExistente = False
        for datos in fila:
            CodigoDeLaRegion = fila[0]
            if CodigoDeLaRegion == CodiRegi:
                RegionExistente=True
                break
    except Exception:
        print("Error en revisar la existencia de la región.\n")
    if RegionExistente==False:
        print("No hay region creada para dicha comuna, intente con un codigo distinto, o cree una region correspondiente previa a crear esta comuna. \n")
        return
    #? Si se llega hasta aca, es porque es valido insertarlo, tanto por el nombre nuevo, codigo nuevo y region existente
    cursor.execute(
        """
    INSERT INTO CASOS_POR_COMUNA
    VALUES(:1, :2, :3, 0, 0)
    """, [int(CodiRegi), NombreNuevo, int(CodigoNuevo)]
    )
    connection.commit()


regiones_archivo.close()
comunas_archivo.close()
connection.close()
