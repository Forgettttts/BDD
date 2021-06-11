regiones_archivo = open("RegionesComunas.csv", "r")
comunas_archivo = open("CasosConfirmadosPorComuna.csv", "r")

for linea_leida in regiones_archivo:
    NombreRegion, CodigoRegion, CodigoComuna = linea_leida.strip(
        "\n").split(",")
    print(NombreRegion)
    break
