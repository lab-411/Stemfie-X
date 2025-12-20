from lib import *
from ipywidgets import *
from IPython.display import display
from ipywidgets import HTML as wHTML

button1 = Button(description="Create", layout=Layout(width = "140px"))
button2 = Button(description="Save STEP/STL",   layout=Layout(width = "140px"))
output1 = Output(layout={'border': '1px solid black'})
output2 = Output(layout={'border': '1px solid black'})
output3 = Output(layout={'border': '1px solid black'})
output4 = Output() #layout={'border': '1px solid black'})

text1 = Label(value="Size D",      layout=Layout(width = "80px"))
text2 = Label(value="Thickness H", layout=Layout(width = "80px"))
text3 = Label(value="BU")
text4 = Label(value=" ",         layout=Layout(width = "80px"))
text5 = Label(value=" ",         layout=Layout(width = "200px"))
text6 = Label(value=" ",         layout=Layout(width = "200px"))

brace_size =  IntText( value=3,  disabled=False, layout=Layout(width = "140px"))
brace_thick = Dropdown(options=[('1/4', 1/4), ('1/2', 1/2), ('3/4', 3/4), ('1',1 ), ('1+1/4', 5/4 ),
                                 ('1+1/2', 3/2 ), ('1+3/4', 7/4), ('2', 2)   ], value=1/4, 
                               layout=Layout(width = "140px"))

br = Brace(3)
br.name = ''

def on_button1_clicked(bc):
    global br
    br = Brace(brace_size.value, brace_thick.value)
    dd = br.convert_param(brace_size.value)
    hh = br.convert_param(brace_thick.value)
    br.name = 'brace_B_'+dd+'_'+hh
    text5.value = br.name
    text6.value = ' '

    with output1:
        clear_output()
        display(SVG(br.obj.toSvg(opts={ "width": 300,   "height": 150,       "marginLeft": 10, 
                                       "marginTop": 10, "showAxes": False,  "projectionDir": (0, 0, 1),
                                       "strokeColor": (255, 0, 0),          "showHidden": True,
                                      } ) ) )

    bb = br.copy()
    bb.Rx()
    with output2:
        clear_output()
        display(SVG(bb.obj.toSvg(opts={ "width": 300,   "height": 150,       "marginLeft": 10, 
                                       "marginTop": 10, "showAxes": False,  "projectionDir": (0 , 0, 1),
                                       "strokeColor": (255, 0, 0),          "showHidden": True,
                                      } ) ) )

    bb = br.copy()
    bb.Ry()
    with output3:
        clear_output()
        display(SVG(bb.obj.toSvg(opts={ "width": 300,   "height": 150,       "marginLeft": 10, 
                                       "marginTop": 10, "showAxes": False,  "projectionDir": (0, 0, 1),
                                       "strokeColor": (255, 0, 0),          "showHidden": True,
                                      } ) ) )

    with output4:
        clear_output()
        display(SVG(br.obj.toSvg(opts={ "width": brace_size.value*80 +10,   "height": brace_size.value*40+10,
                                       "marginLeft": 10, 
                                       "marginTop": 10, "showAxes": False,  "projectionDir": (1, 1, 1),
                                       "strokeColor": (255, 0, 0),          "showHidden": True,
                                      } ) ) )

def on_button2_clicked(bc):
    global br
    text6.value = './export/' +br.name
    br.export_step('./export/'+br.name)
    br.export_stl('./export/'+br.name)

button1.on_click(on_button1_clicked)
button2.on_click(on_button2_clicked)
     
'''   
VBox( [ 
    HBox( [wHTML("<H2> <font color=maroon> Parameters</font></H2>") ]),
    HBox([text1, brace_size, text3]),
    HBox([text2,brace_thick,text3]),
    HBox([text4, button1, text5]),
    HBox([text4, button2, text6]),
    #HBox([text4, output1, output2]),
    #HBox([text4, output3, output4])
    HBox([text4, output4])
])
'''
