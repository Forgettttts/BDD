import cx_Oracle
from prettytable import PrettyTable

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
connection.commit()

regiones_archivo.close()
comunas_archivo.close()
def crear_comuna(NombreNuevo, CodigoNuevo):
    try:
        #? Revision de existencia previa en tabla del nombre y/o codigo
        db=""" SELECT * FROM CASOS_POR_COMUNA """
        cursor.execute(db)
        fila=cursor.fetchall()
        for datos in fila:
            NomCom= datos[1]
            CodCom= datos[2]
            if NombreNuevo == NomCom:
                print("Nombre de comuna ya en uso, por favor, intente con otro.\n")
                if int(CodigoNuevo) == int(CodCom):
                    print("Tambi??n el c??digo de comuna ya en uso, por favor, intente con otro.\n")
                return
            if int(CodigoNuevo) == int(CodCom):
                print("Codigo de comuna ya en uso, por favor, intente con otro.\n")
                return
    except Exception:
        print("Error en revisar la existencia previa del nombre o del codigo de comuna.\n")

    RegionExistente = False
    try:
        #? Revision de existencia de la region
        db = """ SELECT * FROM CASOS_POR_REGION """
        cursor.execute(db)
        fila = cursor.fetchall()
        if (len(CodigoNuevo) == 4):
            CodiRegi = CodigoNuevo[0:1]
        elif(len(CodigoNuevo) == 5):
            CodiRegi = CodigoNuevo[0:2]
        for datos in fila:
            CodigoDeLaRegion = datos[0]
            if int(CodigoDeLaRegion) == int(CodiRegi):
                RegionExistente=True
                break
    except Exception:
        print("Error en revisar la existencia de la regi??n.\n")
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
    print("Comuna de:", NombreNuevo, "con el c??digo:", CodigoNuevo, "creada con ??xito.\n")

def crear_region(NombreNuevo, CodigoNuevo):
    try:
        #? Revision de existencia previa en tabla del nombre y/o codigo
        db = """ SELECT * FROM CASOS_POR_REGION """
        cursor.execute(db)
        fila = cursor.fetchall()
        for datos in fila:
            NomReg = datos[1]
            CodReg = datos[2]
            if NombreNuevo.upper() == NomReg.upper():
                print("Nombre de regi??n ya en uso, por favor, intente con otro.\n")
                if int(CodigoNuevo) == int(CodReg):
                    print(
                        "Tambi??n el c??digo de regi??n ya en uso, por favor, intente con otro.\n")
                return
            if int(CodigoNuevo) == int(CodReg):
                print("Codigo de regi??n ya en uso, por favor, intente con otro.\n")
                return
    except Exception:
        print(
            "Error en revisar la existencia previa del nombre o del codigo de la regi??n.\n")
    #Si es que se llega hasta aca es porque se puede crear sin problemas de codigo
    cursor.execute(
        """
        INSERT INTO CASOS_POR_REGION
        VALUES(:1,:2, 0, 0)
        """, [int(CodigoNuevo), NombreNuevo]
        )
    connection.commit()
    print("Regi??n de:", NombreNuevo, "con el c??digo:",CodigoNuevo, "creada con ??xito.\n")

def casos_totales_comuna(CodigoCom):
    #Se buscan los datos, correspondientes al codigo de comuna entregado
    cursor.execute("""SELECT NombreComuna, CasosConfirmados FROM CASOS_POR_COMUNA WHERE CodigoComuna=:1""",[str(CodigoCom)])
    comuna, casos = cursor.fetchone()
    #Se printean resultados
    print("Casos de la comuna:", comuna, "=", casos, "[casos]. \n")


def casos_totales_region(CodigoReg):
    #Se buscan los datos, correspondientes al codigo de region entregado
    cursor.execute("""SELECT NombreRegion, CasosConfirmados FROM CASOS_POR_REGION WHERE CodigoRegion=:1""", [str(CodigoReg)])
    region, casos = cursor.fetchone()
    #Se printean resultados
    print("Casos de la regi??n:", region, "=", casos, "[casos]. \n")


def casos_total_todas_comunas():
    #Se genera la tabla donde se mostraran resultados
    tabla = PrettyTable(["Comuna", "Casos totales"])
    cursor.execute(""" SELECT * FROM CASOS_POR_COMUNA """)#Se buscan resultados
    fila = cursor.fetchall()
    #se rellena tabla con resultados
    for datos in fila:
        tabla.add_row([datos[1], datos[4]])
    #se muestran resultados
    print(tabla)

