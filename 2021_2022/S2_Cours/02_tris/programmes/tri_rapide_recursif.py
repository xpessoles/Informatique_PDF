def tri_rapide(a,g,d):
    if g>=d-1:
        return
    else:
        m,a=partition(a,g,d)
        tri_rapide(a,g,m)
        tri_rapide(a,m+1,d)
      