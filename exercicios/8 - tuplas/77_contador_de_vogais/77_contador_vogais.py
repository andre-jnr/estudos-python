palavras = ('estudar', 'trabalhar', 'viver', 'feliz', 'sobreviver')

for palavra in range(0, len(palavras)):
    print(f' \nA palavra {palavras[palavra]} tem: ', end='')
    for vogal in palavras[palavra]:
        if vogal == 'a' or vogal == 'e' or vogal == 'i' or vogal == 'o' or vogal == 'u':
            print(vogal, end=' ')