def casos_total_todas_regiones():
    #Se genera la tabla donde se mostraran resultados
    tabla = PrettyTable(["Regi??n", "Casos totales"])
    cursor.execute(""" SELECT * FROM CASOS_POR_REGION """)#Se buscan resultados
    fila = cursor.fetchall()
    #se rellena tabla con resultados
    for datos in fila:
        tabla.add_row([datos[1], datos[3]])
    #se muestran resultados
    print(tabla)

def a??adir_casos_comuna(CodComuna, Nuevos):
    #se revisa si es que la comuna existe
    try:
        existencia_comuna=False
        db = """ SELECT * FROM CASOS_POR_COMUNA """
        cursor.execute(db)
        fila = cursor.fetchall()
        for datos in fila:
            CodCom = datos[2]
            if int(CodComuna) == int(CodCom):
                existencia_comuna=True
                break
    except Exception:
        print("Error en revisar la existencia de la comuna a actualizar.\n")
    if (existencia_comuna==False):
        print("Comuna no existente, ingrese una existente o cree una nueva.\n")
        return
    #si es que llegamos aqui, es pq la comuna existe, y se procede
    cursor.execute(
        """
        UPDATE CASOS_POR_COMUNA
        SET CasosConfirmados=CasosConfirmados+ :1
        WHERE CodigoComuna= :2
        """, [int(Nuevos), int(CodComuna)]
    )
    if (len(CodComuna) == 4):
        CodiRegi = CodComuna[0:1]
    elif(len(CodComuna) == 5):
        CodiRegi = CodComuna[0:2]
    #se actualizan datos de la region
    cursor.execute(
        """
        UPDATE CASOS_POR_REGION
        SET CasosConfirmados=CasosConfirmados+ :1
        WHERE CodigoRegion= :2
        """, [int(Nuevos), int(CodiRegi)]
    )
    connection.commit()
    print("Casos activos, actualizados con ??xito.\n")


def eliminar_casos_comuna(CodComuna, Nuevos):
    #se revisa si es que la comuna existe
    try:
        existencia_comuna = False
        db = """ SELECT * FROM CASOS_POR_COMUNA """
        cursor.execute(db)
        fila = cursor.fetchall()
        for datos in fila:
            CodCom = datos[2]
            if int(CodComuna) == int(CodCom):
                existencia_comuna = True
                break
    except Exception:
        print("Error en revisar la existencia de la comuna a actualizar.\n")
    if (existencia_comuna == False):
        print("Comuna no existente, ingrese una existente o cree una nueva.\n")
        return
    #si es que llegamos aqui, es pq la comuna existe, y se procede
    cursor.execute(
        """
        UPDATE CASOS_POR_COMUNA
        SET CasosConfirmados=CasosConfirmados- :1
        WHERE CodigoComuna= :2
        """, [int(Nuevos), int(CodComuna)]
    )
    if (len(CodComuna) == 4):
        CodiRegi = CodComuna[0:1]
    elif(len(CodComuna) == 5):
        CodiRegi = CodComuna[0:2]
    #se actualizan datos de region
    cursor.execute(
        """
        UPDATE CASOS_POR_REGION
        SET CasosConfirmados=CasosConfirmados- :1
        WHERE CodigoRegion= :2
        """, [int(Nuevos), int(CodiRegi)]
    )
    connection.commit()
    print("Casos activos, actualizados con ??xito.\n")

