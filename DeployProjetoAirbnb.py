import pandas as pd
import streamlit as st
import joblib

# modelo = joblib.load('modelo.joblib')

df_dados = pd.read_csv('dados.csv')

df_dados.drop('Unnamed: 0', axis=1, inplace= True)
df_dados.drop('price', axis=1, inplace= True)
atributos = df_dados.columns


x_numericos_keys = ['host_listings_count', 'latitude', 'longitude', 'accommodates', 'bathrooms', 'bedrooms', 'beds', 'extra_people', 'minimum_nights', 'month', 'year', 'n_amenities']

x_tf_keys = ['host_is_superhost', 'instant_bookable']

x_numericos = dict.fromkeys(x_numericos_keys,0)

x_tf = dict.fromkeys(x_tf_keys,0)

x_listas = {}

for col in df_dados:

    valor = df_dados.loc[0, col]

    if 'type' in col:

        objeto_tipo = str(col).split('_')[0]

        nome_tipo = str(col).split('_')[2]

        if f'{objeto_tipo}_type' in x_listas.keys():
        
            
            x_listas[f'{objeto_tipo}_type'].append(nome_tipo)
        else:
            x_listas[f'{objeto_tipo}_type'] = [nome_tipo]
    elif 'cancellation' in col:

        categoria = str(col).replace('cancellation_policy_', '')

        categoria = categoria#.title().replace('_', ' ')

        if 'cancellation_policy' in x_listas.keys():
    
            
            x_listas['cancellation_policy'].append(categoria)
        else:
            x_listas['cancellation_policy'] = [categoria]

    
print(x_listas)

for item in x_numericos:

    if item == 'latitude' or item == 'longitude':
        valor = st.number_input(f'{item}', step= 0.00001, value= 0.0, format='%.5f')
    valor = st.number_input(f'{item}')
    x_numericos[item] = valor

for item in x_tf:
    valor = st.selectbox(f'{item}', ('Sim', 'Não'))

    x_tf[item] = 1 if valor == 'Sim' else 0

for item, lista_opcoes in x_listas.items():

    valor = st.selectbox(f'{item}', lista_opcoes)

botao = st.button('Prever Valor do Imóvel')



