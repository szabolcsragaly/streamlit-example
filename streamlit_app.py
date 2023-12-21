import altair as alt
# app.py

import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

# Felhasználói bemeneti mezők
claw_length = st.number_input('Claw Length (cm):', min_value=0.0, max_value=100.0, value=50.0)
endangered = st.selectbox('Endangered:', [0, 1], index=0)
size_cm = st.number_input('Size (cm):', min_value=0.0, max_value=100.0, value=50.0)
specie = st.selectbox('Specie:', [0, 1], index=0)
sub_specie = st.selectbox('Sub-specie:', [0, 1], index=0)
tail_length = st.number_input('Tail Length (cm):', min_value=0.0, max_value=100.0, value=50.0)

# Prediktív modell
def predict(claw_length, endangered, size_cm, specie, sub_specie, tail_length):
    # Dummy adatok generálása
    data = {
        'claw_length_cm': [1, 2, 3, 4, 5],
        'endangered': [0, 1, 0, 1, 0],
        'size_cm': [10, 15, 20, 25, 30],
        'specie': [0, 1, 0, 1, 0],
        'sub_specie': [0, 1, 0, 1, 0],
        'tail_length_cm': [5, 10, 15, 20, 25],
        'weight_kg': [2, 4, 6, 8, 10]
    }
    df = pd.DataFrame(data)

    # Bemeneti változók
    X = df[['claw_length_cm', 'endangered', 'size_cm', 'specie', 'sub_specie', 'tail_length_cm']]
    y = df['weight_kg']

    # Modell tanítása
    model = RandomForestRegressor(random_state=1)
    model.fit(X, y)

    # Predikció
    prediction = model.predict([[claw_length, endangered, size_cm, specie, sub_specie, tail_length]])[0]
    return prediction

# Predikció és eredmény kiírása
if st.button('Prediktálás'):
    result = predict(claw_length, endangered, size_cm, specie, sub_specie, tail_length)
    st.write('Prediktált weight érték:', result)

