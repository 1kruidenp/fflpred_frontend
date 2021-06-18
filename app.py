import streamlit as st
import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import time

import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox


from utils.formation import print_formation, getImage
from utils.player_pictures import get_picture

TEST_LIST = ['Vicente Guaita', 'Karl Darlow',
             'Timothy Castagne', 'Gabriel Magalhães', 'Romain Saïss', 'Reece James', 'James Justin',
             'Wilfried Zaha', 'Heung-Min Son', 'Mateusz Klich', 'Andros Townsend', 'Hélder Wander Sousa de Azevedo e Costa',
             'Patrick Bamford', 'Dominic Calvert-Lewin', 'Harry Kane']
NEWLINE = '\n'



logo = Image.open('images/DEEP_COACH.png')
st.image(logo, use_column_width=False, width=300)

'''
# The Fantasy Football Predictor ⚽️🏆
'''
st.markdown('___')


st.markdown('''
## Input your team:
''')
st.markdown('___')

with st.beta_expander('Input:',expanded=True):


    #with st.form(key='my_form'):

    # FWD
    st.subheader('Select 3 forwards *e.g. Harry Kane*')

    url_positions = 'https://fflpred-d2yuhgnxba-ew.a.run.app/players'
    response_positions= requests.get(url_positions).json()
    options_forward = ("", *[n.title() for n in response_positions['FWD']])

    forwards = st.multiselect('', options_forward, key="1")

    if len(forwards) != 0:
        if len(forwards) == 3:
            st.success('3 players selected')
        elif len(forwards) > 3:
            st.warning('Please choose 3 players')
        elif len(forwards) < 3:
            st.warning(f"Selected {len(forwards)}/3 players")

    # MID
    st.subheader('Select 5 midfielders *e.g. Kevin de Bruyne*')
    options_midfielders = ("", *[n.title() for n in response_positions['MID']])

    midfielders = st.multiselect('', options_midfielders, key="2")

    if len(midfielders) != 0:
        if len(midfielders) == 5:
            st.success('5 players selected')
        elif len(midfielders) > 5:
            st.warning('Please choose 5 players')
        elif len(midfielders) < 5:
            st.warning(f"Selected {len(midfielders)}/5 players")

    # DEF
    st.subheader('Select 5 defenders *e.g. John Stones*')
    options_defenders = ("", *[n.title() for n in response_positions['DEF']])

    defenders = st.multiselect('', options_defenders, key="3")

    if len(defenders) != 0:
        if len(defenders) == 5:
            st.success('5 players selected')
        elif len(defenders) > 5:
            st.warning('Please choose 5 players')
        elif len(defenders) < 5:
            st.warning(f"Selected {len(defenders)}/5 players")

    # GK
    st.subheader('Select 2 goalkeepers *e.g. Hugo Lloris*')
    options_goalkeepers = ("", *[n.title() for n in response_positions['GK']])

    goalkeepers= st.multiselect('', options_goalkeepers, key="4")

    if len(goalkeepers) != 0:
        if len(goalkeepers) == 2:
            st.success('2 players selected')
        elif len(goalkeepers) > 2:
            st.warning('Please choose 2 players')
        elif len(goalkeepers) < 2:
            st.warning(f"Selected {len(goalkeepers)}/2 players")

    # List of players for API params
    full_list = forwards + midfielders + defenders + goalkeepers

    st.markdown('___')

    st.markdown('''
    ## Input your budget :
    ''')

    budget = st.number_input('')

if st.checkbox("Use Pep's team"):
    full_list = [n.lower() for n in TEST_LIST]

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

