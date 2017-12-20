import requests
from bs4 import BeautifulSoup
from PIL import Image
import ast


def get_grass_field(name):
    magnify = 2

    req = requests.get('https://github.com/' + name)

    if req.status_code == 404:
        print('a')
        return 'failed'

    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    b = [ast.literal_eval(str(aa).replace('<rect ', '{"').replace('></rect>', '}').replace(' ', ',"').replace('=', '":')) for aa in soup.find('g').find_all("rect")]

    for i in range(len(b)):
        b[i]['x'] = str((13 - int(b[i]['x'])) * 12)

    im = Image.new('RGB', (634 * magnify, 82 * magnify), (255, 255, 255))

    for i in range(len(b)):
        x = int(b[i]['x'])
        y = int(b[i]['y'])
        red = int('0x' + b[i]['fill'][1:3], 16)
        green = int('0x' + b[i]['fill'][3:5], 16)
        blue = int('0x' + b[i]['fill'][5:], 16)
        color = (red, green, blue)
        for xx in range(x * magnify, (x+10) * magnify):
            for yy in range(y * magnify, (y+10) * magnify):
                im.putpixel((xx, yy), color)

    im.save('sample.png')
get_grass_field('rismme')