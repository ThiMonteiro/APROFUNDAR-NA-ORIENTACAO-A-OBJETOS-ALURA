endereco = "Rua onze, 46, casa, Itaguai, Rio de Janeiro, RJ, 23820-405"

import re # Regular Expression -- RegEx

padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")

busca = padrao.search(endereco) # Match

if busca:
    cep = busca.group()
    print(cep)









