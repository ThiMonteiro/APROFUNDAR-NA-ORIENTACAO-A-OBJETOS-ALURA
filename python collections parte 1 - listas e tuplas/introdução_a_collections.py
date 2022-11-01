idade1 = 39
idade2 = 30
idade3 = 27
idade4 = 18

# print(idade1)
# print(idade2)
# print(idade3)
# print(idade4)

idades = [39, 30, 27, 18]


# tamanho da lista
# print(len(idades))
#
#
# # imprime a lista toda
# print(idades)
#
#
# # imprime um valor colocando a posição
# print(idades[2])
#
#
# # para adicionar um valor a lista
# idades.append(15)
# print(idades)
#
#
# # para passar por cada idade dentro da lista
# for idade in idades:
#     print(idade)
#
#
# # remove um valor dentro da lista
# idades.remove(30)
# print(idades)
#
#
# # vou adicionar mais um valor 27
# idades.append(27)
#
#
# # vou remover a primeira aparição do 27
# idades.remove(27)
# print(idades)
#
#
# # vai remover todos os elementos da lista
# # idades.clear()
# # print(idades)
#
#
# # vai verificar se o 28 está dentro de idades - no caso 28 não está, então é False
# print(28 in idades)
#
#
# # uma codição que vai remover o 15 se ele estiver dentro da lista
# if 15 in idades:
#     idades.remove(15)
# print(idades)
#
# # vai adicionar um valor na posição desejada
# idades.insert(0, 20)
# print(idades)
#
# # ele vai adicionar mais de um valor em nossa lista - ele vai extender a nossa lista
# idades.extend([27,19])
# print(idades)
#
#
#
# # vou criar uma array/lista que vai receber as idades do ano que vem
# idades_no_ano_que_vem = []
# for idade in idades:
#     idades_no_ano_que_vem.append(idade + 1)
# print(idades_no_ano_que_vem)
#
#
# # uma for mais simples de adicionar mais um ano nas idades - compreensao de listas/list compreensions
# idades_no_ano_que_vem = [idade + 1 for idade in idades]
# print(idades_no_ano_que_vem)
#
#
# # vai pegar todas as idades que forem maior que 21
# print([idade for idade in idades if idade > 21])
#
#
# def faz_processamento_de_visualizacao(lista = None):
#     if lista == None:
#         lista = list()
#     else:
#         print(len(lista))
#         print(lista)
#
#
# idades = [1, 3, 53]
# faz_processamento_de_visualizacao(idades)

#---------------------------------------------------------------------------------#
# Objetos próprios


# Classe Conta Corrente
class ContaCorrente:
    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return "[>>Codigo {} Saldo {}<<]".format(self.codigo, self.saldo)


# conta do Thiago
conta_do_thi = ContaCorrente(15)
conta_do_thi.deposita(500)
# print(conta_do_thi)

# conta da Rhebeca
conta_da_rhe = ContaCorrente(47685)
conta_da_rhe.deposita(1000)
# print(conta_da_rhe)


# contas = [conta_do_thi, conta_da_rhe]
# for conta in contas:
#     print(conta)


def deposita_para_todas(contas):
    for conta in contas:
        conta.deposita(100)


contas = [conta_do_thi, conta_da_rhe]
deposita_para_todas(contas)
# print(contas[0], contas[1])

# Tuplas são imutaveis. Não podem ser modificadas.

thiago = ("Thiago", 18, 2004) # tupla()/paranteses
rhebeca = ("Rhebeca", 18, 2004) # tupla()/paranteses
# pedro = (39, "Pedro", 1979) #ruim



def depoista(conta): # variação "funcional" (separando o comportamento dos dados)
    novo_saldo = conta[1] + 100
    codigo = conta[0]
    return (codigo, novo_saldo)


conta_do_thi = (15, 1100)
# print(conta_do_thi)
# print(depoista(conta_do_thi))

usuarios = [thiago, rhebeca]
# print(usuarios)
# usuarios.append(("Paulo", 39, 1979))
# print(usuarios)


conta_do_thi = ContaCorrente(15)
conta_do_thi.deposita(500)


conta_da_rhe = ContaCorrente(23649)
conta_da_rhe.deposita(1000)


# contas = (conta_do_thi, conta_da_rhe)
# for conta in contas:
#     # print(conta)

#---------------------------------------------------------------------------------#

# Herança e Polimorfismo

from abc import ABCMeta, abstractmethod

# Classe Conta
class Conta(metaclass=ABCMeta):
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    @abstractmethod
    def passa_o_mes(self):
        pass

    def __str__(self):
        return "[>>Codigo {} Saldo {}<<]".format(self._codigo, self._saldo)


class ContaCorrente(Conta):
    def passa_o_mes(self):
        self._saldo -= 2


class ContaPoupanca(Conta):
    def passa_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3


class ContaInvestimento(Conta):
    pass


conta16 = ContaCorrente(16)
conta16.deposita(1000)
conta16.passa_o_mes()
# print(conta16)


