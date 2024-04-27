# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados
from salvando_classe_em_json_a import CAMINHO_ARQUIVO,LavaJatoDoTonhao
import json 

with open(CAMINHO_ARQUIVO,'r') as arquivo:
    meses = json.load(arquivo)
    mes_1 = LavaJatoDoTonhao(**meses[0])
    mes_2 = LavaJatoDoTonhao(**meses[1])
    mes_3 = LavaJatoDoTonhao(**meses[2])
    mes_4 = LavaJatoDoTonhao(**meses[3])

    print(mes_1.funcionarios,mes_1.preco)
    print(mes_2.funcionarios,mes_2.preco)
    print(mes_3.funcionarios,mes_3.preco)
    print(mes_4.funcionarios,mes_4.preco)