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
# <font color='navy'> <b> Ako na to</b> </font>

```{figure} ./img/banner.png
:width: 800px
:name: prg_100
```

Pri návrhu našej konštrukcie sme zistili, že potrebujeme spojku v tvare T o hrúbke 1/4 BU. Pri návrhu môžeme ako pomôcku na náčrty používať štvorčekový papier s rastrom 5mm (BU/2), na ktorom získame predstavu o skutočnej veľkosti dielov. 

```{figure} ./img/prg_navrh.jpg
:width: 350px

Náčrt dielu na štvorčekovom papieri.
```

Náš diel do stavebnice "vyrobíme" naprogramovaním v jazyku *Python* s použitím knižníc pre projektovanie dielov. K výrobe dielu potrebujeme 

* elementárne znalosti informatiky a programovania, najlepšie v *Pythone* (súbor, adresár, spustenie programu, základné syntaktické konštrukcie, práca s knižnicami)
* nainštalovaný editor *CQ-Editor* s knižnicou *CadQuery* a v pracovnom adresári rozbalenú knižnicu pre *Stemfie-X* podľa [návodu](./0900_instalacia.md) 
* nainštalované programy pre prehliadanie podkladov pre 3D tlač a generovanie dát pre tlačiareň
* znalosť práce s 3D tlačiarňou 

## <font color='purple'> <b> Návrh dielu</b> </font>

Pri návrhu dielu postupujeme podľa nasledujúcich bodov

* vytvoríme si pracovný adresár a rozbalíme do podadresári *./lib* [knižnicu](./lib/lib.zip) pre návrh dielov 
* spustíme editor *CQ-Editor*, vytvoríme nový súbor (*File -> New*) a **uložíme** (*File -> Save*) ho do pracovného adresára
* vytvoríme program pre návrh dielu

```{code-block} python
:caption: Prvý program

from lib import *            # import kniznice Stemfie-X
b1 = Brace(5)                # vytvorenie spojky o velkost 5BU v rovine XY
b2 = Brace(3).Rz().BU_Tx(2)  # vytvorenie spojky 3BU
                              # Rz()      - otocenie o 90 stupnov okolo osi Z
                              # BU_Tx(2)  - posun v smere osi X o dlzku 2BU      
b1 = b1.U([b2])              # U() union - zjednotenie (spojenie) objektov 
show_object(b1.obj)          # zobrazenie dielu v CQ-Editor
b1.export_step('part_b1')    # vygenerovanie podkladov pre tlac vo formate STEP
```

Program spustíme pomocou zelenej šípky v záhlaví editoru alebo klávesou F5. Osi súradnicovej sústavy sú zobrazené v pravom dolnom rohu okna prehliadača. Pre zobrazenie chybových hláseni pri preklade treba mať aktivovanú voľbu *Current tracebak* vo voľbe *View*.  

```{figure} ./img/prg_cq.png
:width: 600px

Návrh dielu v CQ-Editore.
```

```{admonition} Zdrojové kódy
:class: tip

V tejto publikácii budeme zobrazovať zdrojové kódy príkladov bez príkazov pre import *Stemfie-X* knižníc *lib* a príkazov na export a zobrazenie objektov

      b1 = Brace(5)                
      b2 = Brace(3).Rz().BU_Tx(2)       
      b1 = b1.U([b2])             
      
Príkazy na zobrazenie objektov sa líšia podľa použitého editora a príkazy na export objektov sa používajú v závislosti od kontextu príkladu. 
```

## <font color='purple'> <b> Export podkladov pre tlač </b> </font>

Program vygeneruje príkazom *b1.export_step('part_b1')* podklady pre tlač vo formáte STEP. Tento formát je bezstratový, obsahuje vnútornú štruktúru objektu a vygenerované dáta je možné používať v kompatibilných CAD systémoch, napríklad [FreeCAD](https://www.freecad.org/). 

Podklady je možné vygenerovať aj vo formáte STL príkazom *b1.export_stl('part_b1')*, ktorý je tak isto možné použiť pre 3D tlač, formát STL je stratový, obsahuje len vonkajšie plochy objektu.

Exportované dáta môžeme prehliadať vo vhodnom prehliadači, napríklad [f3d](https://f3d.app/)

```{figure} ./img/part_b1.png
:width: 300px

Prehliadanie vygenerovaných dát v prehliadači *f3d*.
```

## <font color='purple'> <b> 3D Tlač </b> </font>

Vytvorené dáta spracujeme programom pre generovani povelového kódu pre 3D tlačiareň (gcode). Presný postup závisí od použitej tlačiarne, na obrázku je spracovanie podkladov pre tlač pomocou programu [PrusaSlicer](https://www.prusa3d.com). 

```{figure} ./img/prg_slicer.png
:width: 600px

Generovanie dát pre 3D tlač.
```