conta17 = ContaPoupanca(17)
conta17.deposita(1000)
conta17.passa_o_mes()
# print(conta17)


# contas = [conta16, conta17]
# for conta in contas:
#     conta.passa_o_mes()
#     print(conta)

import array as arr

# print(arr.array('d', [1, 3.5]))

# import numpy as np

# numeros = np.array([1, 3.5])
# print(numeros)

# soma = numeros + 3

# print(soma)


# class ContaSalario:
#     def __init__(self, codigo):
#         self._codigo = codigo
#         self._saldo = 0
#
#     def __eq__(self, other):
#         if type(other) != ContaSalario:
#             return False
#
#         return self._codigo == other._codigo and self._saldo == other._saldo
#
#
#     def deposita(self, valor):
#         self._saldo += valor
#
#     def __str__(self):
#         return "[>> Codigo {} Saldo {}]".format(self._codigo, self._saldo)


# conta1 = ContaSalario(37)
# print(conta1)

# conta2 = ContaSalario(37)
# print(conta2)

# Não são iguais. Porque, o objeto pode ser o mesmo, mas a referencia de memoria é diferente.
# print(conta1 == conta2)

#---------------------------------------------------------------------------------#

# idades = [15, 87, 65, 56, 32, 49, 37, 16]

# for c in range(len(idades)):
#     print(c, idades[c])

# for i, v in enumerate(idades):
#     print(f"Index {i} = Idade {v}")


# print(list(range(len(idades)))) # forcei a geração de valores

# print(list(enumerate(idades)))

# Tupla
# idades1 = (15, 87, 65, 56, 32, 49, 37, 16)
# # Uma for de desempacotar as tuplas
# for indice, idade in enumerate(idades1): # unpacking(desempacotar) da nossa tupla
#     print(indice, idade)


# Lista
idades2 = [15, 87, 65, 56, 32, 49, 37, 16]

# Vai fazer o for me passando o indice e idade, dos elementos na lista
# for indice, idade in enumerate(idades2):
#     print(indice, idade)



usuarios = [
    ("Thiago", 18, 2004),
    ("Rhebeca", 37, 1981),
    ("Paulo", 20, 2002)
]
# uma for de desempacotar é passando os nomes para a posição que você deseja.
# for nome, _, _ in usuarios: # "_" significa "Tô nem aí para 1º e 2º posição. Eu quero somente a primeira."
#     print(nome)


# for nome, idade, nascimento in usuarios: # dessa forma é mais legivel que de cima ^^ mas funciona dessa forma
#     print(nome, idade, nascimento)


#---------------------------------------------------------------------------------#



# Ordena em sequência
# print(sorted(idades2))


# Ordena a sequência ao contrario
# print(list(reversed(idades2)))


# Ordena ao contrario e organiza a lista do menor para maior
# print(list(reversed(sorted(idades2))))

# Organiza a lista chamando a função
# idades2.sort()
# print(idades2)

from functools import total_ordering

@total_ordering
class ContaSalario:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0


    def deposita(self, valor):
        self._saldo += valor


    def __str__(self):
        return "[>> Codigo {} Saldo {}]".format(self._codigo, self._saldo)

    def __eq__(self, other):
        if type(other) != ContaSalario:
            return False

        return self._codigo == other._codigo and self._saldo == other._saldo


    def __lt__(self, other):
        if self._saldo != other._saldo:
            return self._saldo < other._saldo

        return self._codigo < other._codigo




# conta_do_thiago = ContaSalario(17)
# conta_do_thiago.deposita(500)
#
# conta_da_rhebeca = ContaSalario(3)
# conta_da_rhebeca.deposita(1000)
#
# conta_da_julia = ContaSalario(133)
# conta_da_julia.deposita(510)
#
# contas = [conta_da_julia, conta_do_thiago, conta_da_rhebeca]

# for conta in contas:
#     print(conta)

# Um método customizado de como pegar os valores do menor para o maior. (obs: só que esse método é muito feio, porque, eu estou pegando um método privado)
# def extrai_saldo(conta):
#     return conta._saldo
#
# for conta in sorted(contas, key=extrai_saldo):
#     print(conta)

# from operator import attrgetter
#
# for conta in sorted(contas, key=attrgetter("_saldo")):
#     print(conta)

# print(conta_do_thiago > conta_da_rhebeca)
#
# for conta in sorted(contas, reverse=True):
#     print(conta)

# conta_do_thiago = ContaSalario(1700)
# conta_do_thiago.deposita(500)
#
# conta_da_rhebeca = ContaSalario(3)
# conta_da_rhebeca.deposita(500)
#
# conta_da_julia = ContaSalario(133)
# conta_da_julia.deposita(1000)
#
# contas = [conta_do_thiago, conta_da_rhebeca, conta_da_julia]
#
# for conta in sorted(contas, key=attrgetter("_saldo", "_codigo")):
#     print(conta)
#
# print(conta_do_thiago == conta_do_thiago)
