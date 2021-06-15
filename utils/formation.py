import matplotlib.pyplot as plt
from numpy import right_shift
import seaborn as sns
import streamlit as st
from skimage import io
import urllib3
from PIL import Image
import requests

from utils.player_pictures import get_picture

def print_formation(best_11):
    left_limit = 25
    right_limit = 285

    best_11['y'] = best_11.position.map({'GK':40, 'DEF':100, 'MID':190, 'FWD':280})
    best_11['x'] = 155
    for position in ['DEF', 'MID', 'FWD']:
        #st.write('hi')
        position_x = []
        position_count = len(best_11[best_11['position']==position])
        if position_count>2:
            #st.write(f'THREE OR MORE {position}: {position_count}')
            for i in range(position_count):
                position_x.append(left_limit+
                                  ((right_limit-left_limit)/
                                   (position_count-1)*i))
            #st.write(position_x)
            player = 0
            for index, row in best_11[best_11['position'] == position].iterrows():
                best_11.loc[index, ['x']] = position_x[player]
                player += 1
                #st.write(player)
        elif position_count == 2:
            #st.write(f'TWO PLAYERS {position}: {position_count}')
            position_x = [105,195]
            player = 0
            for index, row in best_11[best_11['position'] == position].iterrows():
                best_11.loc[index, ['x']] = position_x[player]
                player += 1
        else:
            #st.write(f'ELIF {position}: {position_count}')
            index = best_11[best_11['position']].index
            best_11.loc[index,['x']] = 155

    #st.write(best_11)

    pitch = plt.imread('images/football_pitch.png')
    fig, ax = plt.subplots()
    plt.axis('off')
    ax.imshow(pitch, extent=[0, 310, 0, 400])

    for _, row in best_11.iterrows():
        ax.text(row['x'] - 10,
                row['y'] - 10,
                row['name'].replace(' ', '\n').capitalize(),
                size=6)
        """
        player_url = get_picture(row['name'])
        st.write(player_url)
        """
        #playerpic = io.imread(player_url, )
        #playerpic = urllib2.urlopen(
        #    "http://matplotlib.sourceforge.net/_static/logo2.png")

        # http = urllib3.PoolManager()
        # playerpic = http.request('GET', player_url)
        # st.write(type(playerpic))
        #pic = plt.imread(playerpic)

        """
        if not player_url == 'not found':
            pic = Image.open(requests.get(player_url, stream=True).raw)
            ax.imshow(pic, extent = [row['x'], row['x']+15, row['y'], row['y']+15])
        """
    #sns.scatterplot(data=best_11, x='x', y='y', ax=ax, sizes=[10, 10])

    return fig
