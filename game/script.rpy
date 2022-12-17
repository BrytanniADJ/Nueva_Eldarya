#define fala

define pro = Character("Programadora")

#define cenario
image menu_ini = "images/cenarios/menu_ini.png"

#define personagem

#define selecao
image bella_sil = "images/silhueta/bella.png"
image bella_sele = "images/selecao/bella.png"
#-------------------------------------------------------------------------------
label start:
    jump menu_ini

    return
#_______________________________________________________________________________
label menu_ini:
    pro "label menu_ini"
    scene menu_ini:
    with dissolve
    pro "teste1"
#_______________________________________________________________________________


    return
