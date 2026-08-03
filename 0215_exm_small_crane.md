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
# <font color='navy'> Malý žeriav  </font>

```{figure} ./img/banner.png
:width: 800px
:name: exam_001
```

 
Model malého žeriavu umožňuje zdvíhanie bremena pomocou jednoduchej kladky a navijakom. V modeli sú použité rotačné spoje, rameno žeriavu je možné zdvihať a kabína sa môže otáčať. Model je určený pre mierne pokročilých staviteľov, v prípade potreby vyžaduje mierne úpravy otvorov pre hriadele a fixáciu otočných prvkov vhodným lepidlom. 

```{figure} ./model/0215_mini_zeriav/img/zeriav_01.jpg
:width: 500px

Malý žeriav.
```

## <font color='purple'> Montáž </font>

Model pozostáva z ramena, kabíny a podvozku. Samostatne zložíme rameno a podvozok, na podlahu kabíny upevníme rameno zospodu jednou skrutkou M4x5. Priskrutkujeme jednu stenu kabíny, nasadíme navijak, druhú stenu a strechu. Nasadíme a v prípade potreby fixujeme kľuku navijaku, doplníme povrázok a hák.  


### <font color='brown'> Rameno žeriavu </font>

Pre montážou kladku, podperu ramena a podstavu nasadeníme tesne na hriadele o dĺžke 16mm. Otvory v dieloch sú upravené pre požitie hriadeľov, samotné hriadele sa v nosníkoch ramena majú otáčať voľne. V prípade potreby upravte veľkosti otvorov v ramenách ihlovým pilníkom.  


````{subfigure} AB
:layout-sm: A|B
:gap: 2px
:subcaptions: below
:width: 700px

```{image} ./model/0215_mini_zeriav/img/diely_01.jpg
:alt: Diely ramena
:width: 300px
```

```{image} ./model/0215_mini_zeriav/img/rameno_03.png
:alt: Zostava ramena
:width: 300px
```
Konštrukcia ramena žeriavu.
````

````{dropdown} Diely ramena žeriavu.

```{list-table}
:header-rows: 1

* - Počet
  - Popis
  - Farba
  - Súbor (step)
* - 2
  - Rameno žeriavu
  - žltá
  - [brace_B_17_14](./model/0215_mini_zeriav/parts/brace_B_17_14.step)
* - 2
  - Spojka
  - červená
  - [brace_B_02_01](./model/0215_mini_zeriav/parts/brace_B_02_01.step)
* - 1
  - Kladka
  - oranžová
  - [pulley_A_15](./model/0215_mini_zeriav/parts/pulley_A_15.step)
* - 1
  - Podpera
  - oranžová
  - [podpera](./model/0215_mini_zeriav/parts/podpera.step)
* - 1
  - Podstava
  - červená
  - [rack_2](./model/0215_mini_zeriav/parts/rack_2.step)
* - 3
  - Hriadel 4x15mm
  - 
  - 
* - 8
  - Skrutka M4x8
  - 
  - 
```
````


### <font color='brown'> Podvozok </font>

Hriadele kolies by sa mali v bočniciach podvozku otáčať voľne, os pre otáčanie kabíny by mala byť tesne nasunutá do bloku pdovozku.

````{subfigure} AB
:layout-sm: A|B
:gap: 2px
:subcaptions: below
:width: 700px

```{image} ./model/0215_mini_zeriav/img/diely_03.jpg
:alt: Diely podvozku
:height: 200px
```

```{image} ./model/0215_mini_zeriav/img/podvozok_01.png
:alt: Zostava podvozku
:height: 200px
```

Konštrukcia podvozku žeriavu.
````

````{dropdown} Diely podvozku žeriavu.

