mon = float(input("Monto total del vehículo:$"))
engan = mon * 0.35
prest = mon - engan
mens = prest / 18

print(f"El importe del engache es de: ${engan}")
print(f"El precio total actualizado es de: ${prest}")
print(f"El pago correspondiente a 18 mensualidades es de: ${mens}")


