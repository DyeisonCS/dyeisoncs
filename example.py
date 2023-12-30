import streamlit as st
import pandas as pd
import controllers.MembroController as MembroController
import models.membro as membro


st.title('Cadastro de Membros IPSO')
#st.write("""
# My first app
#Hello *world!*
#""")

st.sidebar.title('Menu')
st.sidebar.selectbox('',options=['Incluir', 'Alterar', 'Excluir', 'Consultar'])

with st.form(key='Cadastro'):
    input_name = st.text_input(label='Insira seu nome')
    input_idade = st.text_input(label='Insira sua idade')
    input_cidade = st.text_input(label='Insira sua cidade')
    input_button_submit = st.form_submit_button('Enviar')

if input_button_submit:
    membro.nome = input_name
    membro.idade = input_idade
    membro.cidade = input_cidade

    MembroController.Incluir(membro.membro(0,input_name, input_idade, input_cidade))
    st.success('Cadastro Realizado com Sucesso')


costumerList = []

for item in MembroController.selecionartodos():
    costumerList.append([item.nome, item.idade, item.cidade])

df = pd.DataFrame(
    costumerList,
    columns = ['nome', 'idade', 'cidade']
)


st.table(df)

#df = pd.read_csv("C:\\Users\\dcsantos\\Downloads\\SUL.csv", delimiter=';')
#
#st.title('Meu primeiro Streamlit App')
#st.write("""
# My first app
#Hello *world!*
#""")
#
#option = st.selectbox(
#    'Qual a carteira?',
#    df['Carteira'])
#
#st.dataframe(df[df["Carteira"] == option])
#
#
#
#st.write('Voce Selecionou:', option)