PLAN1=[[5, 6], [1, 2, None, None, None], [3, 1, 3, 5, None], [3, 2, 4, 5, None], [2, 3, 5, None, None], [3, 2, 3, 4, None]]

PLAN2=[[5, 4], [1,2, None, None, None], [3,1,3,4, None], [1,2, None, None, None], [2,2,5, None, None], [1,4, None, None, None]]



def creerListeVide(n:int):
    return [0]+[None]*(n)

def creerPlanSansVille(n:int):
    P=[[n,0]]+[creerListeVide(n-1)]*n
    return P

def estVoisine(plan,x,y):
    return x in plan[y]

def ajoutRoute(plan,x,y):
    if not estVoisine(plan,x,y):
        i=0
        while plan[x][i]!=None:
            i+=1
        plan[x][i]=y
        plan[x][0]+=1
        j=0
        while plan[y][j]!=None:
            j+=1
        plan[y][j]=x
        plan[y][0]+=1
    plan[0][1]+=1

def afficheToutesLesRoutes(plan):
    routes=[]
    for i in range(1,len(plan)-1):
        for j in range(plan[i][0]):
            route1=(i,plan[i][j+1])
            route2=(plan[i][j+1],i)
            if not route1 in routes and not route2 in routes:
                routes.append((i,plan[i][j+1]))
    return routes

# >>> afficheToutesLesRoutes(PLAN1)
# [(1, 2), (2, 3), (2, 5), (3, 4), (3, 5), (4, 5)]
#
# >>> afficheToutesLesRoutes(PLAN2)
# [(1, 2), (2, 3), (2, 4), (4, 5)]