def foo(v:int) -> int:
    r = 0
    n = 0
    i=1
    while r <= v :
        print(i,r,n,'r<=v ? ',r<=v)
        n = n+1
        r = r+n
        i+=1
    print(i,r,n,'r<=v ? ',r<=v)
    return n