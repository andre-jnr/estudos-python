valores = []
for i in range(0, 5):
    usuario = int(input('Digite um valor: '))
    if i == 0 or usuario > valores[-1]:
        valores.append(usuario)
    else:
        for posicao, valor in enumerate(valores):
            if valor >= usuario:
                valores.insert(posicao, usuario)
                break
print(valores)