#CodigoAMantener puede ser 1 o 2, en el caso de que sea 1, los datos del 2 se suman al primero, viceversa con el caso de que sea =2
def combinar_comuna(CodigoPrimero, CodigoSegundo, CodigoAMantener):
    #Se revisa la existencia de ambas comunas
    try:
        existencia_comuna = False
        db = """ SELECT * FROM CASOS_POR_COMUNA """
        cursor.execute(db)
        fila = cursor.fetchall()
        for datos in fila:
            CodCom = datos[2]
            if int(CodigoPrimero) == int(CodCom):
                existencia_comuna = True
                break
    except Exception:
        print("Error en revisar la existencia de la comuna a actualizar.\n")
    if (existencia_comuna == False):
        print("La primera comuna no existe, ingrese una existente o cree una nueva.\n")
        return
    try:
        existencia_comuna = False
        db = """ SELECT * FROM CASOS_POR_COMUNA """
        cursor.execute(db)
        fila = cursor.fetchall()
        for datos in fila:
            CodCom = datos[2]
            if int(CodigoSegundo) == int(CodCom):
                existencia_comuna = True
                break
    except Exception:
        print("Error en revisar la existencia de la comuna a actualizar.\n")
    if (existencia_comuna == False):
        print("La segunda comuna no existe, ingrese una existente o cree una nueva.\n")
        return

    #A este punto ya se sabe que ambos codigos de comuna, existen en la tabla
    C1=CodigoPrimero
    C2=CodigoSegundo
    Cm=CodigoAMantener
    #Se revisa si es que son de la misma region o no
    if (len(C1) == 4):
        CodiRegi1 = C1[0:1]
    elif(len(C1) == 5):
        CodiRegi1 = C1[0:2]
    if (len(C2) == 4):
        CodiRegi2 = C2[0:1]
    elif(len(C2) == 5):
        CodiRegi2 = C2[0:2]
    if CodiRegi1==CodiRegi2: #Las comunas pertenecen a la misma region
        if int(Cm)==1:
            #Copiamos datos de la comuna a eliminar
            cursor.execute("""SELECT NombreComuna, Poblacion, CasosConfirmados FROM CASOS_POR_COMUNA WHERE CodigoComuna=:1""", [C2])
            Name,PoblaTemp, CasosTemp= cursor.fetchone()
            print("Copiando datos desde la comuna de",Name,"...\n")
            #Colocamos los datos en la comuna de destino
            cursor.execute(
                """
                UPDATE CASOS_POR_COMUNA
                SET CasosConfirmados=CasosConfirmados+ :1, Poblacion=Poblacion+:2
                WHERE CodigoComuna= :3
                """, [int(CasosTemp), int(PoblaTemp), int(C1)]
                )
            #eliminando la comuna que no se mantendra
            cursor.execute("""DELETE FROM CASOS_POR_COMUNA WHERE CodigoComuna=:1""", [C2])
            connection.commit()
            print("Comunas combinadas de manera exitosa.\n")
        elif int(Cm)==2:
            #Copiamos datos de la comuna a eliminar
            cursor.execute(
                """SELECT NombreComuna, Poblacion, CasosConfirmados FROM CASOS_POR_COMUNA WHERE CodigoComuna=:1""", [C1])
            Name, PoblaTemp, CasosTemp = cursor.fetchone()
            print("Copiando datos desde la comuna de", Name, "...\n")
            #Colocamos los datos en la comuna de destino
            cursor.execute(
                """
                UPDATE CASOS_POR_COMUNA
                SET CasosConfirmados=CasosConfirmados+ :1, Poblacion=Poblacion+:2
                WHERE CodigoComuna= :3
                """, [int(CasosTemp), int(PoblaTemp), int(C2)]
            )
            #eliminando la comuna que no se mantendra
            cursor.execute(
                """DELETE FROM CASOS_POR_COMUNA WHERE CodigoComuna=:1""", [C1])
            connection.commit()
            print("Comunas combinadas de manera exitosa.\n")
        else:
            print("Debe seleccionar entre 1 (que se unan en la 1era comuna ingresada) o 2 (union en la 2da comuna ingresada).\n")
            return

    else: #comunas son de distintas regiones
        if int(Cm) == 1:
            #Copiamos datos de la comuna a eliminar
            cursor.execute(
                """SELECT CodigoRegion, NombreComuna, Poblacion, CasosConfirmados FROM CASOS_POR_COMUNA WHERE CodigoComuna=:1""", [C2])
            CodTemp, Name, PoblaTemp, CasosTemp = cursor.fetchone()
            print("Copiando datos desde la comuna de", Name, "...\n")
            #Restamos desde la region de origen
            cursor.execute(
                """
                UPDATE CASOS_POR_REGION
                SET CasosConfirmados=CasosConfirmados- :1, Poblacion=Poblacion-:2
                WHERE CodigoRegion= :3
                """, [int(CasosTemp), int(PoblaTemp), int(CodTemp)]
            )
            #Colocamos los datos en la comuna de destino
            cursor.execute(
                """
                UPDATE CASOS_POR_COMUNA
                SET CasosConfirmados=CasosConfirmados+ :1, Poblacion=Poblacion+:2
                WHERE CodigoComuna= :3
                """, [int(CasosTemp), int(PoblaTemp), int(C1)]
            )
            #Sumamos en la region de destino
            cursor.execute(
                """SELECT CodigoRegion, NombreRegion FROM CASOS_POR_COMUNA WHERE CodigoComuna=:1""", [C1])
            CodDest, NomDest = cursor.fetchone()
            print("Actualizando datos de la region de destino (", NomDest,")\n")
            cursor.execute(
                """
                UPDATE CASOS_POR_REGION
                SET CasosConfirmados=CasosConfirmados+ :1, Poblacion=Poblacion+ :2
                WHERE CodigoRegion= :3
                """, [int(CasosTemp), int(PoblaTemp), int(CodDest)]
            )
            #eliminando la comuna que no se mantendra
            cursor.execute(
                """DELETE FROM CASOS_POR_COMUNA WHERE CodigoComuna=:1""", [C2])
            connection.commit()
            print("Comunas combinadas de manera exitosa.\n")
        elif int(Cm) == 2:
            #Copiamos datos de la comuna a eliminar
            cursor.execute(
                """SELECT CodigoRegion, NombreComuna, Poblacion, CasosConfirmados FROM CASOS_POR_COMUNA WHERE CodigoComuna=:1""", [C1])
            CodTemp, Name, PoblaTemp, CasosTemp = cursor.fetchone()
            print("Copiando datos desde la comuna de", Name, "...\n")
            #Restamos desde la region de origen
            cursor.execute(
                """
                UPDATE CASOS_POR_REGION
                SET CasosConfirmados=CasosConfirmados- :1, Poblacion=Poblacion-:2
                WHERE CodigoRegion= :3
                """, [int(CasosTemp), int(PoblaTemp), int(CodTemp)]
            )

            #Colocamos los datos en la comuna de destino
            cursor.execute(
                """
                UPDATE CASOS_POR_COMUNA
                SET CasosConfirmados=CasosConfirmados+ :1, Poblacion=Poblacion+:2
                WHERE CodigoComuna= :3
                """, [int(CasosTemp), int(PoblaTemp), int(C2)]
            )
            #Sumamos en la region de destino
            cursor.execute(
                """SELECT CodigoRegion, NombreComuna FROM CASOS_POR_COMUNA WHERE CodigoComuna=:1""", [C2])
            CodDest, NomDest = cursor.fetchone()
            print("Actualizando datos de la region de destino (", NomDest, ")\n")
            cursor.execute(
                """
                UPDATE CASOS_POR_REGION
                SET CasosConfirmados=CasosConfirmados+ :1, Poblacion=Poblacion+ :2
                WHERE CodigoRegion= :3
                """, [int(CasosTemp), int(PoblaTemp), int(CodDest)]
            )
            #eliminando la comuna que no se mantendra
            cursor.execute(
                """DELETE FROM CASOS_POR_COMUNA WHERE CodigoComuna=:1""", [C1])
            connection.commit()
            print("Comunas combinadas de manera exitosa.\n")
        else:
            print("Debe seleccionar entre 1 (que se unan en la 1era comuna ingresada) o 2 (union en la 2da comuna ingresada).\n")
            return

