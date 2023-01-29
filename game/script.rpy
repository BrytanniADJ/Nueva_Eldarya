#init python
init python:
    if(persistent.dia == None): #dia = True, noite = False
        persistent.dia = True
    if(persistent.especi == None): #corredor com portal e floresta roxa: especial = True
        persistent.especi = False

    adj_aula = False
    adj_salao = False
    adj_biblio = False
    adj_quarto = False
    adj_alquimia = False

init python:
    crush = "" #Valkion, Leiftan, Kero, Ezarel, Nevra, nulo
    artigo = "" #a, o, as
    nome = "" #Bia, Bianka, Bella, Beatriz, Gêmeas, Bryan, Bryanne, Breno, Princesa
    genero = "" #irmã, irmão, irmãs
    best = "" #valkion, nevra, ezarel, leiftan
    if(persistent.casal == None):
        persistent.casal == False #True = Casal junto

init python:
    if(persistent.cap1 == None):
        persistent.cap1 = True
    if(persistent.cap2 == None):
        persistent.cap2 = True
    if(persistent.cap3 == None):
        persistent.cap3 = True

init python:
    from random import randint
#sorte = randint(1,3?) [faz o sorteio]

init python:
    amigo = 0
    quarto = 0
    histo = 0

#define fala
define pro = Character("", image = "pro")
define bellav1 = Character("", color='#014f59', image = "bellav1",) #1
define bella = Character("",color='#014f59', image = "bella",) #1
define beatriz = Character("", image = "beatriz") #2
define princev1f = Character("", image = "princev1f") #3
define princev1r = Character("", image = "princev1r") #3
define princev1p = Character("", image = "princev1p") #3
define princev2f = Character("", image = "princev2f") #3
define princev3r = Character("", image = "princev3r") #3
define princev3p = Character("", image = "princev3p") #3
define princev3f = Character("", image = "princev3f") #3
define princev2 = Character("", image = "princev2") #3
define princev3 = Character("", image = "princev3") #3
define bianka = Character("", image = "bianka") #4
define gemeas = Character("", image = "gemeas") #5
define bryan = Character("", image = "bryan") #6
define bryanne = Character("", image = "bryanne") #7
define bia = Character("", image = "bia") #8
define breno = Character("", image = "breno") #9

define terfall = Character("", image = "terfall")
define fada1 = Character("", image = "fada1")
define winnie = Character("", image = "winnie")

image terfall = "images/personagens/terfall.png"
image fada1 = "images/personagens/fada1.png"
image winnie = "images/personagens/winnie.png"
image wi1 = "images/personagens/wi1.png"
image wi2 = "images/personagens/wi2.png"
image wi3 = "images/personagens/wi3.png"

         # exemplo_v(roupa)(sentimento)
image side bellav1 = im.Scale("images/caixa/bella v1.png", 1920, 1080, xoffset=0, yoffset=0)
image side bella = im.Scale("images/caixa/bella.png", 1920, 1080, xoffset=0, yoffset=0)

image side princev1f = im.Scale("images/caixa/prince v1f.png", 1920, 1080, xoffset=0, yoffset=0) #feliz (f)
image side princev2f = im.Scale("images/caixa/prince v2f.png", 1920, 1080, xoffset=0, yoffset=0)
image side princev3f = im.Scale("images/caixa/prince v3f.png", 1920, 1080, xoffset=0, yoffset=0)

image side princev1r = im.Scale("images/caixa/prince v1r.png", 1920, 1080, xoffset=0, yoffset=0) #raiva (r)
image side princev3r = im.Scale("images/caixa/prince v3r.png", 1920, 1080, xoffset=0, yoffset=0)

image side princev1p = im.Scale("images/caixa/prince v1p.png", 1920, 1080, xoffset=0, yoffset=0) #preocupada (p)
image side princev3p = im.Scale("images/caixa/prince v3p.png", 1920, 1080, xoffset=0, yoffset=0)

image side terfall = im.Scale("images/caixa/terfall.png", 1920, 1080, xoffset=0, yoffset=0) #Terfall
image side fada1 = im.Scale("images/caixa/fada1.png", 1920, 1080, xoffset=0, yoffset=0) #fada1
image side winnie = im.Scale("images/caixa/winnie.png", 1920, 1080, xoffset=0, yoffset=0) #winnie

#define cenario
image menu_cap1 = "images/cenarios/menu_cap1.png"

