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

def tomas_sorter_function_hard(scrambled_list):
    n = len(scrambled_list)
    
    for i in range(n):
            scrambled_list[i] = scrambled_list[i] #remove this

    return scrambled_list

def tomas_sorter_function_medium(scrambled_list):
    n = len(scrambled_list)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            scrambled_list[j] = scrambled_list[j] #remove this

    return scrambled_list

def tomas_sorter_function_easy(scrambled_list):
    n = len(scrambled_list)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if scrambled_list[j] > scrambled_list[j + 1]:
                # add here
                scrambled_list[j] = scrambled_list[j] #remove this

    return scrambled_list

def tomas_sorter_function(scrambled_list):
    return tomas_sorter_function_hard(tomas_sorter_function_medium(tomas_sorter_function_easy(scrambled_list)))