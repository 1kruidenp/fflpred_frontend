import requests
import json
from bs4 import BeautifulSoup


def get_picture(player_name):
    url = f"https://sofifa.com/players?keyword={player_name}"
    doc = requests.get(url)
    soup = BeautifulSoup(doc.content, 'html.parser')
    #import ipdb; ipdb.set_trace()
    try:
        table = soup.select('.column.col-auto')[0]
        #img_url=table.img['data-srcset'].split(',')[-1][1:-3]
        img_url = table.img['data-src'][0:-9] + '21_60.png'
        image = img_url
    except Exception as e:
        print('Not found ... ')
        image = 'not found'
    return image


if __name__ == '__main__':
    data = json.load(open('players.json'))
    data = list(data['best_transfers']['leaving_player'].values())
    images = []
    for pl in data:
        print(pl)
        images.append(get_picture(pl))
    print(images)
