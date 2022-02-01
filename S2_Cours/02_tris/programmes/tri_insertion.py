def tri_insertion(T,n):
    for i in range(1,n):
        j=i
        v=T[i]
        while j>0 and v<T[j-1]:
            T[j]=T[j-1]
            j=j-1
        T[j]=v
    return T