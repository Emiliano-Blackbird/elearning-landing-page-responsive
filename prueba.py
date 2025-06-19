# def reloj
def reloj(horas, minutos, segundos):
    if horas < 0 or horas > 23:
        return "Error: Horas deben estar entre 0 y 23"
    if minutos < 0 or minutos > 59:
        return "Error: Minutos deben estar entre 0 y 59"
    if segundos < 0 or segundos > 59:
        return "Error: Segundos deben estar entre 0 y 59"

    return f"{horas:02}:{minutos:02}:{segundos:02}"
# Ejemplo de uso
if __name__ == "__main__":
    print(reloj(12, 30, 45))  # Salida: 12:30:45
    print(reloj(23, 59, 59))  # Salida: 23:59:59
    print(reloj(24, 0, 0))    # Salida: Error: Horas deben estar entre 0 y 23
    print(reloj(12, -1, 0))   # Salida: Error: Minutos deben estar entre 0 y 59
    print(reloj(12, 30, 60))  # Salida: Error: Segundos deben estar entre 0 y 59