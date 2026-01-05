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
# <font color='navy'> <b> Diely </b> </font>


```{figure} ./img/banner.png
:width: 800px
```

## <font color='purple'> <b> Parametre  </b> </font>

Vlastnosti dielov stavebnice `STEMFIE-X` definuje základná jednotka **BU** (Basic Unit) a priemer montážnych otvorov **HR** (Hole Radius). Rozmery dielov sú udávané v násobkoch alebo podieloch BU.

```{figure} ./img/brace_rozmery.png
:width: 350px

Základné parametre dielov (spojka, D=8, H=1/4).
```

Na rozdiel od stavebníc, ktoré majú diely z plechu, musíme pri našich konštrukciách uvažovať hrúbku dielov. Štandardné parametre dielov sú definované ako

* veľkost **BU** je 10mm
* priemer montážnych otvorov **HR** je 4mm
* priemer otvorov pre osi a hriadele **HRX** je 4.1mm
* veľkost dielov **D** je celočíselná v násobkoch 1,2 ... **BU** 
* hrúbka dielov **H** je 1, 1/2, 1/3, 1/4 **BU**

Pre jednoduchšiu orientáciu sú diely stavebnice označené typom, ktorý vychádza z ich tvaru a rozmerov, napríklad zobrazená spojka má označenie *brace_B_08*.

```{admonition} Úpravy štandardných parametrov
:class: tip

Pri vytváraní podkladov pre 3D tlač pomocou s využitím knižnice *Stemfie-X* možeme zmenou hodnôt premenných **BU**, **HR** a **HRX** upraviť vlastnosti a rozmery dielov stavebnice. Napríklad ak chceme pre spájanie dielov využiť skrutky, ktoré si v dieloch "vyrežú" vlastný závit, je vhodné hodnotu **HR** zmeniť na veľkosť 3.85mm.

```

### <font color='brown'> <b> 3D Tlač   </b> </font>

Doporučené parametre 3D tlače upravte podľa vašej tlačiarne a použitého materiálu. Diely stavebnice sú v tejto pulikácii generované vo formáte *.step* alebo *.stl*, pre ich tlač použite programové vybavenie doporučované výrobcom tlačiarne.  

* materiál PLA
* hrúbka vrstvy 0.2mm, bez podpier
* perimeter 4x
* výplň 15%
* teplota a rýchlosť tlače podľa doporučenia výrobcu filamentu

```{figure} ./img/slicer.png
:width: 500px

Príprava tlače dielov stavebnice.
```


## <font color='purple'> <b> Prehľad dielov stavebnice </b> </font>

Sada základných typov dielov stavebnice pre konštrukcie v *Stemfie-X* je vygenerovaná vo formáte *.step* a *.stl* pripravených pre 3D tlač. Súčasťou stavebnice sú knižnice pre programovací jazyk *Python*, v ktorom je možné vytvárať si vlastné verzie dielov stavebnice.   

### <font color='brown'> <b> Spojky  </b> </font>

Spojky (Brace) sú základným typom dielov stavebnice, slúžia na spájanie častí konštrukcie, konštrukcie nosníkov a podpôr. V závislosti od použitia môžu mať rôzny tvar, hrúbku a počet montážnych otvorov. V niektorých prípadoch môžu byť dva lebo aj viacej otvorov nahradených montážnou štrbinou.

```{figure} ./img/image_brace.png
:width: 600px

Prevedenia spojok.
```

### <font color='brown'> <b> Nosníky </b> </font>

Nosníky (Beams) slúžia na konštrukciu nosných prvkov konštrukcií, základových platní a konštrukčných prvkov tam, kde sa vyžaduje zvýšená pevnosť alebo nosnosť.

```{figure} ./img/image_block.png
:width: 600px

Rozne prevedenia blokov.
```

### <font color='brown'> <b> Kladky </b> </font>

Kladky a držiaky kladiek slúžia na konštrukciu jednoduchých strojov, lanových prevodov a  kladkostrojov.

```{figure} ./img/image_pulley.png
:width: 600px

Kladky a držiaky kladiek.
```

### <font color='brown'> <b> Ozubené kolesá </b> </font>

Ozubené kolesá sú základom pre konštrukciu prevodoviek k motorom a servám. 

```{figure} ./img/gears_demo.png
:width: 600px

Ozubené kolesá
```

### <font color='brown'> <b> Základné bloky </b> </font>

Základné bloky sú podkladom pre konštrukciu vlastných neštandardných prvkov stavebnice.

```{figure} ./img/image_base.png
:width: 600px

Základné bloky
```
