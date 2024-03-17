from flask import Flask,render_template,request
import pandas as pd
import lightgbm as lgb
from joblib import dump, load
import streamlit as st
import matplotlib.pyplot as plt


dataframe = pd.read_csv('app_train.csv')
col = 'TARGET'
X = dataframe.loc[:, dataframe.columns != col]
y = dataframe['TARGET']
model = load('LGBM_TUNED.joblib')

st.write(X)
st.write("## API client")
id = st.number_input("ID du client", step=1)
st.write(f"s:{id}")

id
if (X['SK_ID_CURR'] == {id}).any() :
    form_array = X[X['SK_ID_CURR'] == {id}]
    prediction = model.predict(form_array)
    if prediction >= 0.478:
        st.write(f"Score du client : {prediction}, le crédit peut-être accordé.")
    else:
        st.write(f"Score du client : {prediction}, ne pas accorder de crédit.")
else:
    st.write(f"Pas de client renseigné avec cet ID.")


# Initialize st.session_state.beans
st.session_state.beans = st.session_state.get("beans", 0)

st.title("Bean counter :paw_prints:")

addend = st.number_input("Beans to add", 0, 10)
if st.button("Add"):
    st.session_state.beans += addend
st.markdown(f"Beans counted: {st.session_state.beans}")

