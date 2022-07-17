### les dictionnaires - le drone

drone={'chassis':1,'moteur':4,'helice':4,'controleurVol':1,'ESC4en1':1,'batterie':1,'plaqueDeDistribution':1}
stock={'chassis':0,'moteur':25,'helice':36,'controleurVol':12,'ESC4en1':8,'batterie':20,'plaqueDeDistribution':7}
limiteMin={'chassis':2,'moteur':8,'helice':8,'controleurVol':2,'ESC4en1':2,'batterie':2,'plaqueDeDistribution':2}
limiteMax={'chassis':15,'moteur':60,'helice':60,'controleurVol':15,'ESC4en1':15,'batterie':30,'plaqueDeDistribution':15}

stock_V2={'chassis':[10,2,15],'moteur':[25,8,60],'helice':[36,8,60],'controleurVol':[12,2,15],'ESC4en1':[8,2,15],'batterie':[20,2,30],'plaqueDeDistribution':[7,2,15]}

### peut-on faire un drone ?
def realiser1Drone(drone:dict,stock:dict):
    '''Verifie que l'on peut faire un drone, renvoie un booleen'''
    rep=True # renverra un booléen, donc initialisation
    n=len(drone) # longueur du dictionnaire
    i=0 # initialisation du compteur
    L=list(drone.keys()) # liste des cles
    while rep==True and i<n:
        if stock[L[i]]<drone[L[i]]:
            rep=False
        i+=1
    return rep

def destocker(drone:dict,stock:dict):
    '''retire du stock les composants utiles pour réaliser un drone, le dictionnaire stock est modifié sans le renvoyer'''
    for composant,nb in drone.items():
        stock[composant]=stock[composant]-nb

def stocker(commande:dict,stock:dict):
    '''ajoute au stock les composants commandés, le dictionnaire stock est modifié sans le renvoyer'''
    for composant,nb in commande.items():
        stock[composant]=stock[composant]+nb

def commanderComposant(stock:dict,limiteMin:dict,limiteMax:dict):
    '''génère le dictionnaire commande afin de reconstituer le stock sans modifier le stock'''
    commande={}
    for composant,nb in stock.items():
        if stock[composant]<=limiteMin[composant]:
            commande[composant]=limiteMax[composant]-stock[composant]
    return commande

# >>> commanderComposant(stock,limiteMin,limiteMax)
# {'chassis': 15}

listeCommande=[3,1,5,2]

def satisfaireClient(listeCommande:list,drone:dict,stock:dict,limiteMin:dict,limiteMax:dict):
    '''affiche les commandes de composant, reconstitue le stock'''
    nbCommande=sum(listeCommande)
    commandeValidee=listeCommande[:]
    indice=1
    while nbCommande>0:
        if realiser1Drone(drone,stock) :
            destocker(drone,stock)
            nbCommande-=1
            print (stock)
            if nbCommande==(sum(commandeValidee)-listeCommande[indice-1]):
                print ('commande '+str(indice)+' de '+str(listeCommande[indice-1])+' drones est validée')
                commandeValidee[indice-1]=0
                indice+=1
        else :
            com=commanderComposant(stock,limiteMin,limiteMax)
            print ('commander les composants : '+str(com))
            stocker(com,stock)
    print ('le stock final est '+str(stock))
    print ('Vos clients sont satisfaits')


# >>> satisfaireClient(listeCommande,drone,stock,limiteMin,limiteMax)
# commander les composants : {'chassis': 15}
# {'chassis': 14, 'moteur': 21, 'helice': 32, 'controleurVol': 11, 'ESC4en1': 7, 'batterie': 19, 'plaqueDeDistribution': 6}
# {'chassis': 13, 'moteur': 17, 'helice': 28, 'controleurVol': 10, 'ESC4en1': 6, 'batterie': 18, 'plaqueDeDistribution': 5}
# {'chassis': 12, 'moteur': 13, 'helice': 24, 'controleurVol': 9, 'ESC4en1': 5, 'batterie': 17, 'plaqueDeDistribution': 4}
# commande 1 de 3 drones est validée
# {'chassis': 11, 'moteur': 9, 'helice': 20, 'controleurVol': 8, 'ESC4en1': 4, 'batterie': 16, 'plaqueDeDistribution': 3}
# commande 2 de 1 drones est validée
# {'chassis': 10, 'moteur': 5, 'helice': 16, 'controleurVol': 7, 'ESC4en1': 3, 'batterie': 15, 'plaqueDeDistribution': 2}
# {'chassis': 9, 'moteur': 1, 'helice': 12, 'controleurVol': 6, 'ESC4en1': 2, 'batterie': 14, 'plaqueDeDistribution': 1}
# commander les composants : {'moteur': 59, 'ESC4en1': 13, 'plaqueDeDistribution': 14}
# {'chassis': 8, 'moteur': 56, 'helice': 8, 'controleurVol': 5, 'ESC4en1': 14, 'batterie': 13, 'plaqueDeDistribution': 14}
# {'chassis': 7, 'moteur': 52, 'helice': 4, 'controleurVol': 4, 'ESC4en1': 13, 'batterie': 12, 'plaqueDeDistribution': 13}
# {'chassis': 6, 'moteur': 48, 'helice': 0, 'controleurVol': 3, 'ESC4en1': 12, 'batterie': 11, 'plaqueDeDistribution': 12}
# commande 3 de 5 drones est validée
# commander les composants : {'helice': 60}
# {'chassis': 5, 'moteur': 44, 'helice': 56, 'controleurVol': 2, 'ESC4en1': 11, 'batterie': 10, 'plaqueDeDistribution': 11}
# {'chassis': 4, 'moteur': 40, 'helice': 52, 'controleurVol': 1, 'ESC4en1': 10, 'batterie': 9, 'plaqueDeDistribution': 10}
# commande 4 de 2 drones est validée
# le stock final est {'chassis': 4, 'moteur': 40, 'helice': 52, 'controleurVol': 1, 'ESC4en1': 10, 'batterie': 9, 'plaqueDeDistribution': 10}
# Vos clients sont satisfaits






