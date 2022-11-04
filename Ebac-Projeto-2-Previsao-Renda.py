import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

sns.set(context='talk', style='ticks')

# st.set_page_config(
#      page_title='EBAC - Previsão de Renda',
#      page_icon='https://ebaconline.com.br/favicon.ico',
#      # layout='wide',
# )

st.markdown('## Análise exploratória da Previsão de Renda')
st.caption('### EBAC - Projeto 2 por Narciso Nascimento')
st.markdown('### Entendimento do negócio')
st.markdown(
     """
     Uma instituição financeira quer conhecer melhor o perfil de renda de seus novos clientes para diversos fins, por exemplo,
     melhor dimensionar o limite de cartões de crédito dos novos clientes, sem necessariamente solicitar olerites ou documentações
     que impactem na experiência do seu cliente.
     
     Para isto, conduziu um estudo com alguns clientes, comprovando suas rendas através de olerites e outros documentos,
     e pretende construir um modelo preditivo para esta renda com base em algumas variáveis que já possui em seu banco de dados.
     
     Estes dados estão no arquivo **previsao_de_renda.csv**.
     
     Variável target: **renda**.
"""
)

# mostrando o dataframe
renda = pd.read_csv('./input/previsao_de_renda.csv')
renda = renda.drop(['Unnamed: 0'], axis=1)
st.markdown('### Visualização do Dataframe')
st.dataframe(renda)

# plots
fig, ax = plt.subplots(8,1,figsize=(10,40))
renda[['posse_de_imovel','renda']].plot(kind='hist', ax=ax[0])

st.write('### Gráficos ao longo do tempo')

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

st.write('## Gráficos bivariada')
fig, ax = plt.subplots(7,1,figsize=(10,50))
sns.barplot(x='posse_de_imovel',y='renda',data=renda, ax=ax[0])
sns.barplot(x='posse_de_veiculo',y='renda',data=renda, ax=ax[1])
sns.barplot(x='qtd_filhos',y='renda',data=renda, ax=ax[2])
sns.barplot(x='tipo_renda',y='renda',data=renda, ax=ax[3])
sns.barplot(x='educacao',y='renda',data=renda, ax=ax[4])
sns.barplot(x='estado_civil',y='renda',data=renda, ax=ax[5])
sns.barplot(x='tipo_residencia',y='renda',data=renda, ax=ax[6])
sns.despine()
st.pyplot(plt)