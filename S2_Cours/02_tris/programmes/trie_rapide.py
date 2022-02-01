#Definition des fonctions
def partition(a,g,d):
    assert g<d
    v=a[g]
    ainf=[]
    asup=[]
    for x in a[g+1:d]:
        if x<v:
            ainf.append(x)
        elif x>v:
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
        
        
        

    
#Programme principal
a=[5,14,11,8,17]
#a=[4,6,3,7,5]
#a=[7,6,4,3,2,1]
tri_rapide(a,0,len(a))