def combinar_regiones(CodigoPrimera, CodigoSegunda, Elegida):
    try:
        existencia_region = False
        db = """ SELECT * FROM CASOS_POR_REGION """
        cursor.execute(db)
        fila = cursor.fetchall()
        for datos in fila:
            CodReg = datos[0]
            if int(CodigoPrimera) == int(CodReg):
                existencia_region = True
                break
    except Exception:
        print("Error en revisar la existencia de la primera region a combinar.\n")
    if (existencia_region == False):
        print("La primera region no existe, ingrese una existente o cree una nueva.\n")
        return
    
    try:
        existencia_region = False
        db = """ SELECT * FROM CASOS_POR_REGION """
        cursor.execute(db)
        fila = cursor.fetchall()
        for datos in fila:
            CodReg = datos[0]
            if int(CodigoSegunda) == int(CodReg):
                existencia_region = True
                break
    except Exception:
        print("Error en revisar la existencia de la segunda region a combinar.\n")
    if (existencia_region == False):
        print("La segunda region no existe, ingrese una existente o cree una nueva.\n")
        return
    if int(Elegida)==1:#Se juntaran en la primera region
        C2=CodigoSegunda
        C1=CodigoPrimera
    elif int(Elegida)==2:#Se juntaran en la segunda region
        C1=CodigoSegunda
        C2=CodigoPrimera
    else:
        print("Debe seleccionar entre 1 (que se unan en la 1era region ingresada) o 2 (union en la 2da region ingresada).\n")
        return
    #?Copiamos datos de la Region a eliminar, C1=REGION DESTINO, C2=REGION A ELIMINAR
    cursor.execute("""SELECT NombreRegion, Poblacion, CasosConfirmados FROM CASOS_POR_REGION WHERE CodigoRegion=:1""", [C2])
    NameTemp,PoblaTemp, CasosTemp= cursor.fetchone()
    print("Copiando datos desde la region de",NameTemp,"...\n")
    #Colocamos los datos en la region de destino
    cursor.execute(
        """
        UPDATE CASOS_POR_REGION
        SET CasosConfirmados=CasosConfirmados+ :1, Poblacion=Poblacion+:2
        WHERE CodigoRegion= :3
        """, [int(CasosTemp), int(PoblaTemp), int(C1)]
        )
    #actualizamos los datos de las comunas, las comunas de la region a eliminar, se a??aden en la comuna de destino
    cursor.execute(
        """
        UPDATE CASOS_POR_COMUNA
        SET CodigoRegion=:1, CodigoComuna=(CodigoComuna-1000* :2)+(:1 *1000)+111
        WHERE CodigoRegion= :2
        """, [int(C1),int(C2)]
    )#se le debe sumar 111 al codigo comuna, para que no hayan conflictos entre los codigos de comuna y sigan el formato usado

    #eliminando la region que no se mantendra
    cursor.execute(
        """DELETE FROM CASOS_POR_REGION WHERE CodigoRegion=:1""", [C2])
    connection.commit()
    print("Regiones combinadas de manera exitosa.\n")

