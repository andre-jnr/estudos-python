sal = float(input("Qual o seu sálario:"))
if sal >= 1250.00:
    nsal = sal + (sal*0.10)
    print(f"Seu novo salário vai ser {nsal:.2f}")
else:
    nsal = sal + (sal*0.15)
    print(f"Seu novo salário vai ser {nsal:.2f}")
