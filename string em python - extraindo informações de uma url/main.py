# url = "bytebank.com/cambio?moedaOrigem=real&quantidade=100&moedaDestino=dolar"
url = " "

# Sanitização da URL
url = url.strip()


# validação da URL
if url == "":
    raise ValueError("A URL está vazia")


# Separa base e os parâmetros
indice_interrogacao = url.find('?')
url_base = url[:indice_interrogacao]
url_parametros = url[indice_interrogacao+1:]
print(url_parametros)


# Busca o valor de um parâmetro
parametro_busca = "quantidade"
indice_parametro = url_parametros.find(parametro_busca) # encontra o indice do meu parametro
indice_valor = indice_parametro + len(parametro_busca) + 1 # encontra o indice do meu valor
indice_e_comercial = url_parametros.find('&', indice_valor) # encontra o indice do meu & comercial

# vai verificar se existe um & comercial dentro daquela string
if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]

print(valor)
