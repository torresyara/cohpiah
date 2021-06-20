import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

'''
Funções implementadas.
'''

def separa_palavras_texto(texto):
    '''Essa função recebe um texto e devolve uma lista das palavras utilizadas no total'''
    lista_sentencas = separa_sentencas(texto)

    lista_frases = []
    for sentenca in lista_sentencas:
        frases = separa_frases(sentenca) 
        for frase in frases:
            lista_frases.append(frase)
            
    lista_palavras = []
    for frase in lista_frases:
        palavras = separa_palavras(frase)
        for palavra in palavras:
            lista_palavras.append(palavra)
        
    return lista_palavras

def tamanho_médio_palavras(texto):
    '''A função recebe um texto e devolve a média simples do número de caracteres por palavra (soma os tamanhos das palavras e divide pelo número total de palavras)'''
    lista_palavras = separa_palavras_texto(texto)
    caracteres = 0

    for palavra in lista_palavras:
        caracteres = caracteres + len(palavra)
    
    return caracteres / len(lista_palavras)

def type_token(texto):
    '''Recebe um texto e devolve o número de palavras diferentes divididas pelo total de palavras'''
    lista_palavras = separa_palavras_texto(texto) 

    return n_palavras_diferentes(lista_palavras) / len(lista_palavras)

def hapax(texto):
    '''Recebe um texto e devolve o número de palavras que aparecem uma única vez dividido pelo número total de palavras'''
    lista_palavras = separa_palavras_texto(texto) 

    return n_palavras_unicas(lista_palavras) / len(lista_palavras) 

def tamanho_médio_sentença(texto): 
    '''Recebe um texto e devolve a a soma dos números de caracteres em todas as sentenças dividida pelo número de sentenças'''
    lista_sentencas = separa_sentencas(texto)
    caracteres = 0
    for sentenca in lista_sentencas:
        caracteres = caracteres + len(sentenca)

    return caracteres / len(lista_sentencas)

def média_frases_por_sentenças(texto): 
    '''Recebe um texto e devolve o número total de frases dividido pelo número de sentenças'''
    numero_sentencas = len(separa_sentencas(texto))

    lista_sentencas = separa_sentencas(texto)
    lista_frases = []
    for sentenca in lista_sentencas:
        frases = separa_frases(sentenca) 
        for frase in frases:
            lista_frases.append(frase)

    numero_frases = len(lista_frases)

    return numero_frases / numero_sentencas

def tamanho_médio_frase(texto): 
    '''Recebe um texto e devolve a soma do número de caracteres em cada frase dividido pelo número de frases do texto'''

    lista_sentencas = separa_sentencas(texto)
    lista_frases = []
    for sentenca in lista_sentencas:
        frases = separa_frases(sentenca) 
        for frase in frases:
            lista_frases.append(frase)
            
    caracteres = 0
    for frase in lista_frases:
        caracteres = caracteres + len(frase)

    return caracteres / len(lista_frases)


def calcula_assinatura(texto):
    '''Essa funcao recebe um texto e devolve a assinatura do texto.'''
    wal_calculado = tamanho_médio_palavras(texto)
    ttr_calculado = type_token(texto)
    hlr_calculado = hapax(texto)
    sal_calculado = tamanho_médio_sentença(texto)
    sac_calculado = média_frases_por_sentenças(texto)
    pal_calculado = tamanho_médio_frase(texto)

    return [wal_calculado, ttr_calculado, hlr_calculado, sal_calculado, sac_calculado, pal_calculado]


def compara_assinatura(as_a, as_b):
    '''Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    wal_diferença = abs(as_b[0] - as_a[0])
    ttr_diferença = abs(as_b[1] - as_a[1])
    hlr_diferença = abs(as_b[2] - as_a[2])
    sal_diferença = abs(as_b[3] - as_a[3])
    sac_diferença = abs(as_b[4] - as_a[4])
    pal_diferença = abs(as_b[5] - as_a[5])

    grau_similaridade = (wal_diferença + ttr_diferença + hlr_diferença + sal_diferença + sac_diferença + pal_diferença) / 6

    return grau_similaridade


def avalia_textos(textos, ass_cp):
    '''Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    lista_assinaturas = list()
    lista_graus_similaridade = list()

    for texto in textos: 
        lista_assinaturas.append(calcula_assinatura(texto))
    for assinatura in lista_assinaturas: 
        lista_graus_similaridade.append(compara_assinatura(assinatura, ass_cp))

    return lista_graus_similaridade.index(min(lista_graus_similaridade)) + 1 

