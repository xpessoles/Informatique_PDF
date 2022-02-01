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
