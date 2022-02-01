def tri_insertion(T,n):
    for i in range(1,n):
        j=i
        v=T[i]
        print(u'i=',i,'j=',j,'v=',v,'T=',T)
        while j>0 and v<T[j-1]:
            T[j]=T[j-1]
            j=j-1
            print(u'i=',i,'j=',j,'v=',v,'T=',T)
        T[j]=v
        print(u'i=',i,'j=',j,'v=',v,'T=',T)
    return T
    
T=[5,14,11,8,17,7]
n=len(T)
tri_insertion(T,n)