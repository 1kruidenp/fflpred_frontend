import streamlit as st
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from utils.formation import print_formation
from utils.pitch import draw_pitch
from bokeh.plotting import figure



'''
# The Fantasy Football Predictor ⚽️🏆
'''
st.markdown('___')

st.markdown('''
## Input your players name :
''')

st.markdown('___')

st.subheader('Select 3 forwards *e.g. Harry Kane*')
options_forward = ('', 'Kevin de Bruyne', 'marc zuck', 'john brain', 'John Stones')

fwd_1 = st.multiselect('', options_forward)
#fwd_2 = st.text_input('Forward 2')
#fwd_3 = st.text_input('Forward 3')

st.subheader('Select 5 midfielders *e.g. Kevin de Bruyne*')
options_midfielders = ('', 'Kevin de Bruyne', 'marc zuck', 'john brain')

mid_1 = st.multiselect('', options_midfielders)
#mid_2 = st.text_input('Midfielder 2')
#mid_3 = st.text_input('Midfielder 3')
#mid_4 = st.text_input('Midfielder 4')
#mid_5 = st.text_input('Midfielder 5')

st.subheader('Select 5 defenders *e.g. John Stones*')
options_defenders = ('', 'Kevin de Bruyne', 'marc zuck', 'john brain', 'John Stones', 'peter parker')

def_1 = st.multiselect('', options_defenders)
#def_2 = st.text_input('Defender 2')
#def_3 = st.text_input('Defender 3')
#def_4 = st.text_input('Defender 4')
#def_5 = st.text_input('Defender 5')

st.subheader('Select 2 goalkeepers *e.g. Hugo Lloris*')
options_goalkeepers = ('', 'Kevin de Bruyne', 'marc zuck', 'john brain', 'John Stones', 'Hugo Lloris')

gk_1= st.multiselect('', options_goalkeepers)
#gk_2= st.text_input('Goalkeeper 2')

st.markdown('___')

st.markdown('''
## Input your budget :
''')

#st.markdown('___')

budget = st.number_input('')

st.markdown('___')

st.markdown('''
## Finally...
''')

# url = ''
params = pd.DataFrame({
          'names': (fwd_1, fwd_1, fwd_1,
                    mid_1, mid_1, mid_1, mid_1, mid_1,
                    def_1, def_1, def_1, def_1, def_1,
                    gk_1, gk_1),
          'positions': ('fwd', 'fwd', 'fwd',
                        'mid', 'mid', 'mid', 'mid', 'mid',
                        'def', 'def', 'def', 'def', 'def',
                        'gk', 'gk')
        })

#          'names': (fwd_1, fwd_2, fwd_3,
#                    mid_1, mid_2, mid_3, mid_4, mid_5,
#                    def_1, def_2, def_3, def_4, def_5,
#                    gk_1, gk_2)

if st.button('Start the Predictions'):
    import time

    'AI computed predictions in progress...'

    # response = requests.get(url, params).json()

    response = {
        "best_11": {
            "name": {
                "29": "dominic calvert-lewin",
                "39": "harry kane",
                "66": "michail antonio",
                "200": "jack harrison",
                "226": "jesse lingard",
                "313": "paul pogba",
                "320": "raphael dias belloli",
                "379": "aaron cresswell",
                "407": "benjamin chilwell",
                "551": "nathaniel phillips",
                "646": "edouard mendy"
            },
            "position": {
                "29": "FWD",
                "39": "FWD",
                "66": "FWD",
                "200": "MID",
                "226": "MID",
                "313": "MID",
                "320": "MID",
                "379": "DEF",
                "407": "DEF",
                "551": "DEF",
                "646": "GK"
            }
        },
        "subs_4": {
            "name": {
                "250": "kevin de bruyne",
                "495": "john stones",
                "613": "victor lindelöf",
                "655": "illan meslier"
            },
            "position": {
                "250": "MID",
                "495": "DEF",
                "613": "DEF",
                "655": "GK"
            }
        },
        "captain": "dominic calvert-lewin",
        "vice_captain": "michail antonio",
        "best_transfers": {
            "leaving_player": {
                "0": "illan meslier",
                "1": "kevin de bruyne",
                "2": "edouard mendy"
            },
            "incoming_player": {
                "0": "vicente guaita",
                "1": "mohamed salah",
                "2": "vicente guaita"
            },
            "points_difference": {
                "0": 5.4,
                "1": 5.206230572269324,
                "2": 4
            }
        }
    }

    # Add a placeholder
    latest_iteration = st.empty()
    bar = st.progress(0)

    for i in range(100):
        # Update the progress bar with each iteration.
        latest_iteration.text(f'{i+1}%')
        bar.progress(i + 1)
        time.sleep(0.001)

    'Here are our predictions:'

    best_11 = pd.DataFrame(response['best_11']).reset_index(drop = True)[['position', 'name']]
    st.write(best_11)

    positions = pd.DataFrame({
        'x': [155, 155, 155, 155, 25, 285],
        'y': [40, 100, 190, 280, 200, 200],
        'position': ['GK', 'DEF', 'MID', 'FWD', 'Left limit', 'right limit']
    })

    #st.write(positions)

    fig = print_formation(best_11)
    st.write(fig)


# top_transfer_1 = response['']
# top_transfer_2 = response['']
# top_transfer_3 = response['']


# sugg_captain = response['']
# sugg_vice_captain = response['']

# bench_player_1 = response['']
# bench_player_1_p = response['']
# bench_player_2 = response['']
# bench_player_2_p = response['']
# bench_player_3 = response['']
# bench_player_3_p = response['']


## st.success(f'Prediction: {x}')

#st.write(f'The players to transfer for this Gameweek:
#         {top_transfer_1}, {top_transfer_2}, {top_transfer_3}')

#st.write(f'Suggestion of the 11 starting players:
#         {sugg_player_1} ({sugg_player_1_p}), {sugg_player_2} ({sugg_player_2_p}),
#         {sugg_player_3} ({sugg_player_3_p}), {sugg_player_4} ({sugg_player_4_p}),
#         {sugg_player_5} ({sugg_player_5_p}), {sugg_player_6} ({sugg_player_6_p}),
#         {sugg_player_7} ({sugg_player_7_p}), {sugg_player_8} ({sugg_player_8_p}),
#         {sugg_player_9} ({sugg_player_9_p}), {sugg_player_10} ({sugg_player_10_p}),
#         {sugg_player_11} ({sugg_player_11_p})')

#st.write(f'Suggestion of a Captain and Vice-Captain:
#         {sugg_captain} & {sugg_vice_captain}')

#st.write(f'Suggestion of the 4 bench players:
#         {bench_player_1} ({bench_player_1_p}),
#         {bench_player_2} ({bench_player_2_p}),
#         {bench_player_3} ({bench_player_3_p})')
