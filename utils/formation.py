import matplotlib.pyplot as plt
from numpy import right_shift
import seaborn as sns
import streamlit as st
#from skimage import io
import urllib3
from PIL import Image
import requests
from io import BytesIO

import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

from utils.player_pictures import get_picture

def getImage(path):
    response = requests.get(path, stream=True)
    print(response.status_code)

    return OffsetImage(Image.open(BytesIO(response.content)), zoom = 0.6)


def print_formation(best_11):

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

    return fig
