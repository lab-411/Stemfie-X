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
# <font color='navy'> Priehradový most  </font>

```{figure} ./img/banner.png
:width: 800px
:name: exam_001
```
Model priehradového mostu patrí medzi jednoduché statické konštrukcie pre začiatočníkov. Model mostu je zameraný na získanie elementárnych zručností pri používaní náradia, spojovacieho materiálu a správneho postupu montáže. Výsledný model zároveň intuitívne prezentuje elementárne poznatky zo statiky, kde je zrejmé, že nosnosť poskladaného mosta je väčšia ako jednoduchej lávky. 

Model mostu je zostavený zo štandardných dielov stavebnice bez dodatočných modifikácií a úprav dielov. 

```{figure} ./model/0210_most/img/most_03.png
:width: 700px
:name: exam_002

Model jednoduchého priehradového cestného mostu
```

## <font color='purple'> Montáž </font>


Postup montáže jedného segmentu mostu je zrejmý z nasledujúceho obrázku. Veľkosť mostu môžete upraviť pridávaním segmentov mostu. Pre montáž sú použité štandardné skrutky M4x6. V prípade potreby si môžete parametre modelu (napríklad šírku mostu) upraviť vygenerovaním upravených dielov pomocou programom s využitím knižnice komponentov.  

```{figure} ./model/0210_most/img/most_07.png
:width: 300px
:name: exam_021

Postup montáže časti segmentu mostu.
```


## <font color='purple'> Diely </font>

Farebné prevedenie dielov je orientačné, pre konštrukciu si môžete zvoliť vlastné farebné prevednie. 

````{dropdown} Zoznam dielov priehradového mostu.

```{list-table}
:header-rows: 1

* - Počet
  - Popis
  - Farba
  - Súbor (step)
* - 3
  - Mostovka
  - bledomodrá
  - [block_U_10_05_14](./model/0210_most/parts/block_U_10_05_14_12.step)
* - 2
  - Pilier
  - hnedá
  - [block_H_05_05_14_12_02_02](./model/0210_most/parts/block_H_05_05_14_12_02_02.step)
* - 8
  - Spojka mostovky
  - oranžová
  - [brace_B_04_14](./model/0210_most/parts/brace_B_04_14.step)
* - 12
  - Diely nosníka
  - červená
  - [brace_B_09_14](./model/0210_most/parts/brace_B_09_14.step)
* - 4
  - Diely nosníka
  - oranžová
  - [brace_B_11_14](./model/0210_most/parts/brace_B_11_14.step)
* - 3
  - Spojky nosníkov
  - šedá
  - [block_U_02_05_14_12](./model/0210_most/parts/block_U_02_05_14_12.step)
* - 36
  - Skrutka M4x6
  - šedá
  - 
```
````


