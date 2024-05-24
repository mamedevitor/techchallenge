import requests, csv
from io import StringIO
from sqlalchemy import create_engine, Column, String, MetaData, Table
from sqlalchemy.orm import sessionmaker
from collections import defaultdict

urls = [['http://vitibrasil.cnpuv.embrapa.br/download/Producao.csv', 'Producao', ';'],
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
        ['http://vitibrasil.cnpuv.embrapa.br/download/ExpSuco.csv', 'Exportacao_Suco', ';']]

engine = create_engine('sqlite:///vitibrasil.db')
metadata = MetaData()
Session = sessionmaker(bind=engine)

with Session() as session:
    for url, nome_tabela, separador in urls:
        try:
            req = requests.get(url)
            req.encoding = 'utf-8'
            if req.status_code == 200:
                csv_data = csv.DictReader(StringIO(req.text), delimiter=separador)
                colunas_renomeadas = []
                contagem_colunas = defaultdict(int)

                for coluna in csv_data.fieldnames:
                    contagem_colunas[coluna] += 1
                    if contagem_colunas[coluna] > 1:
                        colunas_renomeadas.append(f"{coluna}_{contagem_colunas[coluna]}")
                    else: colunas_renomeadas.append(coluna)

                tabela = Table(f'tabela_{nome_tabela}', metadata, *[Column(coluna, String) for coluna in colunas_renomeadas])
                metadata.create_all(engine)
                session.execute(tabela.insert(), [
                    {coluna_renomeada: row[coluna_original]
                    for coluna_original, coluna_renomeada in zip(csv_data.fieldnames, colunas_renomeadas)}
                    for row in csv_data])
                session.commit()
                print(f"Arquivo '{nome_tabela}' baixado e inserido com sucesso!")

            else: print(f"Erro ao baixar o arquivo '{nome_tabela}': {req.status_code}")

        except Exception as e:
            print(f"Erro ao processar o arquivo '{nome_tabela}': {e}")
            session.rollback()

engine.dispose()