#cenario adj
image adj_alquimia = "images/cenarios/adj_alquimia.png"
image adj_aula = "images/cenarios/adj_aula.png"
image adj_biblio = "images/cenarios/adj_biblio.png"
image adj_portas = "images/cenarios/adj_portas.png"
image adj_quarto = "images/cenarios/adj_quarto.png"
image adj_salao = "images/cenarios/adj_salao.png"

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
image qg_quartoValk_d = "images/cenarios/qg_quartoValk_d.png"
image qg_quartoValk_n = "images/cenarios/qg_quartoValk_n.png"
image qg_quartoLeif_d = "images/cenarios/qg_quartoLeif_d.png"
image qg_quartoLeif_n = "images/cenarios/qg_quartoLeif_n.png"


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
    if nome == "Princesa":
        scene adj_portas:
        with pixellate

        princev1f "\[Hoje o dia foi tranquilo como de costume, mas fico preocupada que novas criaturas venham a surgir sem meu conhecimento.\]"
        princev1f "\[Mas uma Terfall me prometeu notícias mais cedo, aparentemente ela encontrou uma fada nova na floresta, só estava pensando em como trazê-la pro reino.\]"
        princev1f "\[Melhor eu a encontrar agora, já que encerrei minhas atividade por hoje.\]"

        jump adj_portas

    elif nome == "Bianka":
        pro "Prólogo da Bianka"

        return
    elif nome == "Bia":
        pro "Prólogo da Bia"

        return
    elif nome == "Bella":
        pro "Prólogo da Bella"

        return
    elif nome == "Beatriz":
        pro "Prólogo da Beatriz"

        return
    elif nome == "Breno":
        pro "Prólogo do Breno"

        return
    elif nome == "Gêmeas":
        pro "Prólogo das Gêmeas"

        return
    else:
        pro "Algum erro na página de prologo."

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

label cap1:
    call screen cap1
label cap2:
    call screen cap2
label cap3:
    call screen cap3

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

#corredores
screen qg_corredor:
    imagemap:
        ground "images/ground/qg_corredor.png"
        hover "images/hover/qg_corredor.png"

        hotspot(1109, 987, 141, 91) action Return("qg_salao")
        hotspot(1741, 510, 104, 124) action Return("qg_quarto_v")
        hotspot(1263, 450, 47, 80) action Return("qg_quarto_l")
        hotspot(849, 467, 80, 68) action Return("qg_quarto_e")
        hotspot(504, 468, 63, 62) action Return("qg_quarto_n")
        hotspot(368, 739, 56, 55) action Return("qg_corredor2")
        hotspot(89, 606, 100, 128) action Return("qg_cristal")

screen qg_corredor2:
    imagemap:
        ground "images/ground/qg_corredor2.png"
        hover "images/hover/qg_corredor2.png"

        hotspot(925, 1007, 153, 68) action Return("qg_corredor")
        hotspot(1696, 501, 97, 94) action Return("qg_quarto1")
        hotspot(1193, 504, 76, 83) action Return("qg_quarto_me")
        hotspot(773, 476, 68, 64) action Return("qg_quarto2")
        hotspot(441, 457, 76, 81) action Return("qg_quarto3")

#quartos
screen qg_quarto_v:
    imagemap:
        ground "images/ground/qg_quartos.png"
        hover "images/hover/qg_quartos.png"

        hotspot(919, 947, 143, 95) action Return("qg_corredor")

screen qg_quarto_l:
    imagemap:
        ground "images/ground/qg_quartos.png"
        hover "images/hover/qg_quartos.png"

        hotspot(919, 947, 143, 95) action Return("qg_corredor")

screen qg_quarto_me:
    imagemap:
        ground "images/ground/qg_quartos.png"
        hover "images/hover/qg_quartos.png"

        hotspot(919, 947, 143, 95) action Return("qg_corredor2")

#[SISTEMA DE MOVIMENTO]---------------------------------------------------------

screen adj_alquimia:
    imagemap:
        ground "images/ground/adj_alquimia.png"
        hover "images/hover/adj_alquimia.png"

        hotspot(1308, 29, 136, 112) action Return("adj_portas")

