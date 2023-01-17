import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 

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
  grafico= sns.lineplot(data=preco_gasolina, x='dia', y='venda', label= 'Média diária', palette='pastel', color= 'green')
  grafico.set(title='Preço médio da gasolina por dia na cidade de São Paulo', xlabel='Dia', ylabel='Preço da gasolina')
  grafico.get_figure().savefig("gasolina.png")
  grafico.figure.set_size_inches(w= 20/2.54, h=15/2.54)  