if  st.checkbox('Start the Predictions'):

    'AI computed predictions in progress...'
    headers={
      'Accept': 'application/json'
    }
    response = requests.post(url, json=params, headers=headers).json()
    #response = json.load(open("test.json"))

    # Add a placeholder
    latest_iteration = st.empty()
    bar = st.progress(0)
    progress = 0

    for _ in range(40):
        # Update the progress bar with each iteration.
        latest_iteration.text(f'{progress+1}%')
        bar.progress(progress + 1)
        progress += 1
        time.sleep(0.01)

    # Transfer players
    best_transfers = pd.DataFrame(response['best_transfers'])
    best_transfers.leaving_player = best_transfers.leaving_player.apply(lambda x: x.title())
    best_transfers.incoming_player = best_transfers.incoming_player.apply(lambda x: x.title())

    # Suggested players

    best_11 = pd.DataFrame(
        response['best_11']).reset_index(drop=True)[['position', 'name']]

    positions = pd.DataFrame({
        'x': [155, 155, 155, 155, 25, 285],
        'y': [40, 100, 190, 280, 200, 200],
        'position': ['GK', 'DEF', 'MID', 'FWD', 'Left limit', 'right limit']
    })

    # Print pitch and formation

    #    fig = print_formation(best_11)

    #if not fig_set:
    left_limit = 25
    right_limit = 285

    best_11['y'] = best_11.position.map({'GK':60, 'DEF':140, 'MID':230, 'FWD':320})
    best_11['x'] = 155
    for position in ['DEF', 'MID', 'FWD']:
        #st.write('hi')
        position_x = []
        position_count = len(best_11[best_11['position']==position])
        if position_count>2:

            for i in range(position_count):
                position_x.append(left_limit+
                                ((right_limit-left_limit)/
                                (position_count-1)*i))
            player = 0
            for index, row in best_11[best_11['position'] == position].iterrows():
                best_11.loc[index, ['x']] = position_x[player]
                player += 1

        elif position_count == 2:
            position_x = [105,195]
            player = 0
            for index, row in best_11[best_11['position'] == position].iterrows():
                best_11.loc[index, ['x']] = position_x[player]
                player += 1
        else:
            index = best_11[best_11['position'] == position].index
            best_11.loc[index,['x']] = 155

    pitch = plt.imread('images/football_pitch.png')
    fig, ax = plt.subplots()
    plt.axis('off')
    ax.imshow(pitch, extent=[0, 310, 0, 400])

    ax.scatter(x = best_11.x, y = best_11.y, s = 1, c = 'green')

    for _, row in best_11.iterrows():
        ax.text(row['x'],
                row['y']-50,
                row['name'].replace(' ', '\n', 1).title(),
                size=5,
                ha = 'center')

        player_url = get_picture(row['name'])

        if not player_url == 'not found':
            image = getImage(player_url)
            ab = AnnotationBbox(image, (row['x'], row['y']), frameon=False, )
            ax.add_artist(ab)
        else:
            image = OffsetImage(Image.open('images/default_avatar.png'),
                                zoom=0.05)
            ab = AnnotationBbox(image,(row['x'], row['y']),frameon=False,)
            ax.add_artist(ab)

        latest_iteration.text(f'{progress}%')
        bar.progress(progress)
        progress+=6
    fig_set = True

    st.write(fig)

    # Captain and Vice Captain

    captain = response['captain'].title()
    captain_image = Image.open(
        BytesIO(
            requests.get(get_picture(response['captain']),
                         stream=True).content))
    vice_captain = response['vice_captain'].title()

    # Bench players

    subs_4 = pd.DataFrame(response['subs_4'])
    subs_4['name'] = subs_4['name'].apply(lambda x: x.title())

    #subs_4['url'] = subs_4['name'].apply(lambda x: get_picture(x))
    #subs_4['image'] = subs_4['url'].apply(lambda x: Image.open(BytesIO(requests.get(x, stream=True).content)) if x != 'not found' else '')

    st.markdown('___')

    st.write(f"""**Bench players :**{NEWLINE}
             {subs_4['name'][0]} ({subs_4['position'][0]}){NEWLINE}
             {subs_4['name'][1]} ({subs_4['position'][1]}){NEWLINE}
             {subs_4['name'][2]} ({subs_4['position'][2]}){NEWLINE}
             {subs_4['name'][3]} ({subs_4['position'][3]})
             """)

    #st.image(subs_4['image'][0])

    st.write(f"""**Captain :**  {NEWLINE}
             {captain}""")

    st.write(f"""**Vice-Captain :**  {NEWLINE}
             {vice_captain}""")

    st.write(f"""**Transfers for this Gameweek :** {NEWLINE}
             {best_transfers.leaving_player[0]} ➣ {best_transfers.incoming_player[0]}: +{int(best_transfers.points_difference[0])} points predicted {NEWLINE}
             {best_transfers.leaving_player[1]} ➣ {best_transfers.incoming_player[1]}: +{int(best_transfers.points_difference[1])} points predicted {NEWLINE}
             {best_transfers.leaving_player[2]} ➣ {best_transfers.incoming_player[2]}: +{int(best_transfers.points_difference[2])} points predicted
             """)

    selected_transfer = st.radio('Select a transfer:',
                                 best_transfers['leaving_player'],
                                 format_func=lambda x: 'Replace ' + x)

    #st.write(selected_transfer)
    new_player = best_transfers.incoming_player[best_transfers.leaving_player == selected_transfer].item().lower()
    #st.write(new_player)

    if  st.button('Rerun with transfer'):
        full_list.remove(selected_transfer.lower())
        full_list.append(new_player)

        params = {'team_list': full_list, 'budget': float(budget)}

        response = requests.post(url, json=params, headers=headers).json()

        # Suggested players

        best_11 = pd.DataFrame(
            response['best_11']).reset_index(drop=True)[['position', 'name']]
        # st.write(best_11)

        positions = pd.DataFrame({
            'x': [155, 155, 155, 155, 25, 285],
            'y': [40, 100, 190, 280, 200, 200],
            'position': ['GK', 'DEF', 'MID', 'FWD', 'Left limit', 'right limit']
        })

        #st.write(positions)

        fig = print_formation(best_11)
        st.write(fig)

        # Captain and Vice Captain

        captain = response['captain'].title()
        captain_image = Image.open(
            BytesIO(
                requests.get(get_picture(response['captain']),
                            stream=True).content))
        vice_captain = response['vice_captain'].title()

        # Bench players

        subs_4 = pd.DataFrame(response['subs_4'])
        subs_4['name'] = subs_4['name'].apply(lambda x: x.title())

        #subs_4['url'] = subs_4['name'].apply(lambda x: get_picture(x))
        #subs_4['image'] = subs_4['url'].apply(lambda x: Image.open(BytesIO(requests.get(x, stream=True).content)) if x != 'not found' else '')

        st.markdown('___')

        st.write(f"""**Bench players :**{NEWLINE}
                {subs_4['name'][0]} ({subs_4['position'][0]}){NEWLINE}
                {subs_4['name'][1]} ({subs_4['position'][1]}){NEWLINE}
                {subs_4['name'][2]} ({subs_4['position'][2]}){NEWLINE}
                {subs_4['name'][3]} ({subs_4['position'][3]})
                """)

        #st.image(subs_4['image'][0])

        st.write(f"""**Captain :**  {NEWLINE}
                {captain}""")

        st.write(f"""**Vice-Captain :**  {NEWLINE}
                {vice_captain}""")
