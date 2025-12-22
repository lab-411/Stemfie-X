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
# <font color='navy'> <b> Spojky </b> </font>

```{figure} ./img/banner.png
:width: 800px
:name: stmx_112
```

```{figure} ./img/image_brace.png
:width: 800px
:name: stmx_110

```

**Spojky** (Brace) sú základným konštrukčným typom dielov v *Stemfie-X* primárne určený pre spájanie dielov, ale je možné ich využiť aj ako konštrukčný prvok na vytváranie vystužených konštrukcií ako sú ramená žeriavov, robotov a pod. Spojky môžu obsahovať montážne otvory ako aj štrbiny. Štandardná hrúbka spojky je 1/4 **BU** (2.5mm), pomocou knižnice je možné programovo vytvárať spojky rôznych tvarov a konfigurácií. Lineárna spojka je rozmerovo kompatibilná s kovovými spojkami stavebníc *Meccano* a *Merkur*. 

## <font color='purple'> <b> Funkcie </b></font>

Základným typom je lineárna spojka *Brace*, oblúková spojka *Brace_Arc* a kruhová spojka *Brace_Circle*. Funkcie pre generovanie spojok majú formát

    Brace(size, height, holes, center)
    Brace_Arc(radius, angle, height, num_holes, center)
    Brace_Circle(radius, height, num_holes, center)
    
    Parametre       Default   Popis 
    --------------------------------------------------------------
    size            1         rozmery v počte otvorov 
    height          1         výška
    length          1         dĺžka 
    radius          5         polomer
    holes           True      lineárna spojka s otvormi / bez otvorov
    num_holes       4         počet montážnych otvorov
    angle           180       uhol v stupňoch
    center          True      poloha v strede súradnicovej sústavy 

    
### <font color='brown'> <b> Značenie dielov </b></font>

    brace_t_dd_hh_pp_ss[s]    basic form
    brace_t_dd_hh_pp          abbreviated forms, unlisted parameters have default values
    brace_t_dd_hh
    brace_t_dd

    t  - brace type                         dd - brace size               hh - brace height
         B - simple brace                        01 ... 99 BU                  01 =    1 BU
         C - circle brace                                                      ...
         A - arc brace                                                         10 =   10 BU
         X - user defined non standard brace                                   12 =  1/2 BU 
                                                                               14 =  1/4 BU
        
    ss - number of slots                    pp - number of holes if it does not match the size
         00 ... 99                               00 ... 99

        
    brace_B_dd_hh_pp_ss
        dd - brace size
        pp - number of holes
        ss - number of slots 
        
    brace_C_dd_hh_pp_ss
        dd - brace radius
        hh - brace height     
        pp - number of holes
        ss - number of slots (TODO, not implemented)

    brace_A_dd_hh_pp_sss
        dd  - brace radius
        hh  - brace height, default value is 1/4 BU      
        pp  - number of holes
        sss - brace angle in [deg] 001 ... 180
        
## <font color='purple'> <b> Použitie </b></font>

### <font color='brown'> <b> Jednoduchá spojka </b></font>

Pre vygenerovanie jednoduchej spojky o hrúbke **1/4 BU** stačí zadať jej rozmer v **BU** jednotkách.

    b0 = Brace(5)    # brace_B_05

```{code-cell} ipython3  
:tags: ["remove-cell"]

from lib import *
from lib.utils import *

b0 = Brace(5)    # brace_B_05
convert_to_image(b0, './src/brace_b0')
```

```{figure} ./src/brace_b0.png
:width: 200px

Jednoducha spojka
```


### <font color='brown'> <b> Spojka so štrbinami </b></font>

Štrbiny požadovanej dĺžky vytvoríme pomocou triedy **Hole_Slot**, posunieme ich pomocou operátora **BU_Tx** do požadovanej pozície a pomocou operátpra **D()** odpočítame od štandardnej spojky.
     
    b1 = Brace(17)
    h1 = Hole_Slot(2, 1/2+1/4).BU_Tx(11)
    h2 = Hole_Slot(2, 1/2+1/4).BU_Tx(4)
    b1.D([h1, h2] )


```{code-cell} ipython3  
:tags: ["remove-cell"]
from lib import *
from lib.utils import *
       
b1 = Brace(17)
h1 = Hole_Slot(2, 1/2+1/4).BU_Tx(11)
h2 = Hole_Slot(2, 1/2+1/4).BU_Tx(4)
b1.D([h1, h2])

convert_to_image(b1, './src/brace_b1')
```


```{figure} ./src/brace_b1.png
:width: 600px

Spojka so štrbinami.
```

### <font color='brown'> <b> Oblúková spojka </b></font>

Pri oblúkovej spojke musí mať tetiva oblúku veľkosť v násobkoch **BU**. Pre výpočet parametrov oblúkovej spojky zadáme dĺžku tetivy a polomer oblúka, napríklad

* radius = 4 BU
* brace length = 7 BU

```{figure} ./img/comp_11.png
:width: 400px

Oblúková a lineárna spojka
```

Z uvedených parametrov musíme pre konštrukciu spojky výpočítať uhol a offsetu voči stredu opísanej kružnice podľa obrázku

```{figure} ./img/tetiva.png
:width: 350px

Veličiny pre výpočet oblúkovej spojky
```

Vstupnými hodnotami pre výpočet sú

* $R$    - circle radius, in BU units
* $D$    - chord length in BU units, D >= 2*R+1

Výstupnými hodnotami sú 

* $\beta$ - calculated angle
* $H$    - calculated offset

$$
\begin{align*}
\beta &= 2 \alpha      \\
\frac{D-1}{2} &= R \cdot \sin(\alpha)    \\
\\
\beta &= 2 \alpha = 2 \cdot \arcsin \Big( \frac{D}{2R} \Big) \\
H &= R \cdot cos(\alpha) \\
\end{align*}
$$

Konštrukcia oblúkovej spojky na základe výpočtu


    from numpy import arcsin, pi

    R = 3   # arc radius
    D = 7   # D >= 2*R+1 
    N = 3   # pocet otvorov
    
    alpha = arcsin( (D-1) / (2*R ) )
    beta = 2*alpha/pi*180
    H = R*cos(alpha)

    b3 = Brace_Arc(R, bdeg, 1/4, N, center=True).Rz(90-bdeg/2).BU_T([0, -H, 0])
    b4 = Brace(D, center=True).BU_Tz(-1/2)


```{code-cell} ipython3  
:tags: ["remove-cell"]
from lib import *
from lib.utils import *
from numpy import arcsin, pi

D = 7   # D >= 2*R+1  
R = 3   # arc radius

alpha = arcsin( (D-1) / (2*R ) )
beta = 2*alpha/pi*180
H = R*cos(alpha)

b3 = Brace_Arc(R, beta, 1/4, 3, center=True).Rz(90-beta/2).BU_T([0, -H, 0])
b4 = Brace(D, center=True).BU_Tz(-1/2)

b3.U(b4)
convert_to_image(b3, './src/brace_b3')
```


```{figure} ./src/brace_b3.png
:width: 250px

Oblukova spojka.
```
