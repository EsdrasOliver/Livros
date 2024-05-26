votaram = {'tom': 'votou'}
voted = {}


def verifica_eleitor(nome):
    if votaram.get(nome):
        print("Mande embora!")
    else:
        voted[nome] = True
        print("Deixe votar!")


verifica_eleitor("tom")  # Deixe votar!
verifica_eleitor("mike")  # Deixe votar!
verifica_eleitor("mike")  # Mande embora!
