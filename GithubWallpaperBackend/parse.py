import requests
from bs4 import BeautifulSoup
# from PIL import Image
import ast


def get_grass_field(username):
    # magnify = 2

    req = requests.get('https://github.com/' + username)

    if req.status_code == 404:
        return None

    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    field = [ast.literal_eval(str(aa).replace('<rect ', '{"').replace('></rect>', '}').replace(' ', ',"').replace('=', '":')) for aa in soup.find('g').find_all("rect")]

    for i in range(len(field)):
        field[i]['x'] = str((13 - int(field[i]['x'])) * 12)

    return field

#    im = Image.new('RGB', (634 * magnify, 82 * magnify), (255, 255, 255))
#
#    for i in range(len(b)):
#        x = int(b[i]['x'])
#        y = int(b[i]['y'])
#        red = int('0x' + b[i]['fill'][1:3], 16)
#        green = int('0x' + b[i]['fill'][3:5], 16)
#        blue = int('0x' + b[i]['fill'][5:], 16)
#        color = (red, green, blue)
#        for xx in range(x * magnify, (x+10) * magnify):
#            for yy in range(y * magnify, (y+10) * magnify):
#                im.putpixel((xx, yy), color)
#    im.save(username+'.jpg', 'JPEG')
#    return True