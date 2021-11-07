# TP 08

def image_noire(n,p,N):
    """image noire avec un niveau N de gris"""
    img=[]
    for i in range(n):
        img.append([N]*p)
    return(img)

def dim(img):
    """donne le couple (n,p) des ordres de la matrice"""
    n=len(img)
    p=len(img[0])
    return (n,p)

def lit_valeurs(nom_de_fichier):
    f=open(nom_de_fichier,'r')
    c=f.read()
    return c.split()

def sauve_image(img,N,f):
    """sauve l'image dans le fichier f (format pgm)"""
    assert(N in range(2**16))
    (n,p)=dim(img)
    f=open(f,'a')
    f.write('P2\n'+str(p)+' '+str(n)+' '+str(N)+'\n')
    for i in range(n):
        for j in range(p):
            f.write(str(img[i][j])+'\n')

def sauve_rectangle_noir(n,p,N,f):
    t=image_noire(n,p,N)
    sauve_image(t,N,f)

def sauve_rectangle_blanc(n,p,N,f):
    t=image_noire(n,p,0)
    sauve_image(t,0,f)

def echiquier(p,N,f):
    img=[]
    ligne_paire = (p*[N]+p*[0])*4
    ligne_impaire = (p*[0]+p*[N])*4
    for i in range(4):
        for j in range(p):
            img.append(ligne_paire)
        for j in range(p):
            img.append(ligne_impaire)
    return(img)
    sauve_image(img,N,f)

def lit_image(nom_de_fichier):
    L=lit_valeurs(nom_de_fichier)
    p,n=int(L[1]),int(L[2])
    N=int(L[3])
    img=[[0]*p for i in range(n)]
    for i in range(n):
        for j in range(p):
            img[i][j]=int(L[i*p+j+4])
    return(img,N)

def negatif(fichier_entree, fichier_sortie):
    img,N=lit_image(fichier_entree)
    n,p=dim(img)
    for i in range(n):
        for j in range(p):
            img[i][j]=N-img[i][j]
    sauve_image(img,N,g)
    return None

def rotation90(fichier_entree, fichier_sortie):
    img,N=lit_image(fichier_entree)
    n,p=dim(img)
    img_sortie=[[img[j][p-i-1] for j in range(n)]for i in range(p)]
    sauve_image(img_sortie,N,fichier_sortie)
    return(None)




