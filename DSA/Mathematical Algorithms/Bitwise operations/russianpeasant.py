#russian peasant method
#multiply two numbers using bitwise operators

def russianpeasnt(a,b):
  res=0
  while(b>0):
    if(b&1):
      res=res+a
    a=a<<1
    b>>=1
  return res
print(russianpeasant(7,6))

      
    
