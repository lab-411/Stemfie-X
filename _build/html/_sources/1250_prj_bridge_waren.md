---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.5
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---
# <font color='navy'> Konštrukcie mostov  </font>

```{figure} ./img/banner.png
:width: 800px
:name: exam_001
```
Stavebné inžinierstvo pozná niekoľko základných konfigurácií priehradových mostných konštrukcií. S využitím štandardných ako aj modifikovaných dielov si môžete vytvoriť most podľa Vašich predstáv a preskúmať vlastnosti konštrukcie.

```{figure} ./model/0212_waren/img/mosty.gif
:width: 700px
:name: exam_005

Typy priehradových mostov.
```

## <font color='purple'> Návrh mostu typu Warren  </font>

Pre model priehradového mostu typu Warren potrebujeme okrem štandardných dielov z knižnice vygenerovať upravené komponenty, ktoré vyplývajú z geometrie konštrukcie. Most je možné zostaviť zo štandardných dielov, jediným špecifickým dielom je šikmá výztuha.


```{figure} ./model/0212_waren/img/most_05.png
:width: 700px
:name: exam_004

Model priehradového mostu s nosníkmi typu [Warren](https://en.wikipedia.org/wiki/Warren_truss) 
```

### <font color='brown'> Návrh modifikovaných dielov  </font>

Vzdialenosť otvorov pre šikmú výztuhu nie je celočíselným násobkom **BU**, 

$$
L=\sqrt{70^2 + 70^2} = 98.99
$$

a je približne o 1 mm kratšia ako je dĺžka štandardnej spojky.

```{figure} ./model/0212_waren/img/vypocet_view.png
:width: 350px
:name: exam_1250b

Dĺžka šikmej výztuhy (všetky miery v mm).
```

Pre spojenie dielov preto použijeme spojku so štrbinou, z dôvodu jednoduchosti a zámennosti použijeme štrbiny na oboch koncoch spojky. Z obrázku je zrejmý presah štrbiny nad montážnym otvorom.

```{figure} ./model/0212_waren/img/vypocet_zostava.png
:width: 330px
:name: exam_1250c

Zostava so šikmou výztuhou..
```


```{code-block} Python
:caption: Konštrukcia šikmej výztuhy.
from lib import *
b6 = Brace(11)
h2 = Hole_Slot(2, 3/4)
h3 = Hole_Slot(2, 3/4).BU_Tx(9)
b6.D([h2,h3])
b6.export_step('../parts/brace_B_11_07_02')  
```


```{code-cell} ipython3  
:tags: ["remove-cell"]

from lib import *
from lib.utils import *

b6 = Brace(11)
h2 = Hole_Slot(2, 3/4)
h3 = Hole_Slot(2, 3/4).BU_Tx(9)
b6.D([h2,h3])
convert_to_image(b6, './src/brace_b6')
```

```{figure} ./src/brace_b6.png
:width: 300px

 Šikmá výstuha
```


### <font color='brown'> Zostava a diely </font>

```{figure} ./model/0212_waren/img/zostava.png
:width: 500px
:name: exam_1250a

Zostava segmentu mostu.
```






