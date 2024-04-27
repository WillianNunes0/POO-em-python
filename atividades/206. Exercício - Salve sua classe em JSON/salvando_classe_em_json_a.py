# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json

class LavaJatoDoTonhao:
    fundada = 2001
    def __init__(self,preco,funcionarios):
        
        self.preco = preco
        self.funcionarios = funcionarios

mes_1 = LavaJatoDoTonhao(30,5)
mes_2 = LavaJatoDoTonhao(40,4)
mes_3 = LavaJatoDoTonhao(45,6)
mes_4 = LavaJatoDoTonhao(50,6)
meses = [vars(mes_1),vars(mes_2),vars(mes_3),vars(mes_4)]

CAMINHO_ARQUIVO = 'meses.json'
with open(CAMINHO_ARQUIVO,'w') as arquivo:
    json.dump(meses,arquivo,ensure_ascii=False,indent=2)
    