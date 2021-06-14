import streamlit as st
import requests
import pandas as pd
import numpy as np

'''
# The Fantasy Football Predictor ⚽️
'''
st.markdown('___')

st.markdown('''
## First... Input your players name :
''')

st.markdown('___')

st.subheader('Forwards *e.g.Harry Kane*')

fwd_1 = st.text_input('Forward 1')
fwd_2 = st.text_input('Forward 2')
fwd_3 = st.text_input('Forward 3')

st.markdown('___')

st.subheader('Midfielders *e.g. Kevin de Bruyne*')

mid_1 = st.text_input('Midfielder 1')
mid_2 = st.text_input('Midfielder 2')
mid_3 = st.text_input('Midfielder 3')
mid_4 = st.text_input('Midfielder 4')
mid_5 = st.text_input('Midfielder 5')

st.markdown('___')

st.subheader('Defenders *e.g. Ben Chilwell*')

def_1 = st.text_input('Defender 1')
def_2 = st.text_input('Defender 2')
def_3 = st.text_input('Defender 3')
def_4 = st.text_input('Defender 4')
def_5 = st.text_input('Defender 5')

st.markdown('___')

st.subheader('Goalkeepers *e.g. Hugo Lloris*')

gk_1= st.text_input('Goalkeeper 1')
gk_2= st.text_input('Goalkeeper 2')

st.markdown('___')

st.markdown('''
## 2. Then... Input your budget :
''')

st.markdown('___')

budget = st.number_input('Actual budget')

st.markdown('___')

st.markdown('''
## Finally... 
''')

if st.button('Start the Predictions'):
    import time
    'AI computed predictions in progress...'

    # Add a placeholder
    latest_iteration = st.empty()
    bar = st.progress(0)

    for i in range(100):
        # Update the progress bar with each iteration.
        latest_iteration.text(f'{i+1}%')
        bar.progress(i + 1)
        time.sleep(0.1)
        
    '...tadaaa! 🏆'
#        st.success(f'Prediction: {x}')

# url = ''
params = pd.DataFrame({
          'names': (fwd_1, fwd_2, fwd_3, 
                    mid_1, mid_2, mid_3, mid_4, mid_5, 
                    def_1, def_2, def_3, def_4, def_5, 
                    gk_1, gk_2),
          'positions': ('fwd', 'fwd', 'fwd', 
                        'mid', 'mid', 'mid', 'mid', 'mid', 
                        'def', 'def', 'def', 'def', 'def', 
                        'gk', 'gk')
        })
# response = requests.get(url, params).json()
# player_predicted = response['x']