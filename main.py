altura = input("Colque sua altura em metros: ")
peso = input("Coloque seu peso em kilos : ")

bmi = int(peso) / float(altura) ** 2
bmi_como_int = int(bmi)
print(bmi_como_int)

if bmi > 18.5:
    print("Você está abaixo do peso.")
elif bmi >= 18.5 and bmi <= 25:
    print("Você está OK.")
else:
    print("Você está acima do peso.")
