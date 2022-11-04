import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(
     page_title='EBAC - Previsão de Renda',
     page_icon='https://ebaconline.com.br/favicon.ico',
     layout='wide',
     initial_sidebar_state='auto'
)

st.markdown('## Análise exploratória da Previsão de Renda')
st.caption('### EBAC - Projeto 2 por Narciso Nascimento')
st.markdown('### Gráficos ao longo do tempo')
# st.sidebar.header("Ao Longo do Tempo")

sns.set(context='talk', style='ticks')

# carregando o dataframe
renda = pd.read_csv('./input/previsao_de_renda.csv')
renda = renda.drop(['Unnamed: 0'], axis=1)

# plots
fig, ax = plt.subplots(8,1,figsize=(20,80))
renda[['posse_de_imovel','renda']].plot(kind='hist', ax=ax[0])

sns.lineplot(x='data_ref', y='renda',
             hue='posse_de_imovel', data=renda, ax=ax[1])
ax[1].tick_params(axis='x', rotation=45)
sns.lineplot(x='data_ref', y='renda',
             hue='posse_de_veiculo', data=renda, ax=ax[2])
ax[2].tick_params(axis='x', rotation=45)
sns.lineplot(x='data_ref', y='renda', hue='qtd_filhos', data=renda, ax=ax[3])
ax[3].tick_params(axis='x', rotation=45)
sns.lineplot(x='data_ref', y='renda', hue='tipo_renda', data=renda, ax=ax[4])
ax[4].tick_params(axis='x', rotation=45)
sns.lineplot(x='data_ref', y='renda', hue='educacao', data=renda, ax=ax[5])
ax[5].tick_params(axis='x', rotation=45)
sns.lineplot(x='data_ref', y='renda', hue='estado_civil', data=renda, ax=ax[6])
ax[6].tick_params(axis='x', rotation=45)
sns.lineplot(x='data_ref', y='renda',
             hue='tipo_residencia', data=renda, ax=ax[7])
ax[7].tick_params(axis='x', rotation=45)
sns.despine()
st.pyplot(plt)