#Definition des fonctions

def tri_fusion(a,g,d):
    a0=a[:]
    if g>=d-1:
        return
    else:
        m=(g+d)//2
        tri_fusion(a,g,m)
        tri_fusion(a,m,d)
        a0[g:d]=a[g:d]
        fusion(a0,a,g,m,d)
        
def fusion(a0,a,g,m,d):
    i,j=g,m
    for k in range(g,d):
        if i<m and (j==d or a0[i]<=a0[j]):
            a[k]=a0[i]
            i=i+1
        else:
            a[k]=a0[j]
            j=j+1
            
#Programme principal
a=[5,14,11,8,17]
#a=[4,6,3,7,5]
a=[7,6,4,3,2,1]
tri_fusion(a,0,len(a))