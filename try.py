regiones_archivo = open("RegionesComunas.csv", "r")
comunas_archivo = open("CasosConfirmadosPorComuna.csv", "r")

for linea_leida in comunas_archivo:
    NombreComuna, CodigoComuna, Poblacion, CasosConfirmados = linea_leida.strip("\n").split(",")
    print(NombreComuna)
    break
