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
st.markdown('### Análise Bivariada')
# st.sidebar.header("Ao Longo do Tempo")

sns.set(context='talk', style='ticks')

# carregando o dataframe
renda = pd.read_csv('./input/previsao_de_renda.csv')
renda = renda.drop(['Unnamed: 0'], axis=1)

# plots
fig, ax = plt.subplots(7, 1, figsize=(20, 50))
sns.barplot(x='posse_de_imovel', y='renda', data=renda, ax=ax[0])
sns.barplot(x='posse_de_veiculo', y='renda', data=renda, ax=ax[1])
sns.barplot(x='qtd_filhos', y='renda', data=renda, ax=ax[2])
sns.barplot(x='tipo_renda', y='renda', data=renda, ax=ax[3])
sns.barplot(x='educacao', y='renda', data=renda, ax=ax[4])
sns.barplot(x='estado_civil', y='renda', data=renda, ax=ax[5])
sns.barplot(x='tipo_residencia', y='renda', data=renda, ax=ax[6])
sns.despine()
st.pyplot(plt)