```{list-table}
:header-rows: 1

* - Počet
  - Popis
  - Farba
  - Súbor (step)
* - 2
  - Bočnica
  - žltá
  - [brace_B_09_14](./model/0215_mini_zeriav/parts/brace_B_09_14.step)
* - 1
  - Blok predný
  - žltá
  - [block_B_03_01_01](./model/0215_mini_zeriav/parts/block_B_03_01_01.step)
* - 1
  - Blok zadný
  - žltá
  - [block_B_03_02_01](./model/0215_mini_zeriav/parts/block_B_03_02_01.step)
* - 4
  - Disk kolesa
  - červená
  - [tire_D_01_03_15](./model/0215_mini_zeriav/parts/tire_D_01_03_15.step)
* - 4
  - Pneumatika
  - čierna
  - [tire_T_01_03_15](./model/0215_mini_zeriav/parts/tire_T_01_03_15.step)
* - 2
  - Hriadel 4x50mm
  - 
  - 
* - 1
  - Hriadel 4x30mm
  - 
  - 
* - 6
  - Skrutka M4x8
  - 
  - 
```
````


### <font color='brown'> Kabína </font>

Pre upevnenie strechy kabíny sú použité skrutky M4x5, dlhšie krutky bu zasahovali do navijaku.

````{subfigure} AB
:layout-sm: A|B
:gap: 2px
:subcaptions: below
:width: 700px


```{image} ./model/0215_mini_zeriav/img/kabina_05.png
:alt: Zostava kabíny
:height: 200px
```

```{image} ./model/0215_mini_zeriav/img/navijak_01.png
:alt: Zostava navijaku
:height: 200px
```

Konštrukcia kabíny.
````

````{dropdown} Diely kabíny žeriavu.

```{list-table}
:header-rows: 1

* - Počet
  - Popis
  - Farba
  - Súbor (step)
* - 2
  - Bočnica kabíny
  - bledomodrá
  - [block_X_05_04](./model/0215_mini_zeriav/parts/block_X_05_04.step)
* - 1
  - Podlaha
  - šedá
  - [block_U_05_03](./model/0215_mini_zeriav/parts/block_U_05_03.step)
* - 1
  - Strecha
  - šedá
  - [block_U_02_03](./model/0215_mini_zeriav/parts/block_U_02_03.step)
* - 4
  - Skrutka M4x5
  - 
  - Upevnenie strechy
* - 4
  - Skrutka M4x8
  - 
  - Upevnenie podlahy
```
````

````{dropdown} Diely navijaka.

```{list-table}
:header-rows: 1

* - Počet
  - Popis
  - Farba
  - Súbor (step)
* - 2
  - Bočnica navijaka
  - žltá
  - [wheel_A_15_14](./model/0215_mini_zeriav/parts/wheel_A_15_14.step)
* - 1
  - Valec navijaka
  - žltá
  - [base_C_01_13](./model/0215_mini_zeriav/parts/base_C_01_13.step)
* - 1
  - Teleso kluky
  - zelená
  - [wheel_B_02_14](./model/0215_mini_zeriav/parts/wheel_B_02_14.step)
* - 1
  - Rúčka kluky
  - zelená
  - [base_C_01_15](./model/0215_mini_zeriav/parts/base_C_01_15.step)
* - 1
  - Hák
  - červená
  - [comp_C_hook_block_02](./model/0215_mini_zeriav/parts/comp_C_hook_block_02.step)
* - 1
  - Skrutka M4x20
  - 
  - Upevnenie kluky
```
````



### <font color='brown'> Zostava žeriava </font>

```{figure} ./model/0215_mini_zeriav/img/img_sc_02.png
:width: 350px

Zostava malého žeriavu (ver. 1.0).
```


````{subfigure} AB
:layout-sm: A|B
:gap: 2px
:subcaptions: below
:width: 700px

```{image} ./model/0215_mini_zeriav/img/diely_05.jpg
:alt: Detail kabíny a podpery ramena
:height: 200px
```

```{image} ./model/0215_mini_zeriav/img/diely_04.jpg
:alt: Detail navijaku
:height: 200px
```

Detaily konštrukcie.
````




