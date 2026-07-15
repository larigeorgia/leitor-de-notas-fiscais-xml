import xmltodict
import pandas as pd
import os
import sys
from dotenv import load_dotenv

def ler_xml_nfs(nota):
    with open(nota, 'rb') as arquivo:
        documento = xmltodict.parse(arquivo)
    nf = documento['NFSe']['infNFSe']
    emissor = documento['NFSe']['infNFSe']['emit']
    tomador = documento['NFSe']['infNFSe']['DPS']['infDPS']['toma']
    info_DPS = documento['NFSe']['infNFSe']['DPS']['infDPS']

    codigo_verificação = nf['@Id']
    numero_nf = nf['nNFSe']
    cnpj_emissor = emissor['CNPJ']
    nome_emissor = emissor['xNome']
    valor_liquido = nf['valores']['vLiq']
    cnpj_tomador = tomador['CNPJ']
    nome_tomador = tomador['xNome']
    data_emissao = info_DPS['dhEmi']
    data_competencia = info_DPS['dCompet']
    servico = info_DPS['serv']['cServ']['xDescServ']

    retorno_nf = {
        'Validador da Nf': codigo_verificação,
        'Número da NF': numero_nf,
        'CNPJ do emissor': cnpj_emissor,
        'Nome do emissor': nome_emissor,
        'Valor líquido': valor_liquido,
        'CNPJ do tomador': cnpj_tomador,
        'Nome do tomador': nome_tomador,
        'Data da emissão': data_emissao,
        'Data da competência': data_competencia,
        'Descrição do serviço': servico
    }

    return retorno_nf


load_dotenv()
pasta_notas = os.getenv('CAMINHO_PASTA_NOTAS', 'Nfs')
Nfs = os.listdir(pasta_notas)

novas_notas = []


for arquivo in Nfs:
    if 'xml' and 'Nfe' in arquivo:
        try:
            retorno_nf = ler_xml_nfs(f'Nfs/{arquivo}')
            novas_notas.append(retorno_nf)
        except Exception as e:
            sys.stderr.write(f"ERRO ao processar o arquivo [{arquivo}]: {e}\n")
            continue

caminho_planilha = 'Nfs.xlsx'

if novas_notas:
    novo_registro = pd.DataFrame(novas_notas)
    if os.path.exists(caminho_planilha):
        planilha_existente = pd.read_excel(caminho_planilha)
        tabela_atualizada = pd.concat([planilha_existente, novo_registro], ignore_index=True)
        tabela_atualizada.to_excel(caminho_planilha, index=False)
        print(f"\n {len(novas_notas)} novas notas adicionadas com sucesso à planilha existente!")
    else:
        novo_registro.to_excel(caminho_planilha, index=False)
        print(f"\n Nova planilha criada com {len(novas_notas)} notas processadas!")
else:
    print("\n Nenhuma nova nota foi processada com sucesso nesta execução.")
    