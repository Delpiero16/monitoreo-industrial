LIMITE_ALERTA_GLOBAL = 85.0 

def mostrar_encabezado():
    print("========================================")
    print("    SISTEMA DE MONITOREO INDUSTRIAL     ")
    print("========================================")

def validar_temperatura(temp_actual):
    if temp_actual > LIMITE_ALERTA_GLOBAL:
        return True
    return False

mostrar_encabezado()
lectura_sensor = float(input("Ingrese la temperatura del motor (°C): "))

if validar_temperatura(lectura_sensor):
    print("¡PELIGRO! Temperatura excede el límite operativo.")
else:
    print("Estado del motor: Operativo y estable.")