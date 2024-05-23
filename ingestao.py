import pandas as pd
from sqlalchemy import create_engine


producao_df = pd.read_csv('Producao.csv', delimiter=';')
processa_viniferas_df = pd.read_csv('ProcessaViniferas.csv', delimiter=';')


producao_df.columns = [
    'id',
'control',
'produto',
'ano1970',
'ano1971',
'ano1972',
'ano1973',
'ano1974',
'ano1975',
'ano1976',
'ano1977',
'ano1978',
'ano1979',
'ano1980',
'ano1981',
'ano1982',
'ano1983',
'ano1984',
'ano1985',
'ano1986',
'ano1987',
'ano1988',
'ano1989',
'ano1990',
'ano1991',
'ano1992',
'ano1993',
'ano1994',
'ano1995',
'ano1996',
'ano1997',
'ano1998',
'ano1999',
'ano2000',
'ano2001',
'ano2002',
'ano2003',
'ano2004',
'ano2005',
'ano2006',
'ano2007',
'ano2008',
'ano2009',
'ano2010',
'ano2011',
'ano2012',
'ano2013',
'ano2014',
'ano2015',
'ano2016',
'ano2017',
'ano2018',
'ano2019',
'ano2020',
'ano2021',
'ano2022',
'ano2023']
processa_viniferas_df.columns = ['id', 'control', 'cultivar']

engine = create_engine('sqlite:///vitibrasil.db')

producao_df.to_sql('producao', con=engine, if_exists='replace', index=False)
processa_viniferas_df.to_sql('processa_viniferas', con=engine, if_exists='replace', index=False)

print("Dados carregados e salvos com sucesso no banco de dados SQLite.")
