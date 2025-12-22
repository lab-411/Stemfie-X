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
# <font color='navy'> <b> Nosníky </b> </font>

```{figure} ./img/banner.png
:width: 800px
:name: stmx_201
```

```{figure} ./img/image_block.png
:width: 800px
:name: stmx_110

```

**Nosníky** (Baems) sú druhým základným typom dielov v *Stemfie-X* primárne určené pre použitie ako nosníky a platne. Verzie *U*, *L* a H je možné využiť ako základ pre menšie konštrukcie.

## <font color='purple'> <b> Funkcie </b></font>

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

    
### <font color='brown'> <b> Značenie dielov </b></font>

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
        

## <font color='purple'> <b> Použitie </b></font>     

### <font color='brown'> <b> Jednoduché nosniky </b></font>


    b1 = Beam_Block(7)          

```{code-cell} ipython3  
:tags: ["remove-cell"]

from lib import *
from lib.utils import *

b0 = Beam_Block(7)
convert_to_image(b0, './src/block_b0')
```

```{figure} ./src/block_b0.png
:width: 300px

Jednoduchý lineárny blok - *block_B_07*
```

    b1 = Beam_Block([3, 3, 2])   
    
```{code-cell} ipython3  
:tags: ["remove-cell"]

from lib import *
from lib.utils import *

b1 = Beam_Block([3, 3, 2])
convert_to_image(b1, './src/block_b1')
```

```{figure} ./src/block_b1.png
:width: 150px

Blok s montážnymi otvormi vo všetkých smeroch - *block_B_03_02_02*.
```


    b2 = Beam_Block([4, 3 ,1/2], [False, False, True])  

```{code-cell} ipython3  
:tags: ["remove-cell"]

from lib import *
from lib.utils import *

b2 = Beam_Block([4,3,1/2], [False, False, True])  
convert_to_image(b2, './src/block_b2')
```

```{figure} ./src/block_b2.png
:width: 150px

Platňa 4x3BU - *block_B_04_03_12_001*.
```

### <font color='brown'> <b> Kombinované nosniky </b></font>

    
    b4 = Beam_U_Block(4,3) 

```{code-cell} ipython3  
:tags: ["remove-cell"]

from lib import *
from lib.utils import *

b4 = Beam_U_Block(4,3)  
convert_to_image(b4, './src/block_b4')
```

```{figure} ./src/block_b4.png
:width: 150px

Blok U - *block_U_04_03*.
```
    
% --------------

    b5 = Beam_H_Block(4,3) 
    
```{code-cell} ipython3  
:tags: ["remove-cell"]

from lib import *
from lib.utils import *

b5 = Beam_H_Block(4,3) 
convert_to_image(b5, './src/block_b5')
```

```{figure} ./src/block_b5.png
:width: 150px

Blok H - *block_H_04_03*.
```

%---------------
    
    b6 = Beam_L_Block(7,2,1/4, 1/2)


```{code-cell} ipython3  
:tags: ["remove-cell"]

from lib import *
from lib.utils import *

b6 = Beam_L_Block(7,2,1/4, 1/2)
convert_to_image(b6, './src/block_b6')
```

```{figure} ./src/block_b6.png
:width: 220px

Blok L - *block_L_07_02_14*.
```
