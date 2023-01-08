def notas(*nota, sit=False):
    '''Funçáo para analisar notas e situaçóes de vários alunos.
        :param n: uma ou mais notas dos alunos (aceita várias)
        :param sit: valor opcional, indicando se deve ou nao adicionar a situação
        : return: dicionário con várias infornaçóes sobre a situaçáo da turma.'''
    dic = {}
    dic['total'] = len(nota)
    dic['maior'] = max(nota)
    dic['menor'] = min(nota)
    dic['media'] = sum(nota) / len(nota)
    if sit == True:
        if dic['media'] > 6:
            dic['situação'] = 'Ótima'
        elif dic['media'] > 4:
            dic['situação'] = 'Boa'
        else:
            dic['situação'] = 'Ruim'
    return dic


print(notas(5.5, 9.5, 10, 6.5, sit=True))
help(notas)
