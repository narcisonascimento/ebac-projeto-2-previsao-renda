import pandas as pd
import streamlit as st

st.set_page_config(
     page_title='EBAC - Previsão de Renda',
     page_icon='https://ebaconline.com.br/favicon.ico',
     layout='wide',
     initial_sidebar_state='auto'
)

# st.sidebar.success("Select a demo above.")
# st.sidebar.header("Home")
# st.sidebar.success("test")

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