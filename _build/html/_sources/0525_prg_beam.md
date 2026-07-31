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
# <font color='navy'> Nosníky </font>

```{figure} ./img/banner.png
:width: 800px
:name: stmx_201
```

```{figure} ./img/image_block.png
:width: 800px
:name: stmx_110

```

**Nosníky** (Baems) sú druhým základným typom dielov v *Stemfie-X* primárne určené pre použitie ako nosníky a platne. Verzie *U*, *L* a H je možné využiť ako základne pre menšie konštrukcie.

## <font color='purple'> Knižnica </font>

Základným typom je jednoduchy nosník (Beam_Block), odvodenými typmi sú verzie *U*, *H*, *L*. 

    Beam_Block([x,y,z], center)
    Beam_Block(d, center)
    Beam_U_Block(x,y)
    Beam_H_Block(x,y)
    Beam_L_Block(x,y)
    
    Parametre       Default   Popis 
    --------------------------------------------------------------
    d               1         rozmery v počte otvorov 
    x,y,z           1         rozmery
    center          True      poloha v strede súradnicovej sústavy 

    
### <font color='brown'> Značenie dielov </font>

    block_t_xx_yy_zz_hhh    basic form
    block_t_xx_yy           abbreviated forms
    block_t_xx

    t  - block type                               xx,yy,zz - block dimension
         B - simple beam                                     01 =   1 BU
         U - beam block modifications                        ...
         H                                                   10 =  10 BU
         L                                                   12 = 1/2 BU
         X - user defined non standard block                 14 = 1/4 BU 
        
    hhh - holes configuration in x y z directions
        000 - no holes
        100 - holes in x direction
        ...
        111 - holes in all directions

    block_B_xx_yy_zz_hhh
    block_H_xx_yy_hx_hy
    block_U_xx_yy_hx_hy
    block_L_xx_yy_hx_hy
        

## <font color='purple'>  Použitie  </font>     

### <font color='brown'> Jednoduché nosniky a bloky </font>

Pomocou parametrov funkcie *Beam_Block()* môžeme vytvárať rôzne typy noníkov, blokov a platní.

```{code-block} Python
:caption: Jednoduchý nosník s montážnymi otvormi v xyz smeroch.
from lib import *
b1 = Beam_Block(7)  
b1.export_step(b1.name)
```
    
    
```{code-cell} ipython3  
:tags: ["remove-cell"]

from lib import *
from lib.utils import *

b0 = Beam_Block(7)
convert_to_image(b0, './src/block_b0')
```

```{figure} ./src/block_b0.png
:width: 300px

Jednoduchý nosník.
```

%--------------------------------------------------

```{code-block} Python
:caption: Blok s redukovanými montážnymi otvormi.
from lib import *
b2 = Beam_Block([3, 3, 2], [False, True, True]) 
b2.export_step(b2.name)
```

```{code-cell} ipython3  
:tags: ["remove-cell"]

from lib import *
from lib.utils import *

b1 = Beam_Block([3, 3, 2], [False, True, True])
convert_to_image(b1, './src/block_b1')
```

```{figure} ./src/block_b1.png
:width: 150px

Blok s redukovanými montážnymi otvormi.
```

%--------------------------------------------------

```{code-block} Python
:caption: Montážna platňa 4x3 BU 
from lib import *
b3 = Beam_Block([4, 3 ,1/2], [False, False, True]) 
b3.export_step(b3.name)
```
 

```{code-cell} ipython3  
:tags: ["remove-cell"]

from lib import *
from lib.utils import *

b2 = Beam_Block([4,3,1/2], [False, False, True])  
convert_to_image(b2, './src/block_b2')
```

```{figure} ./src/block_b2.png
:width: 150px

Montážna platňa 4x3 BU 
```

### <font color='brown'> Kombinované nosniky </font>

Kombinované nosníky sú tuhšie ako jednoduché platne, môžeme ich použiť pri tvorbe väčších a namáhaných konštrukcií. 

```{code-block} Python
:caption: Blok typu U
from lib import *
b4 = Beam_U_Block(4,3)
b4.export_step(b4.name)
```

```{code-cell} ipython3  
:tags: ["remove-cell"]

from lib import *
from lib.utils import *

b4 = Beam_U_Block(4,3)  
convert_to_image(b4, './src/block_b4')
```

```{figure} ./src/block_b4.png
:width: 150px

Blok typu U
```
    
%--------------------------------------------------

```{code-block} Python
:caption: Blok typu H
from lib import *
b5 = Beam_H_Block(4,3) 
b5.export_step(b5.name)
```

```{code-cell} ipython3  
:tags: ["remove-cell"]

from lib import *
from lib.utils import *

b5 = Beam_H_Block(4,3) 
convert_to_image(b5, './src/block_b5')
```

```{figure} ./src/block_b5.png
:width: 150px

Blok typu H 
```

%--------------------------------------------------

```{code-block} Python
:caption: Blok typu L
from lib import *
b6 = Beam_L_Block(7,2,1/4, 1/2)
b6.export_step(b6.name)
```

```{code-cell} ipython3  
:tags: ["remove-cell"]

from lib import *
from lib.utils import *

b6 = Beam_L_Block(7,2,1/4, 1/2)
convert_to_image(b6, './src/block_b6')
```

```{figure} ./src/block_b6.png
:width: 220px

Blok typu L 
```
