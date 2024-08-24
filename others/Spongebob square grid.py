import math
def count_ways(x1,x2,y1,y2):
    mod=10**9+7
    def n_ways(n,k):
         return math.comb(n,k)%mod

    x_steps=x2-x1
    y_steps=y2-y1

    total_steps=x_steps+y_steps

    return n_ways(total_steps,x_steps)

x1,x2,y1,y2 = map(int,input().split())
result=count_ways(x1,x2,y1,y2)
print(result)
