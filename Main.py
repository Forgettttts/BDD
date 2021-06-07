regiones_archivo=open("RegionesComunas.csv","r")
comunas_archivo=open("CasosConfirmadosPorComuna.csv", "r")
for linea_leida in regiones_archivo:
    NombreRegion, CodigoRegion, CodigoComuna=linea_leida.strip("\n").split(",")

for linea_leida in comunas_archivo:
    Comuna, CodigoComuna, Poblacion, CasosConfirmados = linea_leida.strip("\n").split(",")

regiones_archivo.close()
comunas_archivo.close()
