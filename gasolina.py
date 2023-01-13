import pandas as pd
import seaborn as sns
import numpy as np

gasolina_df = pd.read_csv('gasolina.csv', sep=',')
gasolina_df

# código de geração do gráfico 
with sns.axes_style('whitegrid'):
  grafico = sns.lineplot(data=gasolina_df, y='venda', x='dia', palette='pastel')
  grafico.set(title='Preço médio da gasolina nos primeiros 10 dias de Julho/2021, São Paulo:', ylabel='Preço', xlabel='dias', xticks=np.arange(0, 11, 2))
  fig = grafico.get_figure()
  fig.savefig('gasolina.png')