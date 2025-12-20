#from IPython.display import *
from IPython.display import SVG
from lib import *
#import os

#def convert_to_image(comp, file_name):
#    fp = open(file_name+'.svg', 'w')
#    fp.write(comp.obj.toSvg())
#    fp.close()
#    os.system('magick  -density 1200 ' + file_name + '.svg ' + file_name + '.png ')
#    return file_name + '.png'

def show(c, dx=300, dy=200, ax=0, ay=0, az=1):
    display(SVG(c.obj.toSvg(opts={ "width": dx,   "height": dy,       "marginLeft": 0,
                                   "marginTop": 0, "showAxes": False, "projectionDir": (ax, ay, az),
                                    "strokeColor": (0, 0, 0),  "showHidden": True,
                                 }
            )  )  )
