sue=int(input("Cual es su sueldo?: "))
if sue < 10000:
    au=sue*.15
    nsue=au+sue
    print(f"El aumento del sueldo es de ${au} y el sueldo total del trabajador es ${nsue}")
if sue <=15000 and sue>=10000:
    au=sue*.11
    nsue=au+sue
    print(f"El aumento del sueldo es de ${au} y el sueldo total es de ${nsue}")
if sue > 15000:
    au=sue*.8
    nsue=au+sue
    print(f"El aumento del sueldo es de ${au} y el sueldo final es de ${nsue}")
    
