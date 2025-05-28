def dd_to_dms(dd):
    grados = int(dd)
    minutos = int((dd - grados) * 60)
    segundos = (dd - grados - minutos / 60) * 3600
    return grados, minutos, segundos

def dms_to_dd(grados, minutos, segundos):
    return grados + minutos / 60 + segundos / 3600

def main():
    print("Conversión de coordenadas")
    print("1. Grados decimales a grados, minutos y segundos")
    print("2. Grados, minutos y segundos a grados decimales")
    option = input(">>")

    if option == "1":
        lat_dd = float(input("Ingrese la latitud en grados decimales: "))
        lon_dd = float(input("Ingrese la longitud en grados decimales: "))
        lat_dms = dd_to_dms(lat_dd)
        lon_dms = dd_to_dms(lon_dd)
        print(f"Latitud: {lat_dms[0]}° {lat_dms[1]}' {lat_dms[2]:.4f}\" N")
        print(f"Longitud: {lon_dms[0]}° {lon_dms[1]}' {lon_dms[2]:.4f}\" E")

    elif option == "2":
        lat_grados = int(input("Ingrese la latitud en grados: "))
        lat_minutos = int(input("Ingrese los minutos de la latitud: "))
        lat_segundos = float(input("Ingrese los segundos de la latitud: "))
        lon_grados = int(input("Ingrese la longitud en grados: "))
        lon_minutos = int(input("Ingrese los minutos de la longitud: "))
        lon_segundos = float(input("Ingrese los segundos de la longitud: "))
        lat_dd = dms_to_dd(lat_grados, lat_minutos, lat_segundos)
        lon_dd = dms_to_dd(lon_grados, lon_minutos, lon_segundos)
        print(f"Latitud: {lat_dd:.6f}° N")
        print(f"Longitud: {lon_dd:.6f}° E")

    else:
        print("Opción no válida")

if __name__ == "__main__":
    main()