# [ ] listas
# ( ) Tuplas
# { } Dicionarios

usuarios_data_science = [15, 23, 43, 56]
usuarios_machine_learning = [13, 23, 56, 42]

# Nós podemos copiar uma listas usando o .Copy(). OBS: Ele não vai "copiar" aquela lista... vai fazer tipo uma "sombra" daqueles objetos
assistiram = usuarios_data_science.copy()
assistiram.extend(usuarios_machine_learning)
# print(assistiram)
# print(len(assistiram))

#--------------------------------------------------------------------------------#
# Para representar um "Conjunto" no Python temos o "Set"
# Ele é representado por vários elementos sem repetir os elementos
# print(set(assistiram))
#
# seq = [4, 1, 2, 3, 1]
# print(set(seq))

#--------------------------------------------------------------------------------#

# Um "Conjunto" é representado por "{}" e podemos transformar um lista, por exemplo, um "Conjunto" usando a palava "Set"

usuarios_data_science = {15, 23, 43, 56}
usuarios_machine_learning = {13, 23, 56, 42}

# print(usuarios_machine_learning)

#--------------------------------------------------------------------------------#

# Se eu quiser acessar a posição dentro de um conjunto, eu não consigo. Porque, dentro do Conjunto não existe a indexação.

# print(usuarios_machine_learning[3]) # Vai dá Erro


#--------------------------------------------------------------------------------#

# Mas, você pode interar como qualquer interavel

# for usuario in set(assistiram):
#     print(usuario)

#--------------------------------------------------------------------------------#

# Essa é operação do "OU"
# Nós temos a união de 2 Conjutos
# print(usuarios_data_science | usuarios_machine_learning) # Essa "|(Barra)" significa "OU", nós chamamos de pipe.

#--------------------------------------------------------------------------------#

# Essa é operação do "E"
# Nós pegamos tanto o elemento de um conjunto... quanto do outro.
# print(usuarios_data_science & usuarios_machine_learning) # Esse "&" siginica "E"

#--------------------------------------------------------------------------------#

# print(usuarios_data_science - usuarios_machine_learning)

#--------------------------------------------------------------------------------#

fez_ds_mas_nao_fez_ml = usuarios_data_science - usuarios_machine_learning
# print(23 in fez_ds_mas_nao_fez_ml)

#--------------------------------------------------------------------------------#
# Esse aqui é o "OU exclusivo"
# print(usuarios_data_science ^ usuarios_machine_learning)

#--------------------------------------------------------------------------------#

# Um Conjunto no Python ele é mútavel
usuarios = {1, 5, 76, 34, 52, 13, 17}
# print(len(usuarios))

# Nós conseguimos adicionar mais elementos atraves do Add, diferente de um append que adiciona no final.
# O conjunto ele não tem uma posição certa. Ele só está lá dentro, com as posições que ele coloca.
usuarios.add(89)
# print(len(usuarios))
#
# print(usuarios)

#--------------------------------------------------------------------------------#

# Nós conseguimos deixar um conjunto imútavel.
# Vamos "congelar" ele.

usuarios = frozenset(usuarios)
# print(type(usuarios))

# Vai derro. Porque, o Frozen set é diferente de uma Set. Ele não pode adicionar.
# usuarios.add(12)

#--------------------------------------------------------------------------------#

# Conseguimo usar Conjuntos também com objetos, strings. etc.

# meu_texto = "Bem vindo meu nome é Thiago eu gosto muito de nomes e tenho um cachorro"

# print(set(meu_texto.split()))

#--------------------------------------------------------------------------------#

# Dicionários

aparicoes = {"Thiago": 1,"Cachorro": 2,"Nome": 2,"Vindo": 1}

# print(aparicoes["Cachorro"])
#
# print(aparicoes.get("xpto", 0))

#--------------------------------------------------------------------------------#

# Forma de criar um dicionário pelo construtor

aparicoes2 = dict(Thiago = 2, Cachorro = 1)
# print(aparicoes2)

#--------------------------------------------------------------------------------#

# Adicionando novos elementos

aparicoes["Carlos"] = 1
# print(aparicoes)

#--------------------------------------------------------------------------------#

# Removendo elementos

del aparicoes["Carlos"]
# print(aparicoes)

#--------------------------------------------------------------------------------#

# Verificando se tem o elemento dentro do dicionario

# print("Cachorro" in aparicoes)

#--------------------------------------------------------------------------------#

# Como passar por todos os elementos

# for elemento in aparicoes:
#     print(elemento)



#--------------------------------------------------------------------------------#

# Como passar pelas chaves e valores:

# Vou passar pelas Chaves
# for elemento in aparicoes.keys():
#     print(elemento)

# Vou passsar pelos Elementos
# for elemento in aparicoes.values():
#     print(elemento)

#--------------------------------------------------------------------------------#

#Verifica se 1 está dentro de alguma chave
# print(1 in aparicoes.values())

#--------------------------------------------------------------------------------#

