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
# <font color='navy'> <b> Inštalácia</b> </font>

```{figure} ./img/banner.png
:width: 800px
:name: prg_125
```

Programové vybavenie stavebnice `Stemfie-X` pre tvorbu vlastných dielov je založené na programovacom jazyku *Python* a pozostáva z nasledujúcich častí

* Knižnica `Stemfie-X` pre vytváranie dielov stavebnice 
* Platforma `CadQuery` pre parametrické projektovanie pomocou `OpenCascade`
* Programy pre 3D tlač, prehliadače generovaných dielov, editory. 

## <font color='purple'> <b> Inštalácia pre Linux </b></font>

Knižnica `STEMFIE-X`nadstavbou nad `CadQuery` a je v dostupná v zdrojovom tvare v archíve [lib.zip](./lib/lib.zip). Knižnicu po rozbalení ju umiestnite do pracovného adresáru a pri vytváraní ju importujte do vašeho programu ako štandardnú knižnicu v Pythone. Knižnica je univerzálna pre všetky platformy. 

```python

from lib import *
b = Brace(5)
...
```

Inštalácia platformy `CadQuery` je pomocou inštalátora *pip*. Inštalácia obsahuje všetky potrebné komponenty z *Open Cascade Technology (OCCT)* potrebné pre tvorbu konštrukcií. Dokumentácia ku `CadQuery` je dostupná [online](https://cadquery.readthedocs.io/en/latest/intro.html).

    sudo dnf install git
    pip install git+https://github.com/CadQuery/cadquery.git
    
    
Pre platformu `CadQuery` bol vytvorený editor [CQ-Editor](https://github.com/CadQuery/CQ-editor), v ktorom je možné vytvárať a editovať diely stavebnice. Inštalačný skript je dostupný na [github-e](https://github.com/CadQuery/CQ-editor/releases/tag/nightly).
    

```{figure} ./img/cq_editor.png
:width: 700px
:name: prg_126
```

## <font color='purple'> <b> Inštalácia pre Windows</b></font>

TODO
    






