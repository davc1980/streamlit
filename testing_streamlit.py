import streamlit as st
import pandas as pd
st.write("""my first App""")
df = pd.DataFrame({
  'Numero': [1, 2, 3, 4],
  'Calificacion': [10, 20, 30, 40],
  'Nombre': ['pedro', 'juan', 'luis', 'Jose']
})

df2 = pd.DataFrame({
  'Numero': [1, 2, 3, 4],
  'Calificacion': [10, 20, 30, 40],
  'Nombre': ['pedro', 'juan', 'luis', 'Jose']
})

df
df2