# Como posso fazer para passar pelas chaves e valor ao mesmo tempo?

# Versão comum
# for elemento in aparicoes.keys():
#     valor = aparicoes[elemento]
#     print(elemento, valor)


# Versao que se utiliza normalmente
# for elemento in aparicoes.items():
#     print(elemento)


#--------------------------------------------------------------------------------#


# Nós podemos desempacotar esse dicionario também

# for chave, valor in aparicoes.items():
#     print(chave, valor)

# --------------------------------------------------------------------------------#

meu_texto = "Bem vindo meu nome é Thiago eu gosto muito de nomes e tenho um cachorro thiago"
meu_texto = meu_texto.lower()

aparicoes = {}

# for palavra in meu_texto.split():
#     ate_agora = aparicoes.get(palavra, 0)
#     aparicoes[palavra] = ate_agora + 1
#
#
# print(aparicoes)

# --------------------------------------------------------------------------------#

# Vamos usar agora o DefaultDict *Dicionario padrão*

# from collections import defaultdict
#
# aparicoes = defaultdict(int)
#
# for palavra in meu_texto.split():
#     ate_agora = aparicoes[palavra]
#     aparicoes[palavra] = ate_agora + 1
#
#
# print(aparicoes)

# --------------------------------------------------------------------------------#

# vamos tentar simplicar nosso codigo mais ainda

from collections import defaultdict
#
# aparicoes = defaultdict(int)
#
# for palavra in meu_texto.split():
#     aparicoes[palavra] += 1
#
# print(aparicoes)

# Qual é o outro poder do DefaultDict? É que nós podemos usar com outras coisas.

# class Conta:
#     def __init__(self):
#         print("Criando conta..")
#
# contas = defaultdict(Conta)
# print(contas[15])


from collections import Counter
#
# aparicoes = Counter(meu_texto.split())
# print(aparicoes)

# --------------------------------------------------------------------------------#

# Testando o uso de diversas coleções

texto1 = """
Já aconteceu de você preencher um formulário de cadastro em algum site, e o navegador já sugerir quais são suas informações de nome completo, endereço e celular? Ou após você pesquisar sobre algum produto, começar a ver anúncios sobre ele em vários sites? Saiba que nada disso acontece do nada! Essas informações são salvas propositalmente no que chamamos de armazenamento de dados locais. Esse armazenamento é composto por APIs do JavaScript que permitem salvar informações no navegador da pessoa usuária (client side) para diversas finalidades, podendo ser para melhorar a experiência da pessoa usuária, ou até mesmo viabilizar o funcionamento de uma aplicação.

Este é um assunto que vale muito a atenção para você, pessoa desenvolvedora Front-end, se aprofundar e dominar, então vamos abordar neste artigo quais são os principais armazenadores de dados do navegador utilizados atualmente.

O primeiro deles é o localStorage, ele guarda informações de forma persistente no navegador, ou seja, mesmo após você fechar e abrir o navegador, as informações vão continuar salvas. O seu armazenamento máximo é em média 5MB, podendo variar dependendo do navegador utilizado. Este limite de armazenamento pode ser aumentado pela pessoa usuária quando necessário, no entanto apenas alguns navegadores suportam isso.

O localStorage salva dados do tipo string texto, sendo ideal para salvar, por exemplo, informações de login ou de um formulário padrão, porém essas informações coletadas geralmente estão inseridas em objetos no JavaScript. Nesse caso, é preciso utilizar JSON com o método JSON.stringify() para transformar esse objeto em uma string, antes de enviá-lo para o localStorage, como no exemplo abaixo:
"""

texto2 = """
PAULO SILVEIRA:
Python é uma linguagem de programação cada vez mais na moda e não é de agora, né, Guilherme?

GUILHERME SILVEIRA:
É, já tem alguns anos que vem crescendo a adoção de python no mercado e, o que é muito legal também, é que antes da gente utilizar no mercado, é muito fácil de você utilizar dentro de casa em coisas suas do dia a dia, para se acostumar, caso você ainda não esteja programando.

PAULO SILVEIRA:
Pois é, porque muita gente vai para o python por causa da web e os frameworks famosos da web como Django ou Flask, ou por causa do Data Science, por causa do socket learning, ou panda ou numpy. Mas se você está interessado no Python, a grande sacada é que pode usar como uma linguagem de script e aprender de uma maneira muito mais tranquila, ao invés de já cair nesse mundo de um monte de bibliotecas.

"""

def analisa_frequencia_de_letras(texto):
    aparicoes = Counter(texto.lower())
    total_de_caracteres = sum(aparicoes.values())

    proporcoes = [(letra, frequencia / total_de_caracteres) for letra, frequencia in aparicoes.items()]
    proporcoes = Counter(dict(proporcoes))
    mais_comuns = proporcoes.most_common(10)
    for caractere, proporcao in mais_comuns:
        print("{} => {:.2f}%".format(caractere, proporcao * 100))


analisa_frequencia_de_letras(texto1)








