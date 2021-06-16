import streamlit as st
import requests
import json
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup


'''
# The Fantasy Football Predictor ⚽️🏆
'''
st.markdown('___')

st.markdown('''
## Input your players name :
''')

st.markdown('___')

#with st.form(key='my_form'):

# FWD
st.subheader('Select 3 forwards *e.g. Harry Kane*')

url_positions = 'https://fflpred-d2yuhgnxba-ew.a.run.app/players'
response_positions= requests.get(url_positions).json()
options_forward = ("", *[n.title() for n in response_positions['FWD']])

fwd_1 = st.multiselect('', options_forward, key="1")

if len(fwd_1) != 0:
  if len(fwd_1) == 3:
      st.success('3 players selected')
  elif len(fwd_1) > 3:
      st.warning('Please choose 3 players')
  elif len(fwd_1) < 3:
      st.warning(f"Selected {len(fwd_1)}/3 players")

# MID
st.subheader('Select 5 midfielders *e.g. Kevin de Bruyne*')
options_midfielders = ("", *[n.title() for n in response_positions['MID']])

mid_1 = st.multiselect('', options_midfielders, key="2")

if len(mid_1) != 0:
  if len(mid_1) == 5:
      st.success('5 players selected')
  elif len(mid_1) > 5:
      st.warning('Please choose 5 players')
  elif len(mid_1) < 5:
      st.warning(f"Selected {len(mid_1)}/5 players")

# DEF
st.subheader('Select 5 defenders *e.g. John Stones*')
options_defenders = ("", *[n.title() for n in response_positions['DEF']])

def_1 = st.multiselect('', options_defenders, key="3")

if len(def_1) != 0:
  if len(def_1) == 5:
      st.success('5 players selected')
  elif len(def_1) > 5:
      st.warning('Please choose 5 players')
  elif len(def_1) < 5:
      st.warning(f"Selected {len(def_1)}/5 players")

# GK
st.subheader('Select 2 goalkeepers *e.g. Hugo Lloris*')
options_goalkeepers = ("", *[n.title() for n in response_positions['GK']])

gk_1= st.multiselect('', options_goalkeepers, key="4")

if len(gk_1) != 0:
  if len(gk_1) == 3:
      st.success('2 players selected')
  elif len(gk_1) > 2:
      st.warning('Please choose 2 players')
  elif len(gk_1) < 2:
      st.warning(f"Selected {len(gk_1)}/2 players")

# List of players for API params
full_list = fwd_1 + mid_1 + def_1 + gk_1

st.markdown('___')

st.markdown('''
## Input your budget :
''')

budget = st.number_input('')

st.markdown('___')

st.markdown('''
## Finally... 
''')

full_list = [n.lower() for n in full_list]
params = {
    'team_list': full_list,
    'budget': float(budget)
    }
  
url = 'https://fflpred-d2yuhgnxba-ew.a.run.app/give_prediction'
     
# Button to predict

if 	st.button('Start the Predictions'): #st.form_submit_button(label='Submit'):
    import time

    'AI computed predictions in progress...'
    headers={
      'Accept': 'application/json'
    }
    response = requests.post(url, json=params, headers=headers).json()
    #response = json.load(open("test.json"))

    # Add a placeholder
    latest_iteration = st.empty()
    bar = st.progress(0)

    for i in range(100):
        # Update the progress bar with each iteration.
        latest_iteration.text(f'{i+1}%')
        bar.progress(i + 1)
        time.sleep(0.1)
        
    # Transfer players
    top_transfer_players = list(response['best_transfers']['leaving_player'].values())
    top_transfer_subs = list(response['best_transfers']['incoming_player'].values())
    
    top_transfer_1 = top_transfer_players[0].title()
    top_transfer_2 = top_transfer_players[1].title()   
    top_transfer_3 = top_transfer_players[2].title() 

    top_sub_1 = top_transfer_subs[0].title()
    top_sub_2 = top_transfer_subs[1].title()   
    top_sub_3 = top_transfer_subs[2].title()
    
    # Suggested players

    sugg_players = list(response['best_11']['name'].values())
    sugg_players_position = list(response['best_11']['position'].values())
    
    #import ipdb; ipdb.set_trace()

    sugg_player_1 = sugg_players[0].title()
    sugg_player_1_p = sugg_players_position[0]

    sugg_player_2 = sugg_players[1].title()
    sugg_player_2_p = sugg_players_position[1]
        
    sugg_player_3 = sugg_players[2].title()
    sugg_player_3_p = sugg_players_position[2]

    sugg_player_4 = sugg_players[3].title()
    sugg_player_4_p = sugg_players_position[3]
    
    sugg_player_5 = sugg_players[4].title()
    sugg_player_5_p = sugg_players_position[4]

    sugg_player_6 = sugg_players[5].title()
    sugg_player_6_p = sugg_players_position[5]

    sugg_player_7 = sugg_players[6].title()
    sugg_player_7_p = sugg_players_position[6]

    sugg_player_8 = sugg_players[7].title()
    sugg_player_8_p = sugg_players_position[7]
    
    sugg_player_9 = sugg_players[8].title()
    sugg_player_9_p = sugg_players_position[8]

    sugg_player_10 = sugg_players[9].title()
    sugg_player_10_p = sugg_players_position[9]
    
    sugg_player_11 = sugg_players[10].title()
    sugg_player_11_p = sugg_players_position[10]
    
    # Captain and Vice Captain 

    sugg_captain = response['captain'].title()
    sugg_vice_captain = response['vice_captain'].title()

    # Bench players
    
    bench_players = list(response['subs_4']['name'].values())
    bench_players_position = list(response['subs_4']['position'].values())

    bench_player_1 = bench_players[0].title()
    bench_player_1_p = bench_players_position[0]
    
    bench_player_2 = bench_players[1].title()
    bench_player_2_p = bench_players_position[1]
    
    bench_player_3 = bench_players[2].title()
    bench_player_3_p = bench_players_position[2]
    
    bench_player_4 = bench_players[3].title()
    bench_player_4_p = bench_players_position[3]

    st.markdown('___')

    st.write(f"""**Starting 11 :**   
            *Forwards*: {sugg_player_1} ({sugg_player_1_p}), {sugg_player_2} ({sugg_player_2_p}) and {sugg_player_3} ({sugg_player_3_p})                                         
            *Midfielders*: {sugg_player_4} ({sugg_player_4_p}), {sugg_player_5} ({sugg_player_5_p}), {sugg_player_6} ({sugg_player_6_p}) and {sugg_player_7} ({sugg_player_7_p})  
            *Defenders*: {sugg_player_8} ({sugg_player_8_p}), {sugg_player_9} ({sugg_player_9_p}) and {sugg_player_10} ({sugg_player_10_p})                                     
            *Goalkeeper*: {sugg_player_11} ({sugg_player_11_p})""")
    
    st.write(f"""**Bench players :**
             {bench_player_1} ({bench_player_1_p}), 
             {bench_player_2} ({bench_player_2_p}), 
             {bench_player_3} ({bench_player_3_p})""")

    st.write(f"""**Captain :** {sugg_captain}""")
    
    st.write(f"""**Vice-Captain :** {sugg_vice_captain}""")
    
    st.write(f"""**Transfers for this Gameweek :**                 
             {top_transfer_1} ➣ {top_sub_1}         
             {top_transfer_2} ➣ {top_sub_2}         
             {top_transfer_3} ➣ {top_sub_3}
             """)