def contagiados_por_comuna():
    #view para comunas
    cursor.execute(
        """
        CREATE OR REPLACE VIEW CONTAGIADOS_COMUNA AS
        SELECT NombreComuna, Round(((CasosConfirmados/Poblacion)*100),2) AS CONTAGIADOS_POR_COMUNA
        FROM CASOS_POR_COMUNA
        WHERE Poblacion <> 0
        ORDER BY CONTAGIADOS_POR_COMUNA DESC
        """#se calculo directamente el porcentaje, con dos cifras decimales
    )

def contagiados_por_region():
    #view para regiones
    cursor.execute(
        """
        CREATE OR REPLACE VIEW CONTAGIADOS_REGION AS
        SELECT NombreRegion, Round(((CasosConfirmados/Poblacion)*100),2) AS CONTAGIADOS_POR_REGION
        FROM CASOS_POR_REGION
        WHERE Poblacion <> 0
        ORDER BY CONTAGIADOS_POR_REGION DESC
        """#se calculo directamente el porcentaje, con dos cifras decimales
    )

def mas_confirmados_comuna():
    #Se extraen los datos desde la tabla de origen
    try:
        cursor.execute(
            """
            SELECT * FROM CONTAGIADOS_COMUNA 
            """)
        podio=cursor.fetchmany(5)
    except Exception as err:
        print("Error al mostrar 5 comunas mas contagiadas.\n")
        return
    #se crea la tabla
    tabla = PrettyTable(["Comuna", "Porcentaje positividad [%]"])
    #se rellena la tabla
    for linea in podio:
        tabla.add_row([linea[0], linea[1]])
    #se muestra la tabla
    print(tabla)


def mas_confirmados_region():
    #Se extraen los datos desde la tabla de origen
    try:
        cursor.execute(
            """
            SELECT * FROM CONTAGIADOS_REGION 
            """)
        podio = cursor.fetchmany(5)
    except Exception as err:
        print("Error al mostrar 5 regiones mas contagiadas.\n")
        return
    #se crea la tabla
    tabla = PrettyTable(["Regi??n", "Porcentaje positividad [%]"])
    #se rellena la tabla
    for linea in podio:
        tabla.add_row([linea[0], linea[1]])
    #se muestra la tabla
    print(tabla)

print("---------------------------------------------------------------------------------------------------------\n Bienvenido a la Base de datos Chilena del COVID-21 \n A contiuaci??n se presentan varias opciones, seleccione a traves de su n??mero cual quiere ejecutar:\n\n")

casos_totales_region("15")
casos_totales_comuna("15101")

print("Sesion terminada\n")
connection.close()
