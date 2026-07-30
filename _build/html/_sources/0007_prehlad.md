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


# <font color='navy'> Konštrukčné prvky </font>

```{figure} ./img/banner.png
:width: 800px
:name: stmx_33
```

Stavebnica *STEMFIE-X* obsahuje základné typy dielov (spojky, nosníky, kladky, ozubené kolesá ...), ktoré je možné v závislosti od účelu použitia využívať niekoľkými spôsobmi:

* Pre oboznámenie sa zo stavebnicou sú pripravené zostavy dielov pre konštrukciu jednoduchých modelov, diely sú v podobe súborov pripravených pre 3D tlač. Po vytlačení dielov je možné model zostaviť s použitím spojovacieho materiálu (skrutiek, matíc ..) a bežného náradia

* Pre tvorbu vlastných konštrukcií sú vytvorené katalógy dielov vo formáte *.step* a *.stl* pripravených pre 3D tlač. Výber dielov, ich počet a farebné prevedenie pri 3D tlači si definuje konštruktér, vlastné konštrukcie je možné navrhovať jednoducho na papieri pomocou výberu z katalogových dielov alebo pri pokročilých konštruktéroch aj elektronicky vo vhodnom CAD programe, napríklad FreeCAD. 

* Pre pokročilých uživateľov znalých základov programovania je stavebnica dostupná vo forme knižnice pre programovací jazyk *Python*, v ktorom je možné modifikovať alebo vytvárať vlastné verzie dielov stavebnice. Taktiež je možné s využitím zaákaldných metód parametrického projektovania vytvárať špecializované diely pre integráciu motorov, serv, senzorov a elektronických modulov do stavebnice. 

Rozmery všetkých dielov sú udávané v jednotkách **BU** (**B**asic **U**nit, 1BU = 10mm). Pre jednoduchšiu orientáciu v typoch dielov bolo zavedené pomenovanie dielov, ktoré popisuje ich základné vlastnosti, napríklad *brace_B_10* je jednoduchá spojka o obsahujúca 10 montážnych otvorov. 


## <font color='purple'> Spojky  </font>

[Spojky (Brace)](0520_prg_brace) sú základným typom dielov stavebnice, slúžia na spájanie častí konštrukcie, ako nosníkov a podpier. V závislosti od účelu použitia môžu mať rôzny tvar, hrúbku a počet montážnych otvorov. V niektorých prípadoch môžu byť dva lebo aj viacej otvorov nahradených montážnou štrbinou, táto má význam pri požiadavke spájania dielov mimo štandardnej polohy montážneho otvoru. Rovnako môžeme štrbinu využiť aj pri tvorbe lineárnych posuvných mechanizmov.  

```{figure} ./img/image_brace.png
:width: 600px

Rôzne prevedenia spojok.
```

## <font color='purple'> Nosníky  </font>

[Nosníky (Beams)](0525_prg_beam) slúžia na konštrukciu nosných prvkov konštrukcií, základových platní a konštrukčných prvkov tam, kde sa vyžaduje zvýšená pevnosť, tuhosť alebo nosnosť. Okrem rozmerov nosníkov je možné modifikovať aj formu umiestnenia montážnych otvorov, napríklad len v smere vybranej osi. 

```{figure} ./img/image_block.png
:width: 600px

Rôzne prevedenia blokov.
```

## <font color='purple'>  Kladky </font>

[Kladky](0540_prg_pulley) a držiaky kladiek slúžia na konštrukciu jednoduchých strojov, lanových prevodov a  kladkostrojov.

```{figure} ./img/image_pulley.png
:width: 600px

Kladky a držiaky kladiek.
```

## <font color='purple'> Ozubené kolesá  </font>

Ozubené kolesá sú základom pre konštrukciu prevodoviek k motorom a servám. 

```{figure} ./img/gears_demo.png
:width: 600px

Ozubené kolesá
```

## <font color='purple'>  Základné bloky  </font>

[Základné bloky](0535_prg_base) sú podkladom pre konštrukciu vlastných neštandardných prvkov stavebnice.

```{figure} ./img/image_base.png
:width: 600px

Základné bloky
```
