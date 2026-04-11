from protector import sorted

"""
Po dlouhé cestě Jindřich ze Skalice zaskočil do své oblíbené nalévárny. Netrpělivě
tam čekal na svého drahého přítele, pana Ptáčka. Odpil si pár loků piva, když v
tom jeho pohled upoutal mladý bard.

"Hej, ty! Zahraj mi něco, ať mi ta chvíle rychleji uteče," houkl na něj Jindra.
"Samo sebou," odvětil bard, "ale nejdřív mi zaplať pivo."

Jindřich pohlédl na mladíka a poté do svého měšce plného zakrvácených grošů. V
duchu si sice pomyslel: "I'm feeling quite hungry," ale nakonec uznal, že
se raději nechá nasytit kvalitní hudbou. Otočil se proto zpět k bardovi a hodil
mu jeden ze špinavých grošů.

Bard se minci pokusil polapit, ale ta mu vyklouzla z dlaní. Začala se nekontrolovaně
odrážet po místnosti sem a tam. V tu ránu se stal malér. Bardovi spadly
všechny noty na zem a beznadějně se pomíchaly. "Že já blbec jsem se to nenaučil
nazpaměť!" láteřil v duchu hudebník.

"No, tak kde to vázne?" pronesl vážně Jindra a položil ruku na stůl.

Zpocený bard začal zmateně přehrabovat listy papíru. V tu chvíli ho však osvítil
spásný nápad - naprogramovat řadicí algoritmus, který by za něj listy bleskově
uspořádal. "To můj problém určitě vyřeší!" zvolal nadšeně.
"""

# nápověda 1:
"""
scrambled_list je seznam not v nahodném pořadí jak jdou za sebou. 
scrambled_list = [5, 2, 8, 114, 65, .... ]
"""

def tomas_sorter_function_hard(scrambled_list):
    serazene_pole = []
    for i in range(len(scrambled_list)):
        misto_nejmensiho = scrambled_list.index(min(scrambled_list))
        serazene_pole.append(scrambled_list[misto_nejmensiho])
        scrambled_list.pop(misto_nejmensiho)
    return serazene_pole
    
    
    '''
    print(scrambled_list)
    print()
    n = len(scrambled_list)
    for j in range(0, n-1):
        for i in range(0, n-j-1):
            if scrambled_list[i] > scrambled_list[i+1]:
                pomocna = scrambled_list[i]
                scrambled_list[i] = scrambled_list[i+1]
                scrambled_list[i+1] = pomocna
    print(scrambled_list) '''      
    return scrambled_list

# nápověda 2:
"""
Porovnávání každého prvku s každým s vyšším indexem
"""

def tomas_sorter_function_medium(scrambled_list):
    n = len(scrambled_list)
    
    for i in range(0, n):
        for j in range(0, n - i - 1):
            scrambled_list[j] = scrambled_list[j] #remove this

    return scrambled_list

# nápověda 3:
"""
Je prvek s vyšším indexem větší než aktuální prvek?
"""

def tomas_sorter_function_easy(scrambled_list):
    n = len(scrambled_list)
    
    for i in range(0, n):
        for j in range(0, n - i - 1):
            if scrambled_list[j] > scrambled_list[j + 1]:
                # add here
                scrambled_list[j] = scrambled_list[j] #remove this

    return scrambled_list

def tomas_sorter_function(scrambled_list):
    return tomas_sorter_function_hard(tomas_sorter_function_medium(tomas_sorter_function_easy(scrambled_list)))