label adj_alquimia:
    scene adj_alquimia
    with dissolve
    if histo == 0:
        if adj_alquimia == False:
            princev1f "\[Felizmente tudo parece estar no seu devido lugar, como deve ser.\]"
            $adj_alquimia = True

        call screen adj_alquimia
        if _return == "adj_portas":
            jump adj_portas
    else:
        princev1p "\[Melhor eu descansar, está ficando tarde.\]"
        call screen adj_alquimia
        if _return == "adj_portas":
            jump adj_portas

screen adj_aula:
    imagemap:
        ground "images/ground/adj_aula.png"
        hover "images/hover/adj_aula.png"

        hotspot(1821, 559, 87, 99) action Return("adj_portas")

label adj_aula:
    scene adj_aula
    with dissolve
    if histo == 0:
        if adj_aula == False:
            princev1r "\[Ainda não entendo essa decisão das meninas de incluirem uma sala de aula no meu castelo apenas por conta de uma garotinha mal feita.\]"
            $adj_aula = True

        call screen adj_aula
        if _return == "adj_portas":
            jump adj_portas
    else:
        princev1f "\[Só queria ter certeza de que está tudo bem antes de ir me deitar.\]"
        call screen adj_aula
        if _return == "adj_portas":
            jump adj_portas

screen adj_biblio:
    imagemap:
        ground "images/ground/adj_biblio.png"
        hover "images/hover/adj_biblio.png"

        hotspot(449, 958, 105, 97) action Return("adj_portas")

label adj_biblio:
    scene adj_biblio
    with dissolve
    if histo == 0:
        if adj_biblio == False:
            princev1f "\[Todo nosso conhecimento em apenas um lugar, ainda bem que o temos em mãos. Não decaíremos na ignorância como os humanos.\]"
            princev1r "\[Não há nada mais fraco do que crer em deuses cegamente, não somos como eles.\]"
            $adj_biblio = True

        call screen adj_biblio
        if _return == "adj_portas":
            jump adj_portas
    else:
        princev1p "\[Vir aqui antes de dormir é sempre muito agradável, no entando preciso descansar agora.\]"
        call screen adj_biblio
        if _return == "adj_portas":
            jump adj_portas

screen adj_portas:
    imagemap:
        ground "images/ground/adj_portas.png"
        hover "images/hover/adj_portas.png"

        hotspot(755, 481, 83, 67) action Return("adj_alquimia")
        hotspot(1380, 497, 81, 80) action Return("adj_aula")
        hotspot(1178, 484, 98, 80) action Return("adj_biblio")
        hotspot(252, 518, 52, 47) action Return("adj_quarto")
        hotspot(1624, 488, 73, 58) action Return("adj_salao")

label adj_portas:
    scene adj_portas
    with dissolve

    call screen adj_portas
    if _return == "adj_aula":
        jump adj_aula
    elif _return == "adj_salao":
        jump adj_salao
    elif _return == "adj_biblio":
        jump adj_biblio
    elif _return == "adj_quarto":
        jump adj_quarto
    elif _return == "adj_alquimia":
        jump adj_alquimia

screen adj_quarto:
    imagemap:
        ground "images/ground/adj_quarto.png"
        hover "images/hover/adj_quarto.png"

        hotspot(906, 942, 165, 108) action Return("adj_portas")

label adj_quarto:
    scene adj_quarto
    with dissolve
    if histo == 0:
        if adj_quarto == False:
            princev1f "\[Seria ótimo poder descansar depois do longo dia, mas preciso me encontrar com a Terfall\]"
            $adj_quarto = True

            call screen adj_quarto
            if _return == "adj_portas":
                jump adj_portas
    else:
        princev1f "\[teste se deu certo]"

        return
#continua



screen adj_salao:
    imagemap:
        ground "images/ground/adj_salao.png"
        hover "images/hover/adj_salao.png"

        hotspot(1, 413, 80, 96) action Return("adj_portas")

label adj_salao:
    scene adj_salao
    with dissolve
    if histo == 1:
        if adj_portas == False:
            princev1f "\[Elas já saíram, foi realmente de grande ajuda ter as chamado pra resolver esse problema.\]"
            $adj_portas = True
        else:
            princev1f "\[Só queria ter certeza de que estava tudo em ordem, como deve ser.\]"

    else:
        jump dialogo

#[SISTEMA DE DIALOGO]-----------------------------------------------------------

