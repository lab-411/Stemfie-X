'''
Konverzia CadQuery objektu na SVG a PNG obrazok

Instalacia konvertorov
    sudo apt install librsvg2-bin
    sudo apt update && sudo apt install imagemagick libpng-dev libjpeg-dev libtiff-dev
'''

from IPython.display import SVG
from lib import *
import os

def show(c, dx=300, dy=200, ax=0, ay=0, az=1):
    '''
    Zobrazenie obrazku na ploche notebooku / knihy
    obrazok nie je centrovany
    '''
    display(SVG(c.obj.toSvg(opts={ "width": dx,   "height": dy,       "marginLeft": 0,
                                   "marginTop": 0, "showAxes": False, "projectionDir": (ax, ay, az),
                                    "strokeColor": (0, 0, 0),  "showHidden": True,
                                 }
            )  )  )


def convert_to_image(comp, file_name, ax=0.3, ay=0.3, az=1.0, color=(0,0,0)):
    '''
    Generovanie SVG obrazku
    Konverzia na PNG
    Uprava rozmerov
    '''
    fp = open(file_name+'.svg', 'w')
    fp.write(comp.obj.toSvg(opts={
        #"width": 300,
        #"height": 150,
        "marginLeft": 5,
        "marginTop": 5,
        "showAxes": False,
        "projectionDir": (ax, ay, az),
        "strokeColor": (0, 0, 0),
        "showHidden": True,
        }))
    fp.close()

    # konverzia na PNG a orezanie okrajov
    os.system('rsvg-convert -z 2 -o ' + file_name + '.png ' + file_name + '.svg ')
    os.system('convert ' + file_name+ '.png  -trim -fuzz 5%  +repage ' + file_name+'.png')
