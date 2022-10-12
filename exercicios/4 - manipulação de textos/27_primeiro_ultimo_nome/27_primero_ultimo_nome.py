nomec = input("Digite seu nome completo:").strip().capitalize()
nomes = nomec.split()
print('Prazer em conhecer-lo!')
print(f'Seu primeiro nome é {nomes[0]}')
print(f'Seu último nome é {nomes[-1]}')

#print(f'Seu último nome é {len(nomes) - 1})