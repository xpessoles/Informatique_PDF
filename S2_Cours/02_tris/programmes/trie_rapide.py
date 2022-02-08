#Definition des fonctions
def partition(a,g,d):
    assert g<d
    v=a[g]
    ainf=[]
    asup=[]
    for x in a[g+1:d]:
        if x<v:
            ainf.append(x)
        else:
            asup.append(x)
    a=a[0:g]+ainf+[v]+asup+a[d:len(a)]
    m=len(ainf)+g
    return m,a

def tri_rapide(a,g,d):
    if g>=d-1:
        return
    else:
        m,a=partition(a,g,d)
        print(a)
        tri_rapide(a,g,m)
        tri_rapide(a,m+1,d)

def tri_rapide2(t:list)-> list :
    '''Trie la liste t par une méthode récursive
    Entrée : Une liste t
    Sortie : La liste est modifiée et est renvoyée '''
    if len(t) < 2 :
        return (t)
    else :
        x = t[-1]
        a=[]
        b=[]
        for i in range (0,len(t)-1) :
            if t[i] < x :
                a.append(t[i])
            else :
                b.append(t[i])
        return (tri_rapide2(a) + [x] + tri_rapide2(b))



#Programme principal
a=[5,14,11,8,17,7]
a=[5,14,11,8,8,17,7]
#a=[4,6,3,7,5]
#a=[7,6,4,3,2,1]
tri_rapide(a,0,len(a))
#tri_rapide2(a)