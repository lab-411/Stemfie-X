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


# <font color='navy'>  Parametre  </font>


```{figure} ./img/banner.png
:width: 800px
```

## <font color='purple'> Rozmery </font>

Princíp stavebnice *STEMFIE-X* umožňuje tvorbu širokého spektra konštrukčných prvkov. Aby bola dodržaná vzájomná kompatibilita dielov, je vhodné pri návrhu dielov dodržať jednoduché základné pravidlá. 

Vlastnosti dielov stavebnice *STEMFIE-X* definuje základná jednotka **BU** (Basic Unit), priemer montážnych otvorov **HR_BASE** (Hole Radius) pre montážne prvky (skrutky a pod.) a otvory pre pohyblivé spoje, hiadele a osi **HR_AXIS**. Rozmery dielov sú udávané v násobkoch alebo podieloch BU. Pre jednoduchšiu orientáciu sú diely stavebnice označené typom, ktorý vychádza z ich tvaru a rozmerov, napríklad zobrazená spojka na obrázku má označenie *brace_B_08*.

```{figure} ./img/brace_rozmery.png
:width: 400px

Základné parametre dielov (spojka, D=8, H=1/4).
```

Na rozdiel od stavebníc, ktoré majú diely z plechu, musíme pri našich konštrukciách uvažovať s hrúbkou dielov. Štandardné parametre dielov sú definované ako

* štandardná veľkost jednotky **BU** je 10mm
* štandardný priemer montážnych otvorov **HR_BASE** je 4 mm
* priemer otvorov pre rotačné spoje, osi a hriadele **HR_AXIS** je 4.25 mm
* veľkost dielov **D** je celočíselná v násobkoch 1, 2 ... **BU** 
* hrúbka dielov **H** je v násobkoch 1, 1/2, 1/3, 1/4 **BU**

```{admonition} Úpravy štandardných parametrov
:class: tip

Pri vytváraní podkladov pre 3D tlač pomocou s využitím knižnice *Stemfie-X* možeme zmenou hodnôt premenných **BU**, **HR_BASE** a **HR_AXIS** upraviť vlastnosti a rozmery dielov stavebnice. Napríklad ak chceme pre spájanie dielov využiť skrutky, ktoré si v dieloch "vyrežú" vlastný závit, je vhodné hodnotu **HR_BASE** zmeniť na veľkosť 3.95mm. Skutočná veľkosť otvorov vo vytlačených dieloch závisí od použitého materiálu a parametrov tlače. 

```

### <font color='brown'>  3D Tlač dielov </font>

Doporučené parametre 3D tlače upravte podľa vašej tlačiarne a použitého materiálu. Diely stavebnice sú v tejto pulikácii generované vo formáte *.step* alebo *.stl*, pre ich tlač použite programové vybavenie doporučované výrobcom tlačiarne. V programe pre prípravu tlače (*slicer*) je vhodné nastaviť parametre tlače

* materiál PLA
* hrúbka vrstvy 0.2mm, bez podpier
* perimeter 4x
* výplň 15%
* teplota materiálu podľa doporučenia výrobcu filamentu, zvyčajne bližšie k hornej udávanej hranici

```{figure} ./img/slicer.png
:width: 500px

Príprava tlače dielov stavebnice.
```