label dialogo:
    if histo == 0:
        if nome == "Princesa":
            show terfall at center:
                yalign 0.5
            with dissolve
            princev1f "Terfall."
            terfall "Boa noite Princesa."
            princev1f "Bem, onde está a fada?"
            terfall "Bem, ela não queria mesmo vir, mas não foi difícil de trazer."
            terfall "Fique tranquila pequena, não queremos te machucar, vou te soltar ok?"
            show fada1:
                zoom 0.15
                yalign 0.52
                xalign 0.35
            with dissolve
            princev1f "Ah, entendo."
            fada1 ". . ."
            princev1p "Ela parece muito magra."
            princev1f "Mas fadas desse tipo costuma parecer mais magras mesmo."
            terfall "De fato, mas me preocupo que essa fada realmente não tenha se alimentado muito bem. Visto que a encontrei em uma árvore na grande planice."
            princev1p "Não há árvores frutíferas nessa região."
            terfall "Quando a fada me viu, ela bebeu da minha fonte por um longo tempo e quis fugir pra árvore. Não tenho tanta certeza, mas essas fadas costumam viajar em grupo e ela estava sozinha."
            princev1f "Ela pode ser a primeira do grupo a surgir ou se separou delas, mas é bom termos encontrado a nova espécie de fada. Bom trabalho Terfall."
            terfall "Fico feliz que pude ajudar."
            show fada1:
                zoom 0.15
                yalign 0.52
                xalign 0.58
            with move
            fada1 "...!"
            show terfall at right:
                yalign 0.5
            with move
            terfall "Calma garota."
            princev1p "Não precisa ficar com medo pequena, só queremos ajudar."
            princev1f "Visto que você seja de uma espécie de fada desconhecida, você ficará com a Biologus Puella, que  irá estudá-la, pra saber como se comporta, sua adaptalidade..."
            princev1f "Pra que te possamos te proporcionar uma vida melhor, tudo bem? Você também faz parte da família. Tudo que queremos é sua cooperação."
            fada1 "Kare au e marama..."
            princev1f "Nova espécie com linguagem própria? Isso é ótimo!"
            show winnie:
                xalign 0.35
                zoom 0.7
                yalign -1.0
            with dissolve
            winnie "Boa noite Princesa."

            show wi1:
                zoom 0.6
                yalign 0.1
                xalign 0.05
            with dissolve
            show wi2:
                zoom 0.6
                yalign -5.0
                xalign 0.6
            with dissolve
            show wi3:
                zoom 0.6
                yalign 4.5
                xalign 0.35
            with dissolve

            winnie "Desculpe atrapalhar sua conversa, mas eu percebi um rastro de água vindo de fora..."
            terfall "Desculpa Winnie, mas a Princesa havia me chamado."

            show wi1:
                zoom 0.6
                yalign 4.5
                xalign 0.35
            with move
            show wi2:
                zoom 0.6
                yalign 0.1
                xalign 0.05
            with move
            show wi3:
                zoom 0.6
                yalign -5.0
                xalign 0.6
            with move

            winnie "Agora nós vamos ter que limpar tudo!"
            terfall "Não vou contra as ordens da Princesa."
            winnie "Claro, não é você quem limpa sua própria bagunça, não é?!"

            show wi1:
                zoom 0.6
                yalign -5.0
                xalign 0.6
            with move
            show wi2:
                zoom 0.6
                yalign 4.5
                xalign 0.35
            with move
            show wi3:
                zoom 0.6
                yalign 0.1
                xalign 0.05
            with move

            terfall "Sei que é chato, mas você sabe que não tenho culpa."
            winnie "Simplesmente pare de entrar no castelo então, ao menos isso você pode fazer?"
            princev1r "Meninas!"
            princev1r "Primeiramente, EU pedi pra Terfall me encontrar aqui."
            princev1r "E segundo que VOCÊ Winnie tem o dever de limpar o castelo independentemente se acabam sujando ou não, é o SEU trabalho, entendeu?!"

            show wi1:
                zoom 0.6
                yalign 0.1
                xalign 0.05
            with move
            show wi2:
                zoom 0.6
                yalign 0.1
                xalign 0.1
            with move
            show wi3:
                zoom 0.6
                yalign 0.1
                xalign 0.15
            with move

            winnie ". . ."
            princev1r "Responda imediatamente!"
            winnie "Sim senhora, eu entendi..."

            pro "teste"
            jump dialogo




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
    if persistent.dia == True:
        scene qg_corredor_d
        with dissolve

    elif persistent.dia == False:
        scene qg_corredor_n
        with dissolve

    call screen qg_corredor
    if _return == "qg_salao":
        jump qg_salao
    elif _return == "qg_quarto_v":
        jump qg_quarto_v
    elif _return == "qg_quarto_l":
        jump qg_quarto_l
    elif _return == "qg_quarto_e":
        jump qg_quarto_e
    elif _return == "qg_quarto_n":
        jump qg_quarto_n
    elif _return == "qg_corredor2":
        jump qg_corredor2
    elif _return == "qg_cristal":
        jump qg_cristal
    else:
        pro "Algum erro no sistema do salão"

    return

