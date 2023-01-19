#init python
init python:
    if(persistent.dia == None):
        persistent.dia = True
    if(persistent.especi == None):
        persistent.especi = False

init python:
    crush = "" #Valkion, Leiftan, Kero, Ezarel, Nevra, nulo
    artigo = "" #a, o, as
    nome = "" #Bia, Bianka, Bella, Beatriz, Gêmeas, Bryan, Bryanne, Breno, Princesa
    genero = "" #irmã, irmão, irmãs

init python:
    if(persistent.cap1 == None):
        persistent.cap1 = True
    if(persistent.cap2 == None):
        persistent.cap2 = True
    if(persistent.cap3 == None):
        persistent.cap3 = True

# $persistent.cap = True
# [liberar um capítulo]


#dia = True, noite = False
#corredor com portal e floresta roxa: especial = True

#define fala

define pro = Character("", image = "pro")
define bellav1 = Character("", color='#014f59', image = "bellav1",) #1
define bella = Character("",color='#014f59', image = "bella",) #1
define beatriz = Character("", image = "beatriz") #2
define prince = Character("", image = "prince") #3
define bianka = Character("", image = "bianka") #4
define gemeas = Character("", image = "gemeas") #5
define bryan = Character("", image = "bryan") #6
define bryanne = Character("", image = "bryanne") #7
define bia = Character("", image = "bia") #8
define breno = Character("", image = "breno") #9

image side bellav1 = im.Scale("images/caixa/bella v1.png", 1920, 1080, xoffset=0, yoffset=0)
image side bella = im.Scale("images/caixa/bella.png", 1920, 1080, xoffset=0, yoffset=0)

#define cenario
image menu_cap1 = "images/cenarios/menu_cap1.png"

image qg_salao_d = "images/cenarios/qg_salao_d.png"
image qg_salao_n = "images/cenarios/qg_salao_n.png"
image qg_enfermaria_d = "images/cenarios/qg_enfermaria_d.png"
image qg_enfermaria_n = "images/cenarios/qg_enfermaria_n.png"
image qg_escadaria_d = "images/cenarios/qg_escadaria_d.png"
image qg_escadaria_n = "images/cenarios/qg_escadaria_n.png"
image qg_despensa_d = "images/cenarios/qg_despensa_d.png"
image qg_despensa_n = "images/cenarios/qg_despensa_n.png"
image qg_biblioteca_d = "images/cenario/qg_biblioteca_d.png"
image qg_biblioteca_n = "images/cenario/qg_biblioteca_n.png"
image qg_vila_d = "images/cenarios/qg_vila_d.png"
image qg_vila_n = "images/cenarios/qg_vila_n.png"
image qg_corredor_d = "images/cenarios/qg_corredor_d.png"
image qg_corredor_n = "images/cenarios/qg_corredor_n.png"
image qg_alquimia_d = "images/cenarios/qg_alquimia_d.png"
image qg_alquimia_n = "images/cenarios/qg_alquimia_n.png"

#define personagem

#define selecao
#-------------------------------------------------------------------------------
label start:
    pro "Label start, teste."
    if crush == "":
        if nome == "":
            if artigo == "":
                if genero == "":
                    call screen caps
    else:
        jump prologo
    return
#_______________________________________________________________________________

#Labels História
label prologo:

#_______________________________________________________________________________
screen caps:
    add "images/cenarios/menu_caps.png"
    imagemap:
        ground "images/ground/caps.png"
        hover "images/hover/caps.png"

        hotspot(0, 0, 608, 1078) action Jump("cap1")
        if(persistent.cap2):
            hotspot(635, 3, 824, 1075) action Jump("cap2")
        if(persistent.cap3):
            hotspot(1561, 9, 352, 1064) action Jump("cap3")

screen cap1:
    add "images/cenarios/menu_cap1.png"
    imagemap:
        ground "images/ground/cap1.png"
        hover "images/hover/cap1.png"

        hotspot(0, 0, 557, 1078) action Jump("bella")
        hotspot(546, 3, 398, 1075) action Jump("prince")
        hotspot(939, 0, 453, 1078) action Jump("beatriz")
        hotspot(1394, 0, 524, 1078) action Jump("bianka")

screen cap2:
    add "images/cenarios/menu_cap2.png"
    imagemap:
        ground "images/ground/cap2.png"
        hover "images/hover/cap2.png"

        hotspot(0, 0, 642, 1078) action Jump("gemeas")
        hotspot(616, 3, 1299, 1075) action Jump("bia")

