
peso = float(input("Insira o seu peso em kg: "))
altura = float(input("Insira a sua altura em metros e utilize . para separar os cm(exemplo: 1.70): "))

imc = peso / (altura ** 2)

imc = round(imc, 2)

print("Seu IMC é: ", imc)

if imc < 18.5:
    print("Você está abaixo do peso ideal.")
elif imc >= 18.5 and imc <= 24.9:
    print("Seu peso está dentro do ideal.")
elif imc >= 25 and imc <= 29.9:
    print("Você está acima do peso ideal.")
else:
    print("Você está com obesidade.")
