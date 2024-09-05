hora1 = int(input("Hora1: "))
min1 = int(input("Minuto1: "))
hora2 = int(input("Hora2: "))
min2 = int(input("minuto2: "))
hora_excedente = (min1 + min2) // 60
minuto_final = (min1 + min2) % 60
hora_final = hora1 + hora2 + hora_excedente + 12
if (hora_final < 0 or hora_final > 12):
    hora_excedente = (min1 + min2) // 60
    minuto_final = (min1 + min2) % 60
    hora_final = hora1 + hora2 + hora_excedente + 12
    hora_final = hora_final - 12 - 24
    if hora_final < 0:
        hora_final *= -1
    if hora_final > 12:
        hora_final -= 12
    print(f"entrada 1: {hora1}:{min1}")
    print(f"entrada 2: {hora2}:{min2}")
    print(f"saida : {hora_final}:{minuto_final}")
else:
    print(f"entrada 1: {hora1}:{min1}")
    print(f"entrada 2: {hora2}:{min2}")
    print(f"saida : {hora_final}:{minuto_final}")
