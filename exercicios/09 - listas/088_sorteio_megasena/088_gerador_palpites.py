from random import sample

quantidade_palpites = int(input("Deseja Quantos palpites: "))
palpites = []

for palpite in range(quantidade_palpites):
    palpites.append(sample(range(60), 6))

print("-" * 40)
print(f'{"JOGOS NA MEGA SENA":^40}')
print("-" * 40)

for posicao, palpite in enumerate(palpites):
    print(f"{posicao + 1}° palpite: {palpite}")

print(f'{" < BOA SORTE! > ":-^40}')