label qg_quarto_v:
    if persistent.casal == True:
        if persistent.dia == True:
            scene qg_quartoValk_d
            with dissolve

        elif persistent.dia == False:
            scene qg_quartoValk_n
            with dissolve

        call screen qg_quarto_v
        if _return == "corredor":
            jump qg_corredor
    elif persistent.casal == False:
        python:
            sorte = randint(1,4)
        if sorte == 1:
            play sound "bate_porta_v1.mp3"
        elif sorte == 2:
            play sound "bate_porta_v2.mp3"
        elif sorte == 3:
            play sound "bate_porta_v3.mp3"
        elif sorte == 4:
            play sound "bate_porta_v4.mp3"

        if nome == "Beatriz":
            beatriz ""
        elif nome == "Bella":
            pro "teste"
        elif nome == "Princesa":
            pro "teste"
        elif nome == "Bianka":
            pro "teste"
        elif nome == "Gêmeas":
            pro "teste"
        elif nome == "Bryan":
            pro "teste"
        elif nome == "Bryanne":
            pro "teste"
        elif nome == "Bia":
            pro "teste"
        elif nome == "Breno":
            pro "teste"

label qg_quarto_l:
    if persistent.casal == True:
        if persistent.dia == True:
            scene qg_quartoLeif_d
            with dissolve

        elif persistent.dia == False:
            scene qg_quartoLeif_n
            with dissolve

        call screen qg_quarto_l
        if _return == "corredor":
            jump qg_corredor
    elif persistent.casal == False:
        python:
            sorte = randint(1,4)
        if sorte == 1:
            play sound "bate_porta_v1.mp3"
        elif sorte == 2:
            play sound "bate_porta_v2.mp3"
        elif sorte == 3:
            play sound "bate_porta_v3.mp3"
        elif sorte == 4:
            play sound "bate_porta_v4.mp3"

label qg_quarto_e:
    python:
        sorte = randint(1,4)
    if sorte == 1:
        play sound "bate_porta_v1.mp3"
    elif sorte == 2:
        play sound "bate_porta_v2.mp3"
    elif sorte == 3:
        play sound "bate_porta_v3.mp3"
    elif sorte == 4:
        play sound "bate_porta_v4.mp3"

label qg_quarto_n:
    python:
        sorte = randint(1,4)
    if sorte == 1:
        play sound "bate_porta_v1.mp3"
    elif sorte == 2:
        play sound "bate_porta_v2.mp3"
    elif sorte == 3:
        play sound "bate_porta_v3.mp3"
    elif sorte == 4:
        play sound "bate_porta_v4.mp3"

label qg_corredor2:

label qg_cristal:

label qg_quarto1:
    python:
        sorte = randint(1,4)
    if sorte == 1:
        play sound "bate_porta_v1.mp3"
    elif sorte == 2:
        play sound "bate_porta_v2.mp3"
    elif sorte == 3:
        play sound "bate_porta_v3.mp3"
    elif sorte == 4:
        play sound "bate_porta_v4.mp3"

label qg_quarto_me:

label qg_quarto2:
    python:
        sorte = randint(1,4)
    if sorte == 1:
        play sound "bate_porta_v1.mp3"
    elif sorte == 2:
        play sound "bate_porta_v2.mp3"
    elif sorte == 3:
        play sound "bate_porta_v3.mp3"
    elif sorte == 4:
        play sound "bate_porta_v4.mp3"

label qg_quarto3:
    python:
        sorte = randint(1,4)
    if sorte == 1:
        play sound "bate_porta_v1.mp3"
    elif sorte == 2:
        play sound "bate_porta_v2.mp3"
    elif sorte == 3:
        play sound "bate_porta_v3.mp3"
    elif sorte == 4:
        play sound "bate_porta_v4.mp3"


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
