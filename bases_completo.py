import requests
import csv
from io import StringIO
from sqlalchemy import create_engine, Column, String, Integer, MetaData, Table
from sqlalchemy.orm import sessionmaker
from collections import defaultdict

urls = [
    ['http://vitibrasil.cnpuv.embrapa.br/download/Producao.csv', 'Producao', ';'],
    ['http://vitibrasil.cnpuv.embrapa.br/download/ProcessaViniferas.csv', 'Processamento_Viniferas', '\t'],
    ['http://vitibrasil.cnpuv.embrapa.br/download/ProcessaAmericanas.csv', 'Processamento_AmericanasHibridas', '\t'],
    ['http://vitibrasil.cnpuv.embrapa.br/download/ProcessaMesa.csv', 'Processamento_UvasMesa', '\t'],
    ['http://vitibrasil.cnpuv.embrapa.br/download/ProcessaSemclass.csv', 'Processamento_SemClassf', '\t'],
    ['http://vitibrasil.cnpuv.embrapa.br/download/Comercio.csv', 'Comercio', ';'],
    ['http://vitibrasil.cnpuv.embrapa.br/download/ImpVinhos.csv', 'Importacao_Vinhos', ';'],
    ['http://vitibrasil.cnpuv.embrapa.br/download/ImpEspumantes.csv', 'Importacao_Espumantes', ';'],
    ['http://vitibrasil.cnpuv.embrapa.br/download/ImpFrescas.csv', 'Importacao_UvasFrescas', ';'],
    ['http://vitibrasil.cnpuv.embrapa.br/download/ImpPassas.csv', 'Importacao_UvasPassas', ';'],
    ['http://vitibrasil.cnpuv.embrapa.br/download/ImpSuco.csv', 'Importacao_Suco', ';'],
    ['http://vitibrasil.cnpuv.embrapa.br/download/ExpVinho.csv', 'Exportacao_VinhoMesa', ';'],
    ['http://vitibrasil.cnpuv.embrapa.br/download/ExpEspumantes.csv', 'Exportacao_Espumantes', ';'],
    ['http://vitibrasil.cnpuv.embrapa.br/download/ExpUva.csv', 'Exportacao_UvasFrescas', ';'],
    ['http://vitibrasil.cnpuv.embrapa.br/download/ExpSuco.csv', 'Exportacao_Suco', ';']
]

engine = create_engine('sqlite:///vitibrasil.db')
metadata = MetaData()
Session = sessionmaker(bind=engine)

def parse_value(value):
    try:
        return int(value)
    except ValueError:
        return 0

def process_csv_data(csv_data, delimiter):
    csv_reader = csv.reader(StringIO(csv_data), delimiter=delimiter)
    headers = next(csv_reader)
    
    colunas_renomeadas = []
    contagem_colunas = defaultdict(int)
    for coluna in headers:
        if coluna.isdigit():
            coluna = f"ano{coluna}"
        contagem_colunas[coluna] += 1
        if contagem_colunas[coluna] > 1:
            colunas_renomeadas.append(f"{coluna}_{contagem_colunas[coluna]}")
        else:
            colunas_renomeadas.append(coluna)
    
    data = []
    for row in csv_reader:
        new_row = {}
        for coluna_renomeada, valor in zip(colunas_renomeadas, row):
            if "ano" in coluna_renomeada:
                new_row[coluna_renomeada] = parse_value(valor)
            else:
                new_row[coluna_renomeada] = valor
        data.append(new_row)
    
    return data, colunas_renomeadas

with Session() as session:
    for url, nome_tabela, separador in urls:
        try:
            req = requests.get(url)
            req.encoding = 'utf-8'
            if req.status_code == 200:
                data, colunas_renomeadas = process_csv_data(req.text, separador)
                tabela = Table(f'tabela_{nome_tabela}', metadata, *[Column(coluna, Integer if "ano" in coluna else String) for coluna in colunas_renomeadas])
                metadata.create_all(engine)
                session.execute(tabela.insert(), data)
                session.commit()
                print(f"Arquivo '{nome_tabela}' baixado e inserido com sucesso!")
            else:
                print(f"Erro ao baixar o arquivo '{nome_tabela}': {req.status_code}")
        except Exception as e:
            print(f"Erro ao processar o arquivo '{nome_tabela}': {e}")
            session.rollback()

engine.dispose()
