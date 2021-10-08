# Definindo uma Url de exemplo
url = r'bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real'

# Definindo a posição de '?' para poder separar a base e os parametros da url, usando o metodo find
indice_interrogacao = url.find('?')
url_base = url[:indice_interrogacao]
url_parametros = url[indice_interrogacao + 1:]

# Busca o valor de um parametro
parametro_busca = 'moedaOrigem'
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1

indice_e_comercial = url_parametros.find('&', indice_valor)  # Procura o & depois do indice_valo. -1 caso não encontre

# Verifica se há & depois do indice valor
if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor: indice_e_comercial]

# Prints
# print(url)
# print(url_base)
print(url_parametros)
print(valor)
