'''
Padovan Sequence similar to Fibonacci sequence with similar recursive structure. The recursive formula is, 

  P(n) = P(n-2) + P(n-3)
  P(0) = P(1) = P(2) = 1 

  Padovan Sequence: 1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12, 16, 21, 28, 37,…..
  For Padovan Sequence:
  P0 = P1 = P2 = 1 ,
  P(7) = P(5) + P(4)
       = P(3) + P(2) + P(2) + P(1)
       = P(2) + P(1) + 1 + 1 + 1
       = 1 + 1 + 1 + 1 + 1 
       = 5
'''

def padovan(n):
    p2,p1,p,pnext = 1,1,1,1
    print(p2,p1,p,end=" ")
    for i in range(3,n+1):
        pnext = p2+p1
        print(pnext,end=" ") 
        p2 = p1
        p1 = p
        p = pnext

padovan(7)
