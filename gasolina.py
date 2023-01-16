import pandas as pd
import seaborn as sns
import os
from getpass import getpass 

%%writefile gasolina.csv
dia,venda
1,5.11
2,4.99
3,5.02
4,5.21
5,5.07
6,5.09
7,5.13
8,5.12
9,4.94
10,5.03

data= pd.read_csv('./gasolina.csv', sep=',', encoding='utf8')
data.head(11)

preco_gasolina= data[['dia', 'venda']]

with sns.axes_style('whitegrid'):
  grafico= sns.lineplot(data=preco_gasolina, x='dia', y='venda', palette='pastel')
  grafico.set(title='Preço da gasolina por dia', xlabel='Dia', ylabel='Preço da gasolina')
  grafico.get_figure().savefig("gasolina.png")