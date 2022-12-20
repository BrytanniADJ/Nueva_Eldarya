#init python

#define fala

define pro = Character("Programadora")
define bella = Character("Bella")
define beatriz = Character("Beatriz")
define prince = Character("Princesa")
define bianka = Character("Bianka")
define gemeas = Character("Gêmeas")
define bryan = Character("Bryan")
define bryanne = Character("Bryanne")
define bia = Character("Bia")
define breno = Character("Breno")

#define cenario
image menu_cap1 = "images/cenarios/menu_cap1.png"

#define personagem

#define selecao
#-------------------------------------------------------------------------------
label start:
    pro "teste de capitulos"
    jump menu_cap1

    return
#_______________________________________________________________________________
label menu_cap1:
    pro "Capítulos"
    menu:
        "cap1":
            call screen cap1
        "cap2":
            call screen cap2
        "cap3":
            call screen cap3

    return
#_______________________________________________________________________________

screen cap1:
    add "images/cenarios/menu_cap1.png"
    imagemap:
        ground "images/ground/cap1.png"
        hover "images/hover/cap1.png"

        hotspot(22, 278, 485, 767) action Jump("bella")
        hotspot(507, 363, 396, 308) action Jump("prince")
        hotspot(906, 353, 318, 615) action Jump("beatriz")
        hotspot(1198, 162, 469, 501) action Jump("bianka")

screen cap2:
    add "images/cenarios/menu_cap2.png"
    imagemap:
        ground "images/ground/cap2.png"
        hover "images/hover/cap2.png"

        hotspot(147, 385, 462, 643) action Jump("gemeas")
        hotspot(616, 3, 1299, 1075) action Jump("bia")

screen cap3:
    add "images/cenarios/menu_cap3.png"
    imagemap:
        ground "images/ground/cap3.png"
        hover "images/hover/cap3.png"

        hotspot(0, 4, 1918, 1072) action Jump("breno")

#_______________________________________________________________________________









#[SISTEMA DE MOVIMENTO]---------------------------------------------------------

label bella:
    pro "capitulo 1, Bella"

    return

label beatriz:
    pro "capitulo 1, Beatriz"

    return

label prince:
    pro "capitulo 1, Princesa"

    return

label bianka:
    pro "capitulo 1, bianka"

    return

label gemeas:
    pro "capitulo 2, Gêmeas"

    return

label bia:
    pro "capitulo 2, Bia"

    return

label breno:
    pro "capítulo 3, Breno"

    return
