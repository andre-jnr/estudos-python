from random import randint
print("Você vai ter que advinhar o número")
n = randint(0,5)

try:
    ne = int(input("Digite um número de 0 á 5:"))
    if ne == n:
        print(" ")
        print("PARABÉNS! Sorte no jogo, azar no amor kkkk")
    else:
        print(" ")
        print("Errouuuu")
        print(f"O número escolhido foi {n}")

except:
    print("Apenas números seu burro!")
