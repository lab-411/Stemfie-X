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
# <font color='navy'> <b> Vizualizácia </b> </font>

```{figure} ./img/banner.png
:width: 800px
:name: prg_125
```

## <font color='purple'> <b> Prehliadač *F3D* </b></font>

Programč [F3D](https://f3d.app/) je univerzálny open-source prehliadač 3D dát podporujúci množstvo [formátov](https://f3d.app/docs/user/SUPPORTED_FORMATS). Inštalácia je možné zo stránok projektu alebo z repozitárov distribúcií, pre operačné systémy založené na distribúcii Ubuntu  

    sudo apt-get install f3d

Programu je možné používať ako prednastavený systémový prehliadač pre súbory *.step* a *.stl* alebo je ho možné spustiť z konzoly  

    f3d --watch --background-color 1,1,1 --grid=1 --axis=1 --grid-absolute --up +z  <file_name>.step

Parameter *--watch* umožní automatické obnovenie zobrazovaného objektu pri zmene zobrazovaného súboru. Pretože knižnica *Stemfie-X* vytvára primárne objekty v rovine XY, parameter *--up +z* definuje orientáciu mriežky a smer pohľadu. Ovládanie programu je jednoduché, on-screen help sa vyvolá klávesou `h`. 

Konfiguráciu programu je možné uložiť do konfiguračného súboru *config.f3d* 

    [
      {
        "options": {
          "background-color": "1,1,1",
          "color": "0.39, 0.58, 0.92",
          "anti-aliasing": true,
          "watch":1,
          "axis": true,
          "grid": true,
          "up": "+z",
          "grid-absolute":true
        }
      }
    ]

Program spustíme s parametrom s cestou ku konfiguračnému súboru a menom zobrazovaného súboru

    f3d --config=./config.f3d <file_name>.step 
    




%::::{grid} 4
%
%```{grid-item-card} Title
%:img-top: ./img/test_tetiva.png
%:class-card: sd-text-black
%:img-alt: my text
%
%Text
%```
%
%```{grid-item-card} Title
%:img-top: ./img/test_tetiva.png
%:class-card: sd-text-black
%:img-alt: my text
%
%Text
%```
%
%::::
