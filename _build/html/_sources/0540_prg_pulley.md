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
# <font color='navy'> <b> Kladky </b> </font>

```{figure} ./img/banner.png
:width: 800px
:name: stmx_112
```

```{figure} ./img/image_pulley.png
:width: 800px
:name: stmx_110

```

Kladky sú konštrukčnými prvkami pre tvorbu jednoduchých strojov (jednoduchá kladka, kladkostroj) a lanových prevodov.  

## <font color='purple'> <b> Funkcie </b></font>

Knižnica obsahuje základné veľkosti kladiek a držiakov.

    Pulley_A(diam, thick, dp)
    Pulley_B(diam, thick, dp, dh, rh)
    Pulley_C(diam, thick, dp, dh, rh)
    
    Parametre       Default   Popis 
    --------------------------------------------------------------
    diam                      priemer kladky
    thick           1         hrubka kladky
    dp              1/2       zahlbenie kladky (vnutorny priemer)
    dh              1/4       hrubka nosnej vyplne kladky
    rh              [1]       pole priemerov otvorov
    
    Pulley_Holder_A(height)   držiak o šírke 1BU
    Pulley_Holder_B(height)   držiak o šírke 2BU

### <font color='brown'> <b> Značenie dielov </b></font>

    pulley_t_dd_hh

    t  - typ kladky
         A - jednoducha plna kladka pre mensie priemery 
         B - odlahcena kladka pre väčšie priemery
         C - odlahčená kladka s lúčmi pre veľke priemery
    
    dd - priemer hladky
    hh - hrubka kladky
    
    pulhold_t_nn
    
    t  - typ držiaka
    hh - výška držiaka
    
## <font color='purple'> <b> Príklady použitia </b></font>

    p0 = Pulley_A(2,1)        # pulley_A_02_01

```{code-cell} ipython3  
:tags: ["remove-cell"]

from lib import *
from lib.utils import *

p0 = Pulley_A(2,1)
convert_to_image(p0, './src/img_0540a')
```

```{figure} ./src/img_0540a.png
:width: 110px

Jednoducha plná kladka
```


    p1 = Pulley_B(3,1)        # pulley_B_03_01

```{code-cell} ipython3  
:tags: ["remove-cell"]

from lib import *
from lib.utils import *

p1 = Pulley_B(3,1)
convert_to_image(p1, './src/img_0540b')
```

```{figure} ./src/img_0540b.png
:width: 160px

Odľahčená kladka
```

    p1 = Pulley_B(3,1)        # pulley_B_03_01

```{code-cell} ipython3  
:tags: ["remove-cell"]

from lib import *
from lib.utils import *

p2 = Pulley_C(4,1)
convert_to_image(p2, './src/img_0540c')
```

```{figure} ./src/img_0540c.png
:width: 180px

Odľahčená veľká kladka
```


