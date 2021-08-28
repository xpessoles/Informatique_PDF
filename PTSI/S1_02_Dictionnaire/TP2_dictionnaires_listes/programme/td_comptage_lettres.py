### dictionnaire compter les lettres d'un texte

texte="""il est parvenu à la maturité de l’enfance, il a vécu de la vie d’un enfant, il n’a point acheté sa perfection aux dépens de son bonheur ; au contraire, ils ont concouru l’un à l’autre. en acquérant toute la raison de son âge, il a été heureux et libre autant que sa constitution lui permettait de l’être. si la fatale faux vient moissonner en lui la fleur de nos espérances, nous n’aurons point à pleurer à la fois sa vie et sa mort, nous n’aigrirons point nos douleurs du souvenir de celles que nous lui aurons causées ; nous nous dirons : au moins il a joui de son enfance ; nous ne lui avons rien fait perdre de ce que la nature lui avait donné. le grand inconvénient de cette première éducation est qu’elle n’est sensible qu’aux hommes clairvoyants et, que, dans un enfant élevé avec tant de soin, des yeux vulgaires ne voient qu’un polisson. un précepteur songe a son interêt plus qu’à celui de son disciple ; il s’attache à prouver qu’il ne perd pas son temps, et qu’il gagne bien l’argent qu’on lui donne ; il le pourvoit d’un acquis de facile étalage et qu’on puisse montrer quand on veut ; il n’importe que ce qu’il lui apprend soit utile, pourvu qu’il se voie aisé-ment. il accumule, sans choix, sans discernement, cent fatras dans sa mémoire. quand il s’agit d’examiner l’enfant, on lui fait déployer sa marchandise ; il l’étale, on est content ; puis il replie son ballot, et s’en va. mon élève n’est pas si riche, il n’a point de ballot à déployer, il n’a rien à montrer que lui-même. or un enfant, non plus qu’un homme, ne se voit pas en un moment. où sont les observateurs qui sachent saisir au premier coup d’oeil les traits qui le caractérisent ? il en est, mais il en est peu ; et sur cent mille pères, il ne s’en trouvera pas un de ce nombre."""


def compterLettre(texte:str):
    dictionnaire={}
    for lettre in texte:
        if lettre in 'azertyuiopqsdfghjklmwxcvbn':
            if lettre in dictionnaire.keys():
                dictionnaire[lettre]+=1
            else:
                dictionnaire[lettre]=1
    return dictionnaire

def sommeLettre(dictionnaire:dict):
    s=0
    for nb in dictionnaire.values():
        s+=nb
    return s

def frequenceLettre(dictionnaire:dict):
    total=sommeLettre(dictionnaire)
    frequence={}
    for lettre,nombre in dictionnaire.items():
        frequence[lettre]=nombre*100/total
    return frequence

# >>> frequenceLettre(compterLettre(texte))
# {'i': 8.009153318077804, 'l': 6.407322654462242, 'e': 13.272311212814646, 's': 7.780320366132723, 't': 7.093821510297483, 'p': 2.9748283752860414, 'a': 7.780320366132723, 'r': 5.720823798627002, 'v': 1.8306636155606408, 'n': 10.602593440122044, 'u': 7.551487414187643, 'm': 2.288329519450801, 'd': 3.051106025934401, 'f': 1.1441647597254005, 'c': 3.051106025934401, 'o': 6.636155606407323, 'h': 0.7627765064836003, 'x': 0.5339435545385202, 'b': 0.6102212051868803, 'q': 1.7543859649122806, 'g': 0.7627765064836003, 'j': 0.07627765064836003, 'y': 0.30511060259344014}