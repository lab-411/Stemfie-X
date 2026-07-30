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
# <font color='navy'> Žeriav  </font>

```{figure} ./img/banner.png
:width: 800px
:name: exam_001
```

 
Kinematický model malého žeriavu s jednoducho kladkou a navijakom. V modeli sú použité rotačné spoje, rameno žeriavu je možné zdvihať, kabína sa môže otáčať, pre zdvíhanie bremena je použitý navijak. 

```{figure} ./model/0215_mini_zeriav/img/zeriav_01.jpg
:width: 500px

Malý žeriav.
```

## <font color='purple'> Montáž </font>


### <font color='brown'> Rameno žeriavu </font>

````{subfigure} AB|CD
:layout-sm: A|B|C|D
:gap: 2px
:subcaptions: below
:width: 700px

```{image} ./model/0215_mini_zeriav/img/diely_01.jpg
:alt: Diely ramena
:width: 300px
```

```{image} ./model/0215_mini_zeriav/img/diely_02.jpg
:alt: Montáž
:width: 300px
```

```{image} ./model/0215_mini_zeriav/img/rameno_03.png
:alt: Zostava
:width: 300px
```

```{image} ./model/0215_mini_zeriav/img/rameno_04.png
:alt: Zostava
:width: 300px
```

Konštrukcia ramena žeriavu.
````

### <font color='brown'> Podvozok </font>

````{subfigure} AB
:layout-sm: A|B
:gap: 2px
:subcaptions: below
:width: 700px

```{image} ./model/0215_mini_zeriav/img/diely_03.jpg
:alt: Diely podvozku
:width: 300px
```

```{image} ./model/0215_mini_zeriav/img/podvozok_01.png
:alt: Zostava podvozku
:width: 300px
```

Konštrukcia podvozku žeriavu.
````

### <font color='brown'> Kabína </font>

````{subfigure} AB|CD
:layout-sm: A|B|C|D
:gap: 2px
:subcaptions: below
:width: 700px

```{image} ./model/0215_mini_zeriav/img/diely_04.jpg
:alt: Konštrukcia navijaku
:width: 300px
```

```{image} ./model/0215_mini_zeriav/img/diely_05.jpg
:alt: Podpera ramena
:width: 300px
```

```{image} ./model/0215_mini_zeriav/img/kabina_05.png
:alt: Zostava kabíny
:width: 300px
```

```{image} ./model/0215_mini_zeriav/img/kabina_03.png
:alt: Zostava navijaku
:width: 300px
```

Konštrukcia ramena žeriavu.
````



### <font color='brown'> Zostava žeriava </font>

```{figure} ./model/0215_mini_zeriav/img/img_sc_02.png
:width: 350px

Zostava malého žeriavu.
```


## <font color='purple'> Diely </font>

````{dropdown} Diely modelu

```{list-table}
:header-rows: 1

* - Počet
  - Popis
  - Farba
  - Súbor (step)
* - 2
  - Spojka, podvozok
  - červená
  - [brace_B_09](./model/0215_mini_zeriav/parts/brace_B_09_14.step)
* - 3
  - Nosník, podvozok a kabína
  - šedá
  - [block_B_03_02_01](./model/0215_mini_zeriav/parts/block_B_03_02_01.step)
* - 1
  - Podlaha kabíny
  - modrá
  - [block_U_05_03](./model/0215_mini_zeriav/parts/block_U_05_03.step)
* - 1
  - Strecha kabíny
  - modrá
  - [block_U_02_03](./model/0215_mini_zeriav/parts/block_U_02_03.step)
* - 2
  - Stena kabíny
  - oranžová
  - [block_X_05_04](./model/0215_mini_zeriav/parts/block_X_05_04.step)
* - 2
  - Rameno žeriava
  - šedá
  - [brace_B_17](./model/0215_mini_zeriav/parts/brace_B_17_14.step)
* - 2
  - Spojka ramena
  - zelená
  - [base_C_01_01](./model/0215_mini_zeriav/parts/base_C_01_01.step)
* - 1
  - Hák žeriava
  - modrá
  - [comp_C_hook_block_02](./model/0215_mini_zeriav/parts/comp_C_hook_block_02.step)
* - 1
  - Ložisko
  - šedá
  - [base_C_01_12](./model/0215_mini_zeriav/parts/base_C_01_12.step)
* - 1
  - Kladka
  - červená
  - [pulley_A_15](./model/0215_mini_zeriav/parts/pulley_A_15.step)
* - 2
  - Koleso navijaka
  - červená
  - [wheel_A_15_14](./model/0215_mini_zeriav/parts/wheel_A_15_14.step)
* - 1
  - Kľuka navíjaka
  - červená
  - [wheel_B_02_14](./model/0215_mini_zeriav/parts/wheel_B_02_14.step)
* - 2
  - Valec navijaka, kľuka
  - červená
  - [base_C_01_15](./model/0215_mini_zeriav/parts/base_C_01_15.step)
* - 4
  - Disk kolesa
  - béžová
  - [tire_D_01_03_15](./model/0215_mini_zeriav/parts/tire_D_01_03_15.step)
* - 4
  - Pneumatika
  - čierna
  - [tire_T_01_03_15](./model/0215_mini_zeriav/parts/tire_T_01_03_15.step)
* - 18
  - Skrutka M4x5
  - šedá
  - 
* - 1
  - Skrutka M4x20
  - šedá
  - 
* - 2
  - Hriadel D4 x 55mm, kolesá
  - šedá
  -
* - 1
  - Hriadel D4 x 25mm, kabína
  - šedá
  -
* - 2
  - Hriadel D4 x 15mm, kladka a rameno
  - šedá
  -
```
````



