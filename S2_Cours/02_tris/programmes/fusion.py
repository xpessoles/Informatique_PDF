def fusion(a0,a,g,m,d):
    i,j=g,m
    for k in range(g,d):
        if i<m and (j==d or a0[i]<=a0[j]):
            a[k]=a0[i]
            i=i+1
        else:
            a[k]=a0[j]
            j=j+1