screen cap3:
    add "images/cenarios/menu_cap3.png"
    imagemap:
        ground "images/ground/cap3.png"
        hover "images/hover/cap3.png"

        hotspot(0, 4, 1918, 1072) action Jump("breno")

#_______________________________________________________________________________

screen qg_salao:
    imagemap:
        ground "images/ground/qg_salao.png"
        hover "images/hover/qg_salao.png"

        hotspot(1, 684, 80, 83) action Return("qg_corredor")
        hotspot(264, 201, 55, 79) action Return("qg_biblioteca")
        hotspot(392, 716, 79, 88) action Return("qg_despensa")
        hotspot(917, 523, 78, 57) action Return("qg_vila")
        hotspot(938, 228, 65, 62) action Return("qg_enfermaria")
        hotspot(1423, 721, 73, 81) action Return("qg_forja")
        hotspot(1571, 205, 104, 91) action Return("qg_alquimia")
        hotspot(1848, 700, 68, 190) action Return("qg_escadaria")

screen qg_corredor:
    imagemap:
        ground ""
        hover ""

        hotspot() action Return("qg_salao")
        hotspot() action Return("qg_quarto_v")
        hotspot() action Return("qg_quarto_l")
        hotspot() action Return("qg_quarto_e")
        hotspot() action Return("qg_quarto_n")
        hotspot() action Return("qg_corredor2")
        hotspot() action Return("qg_cristal")

screen qg_corredor2:
    imagemap:
        ground ""
        hover ""

        hotspot() action Return("qg_corredor")
        hotspot() action Return("qg_quarto1")
        hotspot() action Return("qg_quarto_me")
        hotspot() action Return("qg_quarto2")
        hotspot() action Return("qg_quarto3")



#[SISTEMA DE MOVIMENTO]---------------------------------------------------------

label qg_salao:
    if persistent.dia == True:
        scene qg_salao_d
        with dissolve
        pro "Chamar salão de dia"

    elif persistent.dia == False:
        scene qg_salao_n
        with dissolve
        pro "Chamar salão de noite"

    call screen qg_salao

    if _return == "qg_corredor":
        jump qg_corredor
    elif _return == "qg_biblioteca":
        jump qg_biblioteca
    elif _return == "qg_despensa":
        jump qg_despensa
    elif _return == "qg_vila":
        jump qg_despensa
    elif _return == "qg_enfermaria":
        jump qg_enfermaria
    elif _return == "qg_forja":
        jump qg_forja
    elif _return == "qg_alquimia":
        jump qg_alquimia
    elif _return == "qg_escadaria":
        jump qg_escadaria
    else:
        pro "Algum tipo de erro com sistema do salão"

        return

label qg_corredor:
    pro "Label do corredor"
    return

label qg_biblioteca:
    pro "Label da biblioteca"
    return

label qg_despensa:
    pro "Label da despensa"
    return

label qg_vila:
    pro "Label da vila"
    return

label qg_enfermaria:
    pro "Label da enfermaria"
    return

label qg_forja:
    pro "Label da forja"
    return

label qg_alquimia:
    pro "Label da alquimia"
    return

label qg_escadaria:
    pro "Label da escadaria"
    return


#[SISTEMA DE MOVIMENTO]---------------------------------------------------------

label bella:
    python:
        crush = "Valkion"
        artigo = "a"
        nome = "Bella"
        genero = "Irmã"
    jump start
    return

label beatriz:
    python:
        crush = "Leiftan"
        artigo = "a"
        nome = "Beatriz"
        genero = "Irmã"
    jump start
    return

label prince:
    python:
        crush = "nulo"
        artigo = "a"
        genero = "Irmã"
        nome = "Princesa"
    jump start
    return

label bianka:
    python:
        crush = "Nevra"
        artigo = "a"
        genero = "Irmã"
        nome = "Bianka"
    jump start
    return

label gemeas:
    python:
        crush = "Kero"
        artigo = "as"
        genero = "Irmãs"
        nome = "Gêmeas"
    jump start
    return

label bia:
    python:
        crush = "Ezarel"
        artigo = "a"
        genero = "Irmã"
        nome = "Bia"
    jump start
    return

label breno:
    python:
        crush = "Valkion"
        artigo = "o"
        genero = "Irmão"
        nome = "Breno"
    jump start
    return
