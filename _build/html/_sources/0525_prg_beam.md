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

`Nosníky` (Baems) sú druhým základným typom dielov v *Stemfie-X* primárne určené pre použitie ako nosníky a platne. Verzie *U*, *L* a H je možné využiť ako základ pre menšie konštrukcie.

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
        
### <font color='brown'> <b> Použitie </b></font>

```{code-cell} ipython3  
from lib import *
b1 = Beam_Block(7).Rz(15)                # jednoduchý nosník Beam_Block
display(SVG(b1.obj.toSvg()))
```

```{code-cell} ipython3  
b2 = Beam_Block([3, 3 ,2], [True, True, True]) # 2x3 Beam_Block
b2.BU_Tx(4).BU_Tx(4)
display(SVG(b2.obj.toSvg()))
```


```{code-cell} ipython3  
b3 = Beam_Block([4, 3 ,1/2], [False, False, True])  # 4x3 BU platňa
display(SVG(b3.obj.toSvg()))
```

```{code-cell} ipython3  
b4 = Beam_U_Block(4,3).Rx(45)   # 4x3 BU U-Shape plate 
display(SVG(b4.obj.toSvg()))
```


```{code-cell} ipython3  
b5 = Beam_H_Block(4,3).Rx(45)   # 4x3 BU U-Shape plate 
display(SVG(b5.obj.toSvg()))
```

```{code-cell} ipython3  
b6 = Beam_L_Block(7,2,1/4, 1/2).Rx(45)   # 4x4 BU L-Shape plate 
display(SVG(b6.obj.toSvg()))
```

