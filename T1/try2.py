regiones_archivo = open("RegionesComunas.csv", "r")
comunas_archivo = open("CasosConfirmadosPorComuna.csv", "r")

for linea_leida, otra_linea in regiones_archivo, comunas_archivo:
    NombreRegion, CodigoRegion, CodigoComuna = linea_leida.strip(
        "\n").split(",")
    NombreComuna, CodigoComuna, Poblacion, CasosConfirmados = linea_leida.strip(
        "\n").split(",")
    print("Region=", NombreRegion, "Comuna=", NombreComuna)
"""
for linea_leida in comunas_archivo:
    NombreComuna, CodigoComuna, Poblacion, CasosConfirmados = linea_leida.strip("\n").split(",")
"""
regiones_archivo.close()
comunas_archivo.close()
